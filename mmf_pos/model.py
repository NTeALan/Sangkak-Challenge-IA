from transformers import AutoTokenizer, BertConfig, BertForTokenClassification, DataCollatorForTokenClassification, Trainer, TrainingArguments
from datasets import Dataset, DatasetDict
from utils import get_tokenizer_training_corpus, load_data, LABEL2ID, ID2LABEL
import evaluate
import numpy as np

class AfrikaPOS:
    def __init__(self, data_dir, num_hiddens, num_attentions, base_model = 'bert-base-uncased', vocab_size = None) -> None:
        self.data_dir = data_dir
        self.base_model = base_model
        self.vocab_size = vocab_size
        self.num_hiddens = num_hiddens
        self.num_attentions = num_attentions
        
        self.build_and_train_tokenizer() # adds self.tokenizer
        self.load_dataset() # adds self.dataset
        self.data_collator = DataCollatorForTokenClassification(tokenizer=self.tokenizer)

        # tokenize the dataset and realign labels
        self.dataset = self.dataset.map(lambda example: self.tokenize_and_align_labels(example), batched=True)

        self.create_model() # adds self.model

        self.eval = evaluate.load('poseval')
    
    def create_model(self):
        config = BertConfig.from_pretrained(self.base_model, 
                                            num_hidden_layers = self.num_hiddens, 
                                            num_attention_heads = self.num_attentions, 
                                            id2label = ID2LABEL, 
                                            vocab_size=self.tokenizer.vocab_size)
        self.model = BertForTokenClassification(config)

    def build_and_train_tokenizer(self):
        training_corpus = get_tokenizer_training_corpus(self.data_dir)
        tokenizer = AutoTokenizer.from_pretrained(self.base_model)
        tokenizer = tokenizer.train_new_from_iterator(training_corpus, tokenizer.vocab_size if self.vocab_size is None else self.vocab_size)
        self.tokenizer = tokenizer
    
    def load_dataset(self):
        ds = {split: Dataset.from_generator(load_data, gen_kwargs={'split': split, 'data_dir': self.data_dir}) for split in ['train', 'test', 'dev']}
        ds = DatasetDict(ds)
        ds = ds.map(lambda x: {'pos_tags_id': list(map(lambda tag: LABEL2ID[tag], x['pos_tags']))})
        self.dataset = ds 
    
    def tokenize_and_align_labels(self, examples):
        """Most of the credit goes to HuggingFace: https://huggingface.co/docs/transformers/v4.33.2/en/tasks/token_classification#preprocess"""
        
        tokenized_inputs = self.tokenizer(examples["tokens"], truncation=True, is_split_into_words=True)

        labels = []
        for i, label in enumerate(examples[f"pos_tags_id"]):
            word_ids = tokenized_inputs.word_ids(batch_index=i)  # Map tokens to their respective word.
            previous_word_idx = None
            label_ids = []
            for word_idx in word_ids:  # Set the special tokens to -100.
                if word_idx is None:
                    label_ids.append(-100)
                elif word_idx != previous_word_idx:  # Only label the first token of a given word.
                    label_ids.append(label[word_idx])
                else:
                    label_ids.append(-100)
                previous_word_idx = word_idx
            labels.append(label_ids)

        tokenized_inputs["labels"] = labels
        return tokenized_inputs

    def compute_metrics(self, p):
        """Most of the credits go to HuggingFace https://huggingface.co/docs/transformers/v4.33.2/en/tasks/token_classification#preprocess"""
        predictions, labels = p
        predictions = np.argmax(predictions, axis=2)

        true_predictions = [
            [ID2LABEL[p] for (p, l) in zip(prediction, label) if l != -100]
            for prediction, label in zip(predictions, labels)
        ]
        true_labels = [
            [ID2LABEL[l] for (p, l) in zip(prediction, label) if l != -100]
            for prediction, label in zip(predictions, labels)
        ]

        results = self.eval.compute(predictions=true_predictions, references=true_labels)

        return {
            "precision": results["weighted avg"]["precision"],
            "recall": results["weighted avg"]["recall"],
            "f1": results["weighted avg"]["f1-score"],
            # "macro-precision": results["macro avg"]["precision"],
            # "macro-recall": results["macro avg"]["recall"],
            # "macro-f1": results["macro avg"]["f1-score"],
            "accuracy": results["accuracy"],
        }
    
    def train_model(self, output_dir):
        training_args = TrainingArguments(
            output_dir=output_dir,
            learning_rate=2e-5,
            per_device_train_batch_size=16,
            per_device_eval_batch_size=16,
            num_train_epochs=2,
            weight_decay=0.01,
            evaluation_strategy="epoch",
            save_strategy="epoch",
            load_best_model_at_end=True
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=self.dataset["train"],
            eval_dataset=self.dataset["dev"],
            tokenizer=self.tokenizer,
            data_collator=self.data_collator,
            compute_metrics=self.compute_metrics,
        )

        trainer.train()
                    
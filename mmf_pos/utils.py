import os 

def get_pos_tags():
    return ["X", "ADJ", "ADP", "ADV", "AUX", "CCONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROPN", "PUNCT", "SCONJ", "SYM", "VERB"]

ID2LABEL = {i: v for i, v in enumerate(get_pos_tags())}
LABEL2ID = {v: i for i, v in enumerate(get_pos_tags())}

def load_data(lang, split, data_dir):
    """load a dataset split

    Arguments
    --------
    lang (str): language code
    split (str): the split to load. train, dev or test
    data_dir (str): the folder containing the data

    Returns
    -------
    a generator of dict whose keys are `tokens` and `pos_tags`
    """
    fname = os.path.join(data_dir, lang, f"{split}.txt")
    with open(fname, "r") as f:
        tokens, tags = [], []
        for line in f:
            line = line.strip()
            if len(line) == 0:
                yield {
                    'tokens': tokens,
                    'pos_tags': tags
                }
                tokens, tags = [], []
            else:
                splits = line.split(" ")
                tokens.append(splits[0])
                tags.append(splits[1])

def get_tokenizer_training_corpus(lang, data_dir):
    """load a dataset split

    Arguments
    --------
    lang (str): language code
    data_dir (str): the folder containing the data

    Returns
    -------
    a generator of list of str
    """

    return (
        d["tokens"] for d in load_data(lang, "train", data_dir)
    )


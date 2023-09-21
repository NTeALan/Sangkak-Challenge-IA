import gradio as gr

def pos_annotation(text):
    # tokens = 
    # tags = 
    return [('CEMAC', 'PROPN'),
        (':', 'PUNCT'),
        ('Dukplɔla', 'NOUN'),
        ('siwo', 'SCONJ'),
        ('le', 'VERB'),
        ('hatsotso', 'NOUN'),
        ('sia', 'DET'),
        ('me', 'ADP'),
        ('wɔ', 'VERB'),
        ('ɖoɖo', 'NOUN'),
        ('ku', 'VERB'),
        ('ɖe', 'ADP'),
        ('nutoame', 'NOUN'),
        ('ƒe', 'DET'),
        ('ganyawo', 'NOUN'),
        ('ŋu', 'ADP'),
        ('le', 'ADP'),
        ('tsɔme', 'NOUN'),
        ('.', 'PUNCT')]

textbox = gr.Textbox(label="Type your text here:", 
                     placeholder="CEMAC : Dukplɔla siwo le hatsotso sia me wɔ ɖoɖo ku ɖe nutoame ƒe ganyawo ŋu le tsɔme .", 
                     lines=2)
highlight = gr.HighlightedText(min_width=300)

demo = gr.Interface(fn=pos_annotation, inputs=textbox, outputs=highlight)
    
demo.launch()  
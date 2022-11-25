from spacy import load  # Carrega um modelo!

nlp = load('pt_core_news_lg')

doc = nlp('gatos cairam do muro.')

for t in doc:
    print('{:10} | {:10} | {:10} | {}'.format(
        t.text,
        t.lemma_,
        t.pos_,
        t.morph
    ))

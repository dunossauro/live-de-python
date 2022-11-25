from spacy import load  # Carrega um modelo!

nlp = load('pt_core_news_lg')

doc = nlp(
    'Eduardo foi a feira.'
)

for t in doc:
    print(
        '{:10} | {:10} | {}'.format(
            t.text,
            t.shape_,
            t.is_alpha
        )
    )

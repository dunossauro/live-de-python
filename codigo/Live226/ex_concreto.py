from spacy import load
from spacy.matcher import Matcher

nlp = load('pt_core_news_lg')

doc = nlp('''
Maria comeu batata
Eduardo comeu batata
Fausto fará magia
Allan comerá as pizzas
Saiu um vídeo novo da Live de python
''')

matcher = Matcher(nlp.vocab)

# padrao = [
#     {'POS': 'PROPN'},
#     {'POS': 'VERB'},
#     {'OP': '?'},
#     {'POS': 'NOUN'}
# ]

padrao = [
    {
        'POS': 'PROPN',
        'MORPH': {'IS_SUPERSET': ['Gender=Fem']}
    },
    {'MORPH': {'IS_SUPERSET': ['Tense=Past']}},
    {'OP': '?'},
    {'POS': 'NOUN'}
]

matcher.add('Regra A', [padrao])

matches = matcher(doc)

for id_, start, stop in matches:
    print(doc[start: stop].text)

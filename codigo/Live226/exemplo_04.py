from spacy import load, displacy

nlp = load('pt_core_news_lg')

texto = '''
João amava Teresa que amava Raimundo
que amava Maria que amava Joaquim que amava Lili
que não amava ninguém.

João foi para os Estados Unidos, Teresa para o convento,
Raimundo morreu de desastre, Maria ficou para tia,
Joaquim suicidou-se e Lili casou com J. Pinto Fernandes
que não tinha entrado na história Google e Youtube
'''

doc = nlp(texto)

displacy.serve(doc, style='ent')

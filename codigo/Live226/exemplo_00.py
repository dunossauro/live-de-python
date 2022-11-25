from spacy import blank

nlp = blank('pt')

doc = nlp('Eduardo foi a feira. Comprou dois pasteis.')

token = doc[1]

span = doc[0:3]

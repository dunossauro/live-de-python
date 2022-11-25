from spacy import load, displacy

nlp = load('pt_core_news_lg')

doc = nlp('Eduardo faz vídeos nos Estados Unidos.')

displacy.serve(doc)

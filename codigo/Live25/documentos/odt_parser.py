import ezodf

doc = ezodf.opendoc('Lista_samurai_X.odt')
linhas = doc.body
# list(linhas)
filtered = filter(lambda x: x.text is not None, linhas)

print(list(map(lambda x: x.text, filtered)))

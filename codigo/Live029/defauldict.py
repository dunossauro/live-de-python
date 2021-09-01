from collections import defaultdict

def none():
    return None

d = defaultdict(none)

d['css']

d.update({'css':00, 'html':'<body></body>'})

print(d)

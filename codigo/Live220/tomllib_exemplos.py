string = """
a = 1

[variaveis]
db = 'ahsuahsuhsa'
path = 'ashduhasd'

[variaveis.prod]
senha = 'senha dahora'

[variaveis.test]
senha = 'senha não tão dahora'

"""
from tomllib import loads, load
from pprint import pprint


pprint(loads(string))

# with open('exemplo.toml', 'rb') as f:
#     pprint(load(f))

# # with open('exemplo.toml', 'r') as f:
# #     pprint(loads(f.read()))

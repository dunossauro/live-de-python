"""Exemplo básico de objetos serializados."""
import pickle
# import _pickle as pickle

# Serialização em runtime
dumped_list = pickle.dumps([1, 2, 3, 4, 'Python'])
print(dumped_list)
print(type(dumped_list))

# Unpickle
obj = pickle.loads(dumped_list)
print(obj)
print(type(obj))

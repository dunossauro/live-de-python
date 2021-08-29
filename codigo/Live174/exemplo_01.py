from pymongo import MongoClient

uri = 'mongodb://root:example@localhost:27017/'

client = MongoClient(uri)
database = client['live_174']  # Tradicional
collection = database['pessoas']


def insert(**args):
    collection.insert(args)
    # collection.inser(
    #     {}  # dict
    # )


def read(**args):
    """
    Um único registro: find_one

    find
    find_one
    find_many
    """
    collection.find(  # vários
        {}
    )


def busca_por_idade(field, op, value):
    collection.find_many(
        {
            field: {
                op: value
            }
        }
    )


def update():
    collection.update(
        {'idade': 18},  # query - find
        {'$set': {'idade': 'dezoito'}}  # A substituição
    )


def delete():
    collection.remove(
        {'idade': {'$lt': 18}}
    )

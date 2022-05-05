from csv import DictReader
from dataclasses import dataclass, InitVar, field
from datetime import datetime


@dataclass
class Row:
    _id: InitVar[str]
    first_name: str
    last_name: str
    email: str
    ultimo_pagamento: InitVar[str]
    status: str
    pagamento: str
    data_pagamento: datetime = field(init=False)
    row_id: int = field(init=False)

    def __post_init__(self, _id, ultimo_pagamento):
        self.data_pagamento: datetime = datetime.strptime(
            ultimo_pagamento, '%Y-%m-%d'
        )
        self.row_id: int = int(_id)


def read_csv_file(csv='dados.csv'):
    with open(csv) as csv_data:
        return list(DictReader(csv_data))


raw_data = read_csv_file()

print(len(raw_data))

data = []

for values in raw_data:
    if '-' in values['ultimo_pagamento'] and values['_id'].isnumeric():
        if None in values:
           values.pop(None)
        try:
            data.append(Row(**values))
        except ValueError:
            print(ValueError, values)
            breakpoint()
        except TypeError:
            print(TypeError, values)
            breakpoint()

print(len(data))

# Filtrar ativos
ativos = list(filter(lambda x: x.status == 'ativo', data))

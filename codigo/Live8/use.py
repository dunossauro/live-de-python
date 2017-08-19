from dml import db_insert, db_select, db_update, db_select
from pprint import pprint


# db_insert('Regis', '98989898', 'regis_@gmail.com')
# db_insert('Fabricio', '98989898', 'fabricio_@gmail.com')
# db_insert('Mazinho', '98989898', 'mazinho_@gmail.com')
# db_insert('diego', '98989898', 'diego_@gmail.com')
# db_insert('Ricardo', '98989898', 'ricardo_@gmail.com')
pprint(db_select('98989898', 'phone'))

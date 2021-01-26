dados = [
    {
        'nome': 'Eduardo',
        'sobrenome': 'Mendes',
        'telefone': {'residencial': '1111-111', 'móvel': '999-999-999'},
        'ddd': 19,
    },
    ...
]

nomes_completos = [f"{dado['nome']} {dado['sobrenome']}" for dado in dados]
  
eduardo_telefone_residencial = [
      dado['telefone']['residencial'] for dado in dados if dado['nome'] == 'Eduardo'
][0]

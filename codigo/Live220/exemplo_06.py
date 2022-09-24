
try:
    try:
        eg = ExceptionGroup(
            'EG', [
                ZeroDivisionError('ERRO por ZERO!'),
                KeyError('Erro na chave!'),
                FileNotFoundError('Não achei o arquivo'),
                ExceptionGroup(
                    'Nested', [LookupError()]
                ),
            ]
        )
        raise eg
    except* ZeroDivisionError as ze:
        print('Deu ruim dividir por zero', ze)
    except* KeyError as ke:
        print('Não achei a chave', ke)
    except* LookupError as ke:
        print('LookupError', ke)
        
except Exception as e:
    print('Deu erro no grupo!', e)

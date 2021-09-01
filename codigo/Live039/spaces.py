# CERTO
spam(ham[1], {eggs: 2})

# ERRADO
spam( ham[ 1 ], { eggs: 2 } )


# CERTO 3107
def xpto(spam: str='eggs',
         *args: [list, tuple]) -> int:
    return None

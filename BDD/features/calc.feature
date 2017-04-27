# language: pt

# Behave
# pip install behave

Funcionalidade: Soma
    Cenario: adicao basica
        Quando somar "2" com "2"
        Então o resultado deve ser "4"

    Cenario: adicao do ponto flutuante
        Quando somar "2.0" com "2.0"
        Então o resultado deve ser "4.0"

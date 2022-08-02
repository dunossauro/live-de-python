def soma_x(val_externo):
    def interna(val_interno):
        return val_externo + val_interno
    return interna


soma_1 = soma_x(1)
soma_10 = soma_x(10)

print(soma_1(10))  # 11
print(soma_10(1))  # 11

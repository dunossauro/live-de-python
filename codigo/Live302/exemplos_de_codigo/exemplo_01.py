from decimal import Decimal, localcontext


print(Decimal(1) / Decimal(7))
# 0.1428571428571428571428571429


with localcontext() as ctx:
    ctx.prec = 1
    print(Decimal(1) / Decimal(7))
    # 0.143
    ctx.prec = 4
    print(Decimal(1) / Decimal(7))


print(Decimal(1) / Decimal(7))
# 0.1428571428571428571428571429

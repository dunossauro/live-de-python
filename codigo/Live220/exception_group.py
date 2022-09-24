# """
# In [16]: try:
#     ...:     try:
#     ...:         eg = ExceptionGroup('g',
#     ...:             [
#     ...:                 ZeroDivisionError(),
#     ...:                 KeyError()
#     ...:             ]
#     ...:         )
#     ...:         raise eg
#     ...:     except* ZeroDivisionError as ze:
#     ...:         print('Divisão por Zero')
#     ...:     except* IndexError as ie:
#     ...:         print('Erro de chave')
#     ...: except ExceptionGroup as eg:
#     ...:     print('Erro do grupo!')
#     ...: 
# """
# # eg = ExceptionGroup(
# #     'one', [
# #         TypeError(),
# #         ZeroDivisionError(),
# #         KeyError()
# #     ]
# # )

# # try:
# #     raise eg
# # except* Exception as ee:
# #     print('Erro genérico!', ee)
# # except* ZeroDivisionError as ze:
# #     print('Erro de divisão!', ze)
# # except* KeyError as ke:
# #     print('Erro de chaves!', ke)
# # except* TypeError as te:
# #     print('Erro de tipo', te)
# # # except* ExceptionGroup as eg:
# # #     print('Erro no grupo')


# # from asyncio import gather, get_event_loop
# from random import randint

# async def xpto(name):
#     r = randint(1, 10)
#     match (r):
#         case 1:
#             raise KeyError(name)
#         case 2:
#             raise TypeError(name)
#         case 3:
#             raise IndexError(name)
#         case _:
#             return 'OK!'


# # async def main():
# #     g = gather(
# #         *[xpto(), xpto(), xpto(), xpto(), xpto(), xpto()]
# #     )
# #     eg = ExceptionGroup(
# #         'XPTO TASK',
# #         [KeyError(), TypeError(), IndexError()]
# #     )
# #     result = []
# #     try:
# #         try:
# #             result = await g
# #         except Exception as e:
# #             raise eg
# #     except* KeyError as ke:
# #         print('KeyError', ke)
# #     except* TypeError as te:
# #         print('TypeError', te)
# #     except* IndexError as ie:
# #         print('IndexError', ie)

# #     return result


# # loop = get_event_loop()
# # print(
# #     loop.run_until_complete(main())
# # )

# from asyncio import TaskGroup, run

# async def main():
#     r1 = 'FAIL'
#     r2 = 'FAIL'
#     r3 = 'FAIL'
#     r4 = 'FAIL'

#     try:
#         async with TaskGroup() as tg:
#             task1 = tg.create_task(xpto(1))
#             task2 = tg.create_task(xpto(2))
#             task3 = tg.create_task(xpto(3))
#             task4 = tg.create_task(xpto(4))
#             r1 = await task1
#             r2 = await task2
#             r3 = await task3
#             r4 = await task4

#     except* KeyError as ke:
#         print('KeyError', ke.exceptions[0])

#     except* TypeError as te:
#         print('TypeError', te.exceptions[0])

#     except* IndexError as ie:
#         print('IndexError', ie.exceptions[0])

#     return r1, r2, r3, r4


# print(run(main()))



eg = ExceptionGroup(
    'EG', [
        TypeError(),
        KeyError(),
        ExceptionGroup('NEG', [
            ZeroDivisionError()
        ])
    ]
)

try:
    raise eg
except* TypeError as te:
    print('TypeError', te)
except* KeyError as ke:
    print('KeyError', ke)
except* ZeroDivisionError as ze:
    print('ZeroDivisionError', ze)

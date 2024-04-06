def funcao_com_argumentos_variaveis(arg, *args):
    print("Primeiro argumento:", arg)

    for i in args:
        print("Argumento de *args", i)


funcao_com_argumentos_variaveis('primeiro_arg', 'arg2', 'arg3', 'arg3')


def somar(*args):
    resultado = 0

    for i in args:
        resultado += i

    return resultado


print(somar(1, 2))
print(somar(1, 2, 4, 6))
print(somar(1, 2, 4, 6, 8, 10))


#  ---------------------------------------------------------------


def concatena(**kwargs):
    print(f'Valores recebidos: {kwargs}')
    resultado = ""

    for i in kwargs.values():
        resultado += f'{i} '

    return resultado


print(concatena(primeiro="eu", segundo="estou", terceiro="aqui!"))


def funcao(arg, *args, arg_nomeado, **kwargs):
    print(f'argumento nao nomeado: {arg}')
    print(f'*args: {args}')
    print(f'Argumento nomeado: {arg_nomeado}')
    print(f'**kwargs: {kwargs}')


funcao("a",                  # (argumento nao nomeados)
       'arg1', 'arg2', 2,  # *args
       arg_nomeado='KW',          # (argumento nomeado)
       kwarg_1='B', kwarg_2='A'   # **kwargs
       )

def inverte_string(texto):
    string_invertida = ''

    for i in range(len(texto)-1, -1, -1):
        string_invertida = string_invertida + texto[i]
    return string_invertida


input = input('Digite uma string: ')

resultado = inverte_string(input)
print(f'A string invertida é: {resultado}')

def soma_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

def substituir_palavra(lista, palavra_procurada, nova_palavra):
    nova_lista = [nova_palavra if palavra == palavra_procurada else palavra for palavra in lista]
    return nova_lista

def gerar_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Exemplos de uso:  

# Questão 1
lista_numeros = [1, 2, 3, 4]
soma, media = soma_media(lista_numeros)
print("Soma:", soma)
print("Média:", media)

# Questão 2
lista_palavras = ["flamengo", "gabigol", "dopping"]
nova_lista = substituir_palavra(lista_palavras, "flamengo", "pedro")
print("Lista alterada:", nova_lista)

# Questão 3
num_linhas = 4
print("Triângulo de asteriscos:")
gerar_triangulo(num_linhas)




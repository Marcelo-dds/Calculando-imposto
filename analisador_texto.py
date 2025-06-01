import string
from collections import Counter
'''
Contagem de palavras: 8
Frequência de palavras: Counter({'Olá': 2, 'mundo': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste': 1, 'novamente': 1})
Frequência de letras: Counter({' ': 7, 'e': 6, 'o': 4, 't': 4, 'm': 3, 'n': 3, 'l': 2, 'á': 2, 'u': 2, 's': 2, 'd': 1, 'é': 1, 'v': 1, 'a': 1})
```

Dica: use o módulo `string` para obter uma lista de caracteres de pontuação. Exemplo:

'''
print(string.punctuation)
#todas as letras 
print(string.ascii_letters)
#todos os numeros 
print(string.digits)

print(Counter(['a', 'b', 'a', 'c', 'b', 'a']))
print(Counter('abacba'))

#solução simples 
#maketran o primeiro parametro e transformar segundo e substituir e o terceiro e remover 
def analisar_texto(texto):
    tratamento = str.maketrans("","",string.punctuation)
    texto_tratado = texto.translate(tratamento)
    palavras = texto_tratado.split()
    contagem_palavras = len(palavras)
    frequencia_palavras = Counter(palavras)
    frequencia_letras = Counter(texto_tratado.lower())
    
    return contagem_palavras, frequencia_palavras, frequencia_letras

texto = "Olá mundo! Este é um teste . Ola novamente"
# quando vc tem mais de um retorno e retornadao uma tupla . usando esse modulo estamos fazendo onepack de tupla associando cada retorno em cada propriedade
contagem_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)

print(f"Contagem de palavras:{contagem_palavras} ")
print(f"Frequencia de palavras:{frequencia_palavras} ")
print(f"Frequencia de Letras:{frequencia_letras} ")

vogais = "aeiou"
numeros = "12345"
remove = "a"
guia_troca = str.maketrans(vogais,numeros,remove)

print(guia_troca)

letras_minusculas = string.ascii_lowercase

print(letras_minusculas.translate(guia_troca))
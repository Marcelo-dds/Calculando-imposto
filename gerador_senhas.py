import string
import random

'''print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

print(random.choice(string.digits))

# usando o parametro choices ele retorna uma lista e o k= ele retorna quantos eu numeros eu pedir 

escolhas = print(random.choices(string.digits,k=5))

random.shuffle(escolhas) # ele embaralha 
'''
def gerar_senha(tamanho):
    if tamanho < 4:
        print("O tamanho tem que ser maior que 4.")
    else:
        senha = [
            random.choice(string.ascii_letters),
            random.choice(string.digits),
            random.choice(string.punctuation),
        ]
        possibilidades = string.ascii_letters + string.digits + string.punctuation
        senha.extend(random.choices(possibilidades, k=tamanho - 3))
        random.shuffle(senha)
        return "".join(senha)

tamanho = int(input("Digite o comprimento da senha: "))
print(gerar_senha(tamanho))
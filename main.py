import string
import os
import requests
import unicodedata

response = requests.get("https://api.dicionario-aberto.net/random")
if response.status_code == 200:
    dados = response.json()
    palavra = dados.get("word")
else:
    print("Erro na requisição")
    palavra = " "

palavra = "teste"
palavra_encripitada = ["_"] * 5
status_letras = [" "] * 5
letras_inexistentes = []
vidas = 5

while True:
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    for i in range(len(palavra_encripitada)):
        print(palavra_encripitada[i],end=" ")
    
    print()
    
    for i in range(len(palavra_encripitada)):
        print(status_letras[i],end=" ")

    print()
    print("Letra que não estão na palavra:",end=" ")
     
    for letra in letras_inexistentes:
        print(letra,end=" ") 

    tentativa = input("\n\nInforme uma palavra:").lower()
    
    for i,letra in enumerate(tentativa):
        print(i)
        palavra_encripitada[i] = letra

        if letra == palavra[i]:
            status_letras[i] = "*"
        elif letra in palavra:
            status_letras[i] = "!"
        else:
            status_letras[i] = "x"
            if letra not in letras_inexistentes:
                letras_inexistentes.append(letra)

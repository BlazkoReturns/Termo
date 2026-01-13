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

palavra_encripitada = ["_"] * len(palavra)
letras_usadas = []
vidas = 5

while True:
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    for i in range(len(palavra_encripitada)):
        print(palavra_encripitada[i],end=" ")

    if "_" not in palavra_encripitada:
         print("\nVocê acertou a palavra.")
         input("Pressione uma tecla para sair..")
         break

    tentativa = input("\n\nInforme uma letra:").lower()
    
    if tentativa in letras_usadas:
        continue

    if tentativa not in string.ascii_lowercase:
        continue  

    letras_usadas.append(tentativa)
    encontrou_letra = False

    for i in range(len(palavra)):
        letra = unicodedata.normalize('NFD', palavra[i]).encode('ascii', 'ignore').decode('utf-8')
        if letra == tentativa:
            palavra_encripitada[i] = palavra[i]
            encontrou_letra = True
    
    if not encontrou_letra:
        vidas -= 1
        
    if vidas == 0:
         print(f"\nVocê perdeu.A palavra era {palavra}")
         input("Pressione uma tecla para sair..")
         break
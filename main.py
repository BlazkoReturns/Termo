import string
import os
import time
import unicodedata
import random

BANCO_DE_PALAVRAS = [
    "termo", "sagaz", "amigo", "nobre", "algoz", "fazer", "ideia", 
    "moral", "poder", "honra", "justo", "muito", "anexo", "etnia"
]

palavra = random.choice(BANCO_DE_PALAVRAS)
palavra_encripitada = ["_"] * 5
status_letras = [" "] * 5
letras_inexistentes = []
vidas = 5

while True:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if not vidas:
        print(f"Não conseguiu desvendar a palavra. A palavra era {palavra}.")
        break
    
    print("* -> letra na posição correta  ! -> letra na posição incorreta  x -> letra não existe na palavra")
    print("Letras que não estão na palavra:",end=" ") 
    print(*letras_inexistentes,end=" ") 
    print(f"\nTentativas restantes: {vidas}\n")
    print(*palavra_encripitada,sep=" ")
    print(*status_letras,sep=" ")

    tentativa = input("\nInforme uma palavra:").lower()
    
    if len(tentativa)  != 5:
        print("Tentativa deve ter exatamente 5 letras.", end="", flush=True)
        for _ in range(3):
           time.sleep(1)
           print(".", end="", flush=True)
        continue

    for i,letra in enumerate(tentativa):
        
        palavra_encripitada[i] = letra
        
        
        if letra == unicodedata.normalize('NFD', palavra[i]).encode('ascii', 'ignore').decode('utf-8'):
            status_letras[i] = "*"
        elif letra in palavra:
            status_letras[i] = "!"
        else:
            status_letras[i] = "x"
            if letra not in letras_inexistentes:
                letras_inexistentes.append(letra)
    
    if "x" in status_letras or "!" in status_letras:
        vidas -= 1
    else:
       print("Parabéns, você desvendou a palavra.")
       break
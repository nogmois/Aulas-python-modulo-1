# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO"
cid = str(input('Em que cidade você nasceu? ')).strip() # tira os espaços laterais
print(cid[:5].upper() == 'SANTO') # deixa tudo MAIUSCULO
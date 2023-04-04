import tkinter as tk

local = []
while True:
    entrada = input("Digite uma localização dos nós da treliça no plano (ou pressione Enter para finalizar): ")
    if entrada:
        local.append(entrada)
    else:
        break

print("Você digitou as seguintes localizações:")
for local in local:
    print(local)
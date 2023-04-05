import tkinter as tk
from tkinter import messagebox

#criação da janela
janela = tk.Tk()
janela.title("Calculador de solução de problemas de estática e resistência dos materiais")

lista_nos = []

#leitura dos nós
label = tk.Label(janela, text="Digite as coordenadas dos nós:")
label.pack()

entry = tk.Entry(janela)
entry.pack()

button = tk.Button(janela, text="Salvar")
button.pack()

text = tk.Text(janela)
text.pack()

#verificação se o número que vem antes da vírgula de um elemento é igual ao de outro elemento
def verificar(info1, info2):
    return info1.split(',')[0] == info2.split(',')[0]

#salva as informações digitadas na caixa de texto e as digita separando os termos linha por linha
def salvar():
    info = entry.get()
    for i, saved_info in enumerate(lista_nos):
        if verificar(info, saved_info):
            lista_nos[i] = info
            text.insert(tk.END, "Elementos com o mesmo valor antes da vírgula!\n")
            break
    else:
        lista_nos.append(info)
    text.delete('1.0', tk.END)
    for info in lista_nos:
        for line in info.split(';'):
            text.insert(tk.END, line + '\n')

#mensagem mostrando a lista contendo os nós            
def msg():            
    messagebox.showinfo("Message", lista_nos)
button.config(command=lambda: [salvar(),msg()])

janela.mainloop()

import tkinter as tk
from tkinter import messagebox

# Cria uma janela principal
janela = tk.Tk()
janela.title("Exemplo de interface gráfica")
largura_janela = 500
altura_janela = 300

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2

janela.geometry("{}x{}+{}+{}".format(largura_janela, altura_janela, pos_x, pos_y))

entrada = tk.Entry(janela, width=50)

botao_salvar = tk.Button(janela, text='Salvar', command=lambda: salvar(entrada.get()))

mensagem = tk.Label(janela, text="")
mensagem.pack()

def salvar(texto):
    mensagem.config(text=texto)
    print('Texto salvo:', texto)

entrada.pack()
botao_salvar.pack()

janela.mainloop()
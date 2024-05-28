import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk

#começar com tela com um botão e um entry (nome)- v1
#adicionar mais duas entrys (cpf e estado) e suas labels - v2
#mudar o fundo para uma imagem mais bonita, adicionar readme.txt explicando como usar - v3
#adicionar clicar no botão salva os 3 dados em um sqlite - v4
#Criar uma branch em que le um config.txt com uma lista de 5 estados possiveis separados por pular linha - x1
#Mudar o separador para ; e adicionar mais 5 estados - x2
#Voltar para main, criar outra branch e criar um dropdown com 3 opções (clt, mei, socio) - y1
#Voltar para main, Corrigir o bug da função de cpf - v5
#Merge de x com v - v6
#Adicionar verificação de CPF e de estado, com base na função cpf e na lista de estados .txt antes de adicionar no sqlite v7

def Main():
    root = tkinter.Tk()
    root.title("Trabalho RAD")
    root.resizable(False, False)

     # Abrir a imagem usando Pillow
    imagem = Image.open("imagem.jpg")

    # Converter a imagem para um formato que o Tkinter possa usar
    imagem_tk = ImageTk.PhotoImage(imagem)

    # Adicionar a imagem de fundo
    canvas = tkinter.Canvas(root, width=imagem.width, height=imagem.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=imagem_tk, anchor="nw")
    
    label = tkinter.Label(root, text="Nome")
    label.pack()

    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e1.pack()

    label = tkinter.Label(root, text="Cpf")
    label.pack()

    textoEntrada = tkinter.StringVar()
    e2 = tkinter.Entry(root)
    e2.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e2.pack()

    label = tkinter.Label(root, text="Estado")
    label.pack()

    textoEntrada = tkinter.StringVar()
    e3 = tkinter.Entry(root)
    e3.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e3.pack()

    root.mainloop()

Main()


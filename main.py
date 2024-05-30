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

def salvar_dados(nome, cpf, estado):
    # Conectar ao banco de dados SQLite (ou criar se não existir)
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome TEXT NOT NULL,
                          cpf TEXT NOT NULL,
                          estado TEXT NOT NULL)''')

    cursor.execute("INSERT INTO clientes (nome, cpf, estado) VALUES (?, ?, ?)", (nome, cpf, estado))
    conn.commit()

    conn.close()

def Main():
    root = tkinter.Tk()
    root.title("Trabalho RAD")
    root.resizable(False, False)

    # Abrir a imagem usando Pil
    imagem = Image.open("imagem.jpg")

    # Converter a imagem o Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem)

    # Adicionar a imagem de fundo
    canvas = tkinter.Canvas(root, width=imagem.width, height=imagem.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=imagem_tk, anchor="nw")
    
    label = tkinter.Label(canvas, text="Nome")
    label.place(x=50, y=50) 

    textoEntradaNome = tkinter.StringVar()
    e1 = tkinter.Entry(canvas, textvariable=textoEntradaNome)
    e1.place(x=150, y=50) 

    label = tkinter.Label(canvas, text="Cpf")
    label.place(x=50, y=80)  

    textoEntradaCpf = tkinter.StringVar()
    e2 = tkinter.Entry(canvas, textvariable=textoEntradaCpf)
    e2.place(x=150, y=80)  

    label = tkinter.Label(canvas, text="Estado")
    label.place(x=50, y=110)  

    textoEntradaEstado = tkinter.StringVar()
    e3 = tkinter.Entry(canvas, textvariable=textoEntradaEstado)
    e3.place(x=150, y=110) 

    # Botão para salvar
    botao_salvar = tkinter.Button(canvas, text="Salvar", command=lambda: salvar_dados(textoEntradaNome.get(), textoEntradaCpf.get(), textoEntradaEstado.get()))
    botao_salvar.place(x=50, y=150) 

    root.mainloop()

Main()

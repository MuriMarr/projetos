import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import csv
import os

# Registro de horário de entrada
def registrar_entrada():
    agora = datetime.now()
    data = agora.strftime("%Y-%m-%d")
    hora_entrada = agora.strftime("%H:%M:%S")
    with open('cartão_ponto.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data, hora_entrada, ''])
        messagebox.showinfo("Registro de Entrada", f"Entrada registrada em {hora_entrada}")

# Registro de horário de saída
def registrar_saida():
    agora = datetime.now()
    data = agora.strftime("%Y-%m-%d")
    hora_saida = agora.strftime("%H:%M:%S")

    # Ler dados existentes
    registros = []
    with open('cartao_ponto.csv', 'r') as file:
        reader = csv.reader(file)
        registros = list(reader)
    
    # Atualização do último registro de entrada com a hora de saída
    for registro in reversed(registros):
        if registro[0] == data and registro[2] == '':
            registro[2] = hora_saida
            break
    
    # Escrever os dados atualizados de volta no arquivo

    with open('cartao_ponto.csv', 'w', newline= '') as file:
        writer = csv.writer(file)
        writer.writerows(registros)

    messagebox.showinfo("Registro de Saída", f"Saída registrada em {hora_saida}")

# Janela principal
janela = tk.Tk()
janela.title("Cartão de Ponto Digital")

# Arquivo CSV (se não existir, criar com cabeçalho)
if not os.path.exists('cartao_ponto.csv'):
    with open('cartao_ponto.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data", "Entrada", "Saída"])

# Botão para registrar entrada
botao_entrada = tk.Button(janela, text="Registrar Entrada", command=registrar_entrada)
botao_entrada.pack(padx=10, pady=10)

# Botão para registrar saída
botao_saida = tk.Button(janela, text="Registrar Saída", command=registrar_saida)
botao_saida.pack(padx=10, pady=10)

# Iniciar o Loop principal da interface
janela.mainloop()
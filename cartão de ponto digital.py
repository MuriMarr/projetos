import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import sqlite3
import os

conn = sqlite3.connect('ponto.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS ponto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    hora_entrada TEXT,
    hora_saida TEXT
    )
''')
conn.commit()

# Carregar registros pelo TreeView
def carregar_registros():
    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("SELECT data, hora_entrada, hora_saida FROM ponto ORDER BY id DESC LIMIT 20")
    registros = cursor.fetchall()

    for registro in registros:
        tree.insert('', 'end', values=registro)

# Registro de horário de entrada
def registrar_entrada():
    agora = datetime.now()
    data = agora.strftime("%Y-%m-%d")
    hora_entrada = agora.strftime("%H:%M:%S")
    
    cursor.execute("INSERT INTO ponto (data, hora_entrada) VALUES (?, ?)", (data, hora_entrada))
    conn.commit()
    messagebox.showinfo("Registro de Entrada", f"Entrada registrada em {hora_entrada}")

# Registro de horário de saída
def registrar_saida():
    agora = datetime.now()
    data = agora.strftime("%Y-%m-%d")
    hora_saida = agora.strftime("%H:%M:%S")

    cursor.execute("""SELECT id FROM ponto WHERE data = ? AND hora_saida IS NULL""", (data,))
    resultados = cursor.fetchall()
    
    if resultados:
        ultimo_id = resultados[-1][0]
        cursor.execute("UPDATE ponto SET hora_saida = ? WHERE id = ?", (hora_saida, ultimo_id))
        conn.commit()
        messagebox.showinfo("Registro de Saída", f"Saída registrada em {hora_saida}")
    else:
        messagebox.showwarning("Atenção", "Nenhum registro de entrada encontrado para hoje.")

    carregar_registros()

# Janela principal
janela = tk.Tk()
janela.title("Cartão de Ponto Digital")

# Botões para registrar entrada e saída
tk.Button(janela, text="Registrar Entrada", command=registrar_entrada).pack(padx=10, pady=10)
tk.Button(janela, text="Registrar Saída", command=registrar_saida).pack(padx=10, pady=10)

# TreeView (tabela)
colunas = ("Data", "Entrada", "Saída")
tree = ttk.Treeview(janela, columns=colunas, show='headings')
for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(padx=10, pady=10)

# Carregar registros ao iniciar
carregar_registros()

janela.mainloop()

# Encerra a conexão com o banco de dados
conn.close()
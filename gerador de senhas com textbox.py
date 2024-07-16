import tkinter as tk
import string
import random

# Função para gerar uma senha aleatória
def gerar_senha(tamanho=9, maiusculas=True, minusculas=True, digitos=True, simbolos=True):
    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if digitos:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Função para exibir a senha gerada
def exibir_senha():
     senha = gerar_senha()
     entrada_senha.delete(0, tk.END)
     entrada_senha.insert(0, senha)

# Janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Textbox da senha
entrada_senha = tk.Entry(janela, width=50)
entrada_senha.pack(padx=10, pady=10)

# Botão para gerar a senha
botao_gerar = tk.Button(janela, text="Gerar Senha", command=exibir_senha)
botao_gerar.pack(padx=10, pady=10)

# Iniciar o loop principal da interface
janela.mainloop()
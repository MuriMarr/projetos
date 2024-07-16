import random
import string

def gerar_senha(tamanho=15, maiusculas=True, minusculas=True, digitos=True, simbolos=True):
    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if digitos:   
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        raise ValueError("Pelo menos uma categoria de caracteres deve ser selecionado.")
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
        print("Iniciando o gerador de senhas...")
        tamanho = int(input("Digite o tamanho da senha: "))
        incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'        
        incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
        incluir_digitos = input("Incluir dígitos? (s/n): ").lower() == 's'
        incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'
    
        senha = gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_digitos, incluir_simbolos)
        print(f"Senha gerada: {senha}")

if __name__ == "__main__":
    main()
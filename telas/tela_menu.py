import tkinter as tk

# Função para criar a tela de cada tema
def abrir_tela(titulo, aula_texto):
    tela = tk.Toplevel(root)
    tela.title(titulo)
    tela.geometry("500x400")
    tela.configure(bg="#274C5C")

    tk.Label(
        tela, text=f"Aula de {titulo}",
        font=("Arial", 16, "bold"),
        bg="#274C5C", fg="white"
    ).pack(pady=10)

    tk.Label(
        tela, text=aula_texto,
        wraplength=450, justify="left",
        bg="#274C5C", fg="white"
    ).pack(pady=10)

    tk.Label(
        tela, text="👉 Em breve: exercícios interativos!",
        fg="yellow", bg="#274C5C"
    ).pack(pady=20)

    tk.Button(
        tela, text="Voltar ao Menu", command=tela.destroy,
        bg="#1ABC9C", fg="white", relief="groove", padx=10, pady=5
    ).pack(pady=10)


# Funções para cada tema
def abrir_soma(): abrir_tela("Soma", "A soma é a operação de juntar valores. Exemplo: 2 + 3 = 5")
def abrir_subtracao(): abrir_tela("Subtração", "A subtração é a operação de retirar valores. Exemplo: 7 - 2 = 5")
def abrir_multiplicacao(): abrir_tela("Multiplicação", "A multiplicação é uma soma repetida. Exemplo: 3 × 4 = 12")
def abrir_divisao(): abrir_tela("Divisão", "A divisão reparte um valor em partes iguais. Exemplo: 12 ÷ 3 = 4")
def abrir_fracoes(): abrir_tela("Frações", "Frações representam partes de um todo. Exemplo: 1/2 significa metade.")
def abrir_potencias(): abrir_tela("Potências", "Potência é multiplicar um número por ele mesmo. Exemplo: 2² = 2 × 2 = 4")
def abrir_raizes(): abrir_tela("Raízes", "Raiz quadrada é o número que multiplicado por ele mesmo dá o valor. Exemplo: √9 = 3")
def abrir_porcentagens(): abrir_tela("Porcentagens", "Porcentagem indica uma parte de 100. Exemplo: 25% de 200 = 50")


# Janela principal
root = tk.Tk()
root.title("EducaMath - Menu Principal")
root.geometry("600x600")
root.configure(bg="#274C5C")

# Boas-vindas
tk.Label(
    root, text="👋 Bem-vindo ao EducaMath!",
    font=("Arial", 18, "bold"),
    fg="white", bg="#274C5C"
).pack(pady=20)

# Estilo dos botões
estilo_btn = {
    "width": 20,
    "bg": "#1ABC9C",
    "fg": "white",
    "activebackground": "#118F76",
    "activeforeground": "white",
    "relief": "groove",
    "bd": 3,
    "font": ("Arial", 12, "bold"),
    "padx": 5,
    "pady": 5
}

# Frame para centralizar os botões em grade
frame_botoes = tk.Frame(root, bg="#274C5C")
frame_botoes.pack(pady=20)

# Lista de botões
botoes = [
    ("Soma", abrir_soma),
    ("Subtração", abrir_subtracao),
    ("Multiplicação", abrir_multiplicacao),
    ("Divisão", abrir_divisao),
    ("Frações", abrir_fracoes),
    ("Potências", abrir_potencias),
    ("Raízes", abrir_raizes),
    ("Porcentagens", abrir_porcentagens),
]

# Distribuir os botões em 2 colunas
for i, (texto, comando) in enumerate(botoes):
    linha = i // 2
    coluna = i % 2
    tk.Button(frame_botoes, text=texto, command=comando, **estilo_btn).grid(row=linha, column=coluna, padx=10, pady=10)

# Botão de saída
tk.Button(
    root, text="Sair do EducaMath",
    command=root.quit,
    bg="red", fg="white",
    font=("Arial", 12, "bold"),
    width=25, relief="ridge"
).pack(pady=30)

root.mainloop()

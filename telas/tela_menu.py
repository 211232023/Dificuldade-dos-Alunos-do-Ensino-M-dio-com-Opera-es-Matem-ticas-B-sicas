# telas/tela_menu.py

import tkinter as tk
# Importamos o dicionário de conteúdo para saber quais botões criar
from conteudo.dados import CONTEUDO_EDUCACIONAL

class TelaMenu(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#274C5C")
        
        # O 'controller' é a função em main.py que troca de tela
        self.controller = controller

        # Boas-vindas
        tk.Label(
            self, text="👋 Bem-vindo ao EducaMath!",
            font=("Arial", 18, "bold"),
            fg="white", bg="#274C5C"
        ).pack(pady=20)

        # Estilo dos botões (copiado do seu código)
        estilo_btn = {
            "width": 20, "bg": "#1ABC9C", "fg": "white",
            "activebackground": "#118F76", "activeforeground": "white",
            "relief": "groove", "bd": 3, "font": ("Arial", 12, "bold"),
            "padx": 5, "pady": 5
        }

        frame_botoes = tk.Frame(self, bg="#274C5C")
        frame_botoes.pack(pady=20)

        nomes_botoes = {
            "Adicao": "Soma",
            "Subtracao": "Subtração",
            "Multiplicacao": "Multiplicação",
            "Divisao": "Divisão",
            "Potenciacao": "Potências",
            "Radiciacao": "Raízes",
            "Logaritmicao": "Logaritmos",
        }
        
        botoes_info = list(nomes_botoes.items())

        for i, (chave, texto) in enumerate(botoes_info):
            linha = i // 2
            coluna = i % 2
            
            # O comando agora chama o controller, passando a chave do tópico
            comando = lambda c=chave: self.controller(c)
            
            tk.Button(
                frame_botoes, text=texto, command=comando, **estilo_btn
            ).grid(row=linha, column=coluna, padx=10, pady=10)

        # Botão de saída
        tk.Button(
            self, text="Sair do EducaMath",
            command=self.quit, # Comando para fechar o programa
            bg="red", fg="white",
            font=("Arial", 12, "bold"),
            width=25, relief="ridge"
        ).pack(pady=30)
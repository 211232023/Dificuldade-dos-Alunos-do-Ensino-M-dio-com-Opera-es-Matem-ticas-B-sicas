# telas/tela_menu.py

import tkinter as tk
from conteudo.dados import CONTEUDO_EDUCACIONAL

class TelaMenu(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#274C5C")
        
        self.controller = controller

        main_frame = tk.Frame(self, bg="#274C5C")
        main_frame.pack(expand=True)

        # Boas-vindas com fonte maior
        tk.Label(
            main_frame, text="👋 Bem-vindo ao EducaMath!",
            font=("Arial", 36, "bold"),
            fg="white", bg="#274C5C"
        ).pack(pady=(30, 10))

        # --- MUDANÇA SUTIL: Adicionando um subtítulo/instrução ---
        tk.Label(
            main_frame, text="Selecione um tópico abaixo para começar a aprender.",
            font=("Arial", 16),
            fg="#BDC3C7", bg="#274C5C" # Cor cinza claro
        ).pack(pady=(0, 30))

        estilo_btn = {
            "width": 20, "bg": "#1ABC9C", "fg": "white",
            "activebackground": "#118F76", "activeforeground": "white",
            "relief": "groove", "bd": 3, "font": ("Arial", 16, "bold"),
            "padx": 10, "pady": 10
        }

        frame_botoes = tk.Frame(main_frame, bg="#274C5C")
        frame_botoes.pack(pady=20, padx=20)

        nomes_botoes = {
            "Adicao": "Soma", "Subtracao": "Subtração",
            "Multiplicacao": "Multiplicação", "Divisao": "Divisão",
            "Potenciacao": "Potências", "Radiciacao": "Raízes",
            "Logaritmicao": "Logaritmos",
        }
        
        botoes_info = list(nomes_botoes.items())

        for i, (chave, texto) in enumerate(botoes_info):
            linha = i // 2
            coluna = i % 2
            
            comando = lambda c=chave: self.controller(c)
            
            tk.Button(
                frame_botoes, text=texto, command=comando, **estilo_btn
            ).grid(row=linha, column=coluna, padx=15, pady=15)

        tk.Button(
            main_frame, text="Sair do EducaMath",
            command=self.quit,
            bg="#E74C3C", fg="white",
            font=("Arial", 14, "bold"),
            width=25, relief="ridge"
        ).pack(pady=40)
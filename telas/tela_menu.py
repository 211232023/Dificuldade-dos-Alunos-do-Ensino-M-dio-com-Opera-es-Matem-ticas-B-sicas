# telas/tela_menu.py

import tkinter as tk
from conteudo.dados import CONTEUDO_EDUCACIONAL
from estilos import CORES, FONTES # Importação centralizada

# --- Widget Customizado para Botões com Hover e Clique ---
class HoverButton(tk.Button):
    def __init__(self, master, hover_color, click_color, **kw):
        super().__init__(master=master, **kw)
        self.default_bg = self["background"]
        self.hover_color = hover_color
        self.click_color = click_color
        
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
        self.bind("<ButtonRelease-1>", self.on_release)

    def on_enter(self, e):
        self['background'] = self.hover_color

    def on_leave(self, e):
        self['background'] = self.default_bg

    def on_click(self, e):
        self['background'] = self.click_color

    def on_release(self, e):
        # Ao soltar o clique, volta para a cor de hover se o mouse estiver sobre o botão
        if self.winfo_containing(e.x_root, e.y_root) == self:
            self['background'] = self.hover_color
        else:
            self['background'] = self.default_bg

class TelaMenu(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg=CORES["background"])
        
        self.controller = controller

        main_frame = tk.Frame(self, bg=CORES["background"])
        main_frame.pack(expand=True, padx=60, pady=40)

        # Título com ícone
        tk.Label(
            main_frame, text="📚 EducaMath",
            font=FONTES["titulo"],
            fg=CORES["texto_titulo"], bg=CORES["background"]
        ).pack(pady=(20, 10))

        tk.Label(
            main_frame, text="Sua jornada no mundo da matemática começa aqui.",
            font=("Arial", 18),
            fg=CORES["texto_primario"], bg=CORES["background"]
        ).pack(pady=(0, 50))

        estilo_btn_topicos = {
            "bg": CORES["acento_primario"],
            "fg": CORES["texto_titulo"],
            "activebackground": CORES["botao_click"],
            "activeforeground": CORES["texto_titulo"],
            "relief": "flat", "bd": 0,
            "font": ("Arial", 15, "bold"),
            "width": 20, "pady": 15
        }

        frame_botoes = tk.Frame(main_frame, bg=CORES["background"])
        frame_botoes.pack(pady=20, padx=20)

        nomes_botoes = {
            "Adicao": "Soma", "Subtracao": "Subtração",
            "Multiplicacao": "Multiplicação", "Divisao": "Divisão",
            "Potenciacao": "Potências", "Radiciacao": "Raízes",
            "Logaritmicao": "Logaritmos", "Fracao": "Frações" # <-- BOTÃO ADICIONADO AQUI
        }
        
        botoes_info = list(nomes_botoes.items())

        for i, (chave, texto) in enumerate(botoes_info):
            linha = i // 2
            coluna = i % 2
            comando = lambda c=chave: self.controller(c)
            
            btn = HoverButton(frame_botoes, 
                              hover_color=CORES["botao_hover"],
                              click_color=CORES["botao_click"],
                              text=texto, command=comando, **estilo_btn_topicos)
            btn.grid(row=linha, column=coluna, padx=20, pady=15)

        estilo_btn_sair = {
            "bg": CORES["botao_sair"],
            "fg": "white",
            "activebackground": CORES["botao_sair_hover"],
            "activeforeground": "white",
            "relief": "flat", "bd": 0,
            "font": ("Arial", 14, "bold"),
            "width": 25, "pady": 15
        }

        HoverButton(
            main_frame, text="Sair do EducaMath",
            command=self.quit,
            hover_color=CORES["botao_sair_hover"],
            click_color=CORES["botao_sair_hover"],
            **estilo_btn_sair
        ).pack(pady=60)
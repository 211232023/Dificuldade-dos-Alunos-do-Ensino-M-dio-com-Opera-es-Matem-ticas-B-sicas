# telas/tela_topico.py

import tkinter as tk
# --- CORREÇÃO AQUI ---
# Adicionamos o 'D' que faltava em CONTEUDO_EDUCACIONAL
from conteudo.dados import CONTEUDO_EDUCACIONAL

class TelaTopico(tk.Frame):
    def __init__(self, master, nome_topico_chave, voltar_callback):
        super().__init__(master, bg="#274C5C")
        
        info = CONTEUDO_EDUCACIONAL[nome_topico_chave]

        # --- DEFINIÇÃO DE FONTES PARA MELHOR HIERARQUIA ---
        self.FONTE_TITULO = ("Arial", 28, "bold")
        self.FONTE_SUBTITULO = ("Arial", 18, "bold")
        self.FONTE_PARAGRAFO = ("Arial", 14)
        self.FONTE_CODIGO = ("Courier", 14, "bold")

        # --- LAYOUT PRINCIPAL (TÍTULO, CONTEÚDO, BOTÕES) ---
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 1. TÍTULO
        frame_titulo = tk.Frame(self, bg="#274C5C")
        frame_titulo.grid(row=0, column=0, sticky="ew", padx=50, pady=(20,10))
        
        tk.Label(
            frame_titulo, text=info["titulo"], font=self.FONTE_TITULO, 
            bg="#274C5C", fg="white"
        ).pack()

        # --- ÁREA DE ROLAGEM PARA O CONTEÚDO ---
        # 2. ÁREA DE CONTEÚDO COM SCROLL
        canvas = tk.Canvas(self, bg="#274C5C", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#274C5C")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.grid(row=1, column=0, sticky="nsew", padx=(50, 30))
        scrollbar.grid(row=1, column=1, sticky="ns")
        
        # Renderiza o conteúdo DENTRO do frame rolável
        self.renderizar_conteudo(scrollable_frame, info["teoria"])

        # 3. BOTÕES NA PARTE INFERIOR
        frame_botoes = tk.Frame(self, bg="#274C5C")
        frame_botoes.grid(row=2, column=0, sticky="ew", pady=20)
        frame_botoes.grid_columnconfigure(0, weight=1)
        frame_botoes.grid_columnconfigure(2, weight=1)

        tk.Button(
            frame_botoes, text="Voltar ao Menu", command=voltar_callback,
            bg="#1ABC9C", fg="white", font=("Arial", 14, "bold"), relief="groove", padx=10, pady=10
        ).grid(row=0, column=1, pady=10)

    def renderizar_conteudo(self, master_frame, teoria):
        # Esta função desenha o conteúdo dentro da área de rolagem
        for item in teoria:
            tipo = item.get("tipo", "")
            
            if tipo in ["paragrafo", "subtitulo", "codigo"]:
                conteudo = item.get("conteudo", "")
                if tipo == "paragrafo":
                    tk.Label(master_frame, text=conteudo, font=self.FONTE_PARAGRAFO, wraplength=800, 
                              justify="left", bg="#274C5C", fg="white").pack(pady=5, padx=10, anchor="w")
                elif tipo == "subtitulo":
                    tk.Label(master_frame, text=conteudo, font=self.FONTE_SUBTITULO,
                              bg="#274C5C", fg="white").pack(pady=(15, 5), padx=10, anchor="w")
                elif tipo == "codigo":
                    tk.Label(master_frame, text=conteudo, font=self.FONTE_CODIGO, justify="left",
                              bg="#34495E", fg="#ECF0F1", relief="sunken", bd=2).pack(pady=10, padx=20, anchor="w")
            
            elif tipo in ["lista_ordenada", "lista_nao_ordenada"]:
                itens_da_lista = item.get("itens", [])
                for i, texto_item in enumerate(itens_da_lista):
                    prefixo = f"{i+1}. " if tipo == "lista_ordenada" else "• "
                    tk.Label(master_frame, text=prefixo + texto_item, font=self.FONTE_PARAGRAFO, 
                              wraplength=780, justify="left", bg="#274C5C", fg="white"
                              ).pack(pady=2, padx=25, anchor="w")
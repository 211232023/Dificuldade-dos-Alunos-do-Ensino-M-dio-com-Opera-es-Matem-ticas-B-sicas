# telas/tela_topico.py

import tkinter as tk
from conteudo.dados import CONTEUDO_EDUCACIONAL

class TelaTopico(tk.Frame):
    def __init__(self, master, nome_topico_chave, voltar_callback, exercicios_callback):
        super().__init__(master, bg="#274C5C")
        
        info = CONTEUDO_EDUCACIONAL[nome_topico_chave]

        # --- Callbacks ---
        self.voltar_callback = voltar_callback
        self.exercicios_callback = exercicios_callback
        self.nome_topico_chave = nome_topico_chave
        
        # Fontes...
        self.FONTE_TITULO = ("Arial", 32, "bold")
        self.FONTE_SUBTITULO = ("Arial", 20, "bold")
        self.FONTE_PARAGRAFO = ("Arial", 16)
        self.FONTE_CODIGO = ("Courier", 16)
        
        # Layout...
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 1. TÍTULO
        tk.Label(self, text=info["titulo"], font=self.FONTE_TITULO, bg="#274C5C", fg="white").grid(row=0, column=0, pady=(30, 15))

        # 2. ÁREA DE CONTEÚDO...
        canvas = tk.Canvas(self, bg="#274C5C", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#2C3E50", padx=20, pady=20)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas_window, width=e.width))
        canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=1, column=0, sticky="nsew", padx=100)
        scrollbar.grid(row=1, column=1, sticky="ns")
        
        self.renderizar_conteudo(scrollable_frame, info["teoria"])

        # --- MUDANÇA PRINCIPAL AQUI ---
        # 3. FRAME INFERIOR PARA OS BOTÕES
        frame_botoes = tk.Frame(self, bg="#274C5C")
        frame_botoes.grid(row=2, column=0, pady=30)
        
        tk.Button(
            frame_botoes, text="Praticar com Exercícios", 
            # Chama a nova função, passando a chave do tópico atual
            command=lambda: self.exercicios_callback(self.nome_topico_chave),
            bg="#2ECC71", fg="white", font=("Arial", 14, "bold"), relief="groove", padx=15, pady=10
        ).pack(side="left", padx=20)
        
        tk.Button(
            frame_botoes, text="Voltar ao Menu", command=self.voltar_callback,
            bg="#3498DB", fg="white", font=("Arial", 14, "bold"), relief="groove", padx=15, pady=10
        ).pack(side="left", padx=20)

    def renderizar_conteudo(self, master_frame, teoria):
        # (Esta função permanece a mesma, sem alterações)
        master_frame.columnconfigure(0, weight=1)
        for item in teoria:
            tipo = item.get("tipo", "")
            if tipo in ["paragrafo", "subtitulo", "codigo"]:
                conteudo = item.get("conteudo", "")
                widget_args = {"master": master_frame, "text": conteudo, "wraplength": 800, "justify": "center", "bg": "#2C3E50", "fg": "white"}
                if tipo == "paragrafo":
                    tk.Label(**widget_args, font=self.FONTE_PARAGRAFO).pack(pady=10)
                elif tipo == "subtitulo":
                    subtitulo_args = widget_args.copy()
                    subtitulo_args["fg"] = "#1ABC9C"
                    tk.Label(**subtitulo_args, font=self.FONTE_SUBTITULO).pack(pady=(20, 10))
                elif tipo == "codigo":
                    codigo_args = widget_args.copy()
                    codigo_args["bg"] = "#34495E"
                    codigo_args["fg"] = "#ECF0F1"
                    tk.Label(**codigo_args, font=self.FONTE_CODIGO, relief="sunken", bd=2, padx=10, pady=10).pack(pady=15)
            elif tipo in ["lista_ordenada", "lista_nao_ordenada"]:
                itens_da_lista = item.get("itens", [])
                for i, texto_item in enumerate(itens_da_lista):
                    prefixo = f"{i+1}. " if tipo == "lista_ordenada" else "• "
                    tk.Label(master_frame, text=prefixo + texto_item, font=self.FONTE_PARAGRAFO, wraplength=780, justify="left", bg="#2C3E50", fg="white").pack(pady=3, anchor="w", padx=30)
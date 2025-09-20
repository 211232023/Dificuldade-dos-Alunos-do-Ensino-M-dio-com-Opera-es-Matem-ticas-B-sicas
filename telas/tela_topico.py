# telas/tela_topico.py

import tkinter as tk
from conteudo.dados import CONTEUDO_EDUCACIONAL

class TelaTopico(tk.Frame):
    def __init__(self, master, nome_topico_chave, voltar_callback, exercicios_callback):
        super().__init__(master, bg="#274C5C")
        
        info = CONTEUDO_EDUCACIONAL[nome_topico_chave]

        # Callbacks
        self.voltar_callback = voltar_callback
        self.exercicios_callback = exercicios_callback
        self.nome_topico_chave = nome_topico_chave
        
        # Fontes
        self.FONTE_TITULO = ("Arial", 32, "bold")
        self.FONTE_SUBTITULO = ("Arial", 20, "bold")
        self.FONTE_PARAGRAFO = ("Arial", 16)
        self.FONTE_PARAGRAFO_BOLD = ("Arial", 16, "bold")
        self.FONTE_CODIGO = ("Courier", 16)

        # Layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 1. TÍTULO
        tk.Label(self, text=info["titulo"], font=self.FONTE_TITULO, bg="#274C5C", fg="white").grid(row=0, column=0, pady=(30, 15))

        # 2. ÁREA DE CONTEÚDO
        self.text_area = tk.Text(self, bg="#2C3E50", fg="white", padx=40, pady=20,
                                 font=self.FONTE_PARAGRAFO, relief="flat", wrap="word",
                                 highlightthickness=0, borderwidth=0)
        self.text_area.grid(row=1, column=0, sticky="nsew", padx=100)
        
        # Configurando as "tags" de estilo
        self.text_area.tag_configure("bold", font=self.FONTE_PARAGRAFO_BOLD)
        self.text_area.tag_configure("subtitulo", font=self.FONTE_SUBTITULO, foreground="#1ABC9C", justify="center")
        self.text_area.tag_configure("codigo", font=self.FONTE_CODIGO, background="#34495E", foreground="#ECF0F1")
        self.text_area.tag_configure("center", justify="center")
        self.text_area.tag_configure("left", justify="left")
        
        # Barra de rolagem
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.text_area.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.text_area.config(yscrollcommand=scrollbar.set)
        
        # Renderiza o conteúdo formatado
        self.renderizar_conteudo_formatado(info["teoria"])
        
        self.text_area.config(state="disabled")

        # 3. BOTÕES
        frame_botoes = tk.Frame(self, bg="#274C5C")
        frame_botoes.grid(row=2, column=0, pady=30)
        
        tk.Button(frame_botoes, text="Praticar com Exercícios", 
                  command=lambda: self.exercicios_callback(self.nome_topico_chave),
                  bg="#2ECC71", fg="white", font=("Arial", 14, "bold"), relief="groove", padx=15, pady=10
                 ).pack(side="left", padx=20)
        
        tk.Button(frame_botoes, text="Voltar ao Menu", command=self.voltar_callback,
                  bg="#3498DB", fg="white", font=("Arial", 14, "bold"), relief="groove", padx=15, pady=10
                 ).pack(side="left", padx=20)

    # --- NOVA FUNÇÃO AUXILIAR ---
    def traduzir_simbolos(self, texto):
        """
        Substitui códigos LaTeX-like por caracteres Unicode corretos.
        """
        substituicoes = {
            '$': '', # Remove os delimitadores de matemática
            '\\times': '×', # Símbolo de multiplicação
            '^2': '²',
            '^3': '³',
            '^4': '⁴',
            '^1': '¹',
            '^0': '⁰',
            # Adicione outras substituições se necessário, como '{' e '}'
            '{': '',
            '}': '',
        }
        for codigo, simbolo in substituicoes.items():
            texto = texto.replace(codigo, simbolo)
        return texto

    def formatar_e_inserir_texto(self, texto, tags=None):
        if tags is None:
            tags = []
            
        partes = texto.split('**')
        for i, parte in enumerate(partes):
            # --- MUDANÇA: Traduz os símbolos antes de inserir ---
            parte_traduzida = self.traduzir_simbolos(parte)

            if i % 2 == 1: # Ímpar: texto que estava entre '**'
                self.text_area.insert("end", parte_traduzida, ("bold",) + tuple(tags))
            else: # Par: texto normal
                self.text_area.insert("end", parte_traduzida, tuple(tags))

    def renderizar_conteudo_formatado(self, teoria):
        for item in teoria:
            tipo = item.get("tipo", "")
            
            if tipo == "paragrafo":
                self.formatar_e_inserir_texto(item.get("conteudo", ""), tags=["center"])
                self.text_area.insert("end", "\n\n")

            elif tipo == "subtitulo":
                conteudo_traduzido = self.traduzir_simbolos(item.get("conteudo", ""))
                self.text_area.insert("end", f'\n{conteudo_traduzido}\n\n', ("subtitulo",))

            elif tipo == "codigo":
                conteudo_traduzido = self.traduzir_simbolos(item.get("conteudo", ""))
                self.text_area.window_create("end", window=tk.Label(self.text_area, text=conteudo_traduzido,
                                                                      font=self.FONTE_CODIGO, bg="#34495E", fg="#ECF0F1",
                                                                      relief="sunken", bd=2, padx=10, pady=10))
                self.text_area.insert("end", "\n\n")

            elif tipo in ["lista_ordenada", "lista_nao_ordenada"]:
                itens = item.get("itens", [])
                for i, texto_item in enumerate(itens):
                    prefixo = f"  {i+1}. " if tipo == "lista_ordenada" else "  • "
                    self.text_area.insert("end", prefixo, ("left",))
                    self.formatar_e_inserir_texto(texto_item, tags=["left"])
                    self.text_area.insert("end", "\n")
                self.text_area.insert("end", "\n")
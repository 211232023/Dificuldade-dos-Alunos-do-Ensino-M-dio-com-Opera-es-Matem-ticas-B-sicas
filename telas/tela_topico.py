import tkinter as tk
from conteudo.dados import CONTEUDO_EDUCACIONAL
from estilos import CORES, FONTES 
from telas.tela_menu import HoverButton 

class TelaTopico(tk.Frame):
    def __init__(self, master, nome_topico_chave, voltar_callback, exercicios_callback):
        super().__init__(master, bg=CORES["background"])
        
        info = CONTEUDO_EDUCACIONAL[nome_topico_chave]
        self.voltar_callback = voltar_callback
        self.exercicios_callback = exercicios_callback
        self.nome_topico_chave = nome_topico_chave
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        tk.Label(self, text=info["titulo"], font=FONTES["subtitulo"], bg=CORES["background"], fg=CORES["texto_titulo"]).grid(row=0, column=0, pady=(40, 25))

        text_frame = tk.Frame(self, bg=CORES["background_secundario"], bd=2, relief="flat", highlightbackground=CORES["borda"], highlightthickness=1)
        text_frame.grid(row=1, column=0, sticky="nsew", padx=100, pady=10)
        text_frame.grid_rowconfigure(0, weight=1)
        text_frame.grid_columnconfigure(0, weight=1)

        self.text_area = tk.Text(text_frame, bg=CORES["background_secundario"], fg=CORES["texto_primario"], padx=50, pady=30,
                                 font=FONTES["paragrafo"], relief="flat", wrap="word",
                                 highlightthickness=0, borderwidth=0, insertbackground=CORES["texto_titulo"])
        self.text_area.grid(row=0, column=0, sticky="nsew")
        
        self.text_area.tag_configure("bold", font=FONTES["paragrafo_bold"])
        self.text_area.tag_configure("subtitulo", font=FONTES["subtitulo"], foreground=CORES["acento_primario"], justify="center", spacing3=15)
        self.text_area.tag_configure("codigo", font=FONTES["codigo"], background=CORES["codigo_background"], foreground=CORES["texto_primario"])
        self.text_area.tag_configure("center", justify="center", spacing3=10)
        self.text_area.tag_configure("left", justify="left")
        
        scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=self.text_area.yview, bg=CORES["background"], troughcolor=CORES["background_secundario"], activebackground=CORES["acento_primario"])
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.text_area.config(yscrollcommand=scrollbar.set)
        
        self.renderizar_conteudo_formatado(info["teoria"])
        self.text_area.config(state="disabled")

        frame_botoes = tk.Frame(self, bg=CORES["background"])
        frame_botoes.grid(row=2, column=0, pady=40)
        
        estilo_btn = {
            "fg": CORES["texto_titulo"],
            "activeforeground": CORES["texto_titulo"],
            "font": ("Arial", 14, "bold"),
            "relief": "flat", "bd": 0,
            "padx": 25, "pady": 15
        }

        HoverButton(frame_botoes, text="Praticar com Exercícios", 
                    command=lambda: self.exercicios_callback(self.nome_topico_chave),
                    bg=CORES["sucesso"], 
                    hover_color=CORES["sucesso_hover"], 
                    click_color=CORES["sucesso_hover"], **estilo_btn).pack(side="left", padx=20)
        
        HoverButton(frame_botoes, text="Voltar ao Menu", command=self.voltar_callback,
                    bg=CORES["acento_primario"], 
                    hover_color=CORES["botao_hover"],
                    click_color=CORES["botao_click"], **estilo_btn).pack(side="left", padx=20)

    def traduzir_simbolos(self, texto):
        substituicoes = {'$': '', '\\times': '×', '^2': '²', '^3': '³', '^4': '⁴', '^1': '¹', '^0': '⁰', '{': '', '}': ''}
        for codigo, simbolo in substituicoes.items():
            texto = texto.replace(codigo, simbolo)
        return texto

    def formatar_e_inserir_texto(self, texto, tags=None):
        tags = tuple(tags) if tags else ()
        partes = texto.split('**')
        for i, parte in enumerate(partes):
            parte_traduzida = self.traduzir_simbolos(parte)
            current_tags = ("bold",) + tags if i % 2 == 1 else tags
            self.text_area.insert("end", parte_traduzida, current_tags)

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
                code_frame = tk.Frame(self.text_area, bg=CORES["codigo_background"], padx=20, pady=20)
                tk.Label(code_frame, text=conteudo_traduzido,
                         font=FONTES["codigo"], bg=CORES["codigo_background"], fg=CORES["texto_primario"], justify="left").pack()
                self.text_area.window_create("end", window=code_frame)
                self.text_area.insert("end", "\n\n")

            elif tipo in ["lista_ordenada", "lista_nao_ordenada"]:
                itens = item.get("itens", [])
                for i, texto_item in enumerate(itens):
                    prefixo = f"  {i+1}. " if tipo == "lista_ordenada" else "  • "
                    self.text_area.insert("end", prefixo, ("left", "bold"))
                    self.formatar_e_inserir_texto(texto_item, tags=["left"])
                    self.text_area.insert("end", "\n")
                self.text_area.insert("end", "\n")
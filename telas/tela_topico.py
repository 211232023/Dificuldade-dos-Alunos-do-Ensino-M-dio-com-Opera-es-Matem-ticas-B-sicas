# telas/tela_topico.py

import tkinter as tk
from conteudo.dados import CONTEUDO_EDUCACIONAL

class TelaTopico(tk.Frame):
    def __init__(self, master, nome_topico_chave, voltar_callback):
        super().__init__(master, bg="#274C5C")
        
        self.voltar_callback = voltar_callback
        
        info = CONTEUDO_EDUCACIONAL[nome_topico_chave]
        
        tk.Label(
            self, text=info["titulo"],
            font=("Arial", 18, "bold"), bg="#274C5C", fg="white"
        ).pack(pady=10)

        # --- INÍCIO DA CORREÇÃO ---
        # Agora o loop trata cada 'tipo' de forma segura
        for item in info["teoria"]:
            tipo = item.get("tipo", "") # Usar .get() é mais seguro
            
            if tipo in ["paragrafo", "subtitulo", "codigo"]:
                conteudo = item.get("conteudo", "")
                if tipo == "paragrafo":
                    tk.Label(
                        self, text=conteudo, wraplength=450, justify="left",
                        bg="#274C5C", fg="white"
                    ).pack(pady=5, padx=10, anchor="w")
                elif tipo == "subtitulo":
                    tk.Label(
                        self, text=conteudo, font=("Arial", 14, "bold"),
                        bg="#274C5C", fg="white"
                    ).pack(pady=(10, 5), padx=10, anchor="w")
                elif tipo == "codigo":
                    tk.Label(
                        self, text=conteudo, font=("Courier", 12), justify="left",
                        bg="#333", fg="#FFF"
                    ).pack(pady=10, padx=20, anchor="w")

            elif tipo in ["lista_ordenada", "lista_nao_ordenada"]:
                # Pega a lista da chave "itens"
                itens_da_lista = item.get("itens", [])
                for i, texto_item in enumerate(itens_da_lista):
                    prefixo = f"{i+1}. " if tipo == "lista_ordenada" else "• "
                    tk.Label(
                        self, text=prefixo + texto_item, wraplength=430, justify="left",
                        bg="#274C5C", fg="white"
                    ).pack(pady=2, padx=20, anchor="w")
        # --- FIM DA CORREÇÃO ---

        tk.Label(
            self, text="👉 Em breve: exercícios interativos!",
            fg="yellow", bg="#274C5C"
        ).pack(pady=20)
        
        tk.Button(
            self, text="Voltar ao Menu", command=self.voltar_callback,
            bg="#1ABC9C", fg="white", relief="groove", padx=10, pady=5
        ).pack(pady=20)
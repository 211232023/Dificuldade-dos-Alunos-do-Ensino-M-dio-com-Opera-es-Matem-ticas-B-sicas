# telas/tela_exercicios.py

import tkinter as tk
import random

# --- Paleta de Cores e Fontes ---
CORES = {
    "background": "#2c3e50",
    "texto_primario": "#ecf0f1",
    "texto_titulo": "#ffffff",
    "acento_primario": "#3498db",
    "acento_hover": "#2980b9",
    "sucesso": "#2ecc71",
    "erro": "#e74c3c",
    "aviso": "#f1c40f",
    "entry_background": "#34495e",
    "entry_borda": "#5d6d7e"
}

FONTES = {
    "contador": ("Arial", 18),
    "pergunta": ("Arial", 28, "bold"),
    "entry": ("Arial", 22),
    "botao": ("Arial", 16, "bold"),
    "feedback": ("Arial", 18, "italic"),
    "placar": ("Arial", 30, "bold")
}

# --- Widget Customizado para Botões com Hover ---
class HoverButton(tk.Button):
    def __init__(self, master, hover_color, **kw):
        super().__init__(master=master, **kw)
        self.default_bg = self["background"]
        self.hover_color = hover_color
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self.hover_color

    def on_leave(self, e):
        self['background'] = self.default_bg

class TelaExercicios(tk.Frame):
    def __init__(self, master, exercicios, voltar_callback):
        super().__init__(master, bg=CORES["background"])
        
        self.voltar_callback = voltar_callback
        random.shuffle(exercicios)
        self.exercicios = exercicios
        self.total_perguntas = len(self.exercicios)
        self.pergunta_atual_index = 0
        self.acertos = 0

        self.label_contador = tk.Label(self, font=FONTES["contador"], bg=CORES["background"], fg=CORES["texto_primario"])
        self.label_pergunta = tk.Label(self, font=FONTES["pergunta"], bg=CORES["background"], fg=CORES["texto_titulo"], wraplength=900)
        
        self.entry_resposta = tk.Entry(self, font=FONTES["entry"], width=20, justify="center", 
                                       bg=CORES["entry_background"], fg=CORES["texto_titulo"], relief="flat", 
                                       insertbackground=CORES["texto_titulo"], highlightthickness=2, 
                                       highlightbackground=CORES["entry_borda"], highlightcolor=CORES["acento_primario"])
        
        self.botao_verificar = HoverButton(self, text="Verificar Resposta", command=self.verificar_resposta, font=FONTES["botao"], 
                                           bg=CORES["acento_primario"], fg=CORES["texto_titulo"], relief="flat", bd=0, padx=25, pady=15,
                                           hover_color=CORES["acento_hover"], activebackground=CORES["acento_hover"], activeforeground=CORES["texto_titulo"])
        
        self.label_feedback = tk.Label(self, font=FONTES["feedback"], bg=CORES["background"])

        self.label_contador.pack(pady=(60, 20))
        self.label_pergunta.pack(pady=30, padx=40)
        self.entry_resposta.pack(pady=25, ipady=15)
        self.botao_verificar.pack(pady=30)
        self.label_feedback.pack(pady=20)
        
        self.mostrar_proxima_pergunta()

    def mostrar_proxima_pergunta(self):
        if self.pergunta_atual_index < self.total_perguntas:
            self.label_feedback.config(text="")
            self.entry_resposta.delete(0, 'end')
            
            self.label_contador.config(text=f"Pergunta {self.pergunta_atual_index + 1} de {self.total_perguntas}")
            pergunta_info = self.exercicios[self.pergunta_atual_index]
            self.label_pergunta.config(text=pergunta_info["pergunta"])
            
            self.botao_verificar.config(state="normal", text="Verificar Resposta", command=self.verificar_resposta)
        else:
            self.mostrar_resultado_final()

    def verificar_resposta(self):
        resposta_usuario = self.entry_resposta.get().strip()
        
        if not resposta_usuario:
            self.label_feedback.config(text="⚠️ Por favor, digite uma resposta.", fg=CORES["aviso"])
            return

        resposta_correta = self.exercicios[self.pergunta_atual_index]["resposta"].strip()

        if resposta_usuario == resposta_correta:
            self.acertos += 1
            self.label_feedback.config(text="✅ Correto!", fg=CORES["sucesso"])
        else:
            self.label_feedback.config(text=f"❌ Incorreto. A resposta era: {resposta_correta}", fg=CORES["erro"])
        
        self.pergunta_atual_index += 1
        
        self.botao_verificar.config(text="Próxima Pergunta ➔", command=self.mostrar_proxima_pergunta)

    def mostrar_resultado_final(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        
        placar_texto = f"Fim dos exercícios!\n\nVocê acertou {self.acertos} de {self.total_perguntas} perguntas."
        tk.Label(self, text=placar_texto, font=FONTES["placar"], bg=CORES["background"], fg=CORES["texto_titulo"]).pack(pady=80)
        
        HoverButton(self, text="Voltar para a Teoria", command=self.voltar_callback, font=FONTES["botao"],
                    bg=CORES["acento_primario"], fg=CORES["texto_titulo"], relief="flat", bd=0, padx=25, pady=15,
                    hover_color=CORES["acento_hover"], activebackground=CORES["acento_hover"], activeforeground=CORES["texto_titulo"]).pack(pady=20)
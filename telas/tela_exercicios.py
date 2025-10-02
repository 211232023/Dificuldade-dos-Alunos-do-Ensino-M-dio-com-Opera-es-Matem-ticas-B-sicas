# telas/tela_exercicios.py

import tkinter as tk
import random
from estilos import CORES, FONTES
from telas.tela_menu import HoverButton

class TelaExercicios(tk.Frame):
    def __init__(self, master, exercicios, voltar_callback, feedback_callback):
        super().__init__(master, bg=CORES["background"])
        
        self.voltar_callback = voltar_callback
        self.feedback_callback = feedback_callback
        random.shuffle(exercicios)
        self.exercicios = exercicios
        self.total_perguntas = len(self.exercicios)
        self.pergunta_atual_index = 0
        self.acertos = 0

        # Frame principal para o conteúdo da pergunta
        frame_conteudo = tk.Frame(self, bg=CORES["background"])
        frame_conteudo.pack(expand=True)

        self.label_contador = tk.Label(frame_conteudo, font=FONTES["contador_exercicio"], bg=CORES["background"], fg=CORES["texto_primario"])
        self.label_pergunta = tk.Label(frame_conteudo, font=FONTES["pergunta_exercicio"], bg=CORES["background"], fg=CORES["texto_titulo"], wraplength=900)
        
        self.entry_resposta = tk.Entry(frame_conteudo, font=FONTES["entry_exercicio"], width=20, justify="center", 
                                       bg=CORES["entry_background"], fg=CORES["texto_titulo"], relief="flat", 
                                       insertbackground=CORES["texto_titulo"], highlightthickness=2, 
                                       highlightbackground=CORES["entry_borda"], highlightcolor=CORES["acento_primario"])
        
        self.botao_principal = HoverButton(frame_conteudo, text="Verificar Resposta", command=self.verificar_resposta, font=FONTES["botao_exercicio"], 
                                           bg=CORES["acento_primario"], fg=CORES["texto_titulo"], relief="flat", bd=0, padx=25, pady=15,
                                           hover_color=CORES["botao_hover"], click_color=CORES["botao_click"],
                                           activebackground=CORES["botao_click"], activeforeground=CORES["texto_titulo"])
        
        self.label_feedback = tk.Label(frame_conteudo, font=FONTES["feedback_exercicio"], bg=CORES["background"])

        self.label_contador.pack(pady=(20, 20))
        self.label_pergunta.pack(pady=30, padx=40)
        self.entry_resposta.pack(pady=25, ipady=15)
        self.botao_principal.pack(pady=30)
        self.label_feedback.pack(pady=20)

        # Frame inferior para o botão de voltar
        frame_voltar = tk.Frame(self, bg=CORES["background"])
        frame_voltar.pack(fill="x", side="bottom", pady=20)
        
        HoverButton(frame_voltar, text="Voltar ao Conteúdo", command=self.voltar_callback, font=("Arial", 12, "bold"),
                    bg=CORES["entry_borda"], fg=CORES["texto_titulo"], relief="flat", bd=0, padx=20, pady=10,
                    hover_color=CORES["botao_hover"], click_color=CORES["botao_click"]).pack()
        
        self.mostrar_proxima_pergunta()

    def mostrar_proxima_pergunta(self):
        # Reativa os widgets e limpa os campos
        self.entry_resposta.config(state="normal")
        self.entry_resposta.delete(0, 'end')
        self.label_feedback.config(text="")
        
        # Atualiza o conteúdo da pergunta
        self.label_contador.config(text=f"Pergunta {self.pergunta_atual_index + 1} de {self.total_perguntas}")
        pergunta_info = self.exercicios[self.pergunta_atual_index]
        self.label_pergunta.config(text=pergunta_info["pergunta"])
        
        # Configura o botão principal para a ação de verificar
        self.botao_principal.config(text="Verificar Resposta", command=self.verificar_resposta)
        self.entry_resposta.focus()

    def verificar_resposta(self):
        resposta_usuario = self.entry_resposta.get().strip()
        
        if not resposta_usuario:
            self.label_feedback.config(text="⚠️ Por favor, digite uma resposta.", fg=CORES["aviso"])
            return
        
        resposta_correta = self.exercicios[self.pergunta_atual_index]["resposta"].strip()

        if resposta_usuario.lower() == resposta_correta.lower():
            self.acertos += 1
            self.label_feedback.config(text="✅ Correto!", fg=CORES["sucesso"])
        else:
            self.label_feedback.config(text=f"❌ Incorreto. A resposta era: {resposta_correta}", fg=CORES["erro"])
        
        self.entry_resposta.config(state="disabled")
        self.pergunta_atual_index += 1
        
        if self.pergunta_atual_index == self.total_perguntas:
            # *** A CORREÇÃO ESTÁ AQUI ***
            # Agora a chamada passa apenas os dois argumentos que a tela de exercícios conhece.
            # O `nome_topico_chave` é gerenciado pelo handler que criamos no main.py.
            self.botao_principal.config(text="Finalizar Exercícios", command=lambda: self.feedback_callback(self.acertos, self.total_perguntas))
        else:
            self.botao_principal.config(text="Próxima Pergunta ➔", command=self.mostrar_proxima_pergunta)
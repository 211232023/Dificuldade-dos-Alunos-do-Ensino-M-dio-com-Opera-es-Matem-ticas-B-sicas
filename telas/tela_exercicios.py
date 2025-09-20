# telas/tela_exercicios.py

import tkinter as tk
import random

class TelaExercicios(tk.Frame):
    def __init__(self, master, exercicios, voltar_callback):
        super().__init__(master, bg="#274C5C")
        
        self.voltar_callback = voltar_callback
        random.shuffle(exercicios)
        self.exercicios = exercicios
        self.total_perguntas = len(self.exercicios)
        
        self.pergunta_atual_index = 0
        self.acertos = 0

        # --- Widgets da tela ---
        self.label_contador = tk.Label(self, font=("Arial", 16), bg="#274C5C", fg="#BDC3C7")
        self.label_pergunta = tk.Label(self, font=("Arial", 22, "bold"), bg="#274C5C", fg="white", wraplength=800)
        self.entry_resposta = tk.Entry(self, font=("Arial", 18), width=20, justify="center")
        self.botao_verificar = tk.Button(self, text="Verificar Resposta", command=self.verificar_resposta, font=("Arial", 14, "bold"), bg="#1ABC9C", fg="white", padx=10, pady=10)
        self.label_feedback = tk.Label(self, font=("Arial", 16, "italic"), bg="#274C5C")

        # Posiciona os widgets na tela
        self.label_contador.pack(pady=(30, 10))
        self.label_pergunta.pack(pady=20, padx=20)
        self.entry_resposta.pack(pady=20, ipady=10)
        self.botao_verificar.pack(pady=20)
        self.label_feedback.pack(pady=10)
        
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
        
        # --- INÍCIO DA CORREÇÃO ---
        # Se a resposta do usuário estiver vazia, a função não faz nada.
        if not resposta_usuario:
            self.label_feedback.config(text="Por favor, digite uma resposta.", fg="yellow")
            return # Interrompe a execução da função aqui
        # --- FIM DA CORREÇÃO ---

        resposta_correta = self.exercicios[self.pergunta_atual_index]["resposta"].strip()

        if resposta_usuario == resposta_correta:
            self.acertos += 1
            self.label_feedback.config(text="Correto! 🎉", fg="#2ECC71")
        else:
            self.label_feedback.config(text=f"Incorreto. A resposta era: {resposta_correta}", fg="#E74C3C")
        
        self.pergunta_atual_index += 1
        
        self.botao_verificar.config(text="Próxima Pergunta", command=self.mostrar_proxima_pergunta)

    def mostrar_resultado_final(self):
        self.label_contador.pack_forget()
        self.label_pergunta.pack_forget()
        self.entry_resposta.pack_forget()
        self.botao_verificar.pack_forget()
        self.label_feedback.pack_forget()
        
        placar_texto = f"Fim dos exercícios!\n\nVocê acertou {self.acertos} de {self.total_perguntas} perguntas."
        tk.Label(self, text=placar_texto, font=("Arial", 24, "bold"), bg="#274C5C", fg="white").pack(pady=50)
        
        tk.Button(self, text="Voltar para a Teoria", command=self.voltar_callback, font=("Arial", 14, "bold"), bg="#1ABC9C", fg="white", padx=10, pady=10).pack(pady=20)
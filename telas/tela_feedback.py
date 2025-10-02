# telas/tela_feedback.py

import tkinter as tk
from estilos import CORES, FONTES
from telas.tela_menu import HoverButton

class TelaFeedback(tk.Frame):
    def __init__(self, master, acertos, total_perguntas, voltar_callback):
        super().__init__(master, bg=CORES["background"])

        erros = total_perguntas - acertos
        try:
            porcentagem = (acertos / total_perguntas) * 100
        except ZeroDivisionError:
            porcentagem = 0

        frame_central = tk.Frame(self, bg=CORES["background"])
        frame_central.pack(expand=True)

        tk.Label(
            frame_central,
            text="Desempenho Final",
            font=FONTES["placar_exercicio"],
            bg=CORES["background"],
            fg=CORES["texto_titulo"]
        ).pack(pady=(0, 40))

        # Usando um frame para organizar os resultados
        frame_stats = tk.Frame(frame_central, bg=CORES["background_secundario"], padx=40, pady=30)
        frame_stats.pack(pady=20)

        # Labels para os resultados
        stats_font = ("Arial", 22)
        tk.Label(frame_stats, text=f"Perguntas Totais:", font=stats_font, bg=CORES["background_secundario"], fg=CORES["texto_primario"]).grid(row=0, column=0, sticky="w", pady=10, padx=10)
        tk.Label(frame_stats, text=f"{total_perguntas}", font=stats_font, bg=CORES["background_secundario"], fg=CORES["texto_titulo"]).grid(row=0, column=1, sticky="e", pady=10, padx=10)

        tk.Label(frame_stats, text="Acertos:", font=stats_font, bg=CORES["background_secundario"], fg=CORES["sucesso"]).grid(row=1, column=0, sticky="w", pady=10, padx=10)
        tk.Label(frame_stats, text=f"{acertos}", font=stats_font, bg=CORES["background_secundario"], fg=CORES["sucesso"]).grid(row=1, column=1, sticky="e", pady=10, padx=10)

        tk.Label(frame_stats, text="Erros:", font=stats_font, bg=CORES["background_secundario"], fg=CORES["erro"]).grid(row=2, column=0, sticky="w", pady=10, padx=10)
        tk.Label(frame_stats, text=f"{erros}", font=stats_font, bg=CORES["background_secundario"], fg=CORES["erro"]).grid(row=2, column=1, sticky="e", pady=10, padx=10)

        tk.Label(frame_stats, text="Porcentagem de Acertos:", font=stats_font, bg=CORES["background_secundario"], fg=CORES["texto_primario"]).grid(row=3, column=0, sticky="w", pady=10, padx=10)
        tk.Label(frame_stats, text=f"{porcentagem:.1f}%", font=stats_font, bg=CORES["background_secundario"], fg=CORES["texto_titulo"]).grid(row=3, column=1, sticky="e", pady=10, padx=10)

        HoverButton(
            frame_central,
            text="Voltar para a Teoria",
            command=voltar_callback,
            font=FONTES["botao_exercicio"],
            bg=CORES["acento_primario"],
            fg=CORES["texto_titulo"],
            relief="flat", bd=0, padx=25, pady=15,
            hover_color=CORES["botao_hover"],
            click_color=CORES["botao_click"]
        ).pack(pady=40)
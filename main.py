# main.py

import tkinter as tk
import sys
import os

# Adiciona o diretório raiz do projeto ao caminho do Python.
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(diretorio_atual)

from telas.tela_menu import TelaMenu
from telas.tela_topico import TelaTopico

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EducaMath")
        
        # --- MUDANÇA 1: Iniciar em tela cheia ---
        self.attributes('-fullscreen', True)
        # --- MUDANÇA 2: Permitir sair da tela cheia com a tecla 'Esc' ---
        self.bind('<Escape>', lambda e: self.attributes('-fullscreen', False))

        # O container principal agora ocupa toda a janela
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frame_atual = None
        self.mostrar_tela_menu()

    def mostrar_tela_menu(self):
        if self.frame_atual:
            self.frame_atual.destroy()
        
        self.frame_atual = TelaMenu(master=self.container, controller=self.mostrar_tela_topico)
        self.frame_atual.pack(fill="both", expand=True)

    def mostrar_tela_topico(self, nome_topico_chave):
        if self.frame_atual:
            self.frame_atual.destroy()
        
        self.frame_atual = TelaTopico(master=self.container, 
                                      nome_topico_chave=nome_topico_chave, 
                                      voltar_callback=self.mostrar_tela_menu)
        self.frame_atual.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
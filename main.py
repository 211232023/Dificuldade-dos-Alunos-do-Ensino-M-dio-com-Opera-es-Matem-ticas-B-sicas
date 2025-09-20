import tkinter as tk
import sys
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(diretorio_atual)

from telas.tela_menu import TelaMenu
from telas.tela_topico import TelaTopico
from telas.tela_exercicios import TelaExercicios 
from conteudo.dados import CONTEUDO_EDUCACIONAL 

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EducaMath")
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda e: self.attributes('-fullscreen', False))

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
                                      voltar_callback=self.mostrar_tela_menu,
                                      # Passa a nova função de controle
                                      exercicios_callback=self.mostrar_tela_exercicios)
        self.frame_atual.pack(fill="both", expand=True)

    def mostrar_tela_exercicios(self, nome_topico_chave):
        if self.frame_atual:
            self.frame_atual.destroy()
        
        exercicios = CONTEUDO_EDUCACIONAL[nome_topico_chave]["exercicios"]
        
        self.frame_atual = TelaExercicios(master=self.container, 
                                          exercicios=exercicios, 
                                          # O botão de voltar na tela de exercícios te leva para a tela do tópico
                                          voltar_callback=lambda: self.mostrar_tela_topico(nome_topico_chave))
        self.frame_atual.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
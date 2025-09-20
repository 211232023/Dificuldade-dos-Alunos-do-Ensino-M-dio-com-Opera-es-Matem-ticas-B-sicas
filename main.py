import tkinter as tk
import sys
import os

# --- INÍCIO DA CORREÇÃO ---
# Adiciona o diretório raiz do projeto ao caminho do Python.
# Isso garante que o programa encontre as pastas 'telas' e 'conteudo'.
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(diretorio_atual)
# --- FIM DA CORREÇÃO ---

from telas.tela_menu import TelaMenu
from telas.tela_topico import TelaTopico

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EducaMath")
        self.geometry("600x600")
        
        # Container onde as telas (frames) serão colocadas e trocadas
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frame_atual = None
        self.mostrar_tela_menu()

    def mostrar_tela_menu(self):
        # Destrói a tela atual (se houver) e mostra a do menu
        if self.frame_atual:
            self.frame_atual.destroy()
        
        # Passamos a função 'mostrar_tela_topico' como o "controller"
        self.frame_atual = TelaMenu(master=self.container, controller=self.mostrar_tela_topico)
        self.frame_atual.pack(fill="both", expand=True)

    def mostrar_tela_topico(self, nome_topico_chave):
        # Destrói a tela atual e mostra a do tópico escolhido
        if self.frame_atual:
            self.frame_atual.destroy()
        
        # Passamos a função 'mostrar_tela_menu' como a função de "voltar"
        self.frame_atual = TelaTopico(master=self.container, 
                                      nome_topico_chave=nome_topico_chave, 
                                      voltar_callback=self.mostrar_tela_menu)
        self.frame_atual.pack(fill="both", expand=True)

# Inicia a aplicação
if __name__ == "__main__":
    app = App()
    app.mainloop()
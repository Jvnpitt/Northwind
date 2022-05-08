import tkinter as tk

class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.pack()
        self.criarbotoes()
        self.crialabel()
        self.entradadados()
        self.BotaoSair()
 
    def criarbotoes(self):
        self.btCriar = tk.Button(self)
        self.btCriar["text"]="Botao1"
        self.btCriar.pack(side="top")

    def crialabel(self):
        self.label = tk.Label(self)
        self.label["text"]="label de dialogo"
        self.label.pack(side="top")
 
    def entradadados(self):
        self.edit = tk.Entry(self)
        self.edit.pack(side="top")

    def BotaoSair(self):
        self.btSair = tk.Button(self, text="sair", fg="red", command=root.destroy)
        self.btSair.pack(side="bottom")



root = tk.Tk()
#criando a aplicação
minhaAplicacao = App(master=root)
minhaAplicacao.master.title("Exemplo de tela")
minhaAplicacao.master.maxsize(400,300)
minhaAplicacao.master.geometry("400x300")

minhaAplicacao.mainloop()
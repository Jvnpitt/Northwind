import pyodbc
from tkinter.messagebox import showinfo
import tkinter
from tkinter import ttk

DADOS_CONEXAO = (
    "Driver={SQL Server};"
    "Server=DESKTOP-SGBVCQD\SQLEXPRESS;"
    "Database=Northwind;"
)

cursor = ''
tree = ''

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))

try:
    conexao = pyodbc.connect(DADOS_CONEXAO)
    print("Conexão Bem Sucedida")
    cursor = conexao.cursor() 
    
except Exception as e:
    print(str(e))

def tela_visualizacao_cliente():
    janela_visualizacao = tkinter.Tk()
    janela_visualizacao.title('Visualização de Clientes')
    janela_visualizacao.geometry("250x700")

    query = "select ContactName from Customers;"
    cursor.execute(query)
    lista_nomes = cursor.fetchall()

    columns = ('Nome_dos_Clientes')
    tree = ttk.Treeview(janela_visualizacao, columns=columns, show='headings', height=30)
    tree.heading('Nome_dos_Clientes', text='Nome dos Cliente')

    for i in lista_nomes:
        tree.insert('', tkinter.END, values=i[0])

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

    scrollbar = ttk.Scrollbar(janela_visualizacao, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    janela_visualizacao.mainloop()

def tela_visao_compras(janela_visualizacao, orderid):
    janela_visualizacao.destroy
    print(orderid)

def tela_getorderid_compras():
    janela_visualizacao = tkinter.Tk()
    janela_visualizacao.title('Visualização de compras')
    janela_visualizacao.geometry("250x250")

    label = tkinter.Label(janela_visualizacao)
    label["text"] = "OrderID"
    label.pack(side="top")

    orderId = tkinter.Entry(janela_visualizacao)
    orderId.pack()
    print(orderId.get())

    btSair = tkinter.Button(janela_visualizacao, text="buscar", fg="blue", command=)
    btSair.pack(side="bottom")

    mensagem = tkinter.Label(janela_visualizacao, text="TI fora da caixa", font="impact 20 bold")
    mensagem.pack()
    mensagem["text"]="texto: "+orderId.get()
    print(mensagem)

    #query = f"""Select P.ProductName from [Order Details] OD
    #            Join  Products P ON P.ProductID = OD.PrductID
    #            where OrderID = {};"""
    #cursor.execute(query)
    #lista_nomes = cursor.fetchall()

    columns = ('Nome_dos_Clientes')
    tree = ttk.Treeview(janela_visualizacao, columns=columns, show='headings', height=30)
    tree.heading('Nome_dos_Clientes', text='Nome dos Cliente')

    #for i in lista_nomes:
    #    tree.insert('', tkinter.END, values=i[0])

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

    scrollbar = ttk.Scrollbar(janela_visualizacao, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    janela_visualizacao.mainloop()

def tela_insercao_cliente():
    janela_insercao = tkinter.Tk()
    janela_insercao.title('Cadastro de Cliente')
    janela_insercao.geometry("700x700")

    texto_visualizacao = tkinter.Label(janela_insercao, text="teste")
    texto_visualizacao.grid(column=0, row=2, padx=10, pady=10)

    text = tkinter.Text(janela_insercao, height=10)
    text.pack()
    janela_insercao.mainloop() 

def tela_remocao_cliente():
    janela_remocao = tkinter.Tk()
    janela_remocao.title('Remover Cadastro')
    janela_remocao.geometry("700x700")
    janela_remocao.mainloop()

def tela_atualizacao_cliente():
    janela_remocao = tkinter.Tk()
    janela_remocao.title('Atualizar Cadastro')
    janela_remocao.geometry("700x700")
    janela_remocao.mainloop()   

janela = tkinter.Tk()

janela.title('Northwind')
janela.geometry("700x700")


# Visualização
texto_visualizacao = tkinter.Label(janela, text="Visualizar tabela clientes")
texto_visualizacao.grid(column=0, row=0, padx=10, pady=10)

botao_viualizacao = tkinter.Button(janela, text="Visualização", command=tela_visualizacao_cliente)
botao_viualizacao.grid(column=0, row=1, padx=150, pady=10)

# Cadastro
texto_cadastro_cliente = tkinter.Label(janela, text="Cadastro de clientes")
texto_cadastro_cliente.grid(column=0, row=2, padx=10, pady=10)

botao_cadastro = tkinter.Button(janela, text="Inserção", command=tela_insercao_cliente)
botao_cadastro.grid(column=0, row=4, padx=150, pady=10)

# Remover
texto_remover_cliente = tkinter.Label(janela, text="Remover clientes")
texto_remover_cliente.grid(column=0, row=5, padx=10, pady=10)

botao_remocao = tkinter.Button(janela, text="remoção", command=tela_remocao_cliente)
botao_remocao.grid(column=0, row=6, padx=150, pady=10)

# Atualizar
texto_atualizar_cliente = tkinter.Label(janela, text="Atualizar dados")
texto_atualizar_cliente.grid(column=0, row=7, padx=10, pady=10)

botao_atualizar = tkinter.Button(janela, text="Atualizar", command=tela_atualizacao_cliente)
botao_atualizar.grid(column=0, row=8, padx=150, pady=10)


# Visualização
texto_visualizacao_compras = tkinter.Label(janela, text="Visualizar tabela compras")
texto_visualizacao_compras.grid(column=0, row=9, padx=150, pady=10)


botao_viualizacao_compras = tkinter.Button(janela, text="Visualização", command=tela_getorderid_compras)
botao_viualizacao_compras.grid(column=0, row=10, padx=150, pady=10)

janela.mainloop() 
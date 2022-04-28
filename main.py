from cProfile import label
from click import command
import requests
import tkinter

def pegar_cotacao():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']    
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f""" Cotação do dólar - {cotacao_dolar} \n Cotação do euro - {cotacao_euro} \n Cotação do bitcoin - {cotacao_btc} \n"""

    texto_cotacoes["text"] = texto

janela = tkinter.Tk()
janela.title('Olá Mundo')
janela.geometry("400x400")

texto_orientacao = tkinter.Label(janela, text="Clique aqui")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = tkinter.Button(janela, text="Refresh", command=pegar_cotacao)
botao.grid(column=0, row=1, padx=150, pady=10)

texto_cotacoes = tkinter.Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-SGBVCQD\SQLEXPRESS;"
    "Database=Northwind;"
)

try:
    conexao = pyodbc.connect(dados_conexao)
    print("Conexão Bem Sucedida")
    csr = conexao.cursor() 
    csr.close()
    del csr
    
except Exception as e:
    print(str(e))
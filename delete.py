import mysql.connector
import customtkinter

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='vicktor873',
    database='dados_vendas',
)
janela = customtkinter.CTk()
janela.title("Open Sistem")
janela.geometry("500x300")
cursor = conexao.cursor()

def delete():
    comando = f'DELETE FROM produtos WHERE nomeproduto = "{nomeproduto.get()}"'
    cursor.execute(comando)
    conexao.commit()
    
nomeproduto = customtkinter.CTkEntry(janela, placeholder_text="Nome do produto: ")
nomeproduto.pack(padx='5', pady='10')

btn = customtkinter.CTkButton(janela, text="deletar", command=delete)
btn.pack(padx='10', pady='10')

janela.mainloop()
cursor.close()
conexao.close()
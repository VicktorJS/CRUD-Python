import mysql.connector
import customtkinter

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='vicktor873',
    database='dados_vendas',
)
janela = customtkinter.CTk()
janela.title('Open Sistem')
janela.geometry('500x300')
cursor = conexao.cursor()

def con():
    comando = f'SELECT * FROM produtos WHERE idproduto = "{idproduto.get()}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)

idproduto = customtkinter.CTkEntry(janela, placeholder_text='ID do produto: ')
idproduto.pack(padx='10', pady='15')

btn = customtkinter.CTkButton(janela, text='Consultar', command=con)
btn.pack(padx='10', pady='10')

janela.mainloop()
cursor.close()
conexao.close()

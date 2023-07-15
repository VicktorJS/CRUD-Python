import customtkinter

janela = customtkinter.CTk()
janela.title('Open Sistem')
janela.geometry('500x300')

def consulta():
    __import__('consulta.py')

def cadastro():
    __import__('cadastro.py')

def update():
    __import__('editor.py')

def delete():
    __import__('delete.py')

titulo = customtkinter.CTkLabel(janela, text='Sistema de dados dos produtos')
titulo.pack(padx=10, pady=5)

option01 = customtkinter.CTkButton(janela, text = 'Consultar dados de produtos', command=consulta)
option01.pack(padx=10, pady=10, )

option02 = customtkinter.CTkButton(janela, text = 'Cadastrar produto', command=cadastro)
option02.pack(padx=10, pady=10)

option03 = customtkinter.CTkButton(janela, text="Editar dados", command=update)
option03.pack(padx=10, pady=10)

option04 = customtkinter.CTkButton(janela, text="Deletar dados de produtos", command=delete)
option04.pack(padx=10, pady=10)

janela.mainloop()
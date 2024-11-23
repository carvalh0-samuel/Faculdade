import tkinter as tk
from tkinter import ttk

#configuracao da janela principal
root = tk.Tk()
root.title("Cadastro")

#define a dimensao da janela
root.geometry("800x600")

#adiciona um titulo na janela
title = tk.Label(root, text="Formulário de Cadastro", font=("arial", 20))
title.pack(pady=10)

#menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Arquivo", menu=file_menu)
file_menu.add_command(label="Novo")
file_menu.add_command(label="Abrir")
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.quit)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Editar", menu=edit_menu)
edit_menu.add_command(label="Copiar")
edit_menu.add_command(label="Colar")

exib_menu = tk.Menu(menu)
menu.add_cascade(label="Exibir", menu=exib_menu)
exib_menu.add_command(label="Pesquisa")
exib_menu.add_command(label="Explorar")

help_menu = tk.Menu(menu)
menu.add_cascade(label="Ajuda", menu=help_menu)
help_menu.add_command(label="Documentação")
help_menu.add_command(label="Sobre")

#formulario
form_frame = tk.Frame(root)
form_frame.pack(padx=20, pady=20)

#campo nome
tk.Label(form_frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

#campo idade
tk.Label(form_frame, text="Cidade:").grid(row=1, column=0, padx=5, pady=5)
entry_city = tk.Entry(form_frame)
entry_city.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Estado:").grid(row=2, column=0, padx=5, pady=5)
entry_est = ttk.Combobox(form_frame, values=["DF","SP","RJ","GO"])
entry_est.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="E-Mail:").grid(row=3, column=0, padx=5, pady=5)
entry_mail = tk.Entry(form_frame)
entry_mail.grid(row=3, column=1, padx=5, pady=5)


#botao de opcao
tk.Label(form_frame, text="Sexo:").grid(row=4, column=0, padx=5, pady=5)
var_option = tk.StringVar(value="Opção 1")
tk.Radiobutton(form_frame, text="Masculino", variable=var_option, value="Opção1").grid(row=4, column=1, padx=5, pady=5)
tk.Radiobutton(form_frame, text="Feminino", variable=var_option, value="Opção2").grid(row=4, column=2, padx=5, pady=5)
tk.Radiobutton(form_frame, text="Outros", variable=var_option, value="Opção3").grid(row=4, column=3, padx=5, pady=5)

#caixa de seleção

tk.Label(form_frame, text="Interesse em Cursos:").grid(row=5, column=0, padx=5, pady=5)
var_check1 = tk.BooleanVar()
tk.Checkbutton(form_frame, text="Linguagem C", variable=var_check1).grid(row=5, column=1, padx=5, pady=5)
var_check2 = tk.BooleanVar()
tk.Checkbutton(form_frame, text="Python", variable=var_check2).grid(row=5, column=2, padx=5, pady=5)
var_check3 = tk.BooleanVar()
tk.Checkbutton(form_frame, text="Java", variable=var_check3).grid(row=5, column=3, padx=5, pady=5)
var_check4 = tk.BooleanVar()
tk.Checkbutton(form_frame, text="PHP", variable=var_check4).grid(row=5, column=4, padx=5, pady=5)

tk.Button(form_frame, text="Enviar").grid(row=6, column=1, padx=10, pady=10)
tk.Button(form_frame, text="Sair", command=root.quit).grid(row=6, column=2, padx=10, pady=10)

#inicia o loop principal da interface grafica
root.mainloop()
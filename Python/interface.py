import tkinter as tk
from tkinter import ttk

#configuracao da janela principal
root = tk.Tk()
root.title("Aula de Python")

#define a dimensao da janela
root.geometry("800x600")

#adiciona um titulo na janela
title = tk.Label(root, text="Meu Formulário", font=("arial", 20))
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

#formulario
form_frame = tk.Frame(root)
form_frame.pack(padx=20, pady=20)

#campo nome
tk.Label(form_frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

#campo idade
tk.Label(form_frame, text="Idade:").grid(row=1, column=0, padx=5, pady=5)
entry_age = tk.Entry(form_frame)
entry_age.grid(row=1, column=1, padx=5, pady=5)

#botao de opcao
tk.Label(form_frame, text="Escolha uma opção:").grid(row=2, column=0, padx=5, pady=5)
var_option = tk.StringVar(value="Opção 1")
tk.Radiobutton(form_frame, text="Opção 1", variable=var_option, value="Opção1").grid(row=2, column=1, padx=5, pady=5)
tk.Radiobutton(form_frame, text="Opção 2", variable=var_option, value="Opção2").grid(row=2, column=2, padx=5, pady=5)

#caixa de seleção

tk.Label(form_frame, text="Selecione:").grid(row=3, column=0, padx=5, pady=5)
var_check1 = tk.BooleanVar()
tk.Checkbutton(form_frame, text="Checkbox 1", variable=var_check1).grid(row=3, column=1, padx=5, pady=5)
var_check2 = tk.BooleanVar()
tk.Checkbutton(form_frame, text="Checkbox 2", variable=var_check2).grid(row=3, column=2, padx=5, pady=5)

#inicia o loop principal da interface grafica
root.mainloop()
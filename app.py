import tkinter as tk
from tkinter import messagebox, simpledialog
import banco_dados

def atualizar_lista():
    """Atualiza a lista de crianças exibida na interface."""
    lista_criancas.delete(0, tk.END)
    criancas = banco_dados.listar_criancas()
    for crianca in criancas:
        lista_criancas.insert(tk.END, f"{crianca[0]}: {crianca[1]}, {crianca[2]} anos, responsável: {crianca[3]}")

def adicionar_crianca():
    """Adiciona uma nova criança ao banco de dados e atualiza a lista na interface."""
    nome = simpledialog.askstring("Adicionar Criança", "Qual o nome da criança?")
    if nome:
        idade = simpledialog.askinteger("Adicionar Criança", "Quantos anos ela tem?")
        if idade is not None:
            nome_responsavel = simpledialog.askstring("Adicionar Criança", "Nome do responsável:")
            if nome_responsavel:
                banco_dados.adicionar_crianca(nome, idade, nome_responsavel)
                atualizar_lista()

def editar_crianca():
    """Edita as informações de uma criança existente."""
    item_selecionado = lista_criancas.curselection()
    if item_selecionado:
        id_crianca = int(lista_criancas.get(item_selecionado).split(":")[0])
        nome = simpledialog.askstring("Editar Criança", "Qual o novo nome da criança?")
        if nome:
            idade = simpledialog.askinteger("Editar Criança", "Nova idade da criança?")
            if idade is not None:
                nome_responsavel = simpledialog.askstring("Editar Criança", "Nome do novo responsável:")
                if nome_responsavel:
                    banco_dados.atualizar_crianca(id_crianca, nome, idade, nome_responsavel)
                    atualizar_lista()

def excluir_crianca():
    """Remove uma criança do banco de dados e atualiza a lista na interface."""
    item_selecionado = lista_criancas.curselection()
    if item_selecionado:
        id_crianca = int(lista_criancas.get(item_selecionado).split(":")[0])
        banco_dados.remover_crianca(id_crianca)
        atualizar_lista()

# Configuração da interface gráfica
app = tk.Tk()
app.title("Cadastro de Crianças da Creche")

# Configura o frame principal
frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

# Configura a lista de crianças
lista_criancas = tk.Listbox(frame, width=50, height=15)
lista_criancas.pack(side=tk.LEFT)

barra_rolagem = tk.Scrollbar(frame)
barra_rolagem.pack(side=tk.RIGHT, fill=tk.Y)
lista_criancas.config(yscrollcommand=barra_rolagem.set)
barra_rolagem.config(command=lista_criancas.yview)

# Configura os botões
frame_botoes = tk.Frame(app)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Adicionar", command=adicionar_crianca).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Editar", command=editar_crianca).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Excluir", command=excluir_crianca).pack(side=tk.LEFT, padx=5)

# Inicializa o banco de dados e atualiza a lista
banco_dados.inicializar_banco()
atualizar_lista()

# Inicia o loop da interface gráfica
app.mainloop()

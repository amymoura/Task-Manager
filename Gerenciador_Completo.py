#Aluna: Amanda Karine de Moura Oliveira, 1° Modulo DS.

#Importando tkinter e messagebox (interação com usuário / entrada e saida)
import tkinter as tk 
from tkinter import messagebox 

# CRIANDO AS FUNÇÕES DO PROGRAMA.

# FUNÇÃO PARA ADICIONAR UMA TAREFA A LISTA.
# Campo de entrada do texto, GET armazena o texto inserido.
# IF verifica se a variável TAREFA não esta vazia, caso sim, executa o ELSE.
# INSERT insere uma nova tarefa no lugar da anterior.
# DELETE limpa o campo de entrada após se adicionar uma tarefa, exibe a mensagem se estiver só.
def adicionar():
    tarefa = entry_tarefa.get()           
    if tarefa:                            
        lista.insert(tk.END, tarefa)      
        entry_tarefa.delete(0, tk.END)    
    else:
        messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.") 

# FUNÇÃO PARA DELETAR UMA TAREFA SELECIONADA NA LISTA.
# Variável ESCOLHIDA declarada como atual tarefa selecionada.
# IF verifica se houve alguma tarefa selecionada, caso não, exibe a mensagem.
# RETURN impede o código de ser executado sem tarefa selecionada. DELETE remove a selecionada na lista.
def excluir():
    escolhida = lista.curselection()  
    if not escolhida:                 
        messagebox.showwarning("Aviso","Selecione uma tarefa a ser excluida!")
        return                        
    lista.delete(escolhida)           
    
# FUNÇÃO PARA CONCLUIR A TAREFA SELECIONADA NA LISTA.
# Variavel ESCOLHIDA é agora a tarefa selecionada na lista, IF se não houver, exibe a mensagem.
# TAREFA recebe o texto da ESCOLHIDA. Se no texto possuir ✔️, exibirá a mensagem.
# Deletar a ESCOLHIDA e logo após insere um nova tarefa no mesmo lugar, identica, acrescentada do ✔️.
# Muda a cor de fundo da tarefa para verde.
def concluir():
    escolhida = lista.curselection()                
    if not escolhida:                               
        messagebox.showwarning("Aviso","Selecione uma tarefa a ser concluida!")
        return 
    tarefa = lista.get(escolhida)                   
    if "✔️" in tarefa:                             
      messagebox.showinfo("Informação", "Essa tarefa já foi concluída!")
      return                                        
    lista.delete(escolhida) 
    lista.insert(escolhida, tarefa + " ✔️​")
    lista.itemconfig(escolhida, {'bg':'#00FF00'})  
    
# CRIANDO A JANELA PRINCIPAL DO PROGRAMA.
# TITLE está definindo o titulo da janela principal.
# GEOMETRY está definindo o tamanho da janela principal. RESIZABLE impede que se possa expandir a janela.
janela = tk.Tk()
janela.title("Gerenciador de Tarefas") 
janela.geometry("650x750") 
janela.resizable(False, False)

# DEFININDO IMAGEM DE FUNDO DO PROGRAMA.
imagem_fundo = tk.PhotoImage(file="PlanoDeFundo.png")

# CONFIGURANDO A IMAGEM DE FUNDO DO PROGRAMA.
# LABEL usado para exibir a imagem na janela, PLACE posiciona o label para que preencha toda a janela.
# RELWIDTH e RELHEIGHT define que o label ocupará 100% da largura e altura da janela(1°linha / 1°coluna).
label_fundo = tk.Label(janela, image=imagem_fundo)
label_fundo.place(relwidth=1, relheight=1)

# CRIANDO UM FRAME PARA UNIR O LISTBOX E A BARRA DE ROLAGEM.
# FRAME será utilizado para agrupar a listbox e a barra, adicionado a janela principal.
# PLACE posiciona o FRAME na janela (110 pixels da esquerda e 132 pixels do topo).
lista_frame = tk.Frame(janela, bg="#cd1702")  
lista_frame.place(x=110, y=132)

# ADICIONANDO UMA BARRA DE ROLAGEM, ASSOCIADA DENTRO DO FRAME ANTERIOR 'LISTA_FRAME'.
# tk.Scrollbar cria uma barra de rolagem associada ao lista_frame.
# side=tk.RIGHT(barra colocada no lado direito), fill=tk.Y(barra irá se estender por toda altura do frame, verticalmente.)
barra_rolagem = tk.Scrollbar(lista_frame)
barra_rolagem.pack(side=tk.RIGHT, fill=tk.Y)

# CRIANDO A LISTBOX PARA EXIBIR AS TAREFAS.
# Um listbox é adicionado ao frame(lista_frame).
# yscrollcommand: vincula a barra de rolagem a rolagem do listbox, se move em conjunto.
# activestyle(none): impede que o visual do item selecionado mude além do que foi programado.
lista = tk.Listbox(
    lista_frame, 
    width=32,                                    # Largura.
    height=8,                                    # Altura.
    font=('Century Gothic', 18),                 # Fonte e tamanho da fonte.
    bg='#F0E68C',                                # Cor do fundo da lista.
    fg='#000000',                                # Cor do texto.
    selectbackground='#FA8072',                  # Alterar cor de fundo do item selecionado.
    selectforeground= '#000000',                 # Alterar cor da fonte do item selecionado.
    yscrollcommand=barra_rolagem.set, 
    activestyle= "none" 
    )
lista.pack(pady=10)                              # Exibe a lista.

# Configurando a barra para que atualize a visualização do item quando a rolagem é feita.
barra_rolagem.config(command=lista.yview)

# CRIANDO UM CAMPO PARA O USUÁRIO INSERIR O TEXTO (TAREFA).
# ENTRY é um widget onde se insere uma linha de texto, que será exibido na janela principal.
# PLACE posiciona o ENTRY na janela (127 pixels da esquerda e 444 pixels do topo).
entry_tarefa = tk.Entry(janela, width=36, font=('Century Gothic', 15), bg="#cd1702", fg="#F8F8FF")
entry_tarefa.place(x=127, y=444) 

# Definindo a imagem do botão Adicionar.
imagem_add = tk.PhotoImage(file="Adicionar.png")

# CRIANDO BOTÃO DE ADICIONAR TAREFA.
# COMMAND=adicionar - vincula a ação do botão a função 'adicionar'.
# PLACE posiciona o BOTÃO na janela (180 pixels da esquerda e 500 pixels do topo).
botao_adicionar = tk.Button(
    janela, image=imagem_add, 
    width=300,
    bg='#FFDEAD',
    font=('Times', 16), 
    command=adicionar)
botao_adicionar.place(x=180, y=500)

# Definindo a imagem do botão Concluir.
imagem_concluir = tk.PhotoImage(file="Concluir.png")

# CRIANDO BOTÃO DE CONCLUIR TAREFA.
# COMMAND=concluir - vincula a ação do botão a função 'concluir'.
# PLACE posiciona o BOTÃO na janela (180 pixels da esquerda e 565 pixels do topo).
botao_concluir = tk.Button(
    janela, 
    image=imagem_concluir, 
    width=300, 
    bg='#FFDEAD',
    font=('Times', 16),
    command=concluir)
botao_concluir.place(x=180, y=565)

# Definindo a imagem do botão Excluir.
imagem_excluir = tk.PhotoImage(file="Excluir.png")

# CRIANDO BOTÃO DE EXCLUIR TAREFA.
# COMMAND=excluir - vincula a ação do botão a função 'excluir'.
# PLACE posiciona o BOTÃO na janela (180 pixels da esquerda e 630 pixels do topo).
botao_excluir = tk.Button(
    janela, 
    image = imagem_excluir, 
    width=300, 
    bg='#FFDEAD',
    font=('Times', 16),
    command=excluir)
botao_excluir.place(x=180, y=630)

# Inicia o loop da janela, sem ele o programa encerraria após a execução do código.
janela.mainloop()

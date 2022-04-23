# Importando a biblioteca tkinter
from tkinter import *  # Utilizando o * para importar todos os módulos da biblioteca tkinter
from tkinter import ttk # A biblioteca ttk é uma biblioteca para criar widgets, como botões, menus, etc.

# Importando Pillow
from PIL import Image, ImageTk


#-- Definindo paleta de cores do app --
cor1 = '#3b3b3b'  # Cor preta
cor2 = '#ffffff'  # Cor branca
cor3 = '#48b3e0'  # Cor azul
cor4 = '#fac123'  # Cor amarela

#-- Configurações da janela principal --
janela = Tk()  # Criando a janela principal
janela.title('')  # Titulo da janela
janela.geometry('650x260')  # Tamanho da janela
janela.configure(background=cor1)  # Cor de fundo da janela
janela.resizable(False, False)  # Janela não redimensionável

#-- Criando os frames --
# Frame superior, onde ficará o título da aplicação, é defindo o Frame, qual janela ele pertence, 
# e o tamanho do frame
frame_top = Frame(janela, width=450, height=50, bg=cor2, pady=0, padx=3, relief=FLAT)
frame_top.place(x=2, y=2)  # Aqui é a posiçao do frame na janela em relação ao x e y
#-- Frame lado esquerdo
frame_left = Frame(janela, width=450, height=220, bg=cor2, pady=0, padx=3, relief=FLAT)
frame_left.place(x=2, y=54)  # Aqui é a posiçao do frame na janela em relação ao x e y
#-- Frame lado direito
frame_right = Frame(janela, width=198, height=260, bg=cor2, pady=0, padx=3, relief=FLAT)
frame_right.place(x=454, y=2)  # Aqui é a posição do frame na janela em relação ao x e y

#-- Estilo para janela --
style = ttk.Style(janela)  # Criando o estilo
style.theme_use('clam')  # Utilizando o tema clam

#-- Parte lógica do app --
#-- Criando um dicioário para armazenar os dados usados no app --
unidades = {
            'Massa':[{'kg':1000}, {'hg':100}, {'dag':10}, {'g':1}, {'dg':0.1}, {'cg':0.01}, {'mg':0.001}],
            'Comprimento':[{'km':1000}, {'hm':100}, {'dam':10}, {'m':1}, {'dm':0.1}, {'cm':0.01}, {'mm':0.001}, {'mph':1609.34}, {'ft':0.3048}, {'in':0.0254}],
            'Tempo':[{'s':1}, {'min':60}, {'h':3600}, {'d':86400}, {'mes':2592000}, {'ano':31104000}],
            'Temperatura':[{'C':1}, {'F':1.8}, {'K':1}],
            'Pressão':[{'Pa':1}, {'atm':101325}, {'bar':100000}, {'psi':6894.7572932}, {'torr':133.32236842}],
            'Velocidade':[{'m/s':1}, {'km/h':3.6}, {'mph':2.23693629}, {'kn':1.94384449}],
            'Área':[{'km²':1}, {'ha':10000}, {'m²':0.0001}, {'dm²':0.01}, {'cm²':0.0001}, {'mm²':0.000001}],
            'Volume':[{'l':1}, {'ml':0.001}, {'cl':0.01}, {'dl':0.1}, {'hl':10}, {'kl':1000}],
            'Energia':[{'J':1}, {'kJ':1000}, {'MJ':1000000}, {'GJ':1000000000}, {'TJ':1000000000000}, {'PJ':1000000000000000}],
}

def mostrar_menu(i):  # Função para mostrar o menu
    
    unidade_de = [] # Lista para armazenar as unidades de entrada
    unidade_para = [] # Lista para armazenar as unidades de saída
    unidade_de_valor = [] # Lista para armazenar os valores das unidades de entrada

    for j in unidades[i]:
        for k, v in j.items(): # Percorrendo as chaves e valores de cada dicionário
            unidade_de.append(k)  # Aqui é representado o nome da unidade
            unidade_para.append(k)  # Aqui é representado o nome da unidade
            unidade_de_valor.append(v)  # Aqui é representado o valor da unidade

    c_de['values'] = unidade_de # Atribuindo as unidades de entrada ao combobox
    c_para['values'] = unidade_para # Atribuindo as unidades de saída ao combobox
    
    label_right['text'] = i  # Aqui altera o texto do label_right para o nome da unidade

    def calcular():
        # Obtendo as unidades
        a = c_de.get()
        b = c_para.get()

        # Obtendo o valor de entrada
        numero_para_converter = float(e_numero.get())       
     
        if unidade_para.index(a) <= unidade_de.index(b): # Verificando se a unidade de saída é maior ou igual a unidade de entrada
            distancia = unidade_para.index(b) - unidade_de.index(a) # Calculando a diferença entre as unidades
            resultado = numero_para_converter *(10**distancia) # Aqui é feito o cálculo
            l_resultado['text'] = resultado # Atribuindo o resultado ao label
        else:
            distancia = unidade_de.index(b) - unidade_para.index(a)
            resultado = numero_para_converter *(10**distancia)
            l_resultado['text'] = resultado


        if unidade_para.index(a) > unidade_de.index(b): # Verificando se a unidade de saída é maior que a unidade de entrada
            if unidade_para.index(a) <= unidade_de.index(b):

                distancia = unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter /(10**distancia)
                l_resultado['text'] = resultado
            else:
                distancia = unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter /(10**distancia)
                l_resultado['text'] = resultado


    

    # Criando Label para o valor de entrada
    l_info = Label(frame_right, text='Digite um número:', width=16, height=2, padx=0, pady=3, relief=FLAT, anchor=NW, bg=cor2, fg=cor1, font=('Ivy 10 bold'))
    l_info.place(x=5, y=110) # Aqui é a posição do label_info na janela em relação ao x e y

    e_numero = Entry(frame_right, width=9, font=('Ivy 15 bold'), justify=CENTER, relief=SOLID)
    e_numero.place(x=5, y=150)

    b_calcular = Button(frame_right, command=calcular, text='Calcular', width=9, height=1, relief=RAISED, overrelief=RIDGE, bg=cor4, fg=cor1, font=('Ivy 10 bold'))
    b_calcular.place(x=110, y=150)

    l_resultado = Label(frame_right, text='', width=15, height=1, padx=0, pady=3, relief=GROOVE, anchor=CENTER, bg=cor2, fg=cor1, font=('Ivy 15 bold'))
    l_resultado.place(x=5, y=200)



#-- Configurando Frame Top --
# Label superior, onde ficará o título da aplicação
label_top = Label(frame_top, text='Calculadora de Unidades de Medidas',height=1, padx=0, relief=FLAT, anchor=CENTER, font=('Ivy 15 bold'), bg=cor2, fg=cor3)
label_top.place(x=50, y=10)  # Aqui é a posição do label na janela em relação ao x e y

#-- Configurando Frame Right --
label_right = Label(frame_right, text='Unidade', width=15, height=1, pady=1, padx=3, relief=GROOVE, anchor=CENTER, font=('Ivy 15 bold'), bg=cor2, fg=cor1)
label_right.place(x=0, y=0)

#-- ComboBox --
l_de = Label(frame_right, text='De:', height=1, pady=1, padx=1, relief=GROOVE, anchor=CENTER, font=('Ivy 10 bold'), bg=cor2, fg=cor1)
l_de.place(x=0, y=50)

c_de = ttk.Combobox(frame_right, width=5, justify=CENTER, font=('Ivy 10 bold'), state='readonly')
c_de.place(x=28, y=50)

l_para = Label(frame_right, text='Para:', height=1, pady=1, padx=1, relief=GROOVE, anchor=CENTER, font=('Ivy 10 bold'), bg=cor2, fg=cor1)
l_para.place(x=90, y=50)

c_para = ttk.Combobox(frame_right, width=5, justify=CENTER, font=('Ivy 10 bold'), state='readonly')
c_para.place(x=130, y=50)


#-- Configurando Frame Left e os botões --
# Primeira Linha de botões
# Botão de Peso
img_0 = Image.open('images/weight.png')  # Abrindo a imagem
img_0 = img_0.resize((40, 40), Image.Resampling.LANCZOS)  # Redimensionando a imagem, passo os parâmetros: largura, altura, método de redimensionamento
img_0 = ImageTk.PhotoImage(img_0)  # Converte a imagem para o formato da biblioteca tkinter
b_0 = Button(frame_left, command=lambda:mostrar_menu('Massa'), text='Massa', image=img_0, compound=LEFT, width=130, height=50, relief=FLAT, anchor=NW, overrelief=SOLID, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

# Botão de Tempo
img_1 = Image.open('images/time.png')  
img_1 = img_1.resize((40, 40), Image.Resampling.LANCZOS)
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frame_left, command=lambda:mostrar_menu('Tempo'), text='Tempo', image=img_1, compound=LEFT, width=130, height=50, relief=FLAT, anchor=NW, overrelief=SOLID, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_1.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

# Botão de Comprimento
img_2 = Image.open('images/length.png')
img_2 = img_2.resize((40, 40), Image.Resampling.LANCZOS)
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frame_left, command=lambda:mostrar_menu('Comprimento'), text='Comprimento', image=img_2, compound=LEFT, width=130, height=50, relief=FLAT, anchor=NW, overrelief=SOLID, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_2.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

# Segunda Linha de botões
# Botão de Área
img_3 = Image.open('images/square.png')
img_3 = img_3.resize((40, 40), Image.Resampling.LANCZOS)
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frame_left, command=lambda:mostrar_menu('Área'), text='Área', image=img_3, compound=LEFT, width=130, height=50, relief=FLAT, anchor=NW, overrelief=SOLID, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_3.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

# Botão de Volume
img_4 = Image.open('images/volume.png')
img_4 = img_4.resize((40, 40), Image.Resampling.LANCZOS)
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frame_left, command=lambda:mostrar_menu('Volume'), text='Volume', image=img_4, compound=LEFT, width=130, height=50, relief=FLAT, anchor=NW, overrelief=SOLID, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_4.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

# Botão de Velocidade
img_5 = Image.open('images/speed.png')
img_5 = img_5.resize((40, 40), Image.Resampling.LANCZOS)
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frame_left, command=lambda:mostrar_menu('Velocidade'), text='Velocidade', image=img_5, compound=LEFT, width=130, height=50, relief=FLAT, anchor=NW, overrelief=SOLID, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_5.grid(row=1, column=2, sticky=NSEW, pady=5, padx=5)

# Terceira Linha de botões
# Botão de Temperatura
img_6 = Image.open('images/temperature.png')
img_6 = img_6.resize((40, 40), Image.Resampling.LANCZOS)
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(frame_left, command=lambda:mostrar_menu('Temperatura'), text='Temperatura', image=img_6, compound=LEFT, width=130, height=50, relief=FLAT, anchor=NW, overrelief=SOLID, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_6.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)

# Botão de Energia
img_7 = Image.open('images/energy.png')
img_7 = img_7.resize((40, 40), Image.Resampling.LANCZOS)
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(frame_left, command=lambda:mostrar_menu('Energia'), text='Energia', image=img_7, compound=LEFT, width=130, height=50, relief=FLAT, anchor=NW, overrelief=SOLID, font=('Ivy 12 bold'), bg=cor3, fg=cor2)
b_7.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)

# Botão de Pressão
img_8 = Image.open('images/pressure.png')
img_8 = img_8.resize((40, 40), Image.Resampling.LANCZOS)
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(frame_left, command=lambda:mostrar_menu('Pressão'), text='Pressão', image=img_8, compound=LEFT, width=130, height=50, relief=FLAT, anchor=NW, overrelief=SOLID, font=('Ivy 12 bold'), bg=cor3, fg=cor2)
b_8.grid(row=2, column=2, sticky=NSEW, pady=5, padx=5)

# Adicionando a função mainloop, ela deve ser chamada para manter a janela sempre aberta
janela.mainloop()

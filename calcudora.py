from tkinter import Tk, Entry, Label, Frame, Button, END
from backend import IMC, Salva


#Estou usando a class para aprimorar meu conhecimento
t = """Abaixo do peso: IMC < 18.5     
Peso normal: 18.5 <= IMC < 25
Sobrepeso: 25 <= IMC < 30      
Obesidade: IMC >= 30              
"""



def calcular():
    imc = IMC(END ,entry_peso, entry_altura, label_Imc)
    imc.Calcular()
       
def salva():
    peso, altura = entry_peso.get(), entry_altura.get()
    imc = round((float(peso)/ (float(altura)**2)), 2)
    salva = Salva(peso, altura, imc)
    salva.salva_imc()
    entry_peso.delete(0,END),
    entry_altura.delete(0,END)
    
root = Tk()
root.title("Calculadora de IMC")
root.geometry("350x350")  # Aumentamos a altura para acomodar a tabela

# Cores
cor_fundo = "#f0f0f0"  # Cinza claro
cor_titulo = "#333"  # Cinza escuro
cor_botao = "#4CAF50"  # Verde

# Estilos
style_titulo = {'font': ('Arial', 16, 'bold'), 'fg': cor_titulo}
style_label = {'font': ('Arial', 12), 'fg': cor_titulo}
style_entry = {'font': ('Arial', 12), 'bg': 'white'}
style_botao = {'font': ('Arial', 12), 'bg': cor_botao, 'fg': 'white'}

root.configure(bg=cor_fundo)

# Frame para os inputs
input_frame = Frame(root, padx=20, pady=20, bg=cor_fundo)
input_frame.pack()

# Label para o título da tabela

label_peso = Label(input_frame, text="Peso (kg):", **style_label)
label_peso.grid(row=0, column=0, padx=5, pady=5)
entry_peso = Entry(input_frame, width=10, **style_entry)
entry_peso.grid(row=0, column=1, padx=5, pady=5)

label_altura = Label(input_frame, text="Altura (m):", **style_label)
label_altura.grid(row=1, column=0, padx=5, pady=5)
entry_altura = Entry(input_frame, width=10, **style_entry)
entry_altura.grid(row=1, column=1, padx=5, pady=5)

# Botão de cálculo
button_imc = Button(root, text="Calcular", command=calcular, **style_botao)
button_imc.pack(pady=10)


Salva_btn = Button(root, text="Salva", command=salva, **style_botao)
Salva_btn.pack() 
# Label para exibir o IMC
label_Imc = Label(root, text="", font=("Arial", 14, 'bold'), fg=cor_titulo)
label_Imc.pack()

# Tabela de classificação
label_classificacao = Label(root, text="Classificação IMC:", **style_titulo)
label_classificacao.pack(pady=10)

label_tabela = Label(root, text=t, font=("Arial", 12), fg=cor_titulo)
label_tabela.pack()

root.mainloop()
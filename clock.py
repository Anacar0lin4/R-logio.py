import tkinter as tk
from time import strftime


# Função para atualizar o tempo
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


# Configuração da janela
root = tk.Tk()
root.title('Relógio Digital')

# Configuração do rótulo para exibir o tempo
label = tk.Label(root, font=('itau display black', 40, 'bold'), background='orange', foreground='white')
label.pack(anchor='center')

time()  # Chama a função de tempo para iniciar o relógio

root.mainloop()  # Inicia a janela principal



import tkinter as tk

# Crea una ventana con TKinter y la retorna
def create_window():
    
    window = tk.Tk()
    window.title("Una Ventana")
    window.geometry("400x400")
    
    label = tk.Label(window, text="Esta ventana está funcionando!")
    label.pack()

    return window

# Despliega una ventana
def display_window(window):

    window.mainloop()

# Programa de prueba
def main():

    window = create_window()
    display_window(window)
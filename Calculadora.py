import tkinter as tk

# --- FUNCIONES ---

def calcularSuma():
    res = int(entrySumaN1.get()) + int(entrySumaN2.get())
    lebelSuma = tk.Label(ventana, bg="skyblue", relief="flat", font=("Times New Roman", 15, "bold"), text="  =  " + str(res))
    lebelSuma.grid(row=0, column=3)

def calcularResta():
    res = int(entryRestaN1.get()) - int(entryRestaN2.get())
    lebelResta = tk.Label(ventana, bg="skyblue", font=("Times New Roman", 15, "bold"), text="  =  " + str(res))
    lebelResta.grid(row=1, column=3)
    

def calcularMultiplicacion():
    res = int(entryMultiplicacionN1.get()) * int(entryMultiplicacionN2.get())
    lebelMultiplicacion = tk.Label(ventana, bg="skyblue", font=("Times New Roman", 15, "bold"), text="  =   " + str(res))
    lebelMultiplicacion.grid(row=2, column=3)
   

def calcularDivision():
    res = int(entryDivisionN1.get()) / int(entryDivisionN2.get())
    lebelDivision = tk.Label(ventana, bg="skyblue", font=("Arial", 15, "bold"), text=" =  " + str(int(res)))
    lebelDivision.grid(row=3, column=3)    

# --- VENTANA DE CALCULADORA ---

ventana = tk.Tk()
ventana.title(" --- C A L C U L A D O R A --- ")
ventana.geometry("500x200")
ventana.iconbitmap("calcu.ico")
ventana.config(bg="#271B4D", relief="groove", bd=8)

# --- SUMA----

entrySumaN1 = tk.Entry(ventana, fg="grey")
entrySumaN1.grid(row=0, column=0, padx=10, pady=10)

botonSuma = tk.Button(ventana, bg="skyblue", bd=5, activebackground="skyblue", text=" + ", command= calcularSuma)
botonSuma.grid(row=0, column=1, padx=20)

entrySumaN2 = tk.Entry(ventana, fg="grey")
entrySumaN2.grid(row=0, column=2, padx=10, pady=10)

# --- RESTA ---

entryRestaN1 = tk.Entry(ventana, fg="grey")
entryRestaN1.grid(row=1, column=0, padx=10, pady=10)

botonResta = tk.Button(ventana, bg="skyblue",bd=5, activebackground="skyblue", text=" - ", command= calcularResta)
botonResta.grid(row=1, column=1, padx=20)

entryRestaN2 = tk.Entry(ventana, fg="grey")
entryRestaN2.grid(row=1, column=2, padx=10, pady=10)

# --- MULTIPLICACION ---

entryMultiplicacionN1 = tk.Entry(ventana,fg="grey")
entryMultiplicacionN1.grid(row=2, column=0, padx=10, pady=10)

botonMultiplicacion = tk.Button(ventana, bg="skyblue", bd=5, activebackground="skyblue", text=" * ", command= calcularMultiplicacion)
botonMultiplicacion.grid(row=2, column=1, padx=20)

entryMultiplicacionN2 = tk.Entry(ventana, fg="grey")
entryMultiplicacionN2.grid(row=2, column=2, padx=10, pady=10)

# --- DIVISION ---

entryDivisionN1 = tk.Entry(ventana, fg="grey")
entryDivisionN1.grid(row=3, column=0, padx=10, pady=10)

botonDivision = tk.Button(ventana, bg="skyblue", bd=5, activebackground="skyblue", text=" / ", command= calcularDivision)
botonDivision.grid(row=3, column=1, padx=20)

entryDivisionN2 = tk.Entry(ventana, fg="grey")
entryDivisionN2.grid(row=3, column=2, padx=10, pady=10)


ventana.mainloop()
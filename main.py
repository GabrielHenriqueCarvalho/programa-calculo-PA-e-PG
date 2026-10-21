import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        tipo = var_tipo.get()
        a = float(entry_a.get())
        r = float(entry_r.get())
        n = int(entry_n.get())
        
        if n <= 0:
            messagebox.showerror("erro, a quantidade de termos deve ser maior que zero")
            return

        soma = 0
        ultimo = a
        termos = []

        for i in range(n):
            termos.append(str(a))
            soma += a
            ultimo = a

            if tipo == 1:
                a += r
            else:
                a *= r

        lbl_sequencia.config(text="sequência: " + " → ".join(termos))
        lbl_ultimo.config(text=f'último termo: {ultimo}')
        lbl_soma.config(text=f'soma dos termos: {soma}')
        
    except ValueError:
        messagebox.showerror("erro, por favor digite valores válidos")

janela = tk.Tk()
janela.title("PA e PG")
janela.geometry("350x400")
janela.resizable(False, False)

lbl_titulo = tk.Label(janela, text="PA e PG Ali", font=("arial", 16, "bold"))
lbl_titulo.pack(pady=10)

frame_tipo = tk.LabelFrame(janela, text=" escolha o tipo de progressão ", padx=10, pady=5)
frame_tipo.pack(pady=10)

var_tipo = tk.IntVar(value=1)
pa = tk.Radiobutton(frame_tipo, text="progressão aritmética (PA)", variable=var_tipo, value=1)
pa.pack(anchor="w")
pg = tk.Radiobutton(frame_tipo, text="progressão geométrica (PG)", variable=var_tipo, value=2)
pg.pack(anchor="w")

frame_inputs = tk.Frame(janela)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="primeiro termo:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
entry_a = tk.Entry(frame_inputs, width=15)
entry_a.grid(row=0, column=1, padx=5, pady=2)

tk.Label(frame_inputs, text="razão:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
entry_r = tk.Entry(frame_inputs, width=15)
entry_r.grid(row=1, column=1, padx=5, pady=2)

tk.Label(frame_inputs, text="quantidade de termos:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
entry_n = tk.Entry(frame_inputs, width=15)
entry_n.grid(row=2, column=1, padx=5, pady=2)

btn_calcular = tk.Button(janela, text="calcular", command=calcular, fg="white", font=("arial", 10, "bold"))
btn_calcular.pack(pady=15)

lbl_sequencia = tk.Label(janela, text="sequência: ", wraplength=400, justify="center")
lbl_sequencia.pack(pady=2)

lbl_ultimo = tk.Label(janela, text="último termo: ", font=("arial", 10, "bold"))
lbl_ultimo.pack(pady=2)

lbl_soma = tk.Label(janela, text="soma dos termos: ", font=("arial", 10, "bold"))
lbl_soma.pack(pady=2)

janela.mainloop()

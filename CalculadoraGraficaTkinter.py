from tkinter import *
#ventana
v = Tk()
v.title("Calculadora")
#indice variable global
i = 0

#entrada de texto
e_t = Entry(v, font = ("Times 24"))
e_t.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady= 5)
#columnspan es para que abarque el espacio de 4 columnas este widget
#los pad serán el tamaño

#funciones
#click botón, val-valor
def c_b(val):
    global i
    e_t.insert(i, val)
    i += 1

#borrar
def brr():
    e_t.delete(0, END)
    i = 0

#operaciones con eval, ec-ecuación, res-resultado
def ops():
    ec = e_t.get()
    res =eval(ec)
    e_t.delete(0, END)
    e_t.insert(0, res)
    i = 0

#botones
b1 = Button(v, text = "1", width = 5, height = 2, command = lambda: c_b(1))
b2 = Button(v, text = "2", width = 5, height = 2, command = lambda: c_b(2))
b3 = Button(v, text = "3", width = 5, height = 2, command = lambda: c_b(3))
b4 = Button(v, text = "4", width = 5, height = 2, command = lambda: c_b(4))
b5 = Button(v, text = "5", width = 5, height = 2, command = lambda: c_b(5))
b6 = Button(v, text = "6", width = 5, height = 2, command = lambda: c_b(6))
b7 = Button(v, text = "7", width = 5, height = 2, command = lambda: c_b(7))
b8 = Button(v, text = "8", width = 5, height = 2, command = lambda: c_b(8))
b9 = Button(v, text = "9", width = 5, height = 2, command = lambda: c_b(9))
b0 = Button(v, text = "0", width = 15, height = 2, command = lambda: c_b(0))
#bb-borrar, bp-punto, bp1-parentesis1, bp2-parentesis2
bb = Button(v, text = "ac", width = 5, height = 2, command = lambda: brr())
bp1 = Button(v, text = "(", width = 5, height = 2, command = lambda: c_b("("))
bp2 = Button(v, text = ")", width = 5, height = 2, command = lambda: c_b(")"))
bp = Button(v, text = ".", width = 5, height = 2, command = lambda: c_b("."))
#bd-división, bm-multiplicación, bs-suma, br-resta, bi-igual
bd = Button(v, text = "/", width = 5, height = 2, command = lambda: c_b("/"))
bm = Button(v, text = "*", width = 5, height = 2, command = lambda: c_b("*"))
bs = Button(v, text = "+", width = 5, height = 2, command = lambda: c_b("+"))
br = Button(v, text = "-", width = 5, height = 2, command = lambda: c_b("-"))
bi = Button(v, text = "=", width = 5, height = 2, command = lambda: ops())

#agregaar botones en pantalla
bb.grid(row = 1, column = 0, padx = 5, pady = 5)
bp1.grid(row = 1, column = 1, padx = 5, pady = 5)
bp2.grid(row = 1, column = 2, padx = 5, pady = 5)
bd.grid(row = 1, column = 3, padx = 5, pady = 5)
b7.grid(row = 2, column = 0, padx = 5, pady = 5)
b8.grid(row = 2, column = 1, padx = 5, pady = 5)
b9.grid(row = 2, column = 2, padx = 5, pady = 5)
bm.grid(row = 2, column = 3, padx = 5, pady = 5)
b4.grid(row = 3, column = 0, padx = 5, pady = 5)
b5.grid(row = 3, column = 1, padx = 5, pady = 5)
b6.grid(row = 3, column = 2, padx = 5, pady = 5)
br.grid(row = 3, column = 3, padx = 5, pady = 5)
b1.grid(row = 4, column = 0, padx = 5, pady = 5)
b2.grid(row = 4, column = 1, padx = 5, pady = 5)
b3.grid(row = 4, column = 2, padx = 5, pady = 5)
bs.grid(row = 4, column = 3, padx = 5, pady = 5)
b0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
bp.grid(row = 5, column = 2, padx = 5, pady = 5)
bi.grid(row = 5, column = 3, padx = 5, pady = 5)


v.mainloop()

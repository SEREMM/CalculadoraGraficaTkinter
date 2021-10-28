import tkinter#llammos a la librería

ventana = tkinter.Tk()#hacemos la ventana
ventana.geometry("1000x300")#le damos tamaño

et = tkinter.Label(ventana, text = "HOLA AMIX!!!", bg = "blue", padx\
 = 20, pady = 20)#\ sirve para dar espacio sin que se pierda el código
#hacemos una etiqueta y agregamos texto y color
et.pack(fill = tkinter.X)
#posiciona fill, x-ancho, y-alto, se debe usar expand = True con Y

b1 = tkinter.Button(ventana, text = "presiona wex :)", bg = "red", command\
 = lambda: print("si lo presionaste wex c:"), padx = 20, pady = 20)
#los pad lo hacen más grande, al botón se les da el nombre como a las variables
b1.pack(side = tkinter.LEFT)

ct = tkinter.Entry(ventana, font = "helvetica 20", bg = "green")
#agrega una entrada de texto y define fuente y tamaño
ct.pack(side = tkinter.RIGHT)#llama al boton

et2 = tkinter.Label(ventana, bg = "purple", padx = 20, pady =20)
et2.pack(fill = tkinter.Y)

def txc():#función para la caja de texto
    ct1 = ct.get()
    et2["text"] = ct1#agrega la entrada a la misma ventana

b2 = tkinter.Button(ventana, text = "click",bg = "yellow", command = txc)#enlaza la caja de texto
b2.pack(side = tkinter.BOTTOM)

"""método GRID:
divide la ventana en columnas COLUMN (vertical) y filas ROW (horizontal),
lo cual da más organización
comienza en 0 para adelante
No se puede utilizar mientras se usa pack"""
"""
b3 = tkinter.Button(ventana, text = "b3", width = 10, height = 5)
b3.grid(row = 0, column = 0)

b4 = tkinter.Button(ventana, text = "b4", width = 10, height = 5)
b4.grid(row = 1, column = 1)

b5 = tkinter.Button(ventana, text = "b5", width = 10, height = 5)
b5.grid(row = 2, column = 2)
"""
ventana.mainloop()#llamamos la ventana

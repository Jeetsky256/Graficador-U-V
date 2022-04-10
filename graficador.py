from re import X
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from math import *
 
root = tkinter.Tk()
root.wm_title("Graficador u-v")
ta=root.geometry("1000x700")

root2 = tkinter.Tk()
root2.wm_title("Graficador x-y ")
ta2=root2.geometry("1000x700")
 
style.use('fivethirtyeight')
 
fig = Figure()
ax1 = fig.add_subplot(111)
 
canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
 
toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

fig2 = Figure()
ax2 = fig2.add_subplot(111)
 
canvas2 = FigureCanvasTkAgg(fig2, master=root2)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas2.draw()
canvas2.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
 
toolbar2 = NavigationToolbar2Tk(canvas2, root2)# barra de iconos
toolbar2.update()
canvas2.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
 
act_rango=False
ul_ran=""
ran=""
act_rango2=False
ul_ran2=""
ran2=""
Con = ""
def animate(i):
    global act_rango
    global ul_ran
    if act_rango==True:
        try:
            lmin = float(ran[0]); lmax = float(ran[1])
            if lmin < lmax:
                x = np.arange(lmin, lmax, .01)#.01
                ul_ran = [lmin, lmax]
            else:
                act_rango = False
        except:
            messagebox.showwarning("Error","Introduzca los valores del rango de x, separado por coma.")
            act_rango=False
            ets.delete(0,len(ets.get()))
    else:
        if ul_ran!="":
            x = np.arange(ul_ran[0],ul_ran[1], .01)#.01
        else:
            x = np.arange(1, 10, .01)#.01
    try:
        solo=eval(graph_data)
        ax1.clear()
        ax1.plot(x,solo)
    except:
        ax1.plot()
    ax1.axhline(0, color="gray")
    ax1.axvline(0, color="gray")
    ani.event_source.stop() #DETIENE ANIMACIÓN
 
def represent():
    global graph_data
    global ran
    global act_rango
    texto_orig=et.get()
    if ets.get()!="":
        rann=ets.get()
        ran=rann.split(",")
        act_rango=True
    ta=texto_orig.replace("sin","np.sin")
    tb=ta.replace("cos","np.cos")
    tl=tb.replace("log","np.log")
    tc=tl.replace("tan","np.tan")
    tr=tc.replace("sqrt","np.sqrt")
    te=tr.replace("exp","np.exp")
    tpi=te.replace("pi","np.pi")
    graph_data=tpi
    ani.event_source.start() #INICIA/REANUDA ANIMACIÓN

def animate2(i):
    global act_rango2
    global ul_ran2
    global Con
    if act_rango2==True:
        try:
            lmin2 = float(ran2[0]); lmax2 = float(ran2[1])
            if lmin2 < lmax2:
                x = np.arange(lmin2, lmax2, .01)#.01
                ul_ran2 = [lmin2, lmax2]
            else:
                act_rango2 = False
        except:
            messagebox.showwarning("Error","Introduzca los valores del rango de x, separado por coma.")
            act_rango2=False
            ets2.delete(0,len(ets2.get()))
    else:
        if ul_ran2!="":
            x = np.arange(ul_ran2[0],ul_ran2[1], 1)#.01
        else:
            x = np.arange(1, 2, 1)#.01
    try:
        solo=eval(graph_data2)
        ax2.clear()
        ax2.plot(x,solo)
        Con = (x,solo)
        print(Con)
    except:
        ax2.plot()
    ax2.axhline(0, color="gray")
    ax2.axvline(0, color="gray")
    ani2.event_source.stop() #DETIENE ANIMACIÓN
    return Con

  
def represent2():
    global graph_data2
    global ran2
    global act_rango2
    texto_orig2=et2.get()
    if ets2.get()!="":
        rann2=ets2.get()
        ran2=rann2.split(",")
        act_rango2=True
    ta=texto_orig2.replace("sin","np.sin")
    tb=ta.replace("cos","np.cos")
    tl=tb.replace("log","np.log")
    tc=tl.replace("tan","np.tan")
    tr=tc.replace("sqrt","np.sqrt")
    te=tr.replace("exp","np.exp")
    tpi=te.replace("pi","np.pi")
    graph_data2=tpi
    ani2.event_source.start() #INICIA/REANUDA ANIMACIÓN

 
 
ani = animation.FuncAnimation(fig, animate, interval=1000)
ani2 = animation.FuncAnimation(fig2, animate2, interval=1000)
plt.show()
 
 
et = tkinter.Entry(master=root,width=60)
et.config(bg="gray87", justify="left")
 
button = tkinter.Button(master=root, text="SET", bg="gray69", command=represent)
button.pack(side=tkinter.BOTTOM)
 
et.pack(side=tkinter.BOTTOM)
ets=tkinter.Entry(master=root,width=20)
ets.config(bg="gray87")
ets.pack(side=tkinter.RIGHT)
#ets.insert(0,"RANGO DE X")

et2 = tkinter.Entry(master=root2,width=60)
et2.config(bg="gray87", justify="left")
 
button2 = tkinter.Button(master=root2, text="SET", bg="gray69", command=represent2)
button2.pack(side=tkinter.BOTTOM)
 
et2.pack(side=tkinter.BOTTOM)
ets2=tkinter.Entry(master=root2,width=20)
ets2.config(bg="gray87")
ets2.pack(side=tkinter.RIGHT)
 
tkinter.mainloop()
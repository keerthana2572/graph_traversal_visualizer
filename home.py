
from tkinter import *


ws = Tk()

ws.geometry('800x600')
ws.title('visualizer')
canvas =Canvas(ws)

canvas.config(width=80, height=60)









def nextPage():
    ws.destroy()
    import UI


def prevPage():
    ws.destroy()



Label(
    ws,
    text="Graph Traversal Visualizer",
    padx=20,
    pady=20,
    bg='#231955',
    fg="#47B5FF",
    font=("Philosopher",35)
).pack(expand=True, fill=BOTH)
Button(
    ws,
    text="Start",
    font=("Philosopher",24),
    fg="white",
    bg="black",
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Quit",
    font=("Philosopher",24),
    fg="white",
    bg="black",
    command=prevPage
).pack(fill=X, expand=TRUE, side=LEFT)


ws.mainloop()
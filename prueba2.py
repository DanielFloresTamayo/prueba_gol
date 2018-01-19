import time
from tkinter import *

tk = Tk()
balonX=10
balonY=250
canvas = Canvas(tk, width=800, height=500)
canvas.pack()

my_image = PhotoImage(file="balon.gif")
my_image1 = PhotoImage(file="gool.gif")
my_imageGol= PhotoImage(file="goal.gif")
##arco
xArco=300
imagen = canvas.create_image(xArco, 100, anchor=NW, image=my_image1)
##balon

imagen = canvas.create_image(balonX, balonY, anchor=NW, image=my_image)




def moverBalon(event):
    global balonX
    global balonY
    for x in range(1,5):

        if event.keysym == 'Up':
            canvas.move(2, 0, -3)
        elif event.keysym == 'Down':
            canvas.move(2, 0, 3)
        elif event.keysym == 'Left':
         canvas.move(2, -3, 0)
         balonY = balonY + 3
         if balonY >= 300:
            print(balonY)
        else:
            canvas.move(2, 3, 0)
            balonY = balonY + 3
            if balonY > 550:
                print(balonY)
                print("Goalllllll!!!!!")
                # imagen gano!!!!!
                imagen = canvas.create_image(10, 200, anchor=NW, image=my_imageGol)


canvas.bind_all('<KeyPress-Up>', moverBalon)
canvas.bind_all('<KeyPress-Down>', moverBalon)
canvas.bind_all('<KeyPress-Left>', moverBalon)
canvas.bind_all('<KeyPress-Right>', moverBalon)



tk.mainloop()

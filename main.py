from tkinter import *
from tkinter import ttk
from miloLibrary import *

window = Tk()

label = Label(window, 
			text = "MiloTheCleaner",
			font = ('Arial', 40, 'bold'),
			relief=RAISED)


getFiles = Button(window, 
				text="Clean Up!",
				command=lambda: [findBooks(), findAudio()], #function
				height = 10,
				width = 20,
				activeforeground="#00FF00",
				activebackground="black",
				highlightcolor="#FBC7D4"
				)







label.pack()
getFiles.pack()


window.mainloop()


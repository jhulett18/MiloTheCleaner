from tkinter import *
from tkinter import ttk
from miloLibrary import *

window = Tk()

#Define the size of window or frame
window.geometry("715x250")


# def display_selected(choice):
# 	choice = menu.get()
# 	print(choice)

# def check(dropdownChange):
#     print(f"the variable has changed to '{dropdownChange.get()}'")

# search_location = ["Downloads", "Documents"]
# Text "Please select which folder to organize"
# text = tk.Text(master, conf={}, **kw)


# # Dropdown Menu 
# menu = StringVar()

# # Sets initial value
# menu.set(search_location[0])

# # Tracks changes
# menu.trace_add('write', check)

# Dropdown options
# dropdown= OptionMenu(window, menu, *search_location, command=display_selected(menu))

# Title
label = Label(window, 
			text = "MiloTheCleaner",
			font = ('Arial', 40, 'bold'),
			relief=RAISED)

# Clean button and functions
getFiles = Button(window, 
				text="Clean Up!",
				command=lambda: [findBooks(), findAudio()], #function
				height = 5,
				width = 10,
				activeforeground="#00FF00",
				activebackground="black",
				highlightcolor="#FBC7D4"
				)


# text.pack()
# dropdown.pack(expand=True)
label.pack()
getFiles.pack()


window.mainloop()


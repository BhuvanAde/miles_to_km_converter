import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#label
my_label = tkinter.Label(text= "I Am a Label",font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"


#Buttons
def button_clicked():
    new_text = input.get()
    my_label.config(text = new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=3, row=1)

#Entry

input = tkinter.Entry(width=10)
input.grid(column=4, row=4)
input.get()








window.mainloop()
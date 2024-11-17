import tkinter
from tkinter import messagebox
root = tkinter.Tk()

def on_click_submit():
    name = name_textbox.get()
    messagebox.showinfo("Captured Data", name)

    
root.title("Name Registration")
root.geometry("300x200")
root.configure(bg="#D3D3D3")

name_label = tkinter.Label(root, text="Name")
name_label.pack(anchor=tkinter.W, padx=30)
name_label.configure(bg="#D3D3D3")
name_textbox = tkinter.Entry(root)
name_textbox.pack(anchor=tkinter.W, padx=30)

email_label = tkinter.Label(root, text="Email")
email_label.pack(anchor=tkinter.W, padx=30)
email_textbox = tkinter.Entry(root)
email_textbox.pack(anchor=tkinter.W, padx=30)

phone_label = tkinter.Label(root, text="Phone")
phone_label.pack(anchor=tkinter.W, padx=30)
phone_textbox = tkinter.Entry(root)
phone_textbox.pack(anchor=tkinter.W, padx=30)

submit_button = tkinter.Button(root, text="Submit",command=on_click_submit)
submit_button.pack(anchor=tkinter.S)
root.mainloop()
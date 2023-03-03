#the contacts management app
from tkinter import *
from tkinter import messagebox
#creating the screeen
window= Tk()
window.title("Chris contacts")
window.minsize(width=400, height= 300)
window.config(padx=30,pady=30, bg="black")
##creating the command for saving new contacts

def save():
    contact_answer= contact_input.get()
    name_answer= name_input.get()
    if len(contact_answer)==0 or len(name_answer)==0:
        messagebox.showinfo("Empty filled","No text filled should be left")
    else:
        yes_save = messagebox.askokcancel(f"{name_answer}", f"contacts to save:\n Name: {name_answer}\n Contacts: {contact_answer}\n are you sure you want to save this contacts?")
        if yes_save:
            with open("contact.txt", "a") as file:
                file.write(f"name: {name_answer} | contact: {contact_answer}\n")
            contact_input.delete(0, END)
            name_input.delete(0,END)
            name_input.focus()
def all_contacts():
    def hide_all():
        all_con.destroy()
        close_button.destroy()
    with open("contact.txt") as all_contact:
        power = all_contact.read()
    all_con = Label(text= power, font=("courier", 20), bg="black", fg="white")
    all_con.grid(row= 5, column= 1, columnspan= 4)
    close_button = Button (text ="Hide" , bg="white", fg="black",command= hide_all, font=("courier", 20))
    close_button.grid(row=20, column=5)
##creating the label elements
#name label
title= Label(text="Chris contact's management", font=("courier", 26), width=30, bg="black", fg="white")
title.grid(row=0, column=0, columnspan=5)
name= Label(text="Name:", font=("courier", 23, "italic"), width=10,  bg="black", fg="white")
name.grid(row=1,column=0)

contact= Label(text="Contacts:", font=("courier", 23, "italic"), width=10, bg="black", fg="white")
contact.grid(row=2, column=0)
#creating the user input
name_input=Entry(width= 20, bg='#eee', font=("courier", 23))
name_input.grid(row=1, column=1, columnspan= 2)
contact_input= Entry(width=20, font=("courier", 23), bg="#eee")
contact_input.grid(row= 2, column= 1, columnspan=2)
#creating the submit button
submit_button= Button(text="Create", font=("courier"), width=15, command= save)
submit_button.config(padx=10, pady=10)
submit_button.grid(row=4, column= 1)
all_button= Button(text="ALL", font=("courier"), width=15, command= all_contacts)
all_button.config(padx=10, pady=10)
all_button.grid(row=4, column=2)
window.mainloop()
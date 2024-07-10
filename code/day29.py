from tkinter import *
from tkinter import messagebox
import day29_password

#
# counter = 0
#
# def set_default_email():
#     global counter
#     ye_or_nay=messagebox.askyesno(title="use dafult email", message="Your default email is {abdon3899@gmail.com}")
#     if ye_or_nay == "Yes":
#         user_entry.insert(0,"abdo@nasr.com")
#     else:
#         if counter == 0:
#             x = input("Enter your default email: ")
#             user_entry.delete(0, END)
#             user_entry.insert(0, x)
#             counter += 1


# change email form here
defult_email ="go to line 22 in code to change this email "


def filee():
    websit_name = web_entry.get()
    username=user_entry.get()
    password = pass_entry.get()

    if len(websit_name) < 1 or len(username) < 1 or len(password) < 1 :
        messagebox.showerror(title="warning", message="Please fill all the data ")

    else:
        is_ok =messagebox.askokcancel(title= websit_name, message=f"these are the details entered:\n"
                                                                  f"email:{username} \npassword:{password} \n"
                                                                  f"is it ok to save?")
        if is_ok ==True:
            with open("passwords.txt" , "a") as file:
                file.write(f"{websit_name} | {username} | {password} \n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


def gen_password():
    password = day29_password.generate_password()
    pass_entry.delete(0, END)  # Clear the entry before inserting the new password
    pass_entry.insert(0, password)


# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Logo
canvas = Canvas(width=200, height=200)
pic = PhotoImage(file="logo.png")  # Make sure the logo file is in the same directory
canvas.create_image(100, 100, image=pic)
canvas.grid(row=0, column=1)

# Website label
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

# Website input
web_entry = Entry(width=45)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

# Email label
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

# Email input
user_entry = Entry(width=45)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, defult_email)


# Password label
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0 , padx =0)


# Password input
pass_entry = Entry(width=25)
pass_entry.grid(row=3, column=1, sticky="E", )


# Password button
pass_button = Button(text="Generate Password", width=15 , command=gen_password)
pass_button.grid(row=3, column=2, sticky="W")

# Add button
add_button = Button(text="Add", width=35, command= filee)
add_button.grid(row=4, column=1, columnspan=2)


# set_default_email()


window.mainloop()

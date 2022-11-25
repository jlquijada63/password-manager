from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas

canvas = Canvas(width=200, height=200)
my_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=my_image)  # 100, 100 is the center of the image
canvas.grid(row=0, column=1)

# Labels

website = Label(text='Website: ')
website.grid(column=0, row=1)

email = Label(text='Email/Username: ')
email.grid(column=0, row=2)

password = Label(text='Password: ')
password.grid(column=0, row=3)

# Entries

txt_website = Entry(width=35)
txt_website.grid(column=1, row=1, columnspan=2)
txt_website.focus()

txt_email = Entry(width=35)
txt_email.grid(column=1, row=2, columnspan=2)
txt_email.insert(0, 'test@test.com')

txt_password = Entry(width=21)
txt_password.grid(column=1, row=3)

# Buttons

gen_pass = Button(text='Generate Password')
gen_pass.grid(column=2, row=3)

add = Button(text='add', width=36)
add.grid(column=1, row=4, columnspan=2)







window.mainloop()

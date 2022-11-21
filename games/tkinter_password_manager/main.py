import json
import tkinter as tk
from tkinter import messagebox
import random
from tkinter import ttk

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specific = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
            '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
letters_upper = [x.upper() for x in letters]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    password = ''
    for x in range(3):
        x = random.choice(letters) + random.choice(numbers) + random.choice(specific) + random.choice(letters_upper)
        password += str(x)
    input_password.delete(0, tk.END)
    input_password.insert(0, password)

def find_password():
    get_website = input_website.get().title()
    try:
        with open("data.json", mode="r") as datajson:
            data = json.load(datajson)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if get_website in data:
            email = data[get_website]["email"]
            password = data[get_website]["password"]
            messagebox.showinfo(title=get_website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {get_website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    get_website = input_website.get().title()
    get_email = input_email.get()
    get_password = input_password.get()
    new_data = {
        get_website: {
            "email": get_email,
            "password": get_password,
        }
    }
    if get_website == '' or get_email == '' or get_password == '':
        messagebox.showerror("Oops", "Please don't leave any fields empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, tk.END)
            input_email.delete(0, tk.END)
            input_password.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)
window.resizable(False, False)

# CANVAS
canvas = tk.Canvas(width=470, height=320)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(250, 90, image=logo)

# LABELS
website = tk.Label(text="Website:", font=("Arial", 10, "bold"))
website.place(x=20, y=200)
email = tk.Label(text="Email/Username:", font=("Arial", 10, "bold"))
email.place(x=20, y=225)
password = tk.Label(text="Password:", font=("Arial", 10, "bold"))
password.place(x=20, y=250)

# ENTRIES
input_website = tk.Entry(width=20)
input_website.place(x=150, y=200)

input_email = tk.Entry(width=50)
input_email.place(x=150, y=225)

input_password = tk.Entry(width=20)
input_password.place(x=150, y=250)

# BUTTONS
generate_button = tk.Button(text="Generate Password", font=("Arial", 10, "bold"), command=generate)
generate_button.place(x=320, y=250)

add_button = tk.Button(text="Add", font=("Arial", 10, "bold"), command=save)
add_button.place(x=150, y=290, width=305)

search_button = tk.Button(text="Search", font=("Arial", 10, "bold"), width=16, command=find_password)
search_button.place(x=320, y=195)

canvas.pack()
window.mainloop()

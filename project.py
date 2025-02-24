import tkinter as tk
from tkinter import messagebox

#Button functions
def add_training_plan():
    messagebox.showinfo("Training planning", "Function of adding a training plan")

def add_meal_plan():
    messagebox.showinfo("Nutrition", "Function of adding a meal plan")

def add_water_intake():
    messagebox.showinfo("Water balance", "Function of adding water balance")

def show_about():
    messagebox.showinfo("About app", "This app is for planning your trainings and monitor your health")

# App window
root = tk.Tk()
root.title("Fitness app")
root.geometry("600x400")
root.iconbitmap("fitness.ico")
root.config(bg="#6f89aa")

# Main menu
menubar = tk.Menu(root)
root.config(menu=menubar)

# File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Info menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Info", menu=help_menu)

# Title
title = tk.Label(root, text="Fitness app", bg="#1d4646", fg="#FFECF0", font=("Arimo", 24))
title.pack(pady=10)

# Adding training plan button
training_button = tk.Button(root, text="Add training plan", command=add_training_plan, bg="#946fa3", fg="#FFECF0", font=("Arimo", 16))
training_button.pack(pady=5)

# Adding nutrition plan button
nutrition_button = tk.Button(root, text="Add meal plan", command=add_training_plan, bg="#5c4c84", fg="#FFECF0", font=("Arimo", 16))
nutrition_button.pack(pady=5)

# Adding water intake button
water_button = tk.Button(root, text="Add water balance", command=add_training_plan, bg="#85d6a9", fg="#040414", font=("Arimo", 16))
water_button.pack(pady=5)

root.mainloop()

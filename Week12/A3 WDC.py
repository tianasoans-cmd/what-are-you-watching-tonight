import pandas as pd
import random
import tkinter as tk


df = pd.read_csv("disney+.csv")

l_movies = list(zip(df['title'], df['release_year'].astype(str)))


def suggest():
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    r = random.choice(l_movies)
    name = r[0]
    year = r[1]
    msg = f"{name} ({year})"
    t1.insert(tk.END, msg)
    t1.config(state='disabled')


window = tk.Tk()
window.geometry("1000x600")
window.config(bg="#BFD7ED")
window.title("What are you watching tonight?")

l1 = tk.Label(window, text="What are you watching tonight?",
              font=("Times New Roman", 20), fg="dark blue", bg="white")
b1 = tk.Button(window, text="Suggest Movie", font=("Times New Roman", 15),
               bg="black", fg="white", command=suggest)
t1 = tk.Text(window, width=80, height=10, font=("Times New Roman", 15), state='disabled')

l1.place(x=200, y=40)
b1.place(x=420, y=100)
t1.place(x=200, y=200)

window.mainloop()
# import required modules to make the project run

import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox

# reading the file with the required dataset via Kaggle,  instead of using all the names and info on titles etc.

df = pd.read_csv('disney.csv')

# extracting the needed categories from the above dataset, to show on the final suggestion result
# creating them into a list, for easier use throughout the rest of the code --> including cruicial data that will be
#    used in the final result box.

l_movies = list(zip(
    df['title'],
    df['release_year'].astype(str),
    df['duration'],
    df['description'].astype(str),
    df['type'],
    df['Genre']))

# for the genre list, this will ensure that the movies that have no values in the collumn are removed
# cruicially, this will treat all genre's as strings --> and then split into several categories instead of 1 long one.
# (e.g for movies or shows that have something like Action, Adventure, Comedy it will be seperated into 3 seperate cats.)

genre_list = df['Genre'].dropna().astype(str).apply(lambda x: [g.strip() for g in x.split(',')])
all_genres = sorted(set(g for sublist in genre_list for g in sublist))

# creating the interface using TKinter, making it non-reziable so that the sizing doesn't warp when enlarged
# Inspired by code from Isha Bansal and Phython's documents

window = tk.Tk()
window.geometry("1000x600")
window.resizable(width=False, height=False)
window.config(bg="#BFD7ED")
window.title("What are you watching tonight?")

# creating the options for the optionmenus --> Type (movie or TV Show) and Genre (e.g Comedy,Action)
# drawing on key concepts from Python Tutorial + online forums that discuss the 'Tkinter OptionMenu'

options = ('disney.csv')

#defining what the options are, and what the default should be for the Optionbox
# the default answer is 'any' as it is a broader category

#creating two string varibales for the dropdown OptionMenu's selection
# defining type and genre for the final output
# drawing on concepts from the online documents on Python

type_var = tk.StringVar(value="Any")
genre_var = tk.StringVar(value="Any")

#defining the labels for the OptionMenu
# taking inspiration from Python's online documents + online forum 'geeks for geeks'

type_options = ["Any"] + sorted(df['type'].dropna().unique().tolist())
genre_options = ["Any"] + all_genres

# Creating the physical OptionMenu for genres and types
# inspired by help documents on Python

# 'type' menu setup, including the font, text, back and forground colours and where it is placed

tk.Label(window, text="Select Type:", font=("Times New Roman", 15), bg="#BFD7ED").place(x=200, y=120)
type_menu = tk.OptionMenu(window, type_var, *type_options)
type_menu.place(x=330, y=120)

# 'genre' menu setup, including the font, what the text says, background colour and where it is placed

tk.Label(window, text="Select Genre:", font=("Times New Roman", 15), bg="#BFD7ED").place(x=550, y=120)
genre_menu = tk.OptionMenu(window, genre_var, *genre_options)
genre_menu.place(x=690, y=120)

# creating the box which has the suggestion when users input their preferences
#needed it wider so that the description of the movie would fit in, and all the writing wasn't squished in

t1 = tk.Text(window, width=80, height=12, font=("Times New Roman", 15), state='disabled')
t1.place(x=150, y=250)

# creating the algorithm to suggest for users
# inspired by code from Isha Bansal and Python online documents

# defining suggestion by combining the variables to create an algorithm to accurately suggest something to watch.

def suggest():
    t1.config(state='normal')
    t1.delete('1.0', tk.END)

    selected_type = type_var.get()
    selected_genre = genre_var.get()

    filtered_list = [
        movie for movie in l_movies
        if (selected_type == "Any" or movie[4] == selected_type)
        and (selected_genre == "Any" or selected_genre in movie[5])
    ]

# error code message
# drawing on ideas learnt from Python's online documents about tkinter.messagebox

# this error code message will appear when there is no suggestion found based on input categories
# prompting users to try again, rather than leaving without a reason why there is no answer

    if not filtered_list:
        messagebox.showerror(title="Error", message="No suggestions found, please try again.")
        t1.config(state='disabled')
        return

# the code that will show users what their suggestion is


    r = random.choice(filtered_list)
    name, year, duration, description, type_, genre = r

# this is the order and how they will appear in the textbox on Tkinter --> allowing it to be easily read

    msg = (
        f"🎬 Title: {name}\n"
        f"✨ Year: {year}\n"
        f"🕰️ Duration: {duration}\n"
        f"📺 Type: {type_}\n"
        f"🎨 Genre: {genre}\n\n"
        f"🪩 Description:\n{description}"
    )

    t1.insert(tk.END, msg)
    t1.config(state='disabled')

# all the labels + buttons, placements, colours etc.
# using colour codes from Canva + inspired by code from Isha Bansal

l1 = tk.Label(window, text="What are you watching tonight?",
              font=("Times New Roman", 20), fg="#003b73", bg="#f4f5f4")
l1.place(x=370, y=50)

L2 = tk.Label(window, text="🤔🧚‍♀️📺✨",
              font=("Times New Roman",15), bg="#BFD7ED")
L2.place(x=450, y=80)

b1 = tk.Button(window, text="Suggest Movie", font=("Times New Roman", 15),
               bg="#111410", fg="#003b73", command=suggest)
b1.place(x=420, y=200)

# running the code

window.mainloop()


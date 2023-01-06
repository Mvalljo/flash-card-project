from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


def random_word():
    canvas.delete("word")
    data = pandas.read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient="records")
    word = random.choice(data_dict)
    foreign_word = word["French"]
    front_word = canvas.create_text(400, 263, text=foreign_word, font=("Ariel", 40, "italic"), tags="word")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_img)
canvas.grid(column=0, row=0, columnspan=2)
front_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
random_word()

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, bd=0, command=random_word)
wrong_btn.grid(column=0, row=2)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, bd=0, command=random_word)
right_btn.grid(column=1, row=2)

window.mainloop()

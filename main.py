from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_lean.csv")
    data_dict = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient="records")


# If user clicks on right it should remove word from data_list
# remove()
def words_to_learn():
    random_word()
    data_dict.remove(word)
    # Afterwards it should be saved to new file words_to_lean.csv
    # data.to_csv("words_to_lean.csv", index=False)
    new_data_dict = pandas.DataFrame(data_dict)
    new_data_dict.to_csv("./data/words_to_lean.csv", index=False)


def random_word():
    global word, timer
    window.after_cancel(timer)
    word = random.choice(data_dict)
    canvas.itemconfig(front_title, text="French")
    canvas.itemconfig(front_word, text=word["French"])
    canvas.itemconfig(canvas_img, image=front_card_img)
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=back_card_img)
    canvas.itemconfig(front_title, text="English")
    canvas.itemconfig(front_word, text=word["English"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)
front_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
front_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "italic"), tags="word")
random_word()

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, bd=0, command=random_word)
wrong_btn.grid(column=0, row=2)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, bd=0, command=words_to_learn)
right_btn.grid(column=1, row=2)

window.mainloop()

import tkinter as tk
from tkinter import messagebox
import random
import requests

root = tk.Tk()
root.title("Hangman")

response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt")
words = response.text.split("\n")
word_list = [word.upper() for word in words if len(word) in [5, 6, 7]]

random_word = random.choice(word_list)
guessed_letters = []

hangman_images = [
    '''
       +---+
           |
           |
           |
          ===
    ''',
    '''
       +---+
       O   |
           |
           |
          ===
    ''',
    '''
       +---+
       O   |
       |   |
           |
          ===
    ''',
    '''
       +---+
       O   |
      /|   |
           |
          ===
    ''',
    '''
       +---+
       O   |
      /|\\  |
           |
          ===
    ''',
    '''
       +---+
       O   |
      /|\\  |
      /    |
          ===
    ''',
    '''
       +---+
       O   |
      /|\\  |
      / \\  |
          ===
    '''
]

hangman_image_index = 0


def guess_letter(event=None):
    global hangman_image_index
    letter = letter_entry.get().upper()

    if len(letter) > 1:
        if letter == random_word:
            messagebox.showinfo("Congratulations", "You won!")
            reset_game()
        else:
            hangman_image_index += 1
            update_hangman_image()

            if hangman_image_index == 6:
                messagebox.showinfo("Game Over", "You lost! The word was: " + random_word)
                reset_game()
    elif len(letter) == 1 and letter.isalpha():
        if letter in guessed_letters:
            messagebox.showinfo("Duplicate Letter", "You have already guessed this letter.")
        else:
            guessed_letters.append(letter)
            if letter not in random_word:
                hangman_image_index += 1

            update_word_display()
            update_hangman_image()

            if hangman_image_index == 6:
                messagebox.showinfo("Game Over", "You lost! The word was: " + random_word)
                reset_game()
            elif "_" not in word_label.cget("text"):
                messagebox.showinfo("Congratulations", "You won!")
                reset_game()
    else:
        messagebox.showinfo("Invalid Input", "Please enter a single alphabetic character or a full word.")

    letter_entry.delete(0, tk.END)


def update_word_display():
    word_display = ""
    for char in random_word:
        if char in guessed_letters:
            word_display += char + " "
        else:
            word_display += "_ "
    word_label.config(text=word_display)


def update_hangman_image():
    hangman_image_label.config(text=hangman_images[hangman_image_index])


def reset_game():
    global hangman_image_index, guessed_letters, random_word
    hangman_image_index = 0
    guessed_letters = []
    random_word = random.choice(word_list)
    update_word_display()
    update_hangman_image()
    letter_entry.delete(0, tk.END)


hangman_image_label = tk.Label(root, font=("Courier", 14), justify=tk.LEFT, compound=tk.TOP)
hangman_image_label.pack()

word_label = tk.Label(root, font=("Courier", 20))
word_label.pack()

letter_entry = tk.Entry(root, font=("Courier", 16))
letter_entry.pack()
letter_entry.bind("<Return>", guess_letter)

update_word_display()
update_hangman_image()

root.mainloop()

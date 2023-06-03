import random

word = ['SPORTY', 'SZACHY', 'BURAKI', 'PUCHAR', 'PYTHON', 'KOTLIN', 'BAMBIK', 'KOLARZ', 'ANANAS', 'KLASAB']
random_word = random.choice(word)

print(
    "Witaj w grze w wisielca! Twoim zadaniem jest zgadywać litery 6-literowych słów. Masz 8 prób, później wieszamy cię i tracisz ostatnią szansę!")

hang = 8
guessed_letters = []
tries = 0
while hang > 0:
    for i, letter in enumerate(random_word, start=1):
        if letter in guessed_letters:
            print(f"Litera {i}: {letter}")
        else:
            print(f"Litera {i}: ?")

    guess = input("Podaj literę (zapisz ją używając Caps Locka oraz nie podawaj cyfr, stracisz próbę!): ")

    if not guess.isalpha():
        tries += 1
        print(f"BŁĄD! NIE CZYTASZ POLECENIA!!! Tracisz próbę! Ilość zużytych prób: {tries}")
        hang -= 1
    elif guess in guessed_letters:
        print("Ta litera została już zgadnięta! Spróbuj ponownie.")
    elif guess in random_word:
        tries += 1
        print(f"Brawo! Ta litera jest w moim słowie! Ilość zużytych prób: {tries}")
        guessed_letters.append(guess)
    else:
        tries +=1
        print(f"Ta litera nie występuje w moim słowie! Ilość zużytych prób: {tries}")
        hang -= 1

    if set(random_word) == set(guessed_letters):
        print("Gratulacje! Zgadłeś wszystkie litery. Wygrywasz!")
        break

if hang == 0:
    print("Zostałeś skazany na WYROK ŚMIERCI. GAME OVER.")

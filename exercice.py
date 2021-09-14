#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    return len(string) % 2 == 0



def remove_third_char(string: str) -> str:
    string2 = ""
    index = 0
    for lettre in string:
        if index != 2:
            string2 += lettre
        index += 1
    return string2


def replace_char(string: str, old_char: str, new_char: str) -> str:
    string2 = ""
    for letter in string:
        if letter == old_char:
            string2 += new_char
        else:
          string2 += letter
    return string2


def get_number_of_char(string: str, char: str) -> int:
    counter = 0
    for letter in string:
        if letter == char:
            counter += 1
    return counter


def get_number_of_words(sentence: str, word: str) -> int:
    counter = 0
    for w in sentence.split():
       if w == word:
           counter += 1

    return counter




def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()

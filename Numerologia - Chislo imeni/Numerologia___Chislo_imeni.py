from module1 import*
letters=read_from_file("letters.txt")
numbers=read_from_file("numbers.txt")
one=read_from_file("one.txt")
two=read_from_file("two.txt")
three=read_from_file("three.txt")
four=read_from_file("four.txt")
five=read_from_file("five.txt")
six=read_from_file("six.txt")
seven=read_from_file("seven.txt")
eight=read_from_file("eight.txt")
nine=read_from_file("nine.txt")

while 1:
    print("Привет! Давай узнаем число твоего имени! Для этого введи цифру 1. Если хочешь выйти из программы, введи 2.")
    v=input()
    if v=="1":
        name=input("Введи своё имя: ")
        name_number(letters, numbers, name)
    else:
        print("До встречи!")
# Лаба №1

# print("Hello world,", input('Введите ваше имя -> '))

# Лаба №2

# a = int(input('Введите первое число -> '))
# b = int(input('Введите второе число -> '))
# print(f' {a+b} \n {a-b} \n {a*b} \n {a**b} ')
# if (a != 0 and b != 0):
#   print(f' {a/b} \n {a//b} \n {a%b}')

# Лаба №3

# import random
# Listok = [random.randint(-123, 198) for i in range(10)]
# Listok.sort()
# print(Listok)
# print(max(Listok),'\n',min(Listok))
# sum = 0
# for i in Listok:
#   sum += i
# print(sum)

# Лаба №4

# import random
# from tkinter import filedialog
# file1 = open("laba.txt", "w+")
# Listok1 = [random.randint(-123, 198) for i in range(10)]
# file1.write(' '.join(map(str, Listok1)))
# file1.close()
# file2 = open("laba2.txt", "w+")
# Listok2 = [random.randint(-123, 198) for i in range(10)]
# file2.write(' '.join(map(str, Listok2)))
# file2.close()
# my_file_path = filedialog.askopenfilename()
# my_file = open(my_file_path, "r")
# fileContent = my_file.read()
# print(fileContent)
# fileContentInt = list(map(int, fileContent.split()))
# average = sum(fileContentInt) / len(fileContentInt)
# print(average)

# Лаба №5

# class Cat:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def meow(self):
#     print("Мяу")

#   def description(self):
#     print(f'Имя: {self.name}')
#     print(f'Возраст: {self.age}')

# my_cat = Cat("barsik", 3)
# my_cat.description()
# my_cat.meow()

# class Dog(Cat):
#   def __init__(self, name, age, breed):
#     super().__init__(name, age)
#     self.breed = breed
#   def woof(self):
#     print("Гав")
# my_dog = Dog("Rex", 5, "bruh")
# my_dog.description()
# print(f'Порода: {my_dog.breed}')
# my_dog.meow()

# Лаба №6

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import random
from playsound import playsound

file1 = open("laba.txt", "w+")
Listok1 = [random.randint(-123, 198) for i in range(10)]
file1.write(' '.join(map(str, Listok1)))
file1.close()
file2 = open("laba2.txt", "w+")
Listok2 = [random.randint(-123, 198) for i in range(10)]
file2.write(' '.join(map(str, Listok2)))
file2.close()

window = Tk()

def name_btn_click():
  NamePrint = Name.get()
  NameText['text'] = f'Hello world, {NamePrint}!'

def number_btn_click():
  a = firstNumber.get()
  b = SecondNumber.get()
  a = int(a)
  b = int(b)
  NumberSum['text'] = f' {a+b} \n {a-b} \n {a*b} \n {a**b} \n Дальнейшие операции выполнить невозможно'
  if (a != 0 and b != 0):
     NumberSum['text'] = f' {a+b} \n {a-b} \n {a*b} \n {a**b} \n {a/b} \n {a//b} \n {a%b}'

def random_btn_click():
  Listok = [random.randint(-123, 198) for i in range(10)]
  Listok.sort()
  RandomString['text'] = Listok
  RandomMin['text'] = f' Минимальное число -> {min(Listok)}'
  RandomMax['text'] = f' Максимальное число число -> {max(Listok)}'
  sum = 0
  for i in Listok:
    sum += i
  RandomSum['text'] = f'Сумма всех чисел -> {sum}'

def file_btn_click():
  my_file_path = filedialog.askopenfilename()
  my_file = open(my_file_path, "r")
  fileContent = my_file.read()
  FileText['text'] = fileContent
  fileContentInt = list(map(int, fileContent.split()))
  average = sum(fileContentInt) / len(fileContentInt)
  FileAverage['text'] = f'Среднее значение чисел -> {average}'

def meow_btn_click():
  playsound('sources/meow.mp3')

def bark_btn_click():
  playsound('sources/bark.mp3')

window.title('bruh')
window.geometry('1000x750')

frame = Frame(window)
frame.place(relheight=1, relwidth=1, rely=0.05)

NameTitle = ttk.Label(frame, text='1. Введите ваше имя', font=20)
NameTitle.pack()
Name = ttk.Entry(frame)
Name.pack()
Namebtn = ttk.Button(frame, text='Тык', command=name_btn_click)
Namebtn.pack()
NameText = ttk.Label(frame, font = 200)
NameText.pack()

NumberTitle = Label(frame, text='2. Введите 2 числа', font=100, pady=10)
NumberTitle.pack()
firstNumber = ttk.Entry(frame)
firstNumber.pack()
SecondNumber = ttk.Entry(frame)
SecondNumber.pack()
Numberbtn = ttk.Button(frame, text='Тук', command=number_btn_click)
Numberbtn.pack()
NumberSum = ttk.Label(frame, font = 200)
NumberSum.pack()

RandomTitle = Label(frame, text='3. Вывод 10 рандомных чисел и их сумма', font=100, pady=10)
RandomTitle.pack()
Randombtn = ttk.Button(frame, text='Шпык', command=random_btn_click)
Randombtn.pack()
RandomString = ttk.Label(frame, font = 200)
RandomString.pack()
RandomMin = ttk.Label(frame, font = 200)
RandomMin.pack()
RandomMax = ttk.Label(frame, font = 200)
RandomMax.pack()
RandomSum = ttk.Label(frame, font = 200)
RandomSum.pack()

FileTitle = Label(frame, text='4. Выберите один из файлов, выведите его содержимое и среднее значение чисел', font=100, pady=10)
FileTitle.pack()
FileBtn = ttk.Button(frame, text='Шпык', command=file_btn_click)
FileBtn.pack()
FileText = ttk.Label(frame, font = 200)
FileText.pack()
FileAverage = ttk.Label(frame, font = 200)
FileAverage.pack()

MBTitle = Label(frame, text='5. Пусть кошка погавкает или собака помяукает', font=100, pady=10)
MBTitle.pack()
MeowBtn = ttk.Button(frame, text='Тут котяра гавкнет', command=bark_btn_click)
MeowBtn.pack()
BarkBtn = ttk.Button(frame, text='А тут собака мяукнет', command=meow_btn_click)
BarkBtn.pack()

window.mainloop()

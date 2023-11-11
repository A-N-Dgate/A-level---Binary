from tkinter import *
"""
NOTE: only works with python version 3.4
"""
class menu_window():
    def __init__(self):
        self.window = Tk()
        self.window.title("converter")
    
        self.option1_lbl = Label(self.window, text="1.denary to binary")
        self.option1_lbl.grid(row=0, column=1)
    
        self.option2_lbl = Label(self.window, text="2.binary to denary")
        self.option2_lbl.grid(row=1, column=1)
    
        self.option3_lbl = Label(self.window, text="3.denary to hexedecimal")
        self.option3_lbl.grid(row=2, column=1)
    
        self.option4_lbl = Label(self.window, text="4.hexedecimal to denary")
        self.option4_lbl.grid(row=3, column=1)

        self.option5_lbl = Label(self.window, text="9.quit")
        self.option5_lbl.grid(row=4, column=1)
    
        self.answer_lbl = Label(self.window, text="Enter the number of the option")
        self.answer_lbl.grid(row=5, column=1)
    
        self.answer_entry = Entry(self.window, width=10)
        self.answer_entry.grid(row=6, column=1)
        
        self.ok_button = Button(self.window, text="Enter", command = self.outcome)
        self.ok_button.grid(row=7, column=1, sticky=W)



    def outcome(self):
        answer = self.answer_entry.get()
        if answer == "1":
            self.window.destroy()
            root = choice1_window()
        elif answer == "2":
            self.window.destroy()
            root = choice2_window()
        elif answer == "3":
            self.window.destroy()
            root = choice3_window()
        elif answer == "4":
            self.window.destroy()
            root = choice4_window()
        elif answer == "9":
            messagebox.showinfo("Quit", "You have quit the program")
            self.window.destroy()
        else:
            messagebox.showinfo("Error", "invalid input")
            

class choice1_window():
    def __init__(self):
        self.window = Tk()
        self.window.title("Denary to Binary")

        self.answer_lbl = Label(self.window, text="Enter a number")
        self.answer_lbl.grid(row=0,column=2)

        self.answer_entry = Entry(self.window, width = 10)
        self.answer_entry.grid(row=1, column=2)
        
        self.ok_button = Button(self.window, text="Enter", command = self.display_answer)    
        self.ok_button.grid(row=2,column=2)

    def display_answer(self):
        number = self.answer_entry.get()
        answer = denary_to_binary(number)
        messagebox.showinfo("Binary", answer)
        self.window.destroy()
        root = menu_window()

class choice2_window():
    def __init__(self):
        self.window = Tk()
        self.window.title("Binary to Denary")

        self.answer_lbl = Label(self.window, text="Enter a number")
        self.answer_lbl.grid(row=0,column=2)

        self.answer_entry = Entry(self.window, width = 10)
        self.answer_entry.grid(row=1, column=2)
        
        self.ok_button = Button(self.window, text="Enter", command = self.display_answer)    
        self.ok_button.grid(row=2,column=2)

    def display_answer(self):
        number = self.answer_entry.get()
        answer = binary_to_denary(number)
        messagebox.showinfo("Denary", answer)
        self.window.destroy()
        root = menu_window()

class choice3_window():
    def __init__(self):
        self.window = Tk()
        self.window.title("Denary to Hexedecimal")

        self.answer_lbl = Label(self.window, text="Enter a number")
        self.answer_lbl.grid(row=0,column=2)

        self.answer_entry = Entry(self.window, width = 10)
        self.answer_entry.grid(row=1, column=2)
        
        self.ok_button = Button(self.window, text="Enter", command = self.display_answer)    
        self.ok_button.grid(row=2,column=2)

    def display_answer(self):
        number = self.answer_entry.get()
        answer = denary_to_hex(number)
        messagebox.showinfo("Hexedecimal", answer)
        self.window.destroy()
        root = menu_window()

class choice4_window():
    def __init__(self):
        self.window = Tk()
        self.window.title("Hexedecimal to Denary")

        self.answer_lbl = Label(self.window, text="Enter a number")
        self.answer_lbl.grid(row=0,column=2)

        self.answer_entry = Entry(self.window, width = 10)
        self.answer_entry.grid(row=1, column=2)
        
        self.ok_button = Button(self.window, text="Enter", command = self.display_answer)    
        self.ok_button.grid(row=2,column=2)

    def display_answer(self):
        number = self.answer_entry.get()
        answer = hex_to_denary(number)
        messagebox.showinfo("Denary", answer)
        self.window.destroy()
        root = menu_window()

        
def denary_to_binary(number):
    number = int(number)
    binary_number = ""
    while number != 0:
        remainder = number % 2
        number = number // 2
        binary_number = str(remainder) + binary_number
    return binary_number

def binary_to_denary(number):
    number = str(number)
    denary_number = 0
    count = 1
    for x in reversed(number):
        x = int(x)
        denary_number += x * count
        count = count * 2
    return denary_number

def denary_to_hex(number):
    number = int(number)
    hexedecimal_number = ""
    while number != 0:
        remainder = number % 16
        if remainder >= 10:
            remainder = number_to_letter(remainder)
        number = number // 16
        hexedecimal_number = str(remainder) + hexedecimal_number
    return hexedecimal_number

def number_to_letter(number):
    if number == 10:
        x = "A"
    elif number == 11:
        x = "B"
    elif number == 12:
        x = "C"
    elif number == 13:
        x = "D"
    elif number == 14:
        x = "E"
    elif number == 15:
        x = "F"
    else:
        x = ""
    return x

def hex_to_denary(number):
    number = str(number)
    denary_number = 0
    count = 1
    for x in reversed(number):
        if not x.isdigit():
            x = letter_to_number(x)
        else:
            x = int(number)
        denary_number += x * count
        count = count * 16
    return denary_number

def letter_to_number(letter):
    letter = letter.upper()
    if letter == "A":
        x = 10
    elif letter == "B":
        x = 11
    elif letter == "C":
        x = 12
    elif letter == "D":
        x = 13
    elif letter == "E":
        x = 14
    elif letter == "F":
        x = 15
    else:
        x = 0
    return x

if __name__ == "__main__":
    root = menu_window()


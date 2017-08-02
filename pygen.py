from tkinter import *
from random import randint

def generate(num):
    # Number of passwords to generate
    num = int(num)

    # Number of lines in the word file
    lc = 2926
    
    for i in range(num):
        file = open("words.txt", "r")
        
        r1 = randint(1, lc) # Line number of first word
        r2 = randint(1, lc) # Line number of second word
        r3 = randint(1, lc) # Line number of third word

        w1 = ""             # Word located at line number r1
        w2 = ""             # Word located at line number r2
        w3 = ""             # Word located at line number r3

        r4 = str(randint(0,999)).zfill(3)   # Random 3-digit number for the
                                            # end of the password.
        
        i = 1

        # Go through the word file finding the cooresponding line numbers.
        # line.strip() removes any tags (like '\n')
        for line in file:
            if i == r1:
                w1 = line.strip()
            if i == r2:
                w2 = line.strip()
            if i == r3:
                w3 = line.strip()
            i += 1

        password = w1+w2+w3+r4
        
        print(password)

        file.close()

def main():
    root = Tk()

    frame = Frame(root)

    # Number of Passwords to generate
    passwordReturn = Spinbox(frame, from_=1, to=99)
    
    genButton = Button(frame,
                       text="Generate",
                       width=20,
                       command= lambda: generate(passwordReturn.get()))

    # Binds the enter key to the generate function
    root.bind("<Return>", lambda x: generate(passwordReturn.get()))
    
    genButton.grid(row=3, column=0, columnspan=2)

    prLabel = Label(frame, text="# of passwords \nto generate: ")
    prLabel.grid(row=1, column=0)

    passwordReturn.grid(row=1, column=1)

    frame.pack()

    
if __name__ == "__main__":
    main()

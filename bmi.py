

import tkinter as tk
from tkinter import messagebox

class BmiCalculator:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("400x530")
        self.root.title("BMI Calculator v.1")
        self.root.config(bg="#b5b5b1")
        self.weight_var = tk.StringVar()
        self.height_var = tk.StringVar()
        self.label1 = tk.Label(self.root,text="Enter your height in cm",font=("Arial",16),bg="#b5b5b1")
        self.label1.pack(pady=27)
        self.heightEntry = tk.Entry(self.root,textvariable=self.height_var,width=15,font=("Arial",16),bd=3)
        self.heightEntry.pack(pady=10)
        self.label2 = tk.Label(self.root, text="Enter your weight in kg", font=("Arial", 16),bg="#b5b5b1")
        self.label2.pack(pady=10)
        self.weightEntry = tk.Entry(self.root,textvariable=self.weight_var,width=15, font=("Arial", 16),bd=3)
        self.weightEntry.pack(pady=20)
        self.button = tk.Button(self.root,text="Calculate BMI", cursor="hand2", font=("Times New Roman",16),bg="black",fg="white",command=self.findBMI)
        self.button.pack(padx=30,pady=20)
        self.bmiLabel = tk.Label(self.root,font=("Tahoma",15),bg="#b5b5b1")
        self.bmiLabel.pack(pady=7)
        self.result = tk.Label(self.root,font=("Tahoma",17),text="",height=2,width=36,bg="#b5b5b1")
        self.result.pack(padx=30,pady=5)
        self.root.mainloop()


    def isValidDecimal(self,strNum):
        if strNum.count(".") <= 1 and strNum.replace(".", "").isnumeric():
            return True
        return False
        

    def findBMI(self):
        weight = self.weight_var.get()
        height = self.height_var.get()

        if weight=="" or weight.isspace() or height=="" or height.isspace():
            self.bmiLabel.config(text="")
            self.result.config(text="Height and Weight cannot be empty",bg="brown",fg="white",font=("Tahoma",15))

        elif self.isValidDecimal(weight)==True and self.isValidDecimal(height)==True:

            heightMetre = float(height)/100
            if float(height)>=100 and (weight!=0.0 or weight!=0):

                bmi = float("{:.2f}".format(float(weight)/heightMetre/heightMetre))

                self.bmiLabel.config(text=f"BMI is {bmi}")

                if bmi<15:
                    self.result.config(text="Very severely underweight",bg="purple",fg="white",font=("Georgia"))
                elif bmi>=15 and bmi<16:
                    self.result.config(text="Severely underweight", bg="blue", fg="white",font=("Georgia"))
                elif bmi>=16 and bmi<18.5:
                    self.result.config(text="Underweight", bg="#3377ff", fg="black",font=("Georgia",18))
                elif bmi>=18.5 and bmi<=24.9:
                    self.result.config(text="Healthy", bg="green", fg="white",font=("Georgia",20))
                elif bmi>=25 and bmi<=29.9:
                    self.result.config(text="Overweight", bg="yellow", fg="black",font=("Georgia",20))
                elif bmi>=30 and bmi<40:
                    self.result.config(text="Obese", bg="orange", fg="black",font=("Georgia",20))
                elif bmi>=40:
                    self.result.config(text="Extremely Obese", bg="red", fg="white",font=("Cambria",23))
            elif heightMetre==0 or weight==0:
                self.bmiLabel.config(text="")
                self.result.config(text="Height and Weight cannot be 0", bg="red", font=("Arial", 15))
            else:

                self.bmiLabel.config(text="")
                self.result.config(text="", bg="#ccffff")
                messagebox.showinfo(title="Message",message="Invalid height and weight")
        else:

            self.bmiLabel.config(text="")
            self.result.config(text="Enter numbers only please",bg="red",font=("Arial",18))

BmiCalculator()

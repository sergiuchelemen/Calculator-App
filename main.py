from tkinter import *
import tkinter as tk
import math

root = Tk()
root.geometry('1000x800')
root.title('Calculator')
root.configure(background='gray25')
equation = ''


def logic(symbol):
    current = e.get()
    e.delete(0, END)
    if current == '+' or current == '-' or current == '*' or current == '/' or current == '(' or \
            current == ')' or current == 'Error: Logarithm from a negative number' \
            or current == 'Error: Square root from a negative number' or current == 'Invalid expression':
        e.insert(0, str(symbol))
    else:
        e.insert(0, str(current) + str(symbol))
    global equation
    equation = equation + str(symbol)


def sum():
    e.delete(0, END)
    e.insert(0, '+')
    global equation
    equation = equation + '+'


def subtraction():
    e.delete(0, END)
    e.insert(0, '-')
    global equation
    equation = equation + '-'


def product():
    e.delete(0, END)
    e.insert(0, '*')
    global equation
    equation = equation + '*'


def divide():
    e.delete(0, END)
    e.insert(0, '/')
    global equation
    equation = equation + '/'


def egal():
    global equation
    try:
        e.insert(0, eval(equation))
    except:
        e.delete(0, END)
        e.insert(0, 'Invalid expression')
        equation = ''
    else:
        e.delete(0, END)
        e.insert(0, eval(equation))
        equation = str(eval(equation))


def sinus():
    current = str(e.get())
    a = current.find('.')
    if a == -1:
        current = int(current)
    else:
        current = float(current)
    e.delete(0, END)
    e.insert(0, eval('math.sin(current)'))
    global equation
    equation = e.get()


def cosin():
    current = str(e.get())
    a = current.find('.')
    if a == -1:
        current = int(current)
    else:
        current = float(current)
    e.delete(0, END)
    e.insert(0, eval('math.cos(current)'))
    global equation
    equation = e.get()


def sqrt():
    global equation
    current = str(e.get())
    e.delete(0, END)
    if current[0] == '-':
        e.insert(0, 'Error: Square root from a negative number')
        equation = ''
    else:
        a = current.find('.')
        if a == -1:
            current = int(current)
        else:
            current = float(current)
        e.insert(0, eval('math.sqrt(current)'))
        equation = e.get()


def logarithm():
    global equation
    current = str(e.get())
    e.delete(0, END)
    if current[0] == '-':
        e.insert(0, 'Error: Logarithm from a negative number')
        equation = ''
    else:
        a = current.find('.')
        if a == -1:
            current = int(current)
        else:
            current = float(current)
        e.insert(0, eval('math.log10(current)'))
        equation = e.get()


def delete():
    e.delete(0, END)
    global equation
    equation = ''


def animation(e):
    btn["bg"] = "grey1"


def exit(e):
    btn["bg"] = "grey15"


# frame
frame = LabelFrame(root, padx=6, pady=10, height=100, width=100, background='grey80')

# entry
e = tk.Entry(frame, borderwidth=5, width=60)
e.grid(row=0, column=0, columnspan=4, ipady=30, ipadx=8)

# little space between entry and buttons
btn = tk.Label(frame, text=' ', background='grey80')
btn.grid(row=2, column=0)

# number
btn = tk.Button(frame, width=12, height=5, text='7', command=lambda: logic(7), background='grey15', borderwidth=5,
                fg='white')
btn.grid(row=3, column=0)


btn = tk.Button(frame, width=12, height=5, text='8', command=lambda: logic(8), background='grey15', borderwidth=5,
                fg='white')
btn.grid(row=3, column=1)


btn = tk.Button(frame, width=12, height=5, text='9', command=lambda: logic(9), background='grey15', borderwidth=5,
                fg='white')
btn.grid(row=3, column=2)

btn = tk.Button(frame, width=12, height=5, text='-', command=subtraction, background='grey51', borderwidth=5,
                fg='white')
btn.grid(row=3, column=3)

btn = tk.Label(frame, text=' ')
btn.grid(row=4, column=0)

btn = tk.Button(frame, width=12, height=5, text='4', command=lambda: logic(4), background='grey15', borderwidth=5,
                fg='white')
btn.grid(row=4, column=0)

btn = tk.Button(frame, width=12, height=5, text='5', command=lambda: logic(5), background='grey15', borderwidth=5,
                fg='white')
btn.grid(row=4, column=1)

btn = tk.Button(frame, width=12, height=5, text='6', command=lambda: logic(6), background='grey15', borderwidth=5,
                fg='white')
btn.grid(row=4, column=2)

btn = tk.Button(frame, width=12, height=5, text='+', command=sum, background='grey51', borderwidth=5,
                fg='white')
btn.grid(row=4, column=3)

btn = tk.Label(frame, text=' ')
btn.grid(row=5, column=0)

btn = tk.Button(frame, width=12, height=5, text='1', command=lambda: logic(1), background='grey15', borderwidth=5,
                fg='white')
btn.grid(row=5, column=0)

btn = tk.Button(frame, width=12, height=5, text='2', command=lambda: logic(2), background='grey15', borderwidth=5,
                fg='white')
btn.grid(row=5, column=1)

btn = tk.Button(frame, width=12, height=5, text='3', command=lambda: logic(3), background='grey15', borderwidth=5,
                fg='white')
btn.grid(row=5, column=2)

btn = tk.Button(frame, width=12, height=5, text='*', command=product, background='grey51', borderwidth=5,
                fg='white')
btn.grid(row=5, column=3)

btn = tk.Button(frame, width=12, height=5, text='(', command=lambda: logic('('), background='grey51', borderwidth=5,
                fg='white')
btn.grid(row=6, column=0)

btn = tk.Button(frame, width=12, height=5, text='/', command=divide, background='grey51', borderwidth=5,
                fg='white')
btn.grid(row=6, column=3)

btn = tk.Button(frame, width=12, height=5, text='0', command=lambda: logic('0'), background='grey15', borderwidth=5,
                fg='white')
btn.grid(row=6, column=1)

btn = tk.Button(frame, width=12, height=5, text=')', command=lambda: logic(')'), background='grey51', borderwidth=5,
                fg='white')
btn.grid(row=6, column=2)

btn = tk.Button(frame, width=12, height=5, text='sin', command=sinus, background='grey51', borderwidth=5,
                fg='white')
btn.grid(row=7, column=0)

btn = tk.Button(frame, width=12, height=5, text='cos', command=cosin, background='grey51', borderwidth=5,
                fg='white')
btn.grid(row=7, column=1)

btn = tk.Button(frame, width=12, height=5, text='sqrt', command=sqrt, background='grey51', borderwidth=5,
                fg='white')
btn.grid(row=7, column=2)

btn = tk.Button(frame, width=12, height=5, text='log', command=logarithm, background='grey51', borderwidth=5,
                fg='white')
btn.grid(row=7, column=3)

btn = tk.Button(frame, width=26, height=5, text='clear', command=delete, background='DarkOrange2', borderwidth=5,
                fg='white')
btn.grid(row=8, column=0, columnspan=2)

btn = tk.Button(frame, width=26, height=5, text='=', command=egal, background='DarkOrange2', borderwidth=5,
                fg='white')
btn.grid(row=8, column=2, columnspan=2)


# main
frame.pack(pady=50)
root.mainloop()

import tkinter as tk
'''Imports Tkinter module tk is an alias for easy access'''

#Button click handler
def press(v):
    entry.insert(tk.END, v)
'''Function to handle button press events, inserts the value v into the entry widget'''

def clear():
    entry.delete(0, tk.END)
'''Function to clear the entry widget
Deletes all characters from index 0 to the end'''

def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current)-1,tk.END)
    '''Deletes last character if entry is not empty'''

def calc():
    try:
        result = eval(entry.get())
        '''entry.get() retrieves the expression(e.g. "2+3*4") from the entry widget
        eval() evaluates the expression and returns the result'''

        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Expression")
        '''Handles invalid expressions (eg.5++) Display appropriate message instead of crashing'''   

#Main window creation
root = tk.Tk() #Creates the main application window 
root.title("Calculator") #Sets the window title
root.configure(bg="#1e1e1e") #Sets the background color 
root.resizable(False, False) #Diables resizing of window

#Entry Widget (Display Screen)
entry = tk.Entry(
    root,
    font=("Times new roman", 20),
    bg="#2d2d2d", 
    fg="white",
    bd=0, 
    justify="right"
    )
'''Text input field
Acts as calculator display
Right-aligned for better calculator look'''

entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)
'''Places entry at top
columnspan=4 makes it stretch across 4 columns'''

#Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

'''Represent calculator buttons 
Stored in list to reduce repetitive code'''

#Dynamic button creation
r=1
c=0
"Rows and columns for grid layout"

for b in buttons:
    cmd = calc if b =='=' else lambda x=b: press(x)
    '''If button is '=' call calc()
    Otherwise call press() with button value lambda x=b prevents late binding issue'''

    tk.Button(
        root,
        text=b,
        command=cmd, #These three lines creates a button widget
        font=("Calibri", 14),
        width=5,
        height=2,
        bg='#ff9500' if b in "+-/*" else "#3a3a3a",
        fg="white",
        bd=0
    ).grid(row=r, column=c, padx=6, pady=6)
    c += 1
    if c==4:
        r+=1
        c=0

    '''Moves to next row after 4 buttons'''

#Clear Button
tk.Button(
    root,
    text='C',
    command=clear,
    font=("Calibri", 14),
    width=22,
    height=2,
    bg='#ff3b3b',
    fg="white",
    bd=0
).grid(row=r, column=0, columnspan=3, padx=6, pady=6)
'''Creates a clear button that spans all 4 columns'''  

tk.Button(
    root,
    text='<--',
    command=backspace,
    font=("Calibri", 14),
    width=10,
    height=2,
    bg="#ff3b3b",
    fg="white",
    bd=0
).grid(row=r, column=3, columnspan=3, padx=6, pady=6)
'''Creates a clear button that spans all 4 columns'''  




root.mainloop()
#Keeps the loop running
    

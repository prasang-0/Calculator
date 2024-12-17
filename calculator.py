import os
import tkinter as tk

def main():
    def adjust_font_size(event):
        window_width = event.width
        
        entry_font_size = max(30, window_width // 15)
        
        entry.config(font=("Digital-7", entry_font_size))
        
    def handle_keypress(event):
        key = event.char
        ctrl_pressed = (event.state & 0x0004) != 0
        
        if key.isdigit() or key in ['+', '-', '*', '/', '.', '%']:
            press(key)
        elif key == '\r':
            calculate()
        elif key == '\x08':
            clear_one()
        elif ctrl_pressed and event.keysym == 'BackSpace':
            clear_all()
        
    def press(key):
        current = entry.get()
        operators = ['+', '-', '*', '/']
        
        if current == "Error" or current == "8008135 ARE LOVE 😼":
            entry.delete(0, tk.END)
        
        if key in operators:
            if current and current[-1] in operators:
                return
        
        entry.insert(tk.END, key)
    
    def clear_all():
        entry.delete(0, tk.END)
    
    def clear_one():
        current = entry.get()
        if current:
            entry.delete(0, tk.END)
            entry.insert(0, current[:-1])
    
    def square():
        try:
            result = float(entry.get()) ** 2
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    
    def cube():
        try:
            result = float(entry.get()) ** 3
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    
    def reciprocal():
        try:
            result = 1 / float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            
    def sq_root():
        try:
            result = float(entry.get()) ** (1 / 2)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    
    def something_nice():
        entry.delete(0, tk.END)
        entry.insert(tk.END, "8008135 ARE LOVE 😼")
    
    def percentage():
        try:
            result = float(entry.get()) / 100
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    
    def calculate():
        expression = entry.get()
        expression = expression.replace(' ', '')
        try:
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    
    root = tk.Tk()
    root.geometry("400x500")
    root.minsize(400, 500)
    root.title("Calculator")
    root.config(bg="#262624")
    
    #icon = tk.PhotoImage(file="calc_png.png")
    icon_path = os.path.join(os.path.dirname(__file__), 'calc_png.png')
    icon = tk.PhotoImage(file=icon_path)
    
    root.iconphoto(True, icon)
    
    entry = tk.Entry(root, width=29, borderwidth=10, font=("Digital-7", 30), justify="right", fg="#d1d1cf",
                     bg="#454543")
    entry.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky='news')
    
    root.bind("<Configure>", adjust_font_size)
    root.bind("<KeyPress>", handle_keypress)
    
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
    
    for j in range(4):
        root.grid_columnconfigure(j, weight=1)
    
    buttons = [('AC', 1, 0), ('⌫', 1, 1), ('%', 1, 2), ('/', 1, 3),
               ('x²', 2, 0), ('x³', 2, 1), ('1/x', 2, 2), ('√x', 2, 3),
               ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
               ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
               ('3', 5, 0), ('2', 5, 1), ('1', 5, 2), ('+', 5, 3),
               ('😼', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3), ]
    
    for (text, row, column) in buttons:
        if text == '=':
            tk.Button(root, text=text, font=("Open Sans", 15), fg="#fcfcf7", bg="#121211", width=5, height=2,
                      command=calculate).grid(row=row, column=column,
                                              padx=1, pady=1, sticky='ew')
        elif text == 'AC':
            tk.Button(root, text=text, font=("Open Sans", 15), fg="#fcfcf7", bg="#121211", width=5, height=2,
                      command=clear_all).grid(row=row, column=column,
                                              padx=1, pady=1, sticky='ew')
        elif text == '⌫':
            tk.Button(root, text=text, font=("Open Sans", 15), fg="#fcfcf7", bg="#121211", width=5, height=2,
                      command=clear_one).grid(row=row, column=column,
                                              padx=1, pady=1, sticky='ew')
        elif text == '%':
            tk.Button(root, text=text, font=("Open Sans", 15), fg="#fcfcf7", bg="#121211", width=5, height=2,
                      command=percentage).grid(row=row, column=column,
                                               padx=1, pady=1, sticky='ew')
        elif text == 'x²':
            tk.Button(root, text=text, font=("Open Sans", 15), fg="#fcfcf7", bg="#121211", width=5, height=2,
                      command=square).grid(row=row, column=column,
                                               padx=1, pady=1, sticky='ew')
        elif text == 'x³':
            tk.Button(root, text=text, font=("Open Sans", 15), fg="#fcfcf7", bg="#121211", width=5, height=2,
                      command=cube).grid(row=row, column=column,
                                               padx=1, pady=1, sticky='ew')
        elif text == '1/x':
            tk.Button(root, text=text, font=("Open Sans", 15), fg="#fcfcf7", bg="#121211", width=5, height=2,
                      command=reciprocal).grid(row=row, column=column,
                                               padx=1, pady=1, sticky='ew')
        elif text == '😼':
            tk.Button(root, text=text, font=("Open Sans", 15), fg="#fcfcf7", bg="#121211", width=5, height=2,
                      command=something_nice).grid(row=row, column=column,
                                               padx=1, pady=1, sticky='ew')
        elif text == '√x':
            tk.Button(root, text=text, font=("Open Sans", 15), fg="#fcfcf7", bg="#121211", width=5, height=2,
                      command=sq_root).grid(row=row, column=column,
                                               padx=1, pady=1, sticky='ew')
        
        else:
            action = lambda t=text: press(t)
            tk.Button(root, text=text, font=("Open Sans", 15), fg="#fcfcf7", bg="#121211", width=5, height=2,
                      command=action).grid(row=row, column=column,
                                           padx=1, pady=1, sticky='ew')
    
    root.mainloop()


if __name__ == "__main__":
    main()
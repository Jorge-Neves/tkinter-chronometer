import tkinter as tk

counter = 0


def counter_label(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()


root = tk.Tk()
root.title("Chronometer")
label = tk.Label(root, fg="black")
label.pack()
counter_label(label)
button = tk.Button(root, text="stop", width=50, command=root.destroy)
button.pack()
root.mainloop()

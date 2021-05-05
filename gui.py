from tkinter import *
from tkinter import filedialog
import tkinter.font as font
from tester_gui import SelectDatabase, AutoAddNewWords, AddNewWords, StartTest, CreateDatabase

root = Tk()
root.resizable(False, False)
root.geometry("500x500")
root.configure(background='#333333')
root.title("Deutsch Vocabulary Test")

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def BackToMenu():
    global btn1, btn2, btn3, btn4, btn5, btn6, text1, text2, text, entry

    widget_list = all_children(root)
    for item in widget_list:
        item.destroy()


    text = Label(root, text="Menu", bg="#333333", fg="white")
    text.config(font=("Roboto", 30))
    text.pack(anchor="center", pady=25)

    btn1 = Button(root, text="Select Vocabulary", fg="white", bg="#555555", padx=10, pady=5, command=lambda:MenuToSelect())
    btn1.pack(anchor='c', pady=1)
    btn2 = Button(root, text="Add A Word", fg="white", bg="#555555", padx=5, pady=5, command=lambda:MenuToAddword())
    btn2.pack(anchor='c', pady=1)
    btn3 = Button(root, text="Add A File", fg="white", bg="#555555", padx=10, pady=5, command=lambda:MenuToAddfile())
    btn3.pack(anchor='c', pady=1)
    btn9 = Button(root, text="Create Vocabulary", fg="white", bg="#555555", padx=10, pady=5, command=lambda:MenuToCreate())
    btn9.pack(anchor='c', pady=1)
    btn4 = Button(root, text="Start Test", fg="white", bg="#3bb85c", padx=10, pady=5)
    btn4.pack(anchor='c', pady=25)

    btn1['font'] = font.Font(size=20)
    btn2['font'] = font.Font(size=20)
    btn3['font'] = font.Font(size=20)
    btn9['font'] = font.Font(size=20)
    btn4['font'] = font.Font(size=40)

def SelectVCB(vcb):
    SelectDatabase(str(vcb))
    BackToMenu()

def AddWord(word, meaning, wrdType, article):
    AddNewWords(word, meaning, wrdType, article)
    BackToMenu()

def AddFile(file):
    AutoAddNewWords(file)
    BackToMenu()

def CreateVCB(vcb):
    CreateDatabase(str(vcb))
    BackToMenu()

def MenuToAddword():
    global btn1, btn2, btn3, btn4, btn7, btn8, text, text3, text4, text5, text6, text7, entry1, entry2, entry3

    widget_list = all_children(root)
    for item in widget_list:
        item.destroy()


    text3 = Label(root, text="Add Word", bg="#333333", fg="white")
    text3.config(font=("Roboto", 30))
    text3.grid(row=0, column=0, padx=150, pady=15, columnspan=3)

    text4 = Label(root, text="Word", bg="#333333", fg="white")
    text4.config(font=("Roboto", 15))
    text4.grid(row=1, column=0, padx=10, pady=15)

    entry1 = Entry(root)
    entry1.grid(row=1, column=1, padx=0, pady=15, ipadx=50, ipady=8)

    text7 = Label(root, text="Type\n(n, v, a)", bg="#333333", fg="white")
    text7.config(font=("Roboto", 15))
    text7.grid(row=2, column=0, padx=10, pady=15)

    entry4 = Entry(root)
    entry4.grid(row=2, column=1, padx=0, pady=15, ipadx=50, ipady=8)

    text6 = Label(root, text="Article\n(Leave empty if none)", bg="#333333", fg="white")
    text6.config(font=("Roboto", 15))
    text6.grid(row=3, column=0, padx=10, pady=15)

    entry2 = Entry(root)
    entry2.grid(row=3, column=1, padx=0, pady=15, ipadx=50, ipady=8)

    text5 = Label(root, text="Meaning", bg="#333333", fg="white")
    text5.config(font=("Roboto", 15))
    text5.grid(row=4, column=0, padx=10, pady=15)

    entry3 = Entry(root)
    entry3.grid(row=4, column=1, padx=0, pady=15, ipadx=50, ipady=8)

    btn7 = Button(root, text="Back", bg="#555555", fg="white", padx=5, pady=5, command=lambda:BackToMenu())
    btn7['font'] = font.Font(size=20)
    btn7.grid(row=5, column=0, pady=40)

    btn8 = Button(root, text="Add", bg="#3bb85c", fg="white", padx=10, pady=5, command=lambda:AddWord(entry1.get(), entry3.get(), entry4.get(), entry2.get()))
    btn8['font'] = font.Font(size=20)
    btn8.grid(row=5, column=1, pady=40)

def AskFileName():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select Vocabulary", filetypes=[("Vocabulary Files", "*.vcb")])
    file = root.filename
    AddFile()

def MenuToAddfile():
    global btn1, btn2, btn3, btn4, btn5, btn6, text1, text2, text, entry

    widget_list = all_children(root)
    for item in widget_list:
        item.destroy()


    text1 = Label(root, text="Add File", bg="#333333", fg="white")
    text1.config(font=("Roboto", 30))
    text1.grid(row=0, column=0, padx=170, pady=25, columnspan=4)

    btn1 = Button(root, text="Select File", bg="#555555", fg="white", padx=5, pady=5, command=AskFileName)
    btn1['font'] = font.Font(size=20)
    btn1.grid(row=1, column=2, padx=0, pady=30, ipadx=10, ipady=8)

    btn5 = Button(root, text="Back", bg="#555555", fg="white", padx=5, pady=5, command=lambda:BackToMenu())
    btn5['font'] = font.Font(size=20)
    btn5.grid(row=2, column=1, pady=50)

    btn6 = Button(root, text="Add", bg="#3bb85c", fg="white", padx=5, pady=5, command=lambda:CreateVCB(entry.get()))
    btn6['font'] = font.Font(size=20)
    btn6.grid(row=2, column=3, pady=50)

def MenuToSelect():
    global btn1, btn2, btn3, btn4, btn5, btn6, text1, text2, text, entry

    widget_list = all_children(root)
    for item in widget_list:
        item.destroy()


    text1 = Label(root, text="Select Vocabulary", bg="#333333", fg="white")
    text1.config(font=("Roboto", 30))
    text1.grid(row=0, column=0, padx=100, pady=25, columnspan=3)

    text2 = Label(root, text="Vocabulary Name", bg="#333333", fg="white")
    text2.config(font=("Roboto", 15))
    text2.grid(row=1, column=0, padx=10, pady=30)

    entry = Entry(root)
    entry.grid(row=1, column=1, padx=0, pady=30, ipadx=50, ipady=8)

    btn5 = Button(root, text="Back", bg="#555555", fg="white", padx=5, pady=5, command=lambda:BackToMenu())
    btn5['font'] = font.Font(size=20)
    btn5.grid(row=2, column=0, pady=50)

    btn6 = Button(root, text="Select", bg="#3bb85c", fg="white", padx=5, pady=5, command=lambda:SelectVCB(entry.get()))
    btn6['font'] = font.Font(size=20)
    btn6.grid(row=2, column=1, pady=50)

def MenuToCreate():
    global btn1, btn2, btn3, btn4, btn5, btn6, text1, text2, text, entry

    widget_list = all_children(root)
    for item in widget_list:
        item.destroy()


    text1 = Label(root, text="Create Vocabulary", bg="#333333", fg="white")
    text1.config(font=("Roboto", 30))
    text1.grid(row=0, column=0, padx=100, pady=25, columnspan=3)

    text2 = Label(root, text="Vocabulary Name", bg="#333333", fg="white")
    text2.config(font=("Roboto", 15))
    text2.grid(row=1, column=0, padx=10, pady=30)

    entry = Entry(root)
    entry.grid(row=1, column=1, padx=0, pady=30, ipadx=50, ipady=8)

    btn5 = Button(root, text="Back", bg="#555555", fg="white", padx=5, pady=5, command=lambda:BackToMenu())
    btn5['font'] = font.Font(size=20)
    btn5.grid(row=2, column=0, pady=50)

    btn6 = Button(root, text="Create", bg="#3bb85c", fg="white", padx=5, pady=5, command=lambda:CreateVCB(entry.get()))
    btn6['font'] = font.Font(size=20)
    btn6.grid(row=2, column=1, pady=50)


text = Label(root, text="Menu", bg="#333333", fg="white")
text.config(font=("Roboto", 30))
text.pack(anchor="center", pady=25)

btn1 = Button(root, text="Select Vocabulary", fg="white", bg="#555555", padx=10, pady=5, command=lambda:MenuToSelect())
btn1.pack(anchor='c', pady=1)
btn2 = Button(root, text="Add A Word", fg="white", bg="#555555", padx=5, pady=5, command=lambda:MenuToAddword())
btn2.pack(anchor='c', pady=1)
btn3 = Button(root, text="Add A File", fg="white", bg="#555555", padx=10, pady=5, command=lambda:MenuToAddfile())
btn3.pack(anchor='c', pady=1)
btn4 = Button(root, text="Create Vocabulary", fg="white", bg="#555555", padx=10, pady=5, command=lambda:MenuToCreate())
btn4.pack(anchor='c', pady=1)
btn5 = Button(root, text="Start Test", fg="white", bg="#3bb85c", padx=10, pady=5)
btn5.pack(anchor='c', pady=25)

btn1['font'] = font.Font(size=20)
btn2['font'] = font.Font(size=20)
btn3['font'] = font.Font(size=20)
btn4['font'] = font.Font(size=20)
btn5['font'] = font.Font(size=40)


root.mainloop()
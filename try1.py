# Am besten importieren Sie nur das, was Sie brauchen. Die Warum-Anweisung spielt keine Rolle mehr, da Python3 jetzt der Standard ist.
# try:
#     import Tkinter as tk
# except:
#     import tkinter as tk

from tkinter import Tk, Label, Button, Entry

translate_dict={"sc":"fM","inc":"Zun","dec":"Abn"}

# Sie verwenden tkinter, also warum haben Sie die Ausgabe auf der Konsole gedruckt?

# def uebersetzung():
#     wort=str(e1.get())
#     if wort in liste:
#         print ("Ja, vorhanden, die Übersetzung ist")
#     else:
#         print ("Nein, noch nicht vorhanden")

# 

def popupmsg():
    # Sie müssen zuerst die Benutzereingaben erhalten. . .
    wort=str(Benutzereingabe.get())
    # Rufen Sie dann den Wert aus dem Schlüssel basierend auf dieser Benutzereingabe ab. . .
    wort_translation = translate_dict.get(wort)
    popup = Tk()
    popup.wm_title("!")
    # Dann können Sie den Wert wie folgt am Ende Ihrer Nachricht hinzufügen. . .
    Übersetzung__label = Label(popup, text="Übersetzung:"+wort_translation)
    Übersetzung__label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop

root = Tk()
root.geometry("300x300")
# make Esc exit the program

root.bind("<Escape>", lambda e: root.destroy())

# Sieht so aus, als hättest du das aus einem Beispiel. . . Pfade sind wichtig, 
# aber machen Sie sich vorerst keine Sorgen, Bilder hinzuzufügen. Sorgen Sie sich darum, die Grundlagen zu verstehen
# logo=PhotoImage(file="../../../../home/michi/python/kruemelmonster.png")
# w=Label(root,compound=CENTER,image=logo)
# w.pack()

# Versuchen Sie, Ihren Variablen und Funktionen keine Namen zu geben, die den Schlüsselwortnamen in Python nahe kommen. Wenn Sie beispielsweise einem tkinter-Label den Namen "label" geben, wird es verwirrend.
output_label=Label(text="Ausgabe")
output_label.pack()
Benutzereingabe=Entry(master=root)
Benutzereingabe.pack()
exit_taste=Button(master=root,text="Exit", command=exit)
exit_taste.pack()
Übersetzen_button1=Button(master=root,text="Übersetzen", command=popupmsg)
Übersetzen_button1.pack()
root.mainloop()

# Sie tun sich selbst keinen Gefallen, indem Sie "Nano" verwenden,
# "Visual Studio Code" herunterladen. Es wird Ihnen viel darüber
# informieren, was mit Ihrer Syntax nicht stimmt, sodass Sie sich
# mehr auf das Erlernen der Konzepte konzentrieren können.

# Ich habe ein bisschen Zeit damit verbracht, also hoffe ich, dass
# es hilft. Wenn ich schwer zu verstehen bin, gib bitte Google die
# Schuld lol.
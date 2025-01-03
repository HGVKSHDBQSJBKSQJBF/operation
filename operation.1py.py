from tkinter import *
from tkinter.messagebox import *
from tkinter.font import *
import random
from enum import Enum
import webbrowser


class op(Enum):
    addition = 1
    soustraction = 2
    multiplication = 3
    division = 4
    puissance2 = 5
    racinecarré = 6


def genererop(operation, alea=False):
    root = Toplevel()
    nombre_2 = 0
    if operation == op.puissance2:
        nombre_1 = random.randint(1, 11)
        chaine2 = f"{nombre_1}² = ?"
        root.title("puissance2")
    elif operation == op.racinecarré:
        nombre_1 = random.randint(1, 11)
        chaine2 = f"racine carré de {nombre_1 * nombre_1} = ?"
        root.title("racine carré")
    elif operation == op.addition:
        nombre_1 = random.randint(1, 100)
        nombre_2 = random.randint(1, 100)
        chaine2 = f"{nombre_1} + {nombre_2} = ?"
        root.title("addition")
    elif operation == op.soustraction:
        nombre_1 = random.randint(1, 100)
        nombre_2 = random.randint(1, 100)
        if nombre_1 < nombre_2:
            nombre_1, nombre_2 = nombre_2, nombre_1
        chaine2 = f"{nombre_1} - {nombre_2} = ?"
        root.title("soustraction")
    elif operation == op.division:
        nombre_2 = random.randint(2, 10)
        nombre_1 = random.randint(2, 10)
        nombre_2 = nombre_2 * nombre_1
        chaine2 = f"{nombre_2} / {nombre_1} = ?"
        root.title("division")
    elif operation == op.multiplication:
        nombre_2 = random.randint(1, 11)
        nombre_1 = random.randint(1, 11)
        chaine2 = f"{nombre_1} x {nombre_2} = ?"
        root.title("multiplication")
    else:
        print("operation invalide")
        return

    f = Font(size=20)
    root.geometry("450x200")
    label2 = Label(root, font=("Comic sans ms", 30), text=chaine2)
    label2.grid(row=0, column=2)

    finbutton = Button(
        root,
        text="fin",
        font=15,
        command=root.destroy,
    )
    finbutton.grid(row=4, column=2)
    entry = Entry(root)
    entry.grid(row=1, column=2)
    entry["font"] = f
    entry.bind(
        "<Return>",
        lambda event: get_text(root, entry, operation, nombre_1, nombre_2, alea),
    )
    button = Button(
        root,
        text="valider",
        command=lambda: get_text(root, entry, operation, nombre_1, nombre_2, alea),
    )
    button.grid(row=3, column=2)
    button["font"] = f
    root.focus()
    entry.focus()
    root.mainloop()


def get_text(root, entry, operation, nombre_1, nombre_2=0, alea=False):
    if operation == op.multiplication:
        solution = nombre_2 * nombre_1
        recommencer = multiplication
    elif operation == op.addition:
        solution = nombre_1 + nombre_2
        recommencer = addition
    elif operation == op.soustraction:
        solution = nombre_1 - nombre_2
        recommencer = soustraction
    elif operation == op.division:
        solution = nombre_2 // nombre_1
        recommencer = division
    elif operation == op.puissance2:
        solution = nombre_1 * nombre_1
        recommencer = puissance2
    elif operation == op.racinecarré:
        solution = nombre_1
        recommencer = racinecarré
    else:
        print("operation invalide")
        return
    if alea:
        recommencer = aleatoire

    text = entry.get()
    try:
        user_reponse = int(text)
    except ValueError:
        erreur = Toplevel()
        erreur.geometry("500x150")
        label = Label(erreur, text="ce n'est pas un nombre", font=("Comic sans ms", 30))
        label.place(x=0, y=0)
        sortie = Button(erreur, text="ok...", command=erreur.destroy, width=15)
        sortie["font"] = f
        sortie.place(x=150, y=90)
        return

    root.destroy()

    def done():
        top.destroy()
        base.focus()

    def again():
        top.destroy()
        recommencer()

    top = Toplevel()
    top.geometry("500x250")
    top.title("veridict")
    nouveau = Button(
        top,
        text="nouveau",
        command=again,
    )
    nouveau.grid(row=4, column=1)
    fin = Button(
        top,
        text="retour",
        command=done,
    )
    fin.grid(row=3, column=1)
    if user_reponse == solution:
        global score
        score += 1
        juste = Label(
            top,
            text="cette reponse est juste",
            font=("Helvetica 14 bold"),
        )
        juste.grid(row=1, column=1)
        chainescore = "score:", score
        scoreprint = Label(top, text=chainescore, font=("Comic Sans MS", 24))
        scoreprint.grid(row=2, column=1)
    else:
        score -= 1
        chainescore = "score:", score
        scoreprint = Label(top, text=chainescore, font=("Comic Sans MS", 24))
        scoreprint.grid(row=2, column=1)
        chainesolution = "cette reponse est fausse", "solution:", solution
        faux = Label(
            top,
            text=chainesolution,
            font=("Helvetica 14 bold"),
        )
        faux.grid(row=1, column=1)
    top.bind("<BackSpace>", lambda event: done())
    top.bind("<Return>", lambda event: again())
    top.focus()
    top.mainloop()


def puissance2():
    genererop(op.puissance2)


def racinecarré():
    genererop(op.racinecarré)


def aleatoire():
    genererop(op(random.randint(1, 6)), True)


def addition():
    genererop(op.addition)


def soustraction():
    genererop(op.soustraction)


def division():
    genererop(op.division)


def multiplication():
    genererop(op.multiplication)


compteur = 0
score = 0
base = Tk()
base.title("operation")

basefortext = Label(
    base,
    text="choisissez une opération:",
    font=("Comic sans ms", 30),
)
basefortext.grid(row=0, column=2)

base.geometry("1000x500")

f = Font(size=20)

# Créer les boutons
width = 12
bouton1 = Button(base, text="multiplication", command=multiplication, width=width)
bouton2 = Button(base, text="division", command=division, width=width)
bouton3 = Button(base, text="soustraction", command=soustraction, width=width)
bouton4 = Button(base, text="addition", command=addition, width=width)
bouton5 = Button(base, text="aléatoire", command=aleatoire, width=width)
bouton6 = Button(base, text="racine carré", command=racinecarré, width=width)
bouton7 = Button(base, text="puissance2", command=puissance2, width=width)
bouton8 = Button(
    base,
    text="a venir",
    width=width,
)
bouton9 = Button(
    base,
    text="a venir",
    width=width,
)
bouton0 = Button(
    base,
    text="a venir",
    width=width,
)
bouton10 = Button(
    base,
    text="a venir",
    width=width,
)
bouton11 = Button(
    base,
    text="a venir",
    width=width,
)

# Ajouter les boutons à la fenêtre
bouton1.place(x=0, y=100)
bouton2.place(x=250, y=100)
bouton3.place(x=500, y=100)
bouton4.place(x=750, y=100)
bouton5.place(x=0, y=200)
bouton6.place(x=250, y=200)
bouton7.place(x=500, y=200)
bouton8.place(x=750, y=200)
bouton9.place(x=0, y=300)
bouton0.place(x=250, y=300)
bouton10.place(x=500, y=300)
bouton11.place(x=750, y=300)

bouton1["font"] = f
bouton2["font"] = f
bouton3["font"] = f
bouton4["font"] = f
bouton5["font"] = f
bouton6["font"] = f
bouton7["font"] = f
bouton8["font"] = f
bouton9["font"] = f
bouton0["font"] = f
bouton10["font"] = f
bouton11["font"] = f

# Ajouter un bouton de fermeture
bouton = Button(base, text="fermer", command=base.destroy)
bouton.place(x=750, y=400)
bouton["font"] = f


def credit():
    def ouvrir_lien():
        webbrowser.open(
            "https://mail.google.com/mail/u/0/?pli=1#inbox?compose=CllgCJqSvdHqRFvPWFsTLDLjXwmHlZPRlSxxfggmbWkHfPvzhSRTgqVrFmmpMSdhCSfRgrzxLqB"
        )

    credit = Toplevel()
    credit.geometry("800x500")
    credit.title(f"credits")
    chaine = f"programeur: ☺lecapitainecoeur☺"
    label = Label(
        credit,
        text=chaine,
        font=("Comic sans ms", 30),
    )
    label.place(x=0, y=0)
    chaine1 = f"créateur: ☺lecapitainecoeur☺"
    label1 = Label(
        credit,
        text=chaine1,
        font=("Comic sans ms", 30),
    )
    label1.place(x=0, y=100)
    chaine2 = f"imaginateur: ☺lecapitainecoeur☺"
    label2 = Label(
        credit,
        text=chaine2,
        font=("Comic sans ms", 30),
    )
    label2.place(x=0, y=200)
    lien = Label(
        credit,
        text="addresse mail createur",
        fg="blue",
        cursor="hand2",
        font=("Comic sans ms", 30),
    )
    lien.place(x=0, y=300)
    lien.bind("<Button-1>", lambda e: ouvrir_lien())
    buton = Button(credit, text="retour", command=credit.destroy)
    buton["font"] = f
    buton.place(x=350, y=400)


createur = Button(base, text="credits", command=credit)
createur.place(x=500, y=400)
createur["font"] = f


base.mainloop()

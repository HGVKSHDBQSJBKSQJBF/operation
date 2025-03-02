from tkinter import *
from tkinter.messagebox import *
from tkinter.font import *
import random
from enum import Enum
import webbrowser
from datetime import datetime


class op(Enum):
    addition = 1
    soustraction = 2
    multiplication = 3
    division = 4
    puissance2 = 5
    racinecarré = 6
    puissance3 = 7
    modulo = 8


class cal(Enum):
    multiplication = 1
    division = 2
    addition = 3
    soustraction = 4
    puissance2 = 5
    racinecarré = 6
    puissance3 = 7
    modulo = 8


def calculette():
    def solution1(operation):
        calcul = Toplevel()
        calcul.geometry("600x250")
        calcul.configure(bg="gray")
        entry = Entry(calcul)
        entry.place(x=0, y=50)
        entry["font"] = f
        if (
            operation == cal.addition
            or operation == cal.soustraction
            or operation == cal.multiplication
            or operation == cal.division
            or operation == cal.modulo
        ):
            entry2 = Entry(calcul)
            entry2.place(x=0, y=150)
            entry2["font"] = f
        calcul.bind(
            "<Return>",
            lambda event: deux_fonction(),
        )

        def entry_get():
            global nombre_1
            nombre_1 = int(entry.get())

        def entry_get2():
            global nombre_2
            nombre_2 = int(entry2.get())

        def valider():
            global solution
            if operation == cal.multiplication:
                solution = nombre_1 * nombre_2
                calcul.title("multplication")
            elif operation == cal.division:
                solution = nombre_1 // nombre_2
                calcul.title("division")
            elif operation == cal.addition:
                solution = nombre_1 + nombre_2
                calcul.title("addition")
            elif operation == cal.soustraction:
                solution = nombre_1 - nombre_2
                calcul.title("soustraction")
            elif operation == cal.puissance2:
                solution = nombre_1 * nombre_1
                calcul.title("puissance2")
            elif operation == cal.racinecarré:
                solution = nombre_1
                calcul.title("racine carré")
            elif operation == cal.puissance3:
                solution = nombre_1 * nombre_1 * nombre_1
                calcul.title("puissance3")
            elif operation == cal.modulo:
                solution = nombre_1 % nombre_2
                calcul.title("modulo")

        def deux_fonction():
            entry_get()
            if (
                operation == cal.addition
                or operation == cal.soustraction
                or operation == cal.multiplication
                or operation == cal.division
                or operation == cal.modulo
            ):
                entry_get2()
            valider()
            calcul.destroy()
            get_solution(solution)

        label = Label(
            calcul, text="entrer le premier nombre", font=("Comic Sans MS", 15)
        )
        label.place(x=0, y=0)
        label.configure(bg="gray")
        if (
            operation == cal.addition
            or operation == cal.soustraction
            or operation == cal.multiplication
            or operation == cal.division
            or operation == cal.modulo
        ):
            label1 = Label(
                calcul,
                text="entrer le deuxieme nombre",
                font=("Comic Sans MS", 15),
            )
            label1.place(x=0, y=100)
            label1.configure(bg="gray")
        buton = Button(calcul, text="valider", command=deux_fonction)
        buton.place(x=275, y=200)
        buton.configure(bg="gray")

    def get_solution(solution):
        resultat = Toplevel()
        resultat.title("resultat")
        resultat.geometry("500x250")
        resultat.configure(bg="gray")
        label2 = Label(
            resultat,
            text=f"le resultat est = ou ≈ {solution}",
            font=("Comic Sans MS", 24),
        )
        label2.place(x=0, y=0)
        label2.configure(bg="gray")
        buton = Button(resultat, text="fermer", command=resultat.destroy)
        buton.place(x=225, y=100)
        buton["font"] = f
        buton.configure(bg="gray")
        resultat.focus()

    def puissance3cal():
        solution1(cal.puissance3)

    def puissance2cal():
        solution1(cal.puissance2)

    def racinecarrécal():
        solution1(cal.racinecarré)

    def additioncal():
        solution1(cal.addition)

    def soustractioncal():
        solution1(cal.soustraction)

    def divisioncal():
        solution1(cal.division)

    def multiplicationcal():
        solution1(cal.multiplication)

    def modulocal():
        solution1(cal.modulo)

    fenetrecalcul = Toplevel()
    fenetrecalcul.title("calculette")
    fenetrecalcul.geometry("1110x300")
    fenetrecalcul.configure(bg="gray")
    f = Font(size=20)

    label2 = Label(
        fenetrecalcul, text="choisissez une operation:", font=("Comic sans ms", 30)
    )
    label2.place(x=0, y=0)
    label2.configure(bg="gray")
    width = 12
    buton1 = Button(
        fenetrecalcul, text="multiplication", command=multiplicationcal, width=width
    )
    buton2 = Button(fenetrecalcul, text="division", command=divisioncal, width=width)
    buton3 = Button(fenetrecalcul, text="addition", command=additioncal, width=width)
    buton5 = Button(
        fenetrecalcul, text="soustraction", command=soustractioncal, width=width
    )
    buton6 = Button(
        fenetrecalcul, text="puissance2", command=puissance2cal, width=width
    )
    buton7 = Button(
        fenetrecalcul, text="puissance3", command=puissance3cal, width=width
    )
    buton8 = Button(
        fenetrecalcul, text="racine carré", command=racinecarrécal, width=width
    )
    buton4 = Button(fenetrecalcul, text="modulo", command=modulocal, width=width)
    buton9 = Button(fenetrecalcul, text="a venir", width=width)
    buton10 = Button(fenetrecalcul, text="a venir", width=width)
    buton11 = Button(fenetrecalcul, text="a venir", width=width)
    buton12 = Button(fenetrecalcul, text="a venir", width=width)
    buton14 = Button(fenetrecalcul, text="a venir", width=width)
    buton15 = Button(fenetrecalcul, text="a venir", width=width)
    fermer = Button(
        fenetrecalcul, text="fermer", command=fenetrecalcul.destroy, width=width
    )
    buton1.grid(row=1, column=0, pady=(75, 10), padx=10)
    buton2.grid(row=1, column=1, pady=(75, 10), padx=10)
    buton3.grid(row=1, column=2, pady=(75, 10), padx=10)
    buton4.grid(row=1, column=3, pady=(75, 10), padx=10)
    buton5.grid(row=1, column=4, pady=(75, 10), padx=10)
    buton6.grid(row=2, column=0, pady=10, padx=10)
    buton7.grid(row=2, column=1, pady=10, padx=10)
    buton8.grid(row=2, column=2, pady=10, padx=10)
    buton9.grid(row=2, column=3, pady=10, padx=10)
    buton10.grid(row=2, column=4, pady=10, padx=10)
    buton11.grid(row=3, column=0, pady=10, padx=10)
    buton12.grid(row=3, column=1, pady=10, padx=10)
    fermer.grid(row=3, column=2, pady=10, padx=10)
    buton14.grid(row=3, column=3, pady=10, padx=10)
    buton15.grid(row=3, column=4, pady=10, padx=10)
    buton1.configure(bg="gray")
    buton2.configure(bg="gray")
    buton3.configure(bg="gray")
    buton4.configure(bg="gray")
    buton5.configure(bg="gray")
    buton6.configure(bg="gray")
    buton7.configure(bg="gray")
    buton8.configure(bg="gray")
    buton9.configure(bg="gray")
    buton10.configure(bg="gray")
    buton11.configure(bg="gray")
    buton12.configure(bg="gray")
    buton14.configure(bg="gray")
    buton15.configure(bg="gray")
    fermer.configure(bg="gray")

    buton1["font"] = f
    buton2["font"] = f
    buton3["font"] = f
    buton4["font"] = f
    buton5["font"] = f
    buton6["font"] = f
    buton7["font"] = f
    buton8["font"] = f
    buton9["font"] = f
    buton10["font"] = f
    buton11["font"] = f
    buton12["font"] = f
    fermer["font"] = f
    buton14["font"] = f
    buton15["font"] = f


def valider_pseudo():
    global pseudo
    pseudo = entry_pseudo.get()
    if pseudo.strip() != "":
        sauvegarder_pseudo(pseudo)  # Enregistrer dans le fichier
        fenetre_pseudo.destroy()
    else:
        showerror("Erreur", "Veuillez entrer un pseudo valide.")


def sauvegarder_pseudo(pseudo):
    with open("pseudo.txt", "w") as fichier:
        fichier.write(pseudo)


def charger_pseudo():
    try:
        with open("pseudo.txt", "r") as fichier:
            return fichier.read().strip()
    except FileNotFoundError:
        return ""


def deux_fonction():
    valider_pseudo()


def destroie():
    fenetre_pseudo.destroy()
    sauvegarder_pseudo(pseudo)


def open_mail(event=None):
    email = "lecapitainecoeurytbpro@gmail.com"
    subject = "idée pour votre projet operation"
    body = "Bonjour,\n\n"

    #  Lien Gmail avec adresse, sujet et corps de message pré-remplis
    gmail_link = f"https://mail.google.com/mail/?view=cm&fs=1&to={email}&su={subject}&body={body}"

    #  Ouvrir Gmail dans le navigateur
    webbrowser.open(gmail_link)


def ouvrir_github():
    webbrowser.open("https://github.com/HGVKSHDBQSJBKSQJBF/operation")


def credit():
    f = Font(size=20)
    credit = Toplevel()
    credit.geometry("600x400")
    credit.title(f"credits")
    credit.configure(bg="gray")
    chaine = f"programeur: ☺lecapitainecoeur☺"
    label = Label(
        credit,
        text=chaine,
        fg="red",
        font=("Comic sans ms", 29),
    )
    label.configure(bg="gray")
    label.place(x=0, y=0)
    chaine1 = f"créateur: ☺lecapitainecoeur☺"
    label1 = Label(
        credit,
        text=chaine1,
        fg="red",
        font=("Comic sans ms", 29),
    )
    label1.place(x=0, y=100)
    label1.configure(bg="gray")
    chaine2 = f"imaginateur: ☺lecapitainecoeur☺"
    label2 = Label(
        credit,
        text=chaine2,
        fg="red",
        font=("Comic sans ms", 29),
    )
    label2.place(x=0, y=200)
    label2.configure(bg="gray")
    buton = Button(credit, text="retour", fg="red", command=credit.destroy)
    buton["font"] = f
    buton.place(x=250, y=325)
    buton.configure(bg="gray")


def afficher_historique():
    with open("scores.txt", "r") as fichier:
        contenu = fichier.read()
        if contenu == "":
            contenu = "Il n'y a pas d'historique pour le moment"
        lignes = contenu.splitlines()
        nombre_de_lignes = len(lignes)
        if nombre_de_lignes >= 40:
            lignes_supprimees = lignes[-20]
            with open("scores.txt", "w") as fichier:
                fichier.writelines(lignes_supprimees)
            with open("scores.txt", "r") as fichier:
                contenu = fichier.read()

    #  Créer une fenêtre pour afficher l'historique
    historique = Toplevel()
    historique.title("Historique des Scores")
    historique.geometry("1000x500")

    #  Zone de texte pour afficher l'historique
    texte = Text(historique, wrap="word", font=("Comic sans ms", 14))
    texte.insert("1.0", contenu)
    texte.config(state="disabled")  # Empêcher la modification du texte
    texte.pack(expand=True, fill="both")


def enregistrer_score(user_reponse, solution, score, chaine2):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("scores.txt", "a") as fichier:
        if user_reponse == solution:
            fichier.write(
                f"{now} | {pseudo} | Réponse correcte | Score: {score} | operation: {chaine2} {user_reponse}\n"
            )
        else:
            fichier.write(
                f"{now} | {pseudo} | Réponse incorrecte | Score: {score}| operation: {chaine2} {user_reponse}\n"
            )


def genererop(operation, alea=False):
    root = Toplevel()
    root.configure(bg="gray")
    nombre_2 = 0
    if operation == op.puissance2:
        nombre_1 = random.randint(1, 11)
        chaine2 = f"{nombre_1}² = ?"
        root.title("puissance2")
    elif operation == op.modulo:
        nombre_1 = random.randint(10, 100)
        nombre_2 = random.randint(1, 10)
        chaine2 = f"{nombre_1} modulo {nombre_2} = ?"
        root.title("modulo")
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
    elif operation == op.puissance3:
        nombre_1 = random.randint(1, 5)
        chaine2 = f"{nombre_1}³ = ?"
        root.title("puissance2")
    else:
        erreur = Toplevel()
        erreur.geometry("500x150")
        erreur.title(f"erreur")
        erreur.configure(bg="gray")
        label = Label(erreur, text="operation invalide", font=("Comic sans ms", 30))
        label.place(x=0, y=0)
        label.configure(bg="gray")
        sortie = Button(erreur, text="ok...", command=erreur.destroy, width=15)
        sortie["font"] = f
        sortie.place(x=150, y=90)
        sortie.configure(bg="gray")
        return

    f = Font(size=20)
    root.geometry("450x200")
    label2 = Label(root, font=("Comic sans ms", 30), text=chaine2)
    label2.grid(row=0, column=2)
    label2.configure(bg="gray")

    finbutton = Button(
        root,
        text="fin",
        font=15,
        command=root.destroy,
    )
    finbutton.grid(row=4, column=2)
    finbutton.configure(bg="gray")
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
    button.configure(bg="gray")

    root.focus()
    entry.focus()
    root.mainloop()


def get_text(root, entry, operation, nombre_1, nombre_2=0, alea=False):
    if operation == op.multiplication:
        solution = nombre_2 * nombre_1
        recommencer = multiplication
        chaine2 = f"{nombre_1} x {nombre_2} = ?"
    elif operation == op.modulo:
        solution = nombre_1 % nombre_2
        recommencer = modulo
        chaine2 = f"{nombre_1} modulo {nombre_2} = ?"
    elif operation == op.addition:
        solution = nombre_1 + nombre_2
        recommencer = addition
        chaine2 = f"{nombre_1} + {nombre_2} = ?"
    elif operation == op.soustraction:
        solution = nombre_1 - nombre_2
        recommencer = soustraction
        chaine2 = f"{nombre_1} - {nombre_2} = ?"
    elif operation == op.division:
        solution = nombre_2 // nombre_1
        recommencer = division
        chaine2 = f"{nombre_1} / {nombre_2} = ?"
    elif operation == op.puissance2:
        solution = nombre_1 * nombre_1
        recommencer = puissance2
        chaine2 = f"{nombre_1}² = ?"
    elif operation == op.racinecarré:
        solution = nombre_1
        recommencer = racinecarré
        chaine2 = f"racine carré de {nombre_1 * nombre_1} = ?"
    elif operation == op.puissance3:
        solution = nombre_1 * nombre_1 * nombre_1
        recommencer = puissance3
        chaine2 = f"{nombre_1}³ = ?"
    else:
        erreur = Toplevel()
        erreur.geometry("500x150")
        erreur.title(f"erreur")
        erreur.configure(bg="gray")
        label = Label(erreur, text="operation invalide", font=("Comic sans ms", 30))
        label.place(x=0, y=0)
        label.configure(bg="gray")
        sortie = Button(erreur, text="ok...", command=erreur.destroy, width=15)
        sortie["font"] = f
        sortie.place(x=150, y=90)
        sortie.configure(bg="gray")
        return
    if alea:
        recommencer = aleatoire

    text = entry.get()
    try:
        user_reponse = int(text)
    except ValueError:
        erreur = Toplevel()
        erreur.geometry("500x150")
        erreur.configure(bg="gray")
        label = Label(erreur, text="ce n'est pas un nombre", font=("Comic sans ms", 30))
        label.place(x=0, y=0)
        label.configure(bg="gray")
        sortie = Button(erreur, text="ok...", command=erreur.destroy, width=15)
        sortie["font"] = f
        sortie.place(x=150, y=90)
        sortie.configure(bg="gray")
        return

    root.destroy()

    def done():
        top.destroy()
        enregistrer_score(user_reponse, solution, score, chaine2)

    def again():
        top.destroy()
        recommencer()
        enregistrer_score(user_reponse, solution, score, chaine2)

    top = Toplevel()
    top.geometry("500x250")
    top.title("veridict")
    top.configure(bg="gray")

    nouveau = Button(
        top,
        text="rejouer",
        command=again,
    )
    nouveau.grid(row=4, column=1)
    nouveau.configure(bg="gray")
    fin = Button(
        top,
        text="retour",
        command=done,
    )
    fin.grid(row=3, column=1)
    fin.configure(bg="gray")

    if user_reponse == solution:
        global score
        score += 1
        juste = Label(
            top,
            text=f"cette reponse est juste",
            font=("Helvetica 14 bold"),
        )
        juste.grid(row=1, column=1)
        juste.configure(bg="gray")
        chainescore = "score:", score
        scoreprint = Label(top, text=chainescore, font=("Comic Sans MS", 24))
        scoreprint.grid(row=2, column=1)
        scoreprint.configure(bg="gray")

    else:
        score -= 1
        chainescore = "score:", score
        scoreprint = Label(top, text=chainescore, font=("Comic Sans MS", 24))
        scoreprint.grid(row=2, column=1)
        scoreprint.configure(bg="gray")
        chainesolution = f"cette reponse est fausse, solution:, {solution}"
        faux = Label(
            top,
            text=chainesolution,
            font=("Helvetica 14 bold"),
        )
        faux.grid(row=1, column=1)
        faux.configure(bg="gray")

    top.bind("<BackSpace>", lambda event: done())
    top.bind("<Return>", lambda event: again())
    top.focus()
    top.mainloop()


def puissance2_3():

    def puissance32():
        puissance2ou3.destroy()
        puissance3()

    def puissance23():
        puissance2ou3.destroy()
        puissance2()

    puissance2ou3 = Toplevel()
    puissance2ou3.configure(bg="gray")
    puissance2ou3.title(f"²ou³")
    puissance2ou3.geometry("400x200")
    label = Label(puissance2ou3, text="p²ou³", font=("Comic sans ms", 30))
    label.place(x=0, y=0)
    label.configure(bg="gray")
    boton = Button(puissance2ou3, text="puissance³", command=puissance32)
    boton.place(x=0, y=100)
    boton["font"] = f
    boton.configure(bg="gray")
    boton1 = Button(puissance2ou3, text="puissance²", command=puissance23)
    boton1.place(x=200, y=100)
    boton1.configure(bg="gray")
    boton1["font"] = f


def puissance3():
    genererop(op.puissance3)


def modulo():
    genererop(op.modulo)


def puissance2():
    genererop(op.puissance2)


def racinecarré():
    genererop(op.racinecarré)


def aleatoire():
    genererop(op(random.randint(1, 7)), True)


def addition():
    genererop(op.addition)


def soustraction():
    genererop(op.soustraction)


def division():
    genererop(op.division)


def multiplication():
    genererop(op.multiplication)


fenetre_pseudo = Tk()

compteur = 0
score = 0
f = Font(size=20)
fenetre_pseudo.title("Connexion")
fenetre_pseudo.geometry("400x300")
fenetre_pseudo.configure(bg="gray")
fenetre_pseudo.focus()

labelpseudo = Label(
    fenetre_pseudo, text="Entrez votre pseudo :", font=("Comic sans ms", 20)
)
labelpseudo.pack(pady=20)
pseudo = charger_pseudo()
labelpseudo.configure(bg="gray")


entry_pseudo = Entry(fenetre_pseudo, font=("Comic sans ms", 16))
entry_pseudo.pack(pady=10)
entry_pseudo.insert(0, pseudo)
entry_pseudo.focus_set()

bouton13 = Button(
    fenetre_pseudo, text="fermer", font=("Comic sans ms", 16), command=destroie, width=6
)
bouton13.pack(pady=(10, 0))
bouton13["font"] = f
bouton13.configure(bg="gray")

bouton_valider = Button(
    fenetre_pseudo,
    text="Valider",
    command=deux_fonction,
    font=("Comic sans ms", 16),
)
bouton_valider.pack(pady=0)
bouton_valider.configure(bg="gray")
fenetre_pseudo.bind("<Return>", lambda event: valider_pseudo())
pseudo = ""

fenetre_pseudo.grab_set()
fenetre_pseudo.mainloop()
fenetre_pseudo.mainloop()

if pseudo != "":
    base = Tk()
    base.focus()
    f = Font(size=20)
    base.configure(bg="gray")
    base.title("operation")
    basefortext = Label(
        base,
        text="choisissez une opération:",
        font=("Comic sans ms", 30),
    )
    basefortext.place(x=0, y=0)
    basefortext.configure(bg="gray")

    base.geometry("900x450")

    width = 12
    bouton1 = Button(base, text="multiplication", command=multiplication, width=width)
    bouton2 = Button(base, text="division", command=division, width=width)
    bouton3 = Button(base, text="soustraction", command=soustraction, width=width)
    bouton4 = Button(base, text="addition", command=addition, width=width)
    bouton5 = Button(base, text="aléatoire", command=aleatoire, width=width)
    bouton6 = Button(base, text="racine carré", command=racinecarré, width=width)
    bouton7 = Button(base, text="puissance2 ou 3", command=puissance2_3, width=width)
    bouton8 = Button(base, text="modulos", width=width, command=modulo)
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
    bouton11 = Button(base, text="calculette", width=width, command=calculette)
    bouton12 = Button(
        base,
        text="historique score",
        width=width,
        command=afficher_historique,
        fg="red",
    )
    bouton13 = Button(base, text="fermer", fg="red", command=base.destroy, width=width)
    bouton14 = Button(base, text="support", command=open_mail, fg="red", width=width)
    bouton15 = Button(base, text="github", command=ouvrir_github, fg="red", width=width)
    createur = Button(base, text="credits", fg="red", command=credit, width=width)

    bouton1.configure(bg="gray")
    bouton2.configure(bg="gray")
    bouton3.configure(bg="gray")
    bouton4.configure(bg="gray")
    bouton5.configure(bg="gray")
    bouton6.configure(bg="gray")
    bouton7.configure(bg="gray")
    bouton8.configure(bg="gray")
    bouton9.configure(bg="gray")
    bouton10.configure(bg="gray")
    bouton11.configure(bg="gray")
    bouton12.configure(bg="gray")
    bouton0.configure(bg="gray")
    bouton13.configure(bg="gray")
    bouton14.configure(bg="gray")
    bouton15.configure(bg="gray")
    createur.configure(bg="gray")

    bouton1.grid(row=1, column=0, pady=(75, 10), padx=10)
    bouton2.grid(row=1, column=1, pady=(75, 10), padx=10)
    bouton3.grid(row=1, column=2, pady=(75, 10), padx=10)
    bouton4.grid(row=1, column=3, pady=(75, 10), padx=10)
    bouton5.grid(row=2, column=0, pady=10, padx=10)
    bouton6.grid(row=2, column=1, pady=10, padx=10)
    bouton7.grid(row=2, column=2, pady=10, padx=10)
    bouton8.grid(row=2, column=3, pady=10, padx=10)
    bouton9.grid(row=3, column=0, pady=10, padx=10)
    bouton0.grid(row=3, column=1, pady=10, padx=10)
    bouton10.grid(row=3, column=2, pady=10, padx=10)
    bouton11.grid(row=3, column=3, pady=10, padx=10)
    bouton12.grid(row=4, column=3, pady=10, padx=10)
    bouton13.grid(row=5, column=1, columnspan=2, pady=10, padx=10)
    bouton14.grid(row=4, column=2, pady=10, padx=10)
    bouton15.grid(row=4, column=1, pady=10, padx=10)
    createur.grid(row=4, column=0, pady=10, padx=10)

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
    bouton12["font"] = f
    bouton13["font"] = f
    bouton14["font"] = f
    bouton15["font"] = f
    createur["font"] = f

    base.mainloop()

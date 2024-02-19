import tkinter as tk
import time

class FenetreOverlay(tk.Tk):
    def __init__(self, x, y):
        tk.Tk.__init__(self)

        # Supprimer la décoration de la fenêtre (pas de bordure supérieure, pas de titre)
        self.overrideredirect(True)

        # Définir la taille de la fenêtre
        self.geometry("400x300+{}+{}".format(x, y))

        # Définir la couleur de fond de la fenêtre sur noir
        self.configure(bg="black")

        # Configurer une étiquette avec un texte blanc
        self.label = tk.Label(self, text="Ceci est une fenêtre overlay", font=("Helvetica", 16), bg="black", fg="white")
        self.label.pack(pady=10)

        # Lier la fermeture de la fenêtre à un événement, par exemple, un clic droit de la souris
        self.bind("<Button-3>", self.fermer_fenetre)

    def fermer_fenetre(self, event=None):
        self.destroy()

    # Ajouter une méthode pour fermer la fenêtre depuis l'extérieur
    def fermer_depuis_exterieur(self):
        self.destroy()

    # Ajouter une méthode pour modifier le texte de l'étiquette
    def modifier_texte(self, nouveau_texte):
        self.label.config(text=nouveau_texte)

if __name__ == "__main__":
    # Exemple d'ouverture de deux fenêtres à des emplacements différents
    fenetre1 = FenetreOverlay(100, 100)
    fenetre2 = FenetreOverlay(300, 100)

    fenetre1.update()
    fenetre2.update()

    time.sleep(2)
    for i in range(1000):
        print(i)
    # Définir les actions après un court délai (par exemple, 1000 millisecondes = 1 seconde)
    fenetre1.after(1000, lambda: fenetre1.modifier_texte("Nouveau texte pour la fenêtre 1"))
    fenetre1.after(2000, lambda: fenetre1.fermer_fenetre())
    fenetre2.after(1000, lambda: fenetre2.fermer_fenetre())

    fenetre1.mainloop()
    fenetre2.mainloop()

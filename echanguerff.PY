
import tkinter as tk
from tkinter import ttk, messagebox

# PARTIE 1 : LA LOGIQUE MÉTIER

TAUX_CONVERSION = {
    "Franc FCFA": 1.0,
    "Eco": 1.0,
    "Dollar": 0.0016,
    "Naira": 2.40,
    "Cedi": 0.024
}

def valider_nom(nom):
    nom_clean = nom.strip()
    if not nom_clean:
        return False, "Veuillez entrer votre nom !"
    if not nom_clean.replace(" ", "").replace("-", "").isalpha():
        return False, "Le nom ne doit contenir que des lettres !"
    return True, nom_clean

def valider_montant(valeur_texte):
    try:
        montant = float(valeur_texte)
        if montant <= 0:
            return False, "Le montant doit être supérieur à 0 !"
        return True, montant
    except ValueError:
        return False, "Veuillez entrer un nombre valide en chiffres !"

def calculer_conversion(montant, devise_source, devise_cible):
    montant_fcfa = montant / TAUX_CONVERSION[devise_source]
    return montant_fcfa * TAUX_CONVERSION[devise_cible]


# PARTIE 2 : LE PONT (Gestion du clic)


def cliquer_sur_convertir():
    nom_valide, res_nom = valider_nom(entry_nom.get())
    if not nom_valide:
        messagebox.showerror("Erreur", res_nom)
        return

    montant_valide, res_montant = valider_montant(entry_montant.get())
    if not montant_valide:
        messagebox.showerror("Erreur", res_montant)
        return

    source = combo_depart.get()
    cible = combo_arrivee.get()

    resultat = calculer_conversion(res_montant, source, cible)

    label_resultat.config(
        text=f"Bonjour {res_nom} !\n{res_montant:.2f} {source} = {resultat:.2f} {cible}"
    )



# PARTIE 3 : INTERFACE GRAPHIQUE (Fond Noir & Plein Écran)


fenetre = tk.Tk()
fenetre.title("Convertisseur de Devises")

# --- 1. ACTIVATION DU PLEIN ÉCRAN ---
fenetre.attributes("-fullscreen", True)

# Appuie sur la touche Échap (Escape) pour quitter le plein écran à tout moment
fenetre.bind("<Escape>", lambda event: fenetre.attributes("-fullscreen", False))

# --- 2. COULEURS DU THÈME SOMBRE ---
FOND_NOIR = "black"
TEXTE_BLANC = "white"
CHAMP_SOMBRE = "#1f1f1f"

fenetre.configure(bg=FOND_NOIR)

# Style pour adapter les menus déroulants (Combobox) au fond noir
style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground=CHAMP_SOMBRE, background="#333333", foreground=TEXTE_BLANC)

# Cadre central pour garder les éléments bien regroupés au milieu de l'écran
cadre_central = tk.Frame(fenetre, bg=FOND_NOIR)
cadre_central.pack(expand=True)

# Titre
label_titre = tk.Label(cadre_central, text="ÉCHANGEUR DE DEVISES", font=("Helvetica", 18, "bold"), bg=FOND_NOIR, fg=TEXTE_BLANC)
label_titre.pack(pady=20)

# Champ Nom
label_nom = tk.Label(cadre_central, text="Votre nom :", bg=FOND_NOIR, fg=TEXTE_BLANC, font=("Helvetica", 11))
label_nom.pack(anchor="w", padx=10)

entry_nom = tk.Entry(cadre_central, width=35, bg=CHAMP_SOMBRE, fg=TEXTE_BLANC, insertbackground=TEXTE_BLANC, font=("Helvetica", 11))
entry_nom.pack(pady=5)

# Champ Montant
label_montant = tk.Label(cadre_central, text="Montant :", bg=FOND_NOIR, fg=TEXTE_BLANC, font=("Helvetica", 11))
label_montant.pack(anchor="w", padx=10)

entry_montant = tk.Entry(cadre_central, width=35, bg=CHAMP_SOMBRE, fg=TEXTE_BLANC, insertbackground=TEXTE_BLANC, font=("Helvetica", 11))
entry_montant.pack(pady=5)

# Liste des devises
liste_devises = list(TAUX_CONVERSION.keys())

# Devise Départ
label_depart = tk.Label(cadre_central, text="De :", bg=FOND_NOIR, fg=TEXTE_BLANC, font=("Helvetica", 11))
label_depart.pack(anchor="w", padx=10)

combo_depart = ttk.Combobox(cadre_central, values=liste_devises, state="readonly", width=33)
combo_depart.set("Franc FCFA")
combo_depart.pack(pady=5)

# Devise Arrivée
label_arrivee = tk.Label(cadre_central, text="Vers :", bg=FOND_NOIR, fg=TEXTE_BLANC, font=("Helvetica", 11))
label_arrivee.pack(anchor="w", padx=10)

combo_arrivee = ttk.Combobox(cadre_central, values=liste_devises, state="readonly", width=33)
combo_arrivee.set("Dollar")
combo_arrivee.pack(pady=5)

# Bouton Convertir
btn_convertir = tk.Button(cadre_central, text="Convertir", command=cliquer_sur_convertir, bg="#4caf50", fg=TEXTE_BLANC, font=("Helvetica", 11, "bold"), padx=10, pady=5)
btn_convertir.pack(pady=25)

# Zone Résultat
label_resultat = tk.Label(cadre_central, text="", font=("Helvetica", 13, "bold"), bg=FOND_NOIR, fg="#00e676")
label_resultat.pack(pady=10)

# Bouton Quitter (placé en bas à droite de l'écran)
btn_quitter = tk.Button(fenetre, text="Fermer (Échap)", command=fenetre.destroy, bg="#d32f2f", fg=TEXTE_BLANC, font=("Helvetica", 10))
btn_quitter.pack(side="bottom", anchor="se", padx=30, pady=30)

fenetre.mainloop()

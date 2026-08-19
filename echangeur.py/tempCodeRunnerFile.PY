 déroulants (Combobox) au fond noir
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
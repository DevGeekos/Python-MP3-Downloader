import os
import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL

# Création du dossier de téléchargement
download_folder = "Téléchargements_MP3"
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Dictionnaire de correspondance des qualités
qualites = {
    "64 : Très basse": "64",
    "96 : Basse": "96",
    "128 : Moyenne": "128",
    "160 : Bonne": "160",
    "192 : Très bonne": "192",
    "256 : Excellente": "256",
    "320 : Exceptionnelle": "320"
}

# Fonction pour télécharger le fichier MP3
def telecharger_mp3():
    url = url_entry.get()
    qualite_label = qualite_var.get()
    qualite = qualites[qualite_label]

    if not url:
        messagebox.showwarning("Erreur", "Veuillez entrer une adresse URL.")
        return

    options = {
        'format': 'bestaudio/best',
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',  # Utilise le nom de la vidéo pour le fichier
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': qualite,
        }],
    }

    try:
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        messagebox.showinfo("Succès", "Téléchargement terminé avec succès !")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du téléchargement : {e}")

# Mode clair et sombre
def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    update_colors()

def update_colors():
    if dark_mode:
        root.config(bg="#2c2c2c")
        title_label.config(bg="#2c2c2c", fg="#00d1ff")
        subtitle_label.config(bg="#2c2c2c", fg="#f0f0f0")
        version_label.config(bg="#2c2c2c", fg="#bbbbbb")
        url_label.config(bg="#2c2c2c", fg="#f0f0f0")
        qualite_label.config(bg="#2c2c2c", fg="#f0f0f0")
        signature_label.config(bg="#2c2c2c", fg="#bbbbbb")
        mode_button.config(text="Mode Clair", bg="#555555", fg="#f0f0f0", activebackground="#777777")
        qualite_menu.config(bg="#555555", fg="#f0f0f0", activebackground="#777777", activeforeground="#f0f0f0")
        download_button.config(bg="#007bff", fg="white", activebackground="#0056b3")
    else:
        root.config(bg="#e0f7fa")
        title_label.config(bg="#e0f7fa", fg="#007bff")
        subtitle_label.config(bg="#e0f7fa", fg="#555555")
        version_label.config(bg="#e0f7fa", fg="#777777")
        url_label.config(bg="#e0f7fa", fg="#333333")
        qualite_label.config(bg="#e0f7fa", fg="#333333")
        signature_label.config(bg="#e0f7fa", fg="#555555")
        mode_button.config(text="Mode Sombre", bg="#e0e0e0", fg="#333333", activebackground="#cccccc")
        qualite_menu.config(bg="#e0e0e0", fg="#333333", activebackground="#d0d0d0", activeforeground="#333333")
        download_button.config(bg="#007bff", fg="white", activebackground="#0056b3")

# Configuration de l'interface graphique
root = tk.Tk()
root.title("Python MP3 Downloader")
root.geometry("700x500")  # Taille ajustée pour inclure le texte supplémentaire

# Initialisation du mode sombre
dark_mode = False

# Titre et descriptions
title_label = tk.Label(root, text="Python MP3 Downloader", font=("Comic Sans MS", 20, "bold"))
title_label.pack(pady=10)

# Sous-titre de description
subtitle_label = tk.Label(root, text="Logiciel open source de téléchargement de mp3 via python", font=("Helvetica", 14))
subtitle_label.pack()

# Version
version_label = tk.Label(root, text="Version 1.0.0", font=("Arial Black", 12))
version_label.pack(pady=(0, 20))

# Champ d'entrée pour l'URL
url_label = tk.Label(root, text="Entrez l'adresse URL :", font=("Segoe UI", 12))
url_label.pack(pady=5)
url_entry = tk.Entry(root, font=("Helvetica", 12), width=45)
url_entry.pack(pady=5)

# Menu déroulant pour la qualité audio avec libellés
qualite_label = tk.Label(root, text="Choisissez la qualité audio :", font=("Verdana", 12))
qualite_label.pack(pady=5)
qualite_var = tk.StringVar(root)
qualite_var.set("128 : Moyenne")  # Valeur par défaut
qualite_menu = tk.OptionMenu(root, qualite_var, *qualites.keys())
qualite_menu.config(width=20, font=("Helvetica", 12))
qualite_menu.pack(pady=5)

# Bouton de téléchargement (rectangle arrondi)
download_button = tk.Button(
    root,
    text="Télécharger",
    font=("Helvetica", 12, "bold"),
    bd=0,
    padx=20,
    pady=10,
    relief="ridge",
    command=telecharger_mp3
)
download_button.pack(pady=20)

# Bouton pour basculer entre le mode clair et sombre
mode_button = tk.Button(root, text="Mode Sombre", font=("Helvetica", 10), command=toggle_mode, width=12)
mode_button.pack(pady=10)

# Signature en bas
signature_label = tk.Label(root, text="By DevGeekos | Tous droits réservés", font=("Verdana", 8))
signature_label.pack(side="bottom", pady=10)

# Appliquer les couleurs initiales
update_colors()

root.mainloop()
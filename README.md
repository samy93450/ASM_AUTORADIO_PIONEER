# ASM Autoradio Pioneer

Application autoradio desktop conçue en HTML/CSS/JavaScript et lancée sous Windows avec **PyWebView**. Le package peut être compilé en un fichier `.exe` autonome avec **PyInstaller**.

## Contenu

- `index.html` — interface et logique principale de l'application.
- `launcher.py` — lanceur desktop local PyWebView.
- `assets/icon-source.png` — source de l'icône Windows.
- `assets/jacket.png` — jaquette de l'application.
- `make_icon.py` — génère le fichier `.ico`.
- `build_exe.bat` — installe les dépendances et compile l'EXE Windows.
- `VERIFIER_AVANT_BUILD.bat` — vérification avant compilation.
- `requirements.txt` — dépendances Python.

## Utilisation depuis les sources

Prérequis : Windows 10/11 et Python 3.11 ou 3.12.

```bash
python -m pip install -r requirements.txt
python launcher.py
```

Le lanceur démarre un serveur uniquement sur `127.0.0.1`, puis ouvre l'application dans une fenêtre PyWebView.

## Créer l'EXE Windows

1. Installer Python 3.11/3.12 et activer **Add Python to PATH**.
2. Lancer `VERIFIER_AVANT_BUILD.bat`.
3. Lancer `build_exe.bat`.
4. Le résultat sera créé dans :

```text
dist/ASM Autoradio Pioneer.exe
```

Le script de build installe automatiquement `pywebview`, `pyinstaller` et `pillow`, crée l'icône `.ico` si nécessaire, puis lance PyInstaller.

## Publication sur GitHub

Créer un nouveau dépôt GitHub, puis depuis ce dossier :

```bash
git init
git add .
git commit -m "Initial release - ASM Autoradio Pioneer"
git branch -M main
git remote add origin https://github.com/VOTRE-COMPTE/ASM-Autoradio-Pioneer.git
git push -u origin main
```

Remplacez `VOTRE-COMPTE` par votre nom d'utilisateur GitHub.

## GitHub Pages

L'interface `index.html` peut être publiée comme démonstration web avec GitHub Pages. Certaines fonctions desktop dépendent toutefois de PyWebView et la lecture des radios dépend de services/flux externes et des règles du navigateur.

Pour activer Pages : **Settings → Pages → Deploy from a branch → main / root**.

## Dépendances et fonctionnement réseau

L'application référence des flux audio et ressources provenant de services externes. Leur disponibilité, leurs URL et leurs conditions d'utilisation peuvent évoluer indépendamment de ce dépôt.

## Données locales

La version Windows utilise un stockage PyWebView persistant dans le profil utilisateur Windows (`LocalAppData`) afin de conserver le stockage web entre les lancements.

## Licence

Aucune licence open source n'est imposée dans ce package. Ajoutez un fichier `LICENSE` uniquement si vous souhaitez définir explicitement les droits de réutilisation du code et des ressources.

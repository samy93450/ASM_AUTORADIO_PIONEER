@echo off
cd /d "%~dp0"
set ERR=0
if not exist index.html echo MANQUANT: index.html&set ERR=1
if not exist launcher.py echo MANQUANT: launcher.py&set ERR=1
if not exist build_exe.bat echo MANQUANT: build_exe.bat&set ERR=1
if not exist assets\icon-source.png echo MANQUANT: assets\icon-source.png&set ERR=1
if not exist assets\jacket.png echo MANQUANT: assets\jacket.png&set ERR=1
if "%ERR%"=="0" (echo DOSSIER COMPLET - PRET POUR BUILD) else (echo ERREURS DETECTEES)
pause

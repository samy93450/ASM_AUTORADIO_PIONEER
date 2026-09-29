@echo off
setlocal
cd /d "%~dp0"
title ASM AUTORADIO PIONEER - BUILD EXE

echo ============================================================
echo   ASM AUTORADIO PIONEER - COMPILATION WINDOWS

echo ============================================================
where py >nul 2>nul && (set PY=py) || (set PY=python)
%PY% --version || goto :python_error

%PY% -m pip install --upgrade pip
%PY% -m pip install pywebview pyinstaller pillow
if errorlevel 1 goto :dep_error

if not exist assets\asm-autoradio.ico (
 echo Creation de l'icone Windows depuis assets\icon-source.png...
 %PY% make_icon.py
 if errorlevel 1 echo AVERTISSEMENT: creation ICO impossible, build sans icone personnalisee.
)

set ICONARG=
if exist assets\asm-autoradio.ico set ICONARG=--icon "assets\asm-autoradio.ico"

%PY% -m PyInstaller --noconfirm --clean --onefile --windowed ^
 --name "ASM Autoradio Pioneer" %ICONARG% ^
 --add-data "index.html;." ^
 --add-data "assets;assets" ^
 --collect-all webview launcher.py
if errorlevel 1 goto :build_error

echo.
echo BUILD TERMINE.
echo EXE : dist\ASM Autoradio Pioneer.exe
pause
exit /b 0
:python_error
echo ERREUR: Python 3 n'est pas installe ou pas dans PATH.
pause
exit /b 1
:dep_error
echo ERREUR: installation des dependances impossible.
pause
exit /b 1
:build_error
echo ERREUR: PyInstaller n'a pas pu creer l'EXE.
pause
exit /b 1

@echo off
echo ==========================================
echo   DIABETES MANAGEMENT SYSTEM - GITHUB
echo ==========================================
echo.
echo Questo script ti aiuta a caricare il progetto su GitHub
echo.
echo PASSO 1: Vai su https://github.com/new
echo PASSO 2: Nome repository: diabetes-management-system
echo PASSO 3: Descrizione: Sistema di gestione pazienti diabetici con PyQt5 e SQLite
echo PASSO 4: Seleziona Pubblico o Privato
echo PASSO 5: NON aggiungere README, .gitignore o license
echo PASSO 6: Clicca "Create repository"
echo.
echo PASSO 7: Copia il tuo username GitHub qui sotto:
set /p GITHUB_USERNAME="Inserisci il tuo username GitHub: "
echo.
echo PASSO 8: Esegui questi comandi:
echo.
echo git remote add origin https://github.com/%GITHUB_USERNAME%/diabetes-management-system.git
echo git branch -M main
echo git push -u origin main
echo.
echo Premi INVIO per eseguire automaticamente...
pause >nul

git remote add origin https://github.com/%GITHUB_USERNAME%/diabetes-management-system.git
git branch -M main
git push -u origin main

echo.
echo ==========================================
echo FATTO! Il repository e' stato caricato su:
echo https://github.com/%GITHUB_USERNAME%/diabetes-management-system
echo ==========================================
pause
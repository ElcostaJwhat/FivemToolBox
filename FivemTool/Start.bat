@echo off
title Menu d'Installation et Lancement du Script
color 0A

:menu
cls
echo ==============================================
echo           Gestion du script
echo ==============================================
echo.
echo 1. Verifier si Python est installe
echo 2. Installer les librairies du script (obligatoire pour qu'il puisse se lancer)
echo 3. Lancer le script Python
echo 4. Quitter
echo.
set /p choix=Veuillez choisir une option [1-4] : 

if "%choix%"=="1" goto verifier_python
if "%choix%"=="2" goto installer_libraries
if "%choix%"=="3" goto lancer_script
if "%choix%"=="4" goto fin
goto menu

:verifier_python
cls
echo Verification de l'installation de Python...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERREUR] Python n'est pas installe. Veuillez l'installer avant de continuer.
) ELSE (
    echo.
    echo [SUCCES] Python est installe sur votre systeme.
)
pause
goto menu

:installer_libraries
cls
echo ===============================================
echo  Installation des Librairies Python necessaires
echo ===============================================
echo.
pip install psutil customtkinter watchdog

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERREUR] Une erreur s'est produite lors de l'installation des librairies.
) ELSE (
    echo.
    echo [SUCCES] Toutes les librairies ont ete installees avec succes !
)
pause
goto menu

:lancer_script
cls
echo Lancement du script Python...
python releasefivetool.py

echo.
echo Script termine. Vous pouvez fermer cette fenetre.
pause
goto menu

:fin
cls
pause
exit

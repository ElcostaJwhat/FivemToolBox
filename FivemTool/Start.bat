@echo off
title 🚀 ReleaseFiveTool - Gestionnaire d'Installation
color 0B
chcp 65001 >nul 2>&1

:menu
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                      🎯 FIVE TOOL                            ║
echo ║                  Gestionnaire d'Installation                 ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo ┌──────────────────────────────────────────────────────────────┐
echo │                        📋 MENU PRINCIPAL                    │
echo └──────────────────────────────────────────────────────────────┘
echo.
echo   🔍 [1] Vérifier l'installation de Python
echo   📦 [2] Installer les dépendances (requis)
echo   🚀 [3] Lancer le script Python
echo   ❌ [4] Quitter
echo.
echo ┌──────────────────────────────────────────────────────────────┐
set /p choix=│ Votre choix [1-4]: 
echo └──────────────────────────────────────────────────────────────┘

if "%choix%"=="1" goto verifier_python
if "%choix%"=="2" goto installer_libs
if "%choix%"=="3" goto lancer_script
if "%choix%"=="4" goto fin
echo.
echo ⚠️  Option invalide. Veuillez choisir entre 1 et 4.
timeout /t 2 >nul
goto menu

:verifier_python
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                  🔍 VÉRIFICATION DE PYTHON                  ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo ⏳ Vérification en cours...
echo.

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ [ERREUR] Python n'est pas installé ou inaccessible
    echo.
    echo 💡 Solutions possibles:
    echo    • Téléchargez Python depuis: https://python.org
    echo    • Vérifiez que Python est dans le PATH système
    echo    • Redémarrez votre terminal après installation
) ELSE (
    for /f "tokens=*" %%i in ('python --version 2^>^&1') do set python_version=%%i
    echo ✅ [SUCCÈS] Python détecté: !python_version!
    echo.
    echo 📊 Informations système:
    python -c "import sys; print(f'   • Architecture: {sys.maxsize > 2**32 and \"64-bit\" or \"32-bit\"}')"
    python -c "import sys; print(f'   • Version: {sys.version.split()[0]}')"
)
echo.
echo ┌──────────────────────────────────────────────────────────────┐
echo │ Appuyez sur une touche pour revenir au menu...
pause >nul
goto menu

:installer_libs
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                📦 INSTALLATION DES DÉPENDANCES              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 🔄 Installation des librairies requises...
echo.
echo ┌─ Librairies à installer: ────────────────────────────────────┐
echo │ • psutil      - Monitoring système                          │
echo │ • customtkinter - Interface graphique moderne               │
echo │ • watchdog    - Surveillance de fichiers                    │
echo └──────────────────────────────────────────────────────────────┘
echo.

pip install psutil customtkinter watchdog
echo.

IF %ERRORLEVEL% NEQ 0 (
    echo ❌ [ERREUR] Échec de l'installation des dépendances
    echo.
    echo 💡 Solutions possibles:
    echo    • Vérifiez votre connexion Internet
    echo    • Exécutez en tant qu'administrateur
    echo    • Utilisez: pip install --user [package]
) ELSE (
    echo ✅ [SUCCÈS] Toutes les dépendances ont été installées!
    echo.
    echo 🎉 Le script est maintenant prêt à être utilisé.
)
echo.
echo ┌──────────────────────────────────────────────────────────────┐
echo │ Appuyez sur une touche pour revenir au menu...
pause >nul
goto menu

:lancer_script
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                   🚀 LANCEMENT DU SCRIPT                    ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

if not exist "releasefivetool.py" (
    echo ❌ [ERREUR] Le fichier 'releasefivetool.py' est introuvable
    echo.
    echo 💡 Vérifiez que le fichier se trouve dans le même dossier
    echo    que ce script BAT.
    echo.
    echo ┌──────────────────────────────────────────────────────────────┐
    echo │ Appuyez sur une touche pour revenir au menu...
    pause >nul
    goto menu
)

echo ⏳ Démarrage en cours...
echo.
echo ┌──────────────────────────────────────────────────────────────┐
echo │                   SORTIE DU SCRIPT PYTHON                   │
echo └──────────────────────────────────────────────────────────────┘

python releasefivetool.py

echo.
echo ┌──────────────────────────────────────────────────────────────┐
echo │ ✅ Script terminé. Retour au menu dans 3 secondes...
timeout /t 3 >nul
goto menu

:fin
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                      👋 AU REVOIR!                          ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo   Merci d'avoir utilisé Five Tool 
echo   
echo   🔗 Pour plus d'informations: https://github.com/ElcostaJwhat/FivemToolBox
echo.
echo ┌──────────────────────────────────────────────────────────────┐
echo │ Fermeture dans 3 secondes...
timeout /t 3 >nul
exit

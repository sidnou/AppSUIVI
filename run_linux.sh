#!/bin/bash

echo "=== Lancement AppSUIVI sur Linux ==="

# Vérification de Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 n'est pas installé"
    echo "Installez-le avec: sudo apt install python3 python3-pip python3-tk"
    exit 1
fi

# Vérification de tkinter
python3 -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "tkinter n'est pas disponible"
    echo "Installez-le avec: sudo apt install python3-tk"
    exit 1
fi

# Activation de l'environnement virtuel s'il existe
if [ -d "venv" ]; then
    echo "Activation de l'environnement virtuel..."
    source venv/bin/activate
fi

# Installation des dépendances
if [ -f "requirements.txt" ]; then
    echo "Installation/mise à jour des dépendances..."
    pip3 install -r requirements.txt
fi

# Vérification des permissions d'affichage (pour X11)
if [ -n "$DISPLAY" ]; then
    echo "✓ Affichage X11 disponible: $DISPLAY"
else
    echo "⚠ Variable DISPLAY non définie - GUI peut ne pas fonctionner"
fi

# Lancement de l'application
echo "Lancement de l'application..."
cd src
python3 gui_v1-2.py

echo "Application fermée"
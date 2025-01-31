# Eco Certificate Demo

Une démonstration d'intégration entre GitHub et Google Colab pour l'analyse d'impact écologique.

## Ouvrir dans Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fabricehong/eco-certificates/blob/main/notebooks/eco_analysis.ipynb?force_timestamp=20250131)

## Structure du Projet

```
eco-certificate/
├── notebooks/
│   └── eco_analysis.ipynb    # Notebook universel (local et Colab)
├── src/
│   └── models/
│       └── eco_calculator.py    # Module de calcul d'impact
└── data/
    └── sample_devices.csv    # Données d'exemple
```

## Utilisation

1. Cliquez sur le badge "Open in Colab" ci-dessus pour l'exécuter dans Colab
2. Ou ouvrez le notebook localement avec Jupyter pour l'exécuter sur votre machine
3. La première cellule détectera automatiquement l'environnement et configurera le notebook en conséquence

## Fonctionnalités

- Calcul d'impact écologique basé sur l'utilisation et l'efficacité
- Notation écologique (A à F)
- Visualisation des résultats avec matplotlib
- Démonstration d'intégration de code source Python avec Colab

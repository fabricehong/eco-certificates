# Eco Certificate Generator

Un système de génération de certificats écologiques pour évaluer et certifier les produits et services selon des critères de durabilité et d'éthique.

## Ouvrir dans Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fabricehong/eco-certificates/blob/main/notebooks/eco_analysis.ipynb?force_timestamp=20250131)

## Description du Projet

Ce projet vise à créer un système complet d'éco-certification qui permet aux entreprises de :
- Évaluer le caractère écologique et éthique de leurs produits/services
- Obtenir des certificats basés sur des critères d'évaluation standardisés
- Démontrer leur engagement écologique de manière transparente
- Assurer la traçabilité de leur chaîne de production européenne

## Fonctionnalités

Le système se compose de trois parties principales :

### 1. Collecte et Analyse des Données 
- Parse les fichiers CSV contenant les réponses aux questionnaires d'évaluation
- Structure les données en objets (Produits, Scores, Composants)
- Valide et nettoie les données d'entrée

### 2. Calcul des Scores 
- Évalue chaque composant de score (réponses Yes/No)
- Calcule un pourcentage global par catégorie (produit/service)
- Attribution de 20% par réponse positive
- Génère une note finale et un grade

### 3. Génération de Certificats 
- Crée des certificats PDF professionnels
- Inclut :
  - Informations détaillées du produit/service
  - Scores calculés et leur répartition
  - Détails des évaluations par catégorie
  - Représentation visuelle des résultats (étoiles/grades)

## Structure du Projet

```
eco-certificate/
├── notebooks/
│   └── eco_analysis.ipynb    # Notebook universel (local et Colab)
├── input/
│   └── product and service form.csv    # Fichier de données d'entrée
├── src/
│   ├── models/
│   │   └── eco_form.py                 # Modèles de données
│   ├── services/
│   │   └── csv_parser.py               # Service de parsing CSV
│   └── main.py                         # Point d'entrée de l'application
```

## Installation

1. Cloner le repository
```bash
git clone https://github.com/fabricehong/eco-certificates.git
cd eco-certificate
```

2. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Utilisation

Deux options s'offrent à vous :

### 1. Via Google Colab
1. Cliquez sur le badge "Open in Colab" ci-dessus
2. Le notebook s'exécutera directement dans votre navigateur
3. La première cellule configurera automatiquement l'environnement

### 2. En Local
1. Préparer le fichier CSV avec les données d'évaluation
2. Exécuter le script principal :
```bash
python src/main.py
```

## État d'Avancement

-  Parsing des données CSV
-  Modélisation des données
-  Calcul des scores
-  Génération des certificats PDF
-  Interface utilisateur

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

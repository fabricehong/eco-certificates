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

## Utilisation Standard

### Préparer les Données d'Entrée

1. Placez votre fichier CSV d'évaluation dans le dossier `input/`
   - Le nom par défaut attendu est `product and service form.csv`
   - Le fichier doit contenir les réponses au questionnaire d'évaluation (Yes/No)
   - Deux exemples sont fournis : 
     - `product and service form - small.csv` (version réduite pour test)
     - `product and service form - full.csv` (version complète)

### Générer les Certificats

#### Option 1 : Via Google Colab (Recommandé)
1. Cliquez sur le badge "Open in Colab" en haut de ce README
2. Uploadez votre fichier CSV quand demandé
3. Exécutez les cellules du notebook
4. Les certificats générés seront disponibles dans le dossier `output/`

#### Option 2 : En Local
1. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Exécutez le script principal :
   ```bash
   python src/main.py
   ```
3. Les certificats seront générés dans le dossier `output/` avec le format :
   - Un fichier PNG par produit/service
   - Nom du fichier : `nom_du_produit_certificate.png`

### Résultats
- Les certificats générés se trouvent dans le dossier `output/`
- Le script affiche un résumé des produits traités avec leurs scores
- Pour chaque produit, vous verrez :
  - Le nom du produit
  - Les scores détaillés
  - Le chemin du certificat généré

## Configuration Avancée (Optionnel)

### Personnalisation des Images
Le générateur utilise par défaut les images fournies dans le dossier `images/` :
- `certificate.png` : Template du certificat
- `active-leave.png` : Icône de feuille active (score positif)
- `unactive-leave.png` : Icône de feuille inactive (score négatif)

Pour personnaliser :
1. Placez vos images dans le dossier `images/`
2. Modifiez les chemins dans `src/main.py` si nécessaire

### Personnalisation des Polices
Par défaut, le système utilise Arial Bold. Pour utiliser d'autres polices :
1. Placez vos fichiers TTF dans le dossier `fonts/`
2. Modifiez les paramètres dans `src/main.py` :
   - `font_path` : Police standard
   - `bold_font_path` : Police en gras
   - `font_size` : Taille des labels
   - `description_font_size` : Taille des descriptions

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

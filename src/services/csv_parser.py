import pandas as pd
from typing import List
from pathlib import Path

from src.models.csv_models import CsvProduct, CsvScore, ScoreComponent, CsvEvaluation

class CsvParser:
    """Parser pour le fichier CSV des produits et services.
    
    Le fichier CSV est structuré en 3 parties:
    1. La ligne 1 contient les en-têtes généraux
    2. La ligne 2 contient les descriptions des scores (local, eco-friendly, living respect)
    3. La ligne 3 contient les descriptions des composants de chaque score
    4. Les lignes suivantes contiennent les données des produits/services
    
    Pour chaque produit/service, on a :
    - 3 colonnes d'identification (nom, id, type)
    - 3 groupes de scores pour les produits (local, eco-friendly, living respect)
    - 3 groupes de scores pour les services (local, eco-friendly, living respect)
    
    Chaque groupe de score contient score_component_size composants,
    chacun avec une réponse Yes/No/None.
    """
    
    def __init__(self, csv_path: Path, score_component_size: int):
        """Initialise le parser avec le chemin du fichier et la taille des composants.
        
        Args:
            csv_path: Chemin vers le fichier CSV
            score_component_size: Nombre de composants par groupe de score
        """
        self.csv_path = csv_path
        self.score_component_size = score_component_size
        self.df = pd.read_csv(self.csv_path)
        
        # Trouver les index de début des scores produits et services
        self.product_score_index = self._find_score_index("product")
        self.service_score_index = self._find_score_index("service")
    
    def _find_score_index(self, score_type: str) -> int:
        """Trouve l'index de début d'un type de score"""
        header_row = self.df.iloc[2]  # Les questions sont dans la ligne 3
        for idx, value in enumerate(header_row):
            if pd.notna(value):
                value_str = str(value).lower()
                if score_type == "product" and "1. product is 100%" in value_str:
                    return idx
                elif score_type == "service" and "1. 100% of the service" in value_str:
                    return idx
        raise ValueError(f"Impossible de trouver l'index de début pour {score_type}")
    
    def _create_evaluation(self, row: pd.Series, start_index: int) -> CsvEvaluation:
        """Crée les scores (local, eco, living) à partir d'une ligne du CSV.
        
        Args:
            row: Ligne du CSV avec les réponses Yes/No
            start_index: Index de la première colonne des scores
            
        Returns:
            Evaluation avec les scores et les labels
        """
        scores = []
        
        # Pour chaque groupe de score (local, eco, living)
        for group in range(3):
            # Index de base pour ce groupe
            base_index = start_index + (group * self.score_component_size)
            
            # Description du score (ligne 1)
            score_description = str(self.df.iloc[1, base_index])
            
            # Composants du score
            components = []
            
            for i in range(self.score_component_size):
                col_index = base_index + i
                # Description du composant (ligne 2)
                component_description = str(self.df.iloc[2, col_index])
                # Valeur du composant (ligne courante)
                value = row.iloc[col_index]
                components.append(ScoreComponent(
                    description=component_description,
                    value=str(value).strip() if pd.notna(value) else None
                ))
            
            scores.append(CsvScore(description=score_description, score_component=components))
        
        # Récupérer les 3 labels qui suivent tous les groupes de scores
        labels = []
        label_start_index = start_index + (3 * self.score_component_size)
        for i in range(3):
            label_index = label_start_index + i
            label = row.iloc[label_index]
            labels.append(str(label).strip() if pd.notna(label) else "")
        
        return CsvEvaluation(scores=scores, labels=labels)

    def parse_products(self) -> List[CsvProduct]:
        """Parse le CSV et retourne la liste des produits avec leurs scores"""
        products = []
        
        # Commencer à la ligne 4 (index 3) qui contient le premier produit
        for _, row in self.df.iloc[3:].iterrows():
            # Skip les lignes vides
            if pd.isna(row.iloc[3]):  # Name est dans la 4ème colonne
                continue
                
            # Créer le produit avec ses infos de base
            product = CsvProduct(
                name=str(row.iloc[3]).strip(),  # Name
                id=str(row.iloc[0]) if pd.notna(row.iloc[0]) else None,  # ID
                type=str(row.iloc[1]).strip() if pd.notna(row.iloc[1]) else None,  # Type
                product_evaluation=self._create_evaluation(row, self.product_score_index),
                service_evaluation=self._create_evaluation(row, self.service_score_index)
            )
            
            print(f"Produit traité avec succès : {product.name}")
            products.append(product)
            
        return products

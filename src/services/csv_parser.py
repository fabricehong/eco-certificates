import pandas as pd
from pathlib import Path
from typing import List
import copy

from models.eco_form import CsvProduct, CsvScore, ScoreComponent


class CsvParser:
    def __init__(self, csv_path: Path, score_component_size: int):
        """Initialize the CSV parser with the path to the CSV file."""
        self.csv_path = csv_path
        self.score_component_size = score_component_size
        self.df = pd.read_csv(self.csv_path)
        
        # Initialiser les index une seule fois
        self.product_score_index = self._find_score_index("product")
        self.service_score_index = self._find_score_index("service")
        
        # Initialiser les scores une seule fois
        self.product_score = self._create_score_template(self.product_score_index)
        self.service_score = self._create_score_template(self.service_score_index)

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

    def _read_score_description(self, start_index: int) -> str:
        """Lit la description complète d'un score"""
        description_row = self.df.iloc[1]  # Les descriptions sont dans la ligne 2
        return str(description_row.iloc[start_index]).strip()

    def _read_component_description(self, index: int) -> str:
        """Lit la description d'un composant de score"""
        component_row = self.df.iloc[2]  # Les questions sont dans la ligne 3
        return str(component_row.iloc[index]).strip()

    def _create_score_component(self, description: str) -> ScoreComponent:
        """Crée un composant de score avec sa description"""
        return ScoreComponent(description=description, value=None)

    def _create_score_template(self, start_index: int) -> CsvScore:
        """Crée un template de score avec sa description et ses composants"""
        score_description = self._read_score_description(start_index)
        
        components = []
        for i in range(self.score_component_size):
            component_description = self._read_component_description(start_index + i)
            components.append(self._create_score_component(component_description))
            
        return CsvScore(description=score_description, score_component=components)

    def _fill_score_values(self, score_template: CsvScore, row: pd.Series, start_index: int) -> CsvScore:
        """Remplit les valeurs d'un score pour un produit donné"""
        score = copy.deepcopy(score_template)
        
        for i, component in enumerate(score.score_component):
            value = row.iloc[start_index + i]
            component.value = str(value).strip() if pd.notna(value) else None
            
        return score

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
                product_scores=[self._fill_score_values(self.product_score, row, self.product_score_index)],
                service_scores=[self._fill_score_values(self.service_score, row, self.service_score_index)]
            )
            
            print(f"Produit traité avec succès : {product.name}")
            products.append(product)
            
        return products

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ScoreComponent:
    """Une colonne du CSV avec son en-tête et sa valeur"""
    description: str      # ex: "1. Product is 100% made of material extracted from European ground"
    value: str       # La valeur dans la colonne (ex: "Yes", "No", ou autre)

    def __str__(self) -> str:
        """Format le composant pour l'affichage"""
        return f"- {self.description}: {self.value if self.value else 'N/A'}"

@dataclass
class CsvScore:
    """Un groupe de colonnes formant un score"""
    description: str        # La description détaillée du score, ex: "The Product is Local ... and all following information in the cell such as examples."
    score_component: List[ScoreComponent]  # Les colonnes de questions/réponses pour ce score

    def __str__(self) -> str:
        """Format le score pour l'affichage"""
        result = [
            f"Description: {self.description}",
            "Components:"
        ]
        result.extend(str(component) for component in self.score_component)
        return "\n".join(result)

@dataclass
class CsvProduct:
    """Un produit du CSV avec ses scores"""
    name: str
    id: str
    type: str
    product_scores: List[CsvScore]
    service_scores: List[CsvScore]

    def __str__(self) -> str:
        """Format le produit pour l'affichage"""
        result = [
            f"Product: {self.name} (ID: {self.id})",
            f"Type: {self.type}\n"
        ]
        
        # Ajouter les scores produit
        result.append("Product Scores:")
        for score in self.product_scores:
            result.append(str(score))
        result.append("")
        
        # Ajouter les scores service
        result.append("Service Scores:")
        for score in self.service_scores:
            result.append(str(score))
            
        return "\n".join(result)

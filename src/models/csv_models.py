from dataclasses import dataclass, asdict
from typing import List, Optional
import json

@dataclass
class ScoreComponent:
    """Une colonne du CSV avec son en-tête et sa valeur"""
    description: str      # ex: "1. Product is 100% made of material extracted from European ground"
    value: str       # La valeur dans la colonne (ex: "Yes", "No", ou autre)


@dataclass
class CsvScore:
    """Un groupe de colonnes formant un score"""
    description: str        # La description détaillée du score, ex: "The Product is Local ... and all following information in the cell such as examples."
    score_component: List[ScoreComponent]  # Les colonnes de questions/réponses pour ce score

@dataclass
class CsvEvaluation:
    scores: List[CsvScore]
    labels: List[str]       # labels bio


@dataclass
class CsvProduct:
    """Un produit du CSV avec ses scores"""
    name: str
    id: Optional[str]
    type: Optional[str]
    product_evaluation: CsvEvaluation
    service_evaluation: CsvEvaluation

    def __str__(self) -> str:
        """Format le produit pour l'affichage"""
        product_dict = asdict(self)
        return json.dumps(product_dict, indent=2)

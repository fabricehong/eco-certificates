from dataclasses import dataclass, asdict
from typing import Optional, List
import json


@dataclass
class EvaluationCriterion:
    """Score d'un composant avec son nombre de réponses positives et le total."""
    description: str
    yes_count: int
    total_questions: int

    def __str__(self):
        """Format le score pour l'affichage"""
        return f"{self.yes_count}/{self.total_questions}"


@dataclass
class Evaluation:
    """Score d'un groupe avec ses composants."""
    local_evaluation: EvaluationCriterion
    ecofriendly_evaluation: EvaluationCriterion
    living_respect_evaluation: EvaluationCriterion
    values_found: bool
    labels: List[str]

    def __str__(self):
        """Format le score pour l'affichage"""
        return "\n".join(
            f"- Local: {self.local_evaluation}",
            f"- Eco-friendly: {self.ecofriendly_evaluation}",
            f"- Living Respect: {self.living_respect_evaluation}"
        )


@dataclass
class ScoreProduct:
    """Produit avec ses scores calculés."""
    name: str
    id: Optional[str]
    type: Optional[str]
    product_evaluation: Evaluation
    service_evaluation: Evaluation

    def __str__(self):
        """Format le produit pour l'affichage"""
        product_dict = asdict(self)
        return json.dumps(product_dict, indent=2)

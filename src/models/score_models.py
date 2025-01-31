from dataclasses import dataclass, asdict
from typing import Optional, List
import json


@dataclass
class ComponentScore:
    """Score d'un composant avec son nombre de réponses positives et le total."""
    yes_count: int
    total_questions: int

    def __str__(self):
        """Format le score pour l'affichage"""
        return f"{self.yes_count}/{self.total_questions}"


@dataclass
class Score:
    """Score d'un groupe avec ses composants."""
    local_score: ComponentScore
    ecofriendly_score: ComponentScore
    living_respect_score: ComponentScore
    values_found: bool
    labels: List[str]

    def __str__(self):
        """Format le score pour l'affichage"""
        return "\n".join(
            f"- Local: {self.local_score}",
            f"- Eco-friendly: {self.ecofriendly_score}",
            f"- Living Respect: {self.living_respect_score}"
        )


@dataclass
class ScoreProduct:
    """Produit avec ses scores calculés."""
    name: str
    id: Optional[str]
    type: Optional[str]
    product_scores: Score
    service_scores: Score

    def __str__(self):
        """Format le produit pour l'affichage"""
        product_dict = asdict(self)
        return json.dumps(product_dict, indent=2)

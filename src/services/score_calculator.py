from typing import List

from src.models.score_models import Evaluation, ScoreProduct, EvaluationCriterion
from src.models.csv_models import CsvProduct, CsvEvaluation


class ScoreCalculator:
    """Calculateur de scores pour les produits et services.
    
    Cette classe transforme les CsvProduct en ScoreProduct en calculant les scores
    à partir des réponses Yes/No du CSV.
    
    Pour chaque produit/service, on calcule 3 scores :
    1. Score Local : basé sur la localisation des activités en Europe
    2. Score Eco-friendly : basé sur l'impact environnemental
    3. Score Living Respect : basé sur le respect des personnes et des animaux
    
    Chaque score est calculé indépendamment à partir de son groupe de composants.
    Un composant avec réponse "Yes" ajoute 1 au score, "No" ou None n'ajoute rien.
    Le score final est le ratio de réponses "Yes" sur le nombre total de composants.
    """
    
    def __init__(self, component_size: int):
        """Initialise le calculateur avec la taille des composants"""
        self.max_score = component_size
        
    def calculate_evaluation_criterion(self, description: str, answers: List[str]) -> EvaluationCriterion:
        """Calcule le score d'un composant basé sur les réponses Yes/No"""
        yes_count = sum(1 for answer in answers if answer and answer.lower() == "yes")
        return EvaluationCriterion(description=description, yes_count=yes_count, total_questions=self.max_score)
    
    def calculate_score(self, evaluation: CsvEvaluation) -> Evaluation:
        """Transforme une liste de CsvScore en Score avec les calculs.
        
        On reçoit 3 CsvScore :
        - Local (index 0)
        - Eco-friendly (index 1)
        - Living Respect (index 2)
        """
        # Chaque CsvScore contient les composants pour son type
        local_csv_evaluation = evaluation.scores[0]
        eco_csv_evaluation = evaluation.scores[1]
        living_csv_evaluation = evaluation.scores[2]

        local_answers = [c.value for c in local_csv_evaluation.score_component]
        eco_answers = [c.value for c in eco_csv_evaluation.score_component]
        living_answers = [c.value for c in living_csv_evaluation.score_component]
        
        # Vérifier si au moins une valeur non-null est trouvée
        all_answers = local_answers + eco_answers + living_answers
        values_found = any(answer is not None for answer in all_answers)
        
        return Evaluation(
            local_evaluation=self.calculate_evaluation_criterion(local_csv_evaluation.description, local_answers),
            ecofriendly_evaluation=self.calculate_evaluation_criterion(eco_csv_evaluation.description, eco_answers),
            living_respect_evaluation=self.calculate_evaluation_criterion(living_csv_evaluation.description, living_answers),
            values_found=values_found,
            labels=[label for label in evaluation.labels if label is not None and label.strip() != ""]
        )
    
    def transform_product(self, csv_product: CsvProduct) -> ScoreProduct:
        """Transforme un CsvProduct en ScoreProduct avec les scores calculés"""
        return ScoreProduct(
            name=csv_product.name,
            id=csv_product.id,
            type=csv_product.type,
            product_evaluation=self.calculate_score(csv_product.product_evaluation),
            service_evaluation=self.calculate_score(csv_product.service_evaluation)
        )
    
    def transform_products(self, csv_products: List[CsvProduct]) -> List[ScoreProduct]:
        """Transforme une liste de CsvProduct en ScoreProduct"""
        return [self.transform_product(p) for p in csv_products]

class EcoCalculator:
    """Calculateur d'impact écologique simple pour la démonstration."""
    
    def __init__(self, base_impact: float = 1.0):
        self.base_impact = base_impact
        
    def calculate_impact(self, usage_hours: float, energy_efficiency: float) -> float:
        """Calcule l'impact écologique basé sur les heures d'utilisation et l'efficacité énergétique."""
        return self.base_impact * usage_hours * (1 / energy_efficiency)
    
    def get_eco_rating(self, impact: float) -> str:
        """Convertit l'impact en notation écologique (A à F)."""
        if impact < 1.0:
            return "A"
        elif impact < 2.0:
            return "B"
        elif impact < 3.0:
            return "C"
        elif impact < 4.0:
            return "D"
        elif impact < 5.0:
            return "E"
        else:
            return "F"

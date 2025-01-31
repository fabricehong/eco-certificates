from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont

from src.models.score_models import Evaluation


@dataclass
class ElementPosition:
    """Position d'un groupe de score sur le certificat.
    
    Args:
        x: Position x du premier symbole
        y: Position y du premier symbole
    """
    x: int
    y: int


class CertificateGenerator:
    """Générateur de certificats d'éco-score.
    
    Cette classe génère une image de certificat pour chaque produit,
    en affichant les scores sous forme de feuilles (actives/inactives).
    """
    
    def __init__(
        self,
        certificate_template: Path,
        active_leaf: Path,
        inactive_leaf: Path,
        local_position: ElementPosition,
        eco_position: ElementPosition,
        living_position: ElementPosition,
        leaf_spacing: int,
        leaf_width: int,
        label_position: ElementPosition,
        font_path: Path,
        font_size: int
    ):
        """Initialise le générateur avec les images et positions.
        
        Args:
            certificate_template: Chemin vers l'image de base du certificat
            active_leaf: Chemin vers l'image de feuille active
            inactive_leaf: Chemin vers l'image de feuille inactive
            local_position: Position des feuilles pour le score local
            eco_position: Position des feuilles pour le score eco-friendly
            living_position: Position des feuilles pour le score living respect
            leaf_spacing: Espacement entre les feuilles (en pixels)
            leaf_width: Largeur souhaitée pour les feuilles (la hauteur sera calculée pour garder le ratio)
            label_position: Position des labels sur le certificat
            font_path: Chemin vers la police à utiliser pour les labels
            font_size: Taille de la police en points
        """
        # Charger les images
        self.template = Image.open(certificate_template).convert('RGBA')
        
        # Charger les feuilles
        active = Image.open(active_leaf).convert('RGBA')
        inactive = Image.open(inactive_leaf).convert('RGBA')
        
        # Calculer la hauteur pour garder le ratio
        ratio = active.height / active.width
        leaf_height = int(leaf_width * ratio)
        
        # Redimensionner les feuilles en gardant le ratio
        self.active_leaf = active.resize((leaf_width, leaf_height))
        self.inactive_leaf = inactive.resize((leaf_width, leaf_height))
        
        # Positions des scores
        self.local_position = local_position
        self.eco_position = eco_position
        self.living_position = living_position
        
        # Espacement entre les feuilles
        self.leaf_spacing = leaf_spacing
        
        # Configuration des labels
        self.label_position = label_position
        self.font = ImageFont.truetype(str(font_path), font_size)
    
    def generate_certificate(self, score: Evaluation, output_path: Path) -> None:
        """Génère le certificat pour un score.
        
        Args:
            score: Score à représenter sur le certificat
            output_path: Chemin où sauvegarder l'image générée
        """
        # Créer une copie de l'image template
        certificate = self.template.copy()
        
        # Dessiner les scores
        self._draw_score(certificate, score.local_evaluation, self.local_position)
        self._draw_score(certificate, score.ecofriendly_evaluation, self.eco_position)
        self._draw_score(certificate, score.living_respect_evaluation, self.living_position)
        
        # Dessiner les labels s'il y en a
        if score.labels:
            draw = ImageDraw.Draw(certificate)
            labels_text = ", ".join(score.labels)
            draw.text(
                (self.label_position.x, self.label_position.y),
                labels_text,
                font=self.font,
                fill=(0, 0, 0)  # Noir
            )
        
        # Sauvegarder l'image
        certificate.save(output_path, 'PNG')
    
    def _draw_score(self, certificate: Image, score: 'ComponentScore', position: ElementPosition) -> None:
        """Dessine un score sous forme de feuilles.
        
        Args:
            certificate: Image du certificat
            score: Score à représenter
            position: Position où dessiner les feuilles
        """
        # Pour chaque feuille possible
        for i in range(score.total_questions):
            # Calculer la position x de cette feuille
            x = position.x + (i * self.leaf_spacing)
            
            # Choisir l'image de feuille selon le score
            leaf = self.active_leaf if i < score.yes_count else self.inactive_leaf
            
            # Créer un masque à partir du canal alpha
            mask = leaf.split()[3] if len(leaf.split()) == 4 else None
            
            # Coller la feuille sur le certificat
            certificate.paste(leaf, (x, position.y), mask)

from pathlib import Path
import sys
from dataclasses import asdict
import json

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

from services.csv_parser import CsvParser
from services.score_calculator import ScoreCalculator
from services.certificate_generator import CertificateGenerator, ElementPosition


def main():
    """Point d'entrée principal."""
    # Créer le parser et le calculateur
    parser = CsvParser(Path("input/product and service form - small.csv"), score_component_size=5)
    calculator = ScoreCalculator(component_size=5)
    
    # Configurer le générateur de certificats
    x = 150
    generator = CertificateGenerator(
        certificate_template=Path("images/certificate.png"),
        active_leaf=Path("images/active-leave.png"),
        inactive_leaf=Path("images/unactive-leave.png"),
        # Positions des scores
        local_position=ElementPosition(x=x, y=820),
        eco_position=ElementPosition(x=x, y=1100),
        living_position=ElementPosition(x=x, y=1350),
        # Positions des descriptions
        local_description_position=ElementPosition(x=x, y=740),
        eco_description_position=ElementPosition(x=x, y=1000),
        living_description_position=ElementPosition(x=x, y=1270),
        # Configuration des feuilles
        leaf_spacing=100,  # Espacement entre les feuilles
        leaf_width=90,     # Largeur des feuilles, la hauteur sera calculée pour garder le ratio
        # Configuration des labels
        label_position=ElementPosition(x=350, y=1700),
        font_path=Path("fonts/Arial Bold.ttf"),
        bold_font_path=Path("fonts/Arial Bold.ttf"),
        font_size=60,  # Taille pour les labels
        description_font_size=50  # Taille pour les descriptions
    )
    
    # Créer le dossier output s'il n'existe pas
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # Lire et traiter les produits
    csv_products = parser.parse_products()
    products_count = 0
    
    # Pour chaque produit
    for csv_product in csv_products:
        # Calculer les scores
        product = calculator.transform_product(csv_product)
        print(f"Produit traité avec succès : {product.name}")
        products_count += 1
        
        # Générer le certificat avec le score approprié (product ou service)
        score = (product.product_evaluation if product.product_evaluation.values_found 
                else product.service_evaluation)
        
        # Générer le nom du fichier
        filename = product.name.lower().replace(" ", "_") + "_certificate.png"
        output_path = output_dir / filename
        
        # Générer le certificat
        generator.generate_certificate(score, output_path)
    
    # Afficher les détails
    print("\nDétails des produits avec scores :")
    print("=" * 50)
    for csv_product in csv_products:
        product = calculator.transform_product(csv_product)
        print(product)
        filename = product.name.lower().replace(" ", "_") + "_certificate.png"
        print(f"Certificat généré : output/{filename}")
        print("=" * 50)
    
    print(f"\nNombre de produits traités : {products_count}")


if __name__ == "__main__":
    main()
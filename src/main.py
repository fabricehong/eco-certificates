from pathlib import Path
import sys

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

from services.csv_parser import CsvParser

def main():
    # Chemin vers le fichier CSV
    csv_path = Path("input/product and service form.csv")
    
    # Créer le parser avec 5 composants par score
    parser = CsvParser(csv_path, score_component_size=5)
    
    # Parser les produits
    products = parser.parse_products()
    
    # Afficher les résultats
    print(f"\nDétails des produits :")
    print("=" * 50)
    for product in products:
        print(str(product))
        print("=" * 50)
    
    print(f"\nNombre de produits trouvés : {len(products)}")

if __name__ == "__main__":
    main()
import os
import shutil
from pathlib import Path

def copy_fonts():
    """Copie les fonts Arial depuis le système vers le projet."""
    # Créer le dossier fonts à la racine du projet
    project_root = Path(__file__).parent.parent
    fonts_dir = project_root / "fonts"
    fonts_dir.mkdir(exist_ok=True)
    
    # Fonts à copier avec leurs chemins possibles
    fonts_to_copy = {
        "Arial Bold.ttf": [
            "/Library/Fonts/Arial Bold.ttf",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
        ],
        "Arial.ttf": [
            "/Library/Fonts/Arial.ttf",
            "/System/Library/Fonts/Supplemental/Arial.ttf"
        ]
    }
    
    # Copier chaque font
    for dest, sources in fonts_to_copy.items():
        found = False
        for source in sources:
            if os.path.exists(source):
                shutil.copy2(source, fonts_dir / dest)
                print(f"Font copiée depuis {source}")
                found = True
                break
        if not found:
            print(f"Font non trouvée: {dest}")
            print(f"Chemins cherchés: {', '.join(sources)}")

if __name__ == "__main__":
    copy_fonts()

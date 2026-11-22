"""
Pagination : traduction d'une adresse logique en adresse physique.
La table des pages associe un numéro de page à un numéro de cadre.
"""

# Définir la taille d'une page à 256 octets
PAGE_SIZE = 256


class PageFault(Exception):
    """Exception déclenchée lorsqu'une page est absente de la mémoire."""

    def __init__(self, page):
        # Afficher un message indiquant le numéro de la page absente
        super().__init__(f"Défaut de page : page {page} absente")

        # Conserver le numéro de la page qui a provoqué l'erreur
        self.page = page


def translate(adresse, table):
    # Calculer le numéro de page à partir de l'adresse logique
    page = adresse // 256

    # Calculer le déplacement à l'intérieur de la page
    decalage = adresse % 256

    # Chercher le cadre correspondant à la page dans la table
    cadre = table.get(page)

    # Vérifier si la page est absente de la mémoire
    if cadre is None:
        # Déclencher une exception PageFault
        raise PageFault(page)

    # Calculer et retourner l'adresse physique
    return cadre * 256 + decalage
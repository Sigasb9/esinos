"""
Pagination : traduction d'une adresse logique en adresse physique.
La table des pages associe un numéro de page à un numéro de cadre.
"""

PAGE_SIZE = 512


class PageFault(Exception):
    """Levée quand la page demandée n'est pas en mémoire."""

    def __init__(self, page):
        super().__init__(f"Défaut de page : page {page} absente")
        self.page = page


def translate(adresse_logique, table_pages):
    """
    Renvoie l'adresse physique correspondant à adresse_logique.
    table_pages : dict {page: cadre} (cadre None ou page absente = pas en mémoire).
    Lève PageFault(page) si la page n'est pas chargée.
    """
    page = adresse_logique // PAGE_SIZE
    decalage = adresse_logique % PAGE_SIZE
    cadre = table_pages.get(page)
    if cadre is None:
        raise PageFault(page)
    return cadre * PAGE_SIZE + decalage

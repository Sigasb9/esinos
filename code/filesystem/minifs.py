"""
Mini système de fichiers (bonus) : disque de n_blocs blocs de BLOCK_SIZE caractères,
allocation non contiguë, table des inodes {nom: {"taille", "blocs"}}.
"""

BLOCK_SIZE = 4


class MiniFS:
    """Disque simulé en mémoire."""

    def __init__(self, n_blocs=16):
        """Crée un disque vide : blocs à None (libres) et table des inodes vide."""
        self.blocs = [None] * n_blocs
        self.inodes = {}

    def creer(self, nom, contenu):
        """Découpe contenu en blocs de BLOCK_SIZE et les écrit dans des blocs libres."""
        # TODO (bonus, à attribuer) :
        # 1. erreur si nom existe déjà
        # 2. morceaux = [contenu[i:i+BLOCK_SIZE] ...] ; erreur si pas assez de blocs libres
        # 3. écrire chaque morceau dans un bloc libre, noter les indices
        # 4. self.inodes[nom] = {"taille": len(contenu), "blocs": indices}
        raise NotImplementedError

    def lire(self, nom):
        """Renvoie le contenu du fichier en recollant ses blocs."""
        # TODO (bonus, à attribuer) : erreur si absent, sinon "".join des blocs de l'inode
        raise NotImplementedError

    def supprimer(self, nom):
        """Libère les blocs du fichier et retire son inode."""
        # TODO (bonus, à attribuer) : remettre ses blocs à None, del self.inodes[nom]
        raise NotImplementedError

    def afficher(self):
        """Affiche la table des inodes et la carte des blocs (libre / occupé)."""
        # TODO (bonus, à attribuer) : print de chaque inode puis d'une ligne type "[X][.][X]..."
        raise NotImplementedError

"""
Définition d'un processus et jeu de données d'exemple.
Utilisé par tous les ordonnanceurs et par les tests.
"""
from dataclasses import dataclass


@dataclass
class Process:
    """Un processus : identifiant, date d'arrivée, durée CPU et priorité (petit = prioritaire)."""
    pid: str
    arrival: int
    burst: int
    priority: int = 0


# Exemple du cours : P1(0,5,3) P2(1,3,2) P3(2,8,1) P4(3,6,4)
EXEMPLE = [
    Process("P1", 0, 5, 3),
    Process("P2", 1, 3, 2),
    Process("P3", 2, 8, 1),
    Process("P4", 3, 6, 4),
]

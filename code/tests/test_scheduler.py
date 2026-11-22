
"""
Tests des ordonnanceurs et des métriques sur l'exemple du cours.
Lancer : python -m unittest discover -s code/tests -t code -v
"""
import unittest

from process import EXEMPLE
from scheduler.fcfs import fcfs
from scheduler.sjf import sjf
from scheduler.priority import priority
from scheduler.rr import rr
from scheduler import metrics


class TestOrdonnanceurs(unittest.TestCase):
    """Moyennes attente / séjour de référence."""

    def verifier(self, gantt, attente, sejour):
        """Compare les moyennes calculées aux valeurs attendues."""
        _, att, sej = metrics.calculer(EXEMPLE, gantt)
        self.assertAlmostEqual(att, attente)
        self.assertAlmostEqual(sej, sejour)

    def test_fcfs(self):
        self.assertEqual(fcfs(EXEMPLE), [("P1", 0, 5), ("P2", 5, 8), ("P3", 8, 16), ("P4", 16, 22)])
        self.verifier(fcfs(EXEMPLE), 5.75, 11.25)

    def test_sjf(self):
        self.verifier(sjf(EXEMPLE), 5.25, 10.75)

    def test_priority(self):
        self.verifier(priority(EXEMPLE), 7.00, 12.50)

    def test_rr_q4(self):
        attendu = [("P1", 0, 4), ("P2", 4, 7), ("P3", 7, 11), ("P4", 11, 15),
                   ("P1", 15, 16), ("P3", 16, 20), ("P4", 20, 22)]
        self.assertEqual(rr(EXEMPLE, 4), attendu)
        self.verifier(rr(EXEMPLE, 4), 9.25, 14.75)

    # Nouveau test1 vérifier FCFS avec un seul processus
    def test_fcfs_un_seul_processus(self):
        processus = [{"pid": "P1", "arrivee": 0, "duree": 5}]
        attendu = [("P1", 0, 5)]
        self.assertEqual(fcfs(processus), attendu)

    # Nouveau test2 vérifier Round Robin avec un quantum de 1
    def test_rr_quantum_un(self):
        processus = [{"pid": "P1", "arrivee": 0, "duree": 2}]
        attendu = [("P1", 0, 1), ("P1", 1, 2)]
        self.assertEqual(rr(processus, 1), attendu)


if __name__ == "__main__":
    unittest.main()

"""
Tests de la mémoire : remplacement de pages, pagination, TLB.
Lancer : python -m unittest discover -s code/tests -t code -v
"""
import unittest

from memory.fifo import fifo
from memory.lru import lru
from memory.optimal import optimal
from memory.paging import translate, PageFault, PAGE_SIZE
from memory.tlb import taux_de_succes_tlb, eat

REFS = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
BELADY = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]


class TestFIFO(unittest.TestCase):
    def test_reference(self):
        self.assertEqual(fifo(REFS, 3)["faults"], 15)

    def test_belady(self):
        self.assertEqual(fifo(BELADY, 3)["faults"], 9)
        self.assertEqual(fifo(BELADY, 4)["faults"], 10)


class TestLRU(unittest.TestCase):
    def test_reference(self):
        self.assertEqual(lru(REFS, 3)["faults"], 12)


class TestOptimal(unittest.TestCase):
    def test_reference(self):
        self.assertEqual(optimal(REFS, 3)["faults"], 9)

    def test_steps(self):
        res = optimal(REFS, 3)
        self.assertEqual(len(res["steps"]), len(REFS))
        self.assertEqual(res["steps"][3], {"page": 2, "frames": [2, 0, 1], "fault": True})


class TestPaging(unittest.TestCase):
    def test_traduction(self):
        self.assertEqual(PAGE_SIZE, 512)
        self.assertEqual(translate(1030, {2: 5}), 5 * 512 + 6)

    def test_defaut(self):
        with self.assertRaises(PageFault) as ctx:
            translate(600, {0: 3})
        self.assertEqual(ctx.exception.page, 1)


class TestTLB(unittest.TestCase):
    def test_taux(self):
        self.assertAlmostEqual(taux_de_succes_tlb([1, 2, 1, 2], 2), 0.5)
        self.assertAlmostEqual(taux_de_succes_tlb([1, 2, 3, 1], 2), 0.0)

    def test_eat(self):
        self.assertAlmostEqual(eat(0.8, 20, 100), 140)


if __name__ == "__main__":
    unittest.main()

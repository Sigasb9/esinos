# esinos

Noyau d'OS simulé en Python 3 (cours Systèmes d'Exploitation, UIR).
Ordonnancement, mémoire (pagination, remplacement de pages, TLB), mini système de fichiers (bonus).

Python 3.10+, bibliothèque standard uniquement.

## Lancer

```bash
python code/main.py
```

## Tests

```bash
python -m unittest discover -s code/tests -t code -v
```

## Équipe

- Sami : process, gantt, main, paging, optimal, tlb, intégration
- Ilias : rr, priority, lru
- Adam : fcfs, sjf, metrics, rapport
- Yassine : fifo, tests, README, vidéo

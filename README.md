
# Projet Systèmes d'exploitation

## 1. Présentation

Ce projet consiste à simuler plusieurs mécanismes des systèmes d'exploitation avec Python.

Il permet de comprendre :
- L'ordonnancement des processus.
- La gestion de la mémoire.
- Le remplacement des pages.
- La pagination.
- Le diagramme de Gantt.

## 2. Technologies utilisées

- Python 3
- Git et GitHub
- Visual Studio Code
- Unittest

## 3. Installation

Cloner le projet :

```bash
git clone https://github.com/Sigasb9/esinos-os-project.git
cd esinos-os-project
```

Vérifier Python :

```bash
python --version
```

## 4. Utilisation

Lancer le programme :

```bash
python code/main.py
```

## 5. Fonctionnalités

### Ordonnancement
- FCFS : premier arrivé, premier servi.
- SJF : processus le plus court en premier.
- Priority : exécution selon la priorité.
- Round Robin : chaque processus reçoit un quantum de temps.

### Gestion de la mémoire
- FIFO : remplace la page la plus ancienne.
- LRU : remplace la page la moins récemment utilisée.
- Optimal : remplace la page utilisée le plus tard.

### Autres fonctionnalités
- Pagination : traduction des adresses logiques en adresses physiques.
- Gantt : visualisation de l'exécution des processus.
- TLB : amélioration de l'accès à la mémoire.

## 6. Exécution des tests

Lancer tous les tests :

```bash
python -m unittest discover -s code/tests -t code -v
```

Les tests vérifient le bon fonctionnement des algorithmes et des fonctionnalités du projet.

## 7. Répartition du travail

**Yassine :**
- Implémentation de FIFO.
- Pagination et diagramme de Gantt : commentaires et tests.
- Ajout de tests dans `test_memory.py` et `test_scheduler.py`.
- Rédaction du README.
- Participation à la vidéo de démonstration.

## 8. Conclusion

Ce projet permet de mieux comprendre les mécanismes des systèmes d'exploitation grâce à des simulations en Python. Il permet également de développer des compétences en programmation et en travail collaboratif avec Git et GitHub.

## Équipe

- Sami : process, main, optimal, tlb, intégration
- Ilias : rr, priority, lru
- Adam : fcfs, sjf, metrics, rapport
- Yassine : fifo, paging, gantt, tests, README, vidéo

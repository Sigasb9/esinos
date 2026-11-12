"""
Point d'entrée d'esinos : menu console qui relie ordonnanceur, mémoire et fichiers.
Lancer depuis la racine : python code/main.py
"""
from process import Process, EXEMPLE
import gantt
from scheduler.fcfs import fcfs
from scheduler.sjf import sjf
from scheduler.priority import priority
from scheduler.rr import rr
from scheduler import metrics
from memory.fifo import fifo
from memory.lru import lru
from memory.optimal import optimal
from memory import paging, tlb
from filesystem.minifs import MiniFS


def lire_entier(message, mini=None, maxi=None):
    """Demande un entier jusqu'à obtenir une saisie valide (jamais de crash sur 'abc')."""
    while True:
        texte = input(message).strip()
        try:
            n = int(texte)
        except ValueError:
            print("  Entrez un nombre entier.")
            continue
        if (mini is not None and n < mini) or (maxi is not None and n > maxi):
            print(f"  Valeur entre {mini} et {maxi} attendue.")
            continue
        return n


def lire_refs():
    """Demande une suite de pages séparées par des espaces (ex : 7 0 1 2)."""
    while True:
        texte = input("Références (vide = exemple du cours) : ").strip()
        if not texte:
            return [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
        try:
            return [int(x) for x in texte.split()]
        except ValueError:
            print("  Uniquement des entiers séparés par des espaces.")


def lire_processus():
    """Renvoie la liste d'exemple ou une liste saisie par l'utilisateur."""
    n = lire_entier("Nombre de processus (0 = exemple du cours) : ", 0, 20)
    if n == 0:
        return list(EXEMPLE)
    procs = []
    for i in range(1, n + 1):
        print(f"P{i} :")
        arrivee = lire_entier("  arrivée : ", 0)
        burst = lire_entier("  burst : ", 1)
        prio = lire_entier("  priorité : ", 0)
        procs.append(Process(f"P{i}", arrivee, burst, prio))
    return procs


def menu_ordonnanceur():
    """Choix d'un algorithme, puis affichage du Gantt et des métriques."""
    procs = lire_processus()
    print("1 FCFS  2 SJF  3 Priorité  4 Round Robin")
    choix = lire_entier("Algorithme : ", 1, 4)
    try:
        if choix == 1:
            g = fcfs(procs)
        elif choix == 2:
            g = sjf(procs)
        elif choix == 3:
            g = priority(procs)
        else:
            g = rr(procs, lire_entier("Quantum : ", 1))
        gantt.afficher(g)
        gantt.afficher_tableau(*metrics.calculer(procs, g))
    except NotImplementedError:
        print("  Pas encore implémenté (TODO de l'équipe).")


def afficher_etapes(nom, res):
    """Affiche le déroulé d'un algorithme de remplacement de pages."""
    print(f"--- {nom} ---")
    for s in res["steps"]:
        print(f"  page {s['page']:>3} -> {s['frames']}{'  défaut' if s['fault'] else ''}")
    print(f"  Total défauts : {res['faults']}")


def menu_memoire():
    """Remplacement de pages, traduction d'adresse et TLB."""
    print("1 FIFO  2 LRU  3 Optimal  4 Comparer  5 Traduire une adresse  6 TLB / EAT")
    choix = lire_entier("Choix : ", 1, 6)
    try:
        if choix <= 4:
            refs = lire_refs()
            n = lire_entier("Nombre de cadres : ", 1)
            algos = {1: [("FIFO", fifo)], 2: [("LRU", lru)], 3: [("Optimal", optimal)],
                     4: [("FIFO", fifo), ("LRU", lru), ("Optimal", optimal)]}[choix]
            for nom, f in algos:
                res = f(refs, n)
                if choix == 4:
                    print(f"  {nom:<8} : {res['faults']} défauts")
                else:
                    afficher_etapes(nom, res)
        elif choix == 5:
            table = {0: 5, 1: 2, 2: None, 3: 7}
            print(f"Table des pages (page -> cadre) : {table}, PAGE_SIZE = {paging.PAGE_SIZE}")
            adr = lire_entier("Adresse logique : ", 0)
            try:
                print(f"  Adresse physique : {paging.translate(adr, table)}")
            except paging.PageFault as e:
                print(f"  {e}")
        else:
            refs = lire_refs()
            taille = lire_entier("Taille de la TLB : ", 1)
            h = tlb.taux_de_succes_tlb(refs, taille)
            t_tlb = lire_entier("Temps TLB (ns) : ", 0)
            t_mem = lire_entier("Temps mémoire (ns) : ", 0)
            print(f"  Taux de succès : {h:.2%}   EAT : {tlb.eat(h, t_tlb, t_mem):.2f} ns")
    except NotImplementedError:
        print("  Pas encore implémenté (TODO de l'équipe).")


def menu_fichiers(fs):
    """Mini système de fichiers (bonus)."""
    print("1 Créer  2 Lire  3 Supprimer  4 Afficher")
    choix = lire_entier("Choix : ", 1, 4)
    try:
        if choix == 1:
            fs.creer(input("Nom : ").strip(), input("Contenu : "))
        elif choix == 2:
            print(f"  {fs.lire(input('Nom : ').strip())}")
        elif choix == 3:
            fs.supprimer(input("Nom : ").strip())
        else:
            fs.afficher()
    except NotImplementedError:
        print("  Pas encore implémenté (TODO de l'équipe).")
    except Exception as e:
        print(f"  Erreur : {e}")


def main():
    """Boucle principale du menu."""
    fs = MiniFS()
    while True:
        print("\n=== esinos ===")
        print("1 Ordonnanceur  2 Mémoire  3 Fichiers (bonus)  4 Quitter")
        choix = lire_entier("Choix : ", 1, 4)
        if choix == 1:
            menu_ordonnanceur()
        elif choix == 2:
            menu_memoire()
        elif choix == 3:
            menu_fichiers(fs)
        else:
            print("Au revoir.")
            break


if __name__ == "__main__":
    main()

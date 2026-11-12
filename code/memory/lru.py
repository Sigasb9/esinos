"""
Remplacement de page LRU : on retire la page utilisée il y a le plus longtemps.
"""


def lru(refs, n_cadres):
    """Simule LRU. Renvoie {"faults": int, "steps": [{"page", "frames", "fault"}]}."""
    # TODO (Ilias) :
    # 1. cadres = [] ; dernier = {} (page -> dernier indice d'utilisation) ; faults = 0 ; steps = []
    # 2. pour i, page dans enumerate(refs) :
    #    - si absente : faults += 1 ; si cadres pleins, victime = page de plus petit dernier[...]
    #      (la remplacer à la même position), sinon ajouter
    #    - dernier[page] = i
    #    - steps.append({"page": page, "frames": list(cadres), "fault": absente})
    # 3. renvoyer {"faults": faults, "steps": steps}
    raise NotImplementedError

"""
Remplacement de page LRU : on retire la page utilisée il y a le plus longtemps.
"""


def lru(refs, n_cadres):
    """Simule LRU. Renvoie {"faults": int, "steps": [{"page", "frames", "fault"}]}.

    refs : liste de pages référencées
    n_cadres : nombre de cadres disponibles
    """
    # 1. cadres = [] ; dernier = {} ; faults = 0 ; steps = []
    cadres = []
    dernier = {}  # page -> dernier indice d'utilisation
    faults = 0
    steps = []

    # 2. pour i, page dans enumerate(refs)
    for i, page in enumerate(refs):
        absente = page not in cadres

        if absente:
            faults += 1
            if len(cadres) < n_cadres:
                cadres.append(page)
            else:
                # victime = page dont le dernier usage est le plus ancien
                victime = min(cadres, key=lambda p: dernier[p])
                cadres[cadres.index(victime)] = page

        dernier[page] = i
        steps.append({"page": page, "frames": list(cadres), "fault": absente})

    # 3. renvoyer le résultat
    return {"faults": faults, "steps": steps}

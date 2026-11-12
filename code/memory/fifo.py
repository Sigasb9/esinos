"""
Remplacement de page FIFO : on retire la page chargée depuis le plus longtemps.
Sert aussi à montrer l'anomalie de Belady.
"""


def fifo(refs, n_cadres):
    """Simule FIFO. Renvoie {"faults": int, "steps": [{"page", "frames", "fault"}]}."""
    # TODO (Yassine) :
    # 1. cadres = [] ; ordre = deque() (ordre de chargement) ; faults = 0 ; steps = []
    # 2. pour chaque page :
    #    - si absente : faults += 1 ; si cadres pleins, retirer ordre.popleft()
    #      (remplacer à la même position dans cadres), sinon ajouter
    #    - steps.append({"page": page, "frames": list(cadres), "fault": absente})
    # 3. renvoyer {"faults": faults, "steps": steps}
    raise NotImplementedError

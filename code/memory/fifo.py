"""
Remplacement de page FIFO : on retire la page chargée depuis le plus longtemps.
Sert aussi à montrer l'anomalie de Belady.
"""


def fifo(refs, n_cadres):
    """Simule FIFO. Renvoie {"faults": int, "steps": [{"page", "frames", "fault"}]}."""
    # TODO (Yassine) :
    cadres = []                                    
    ordre = deque()                                
    faults = 0
    steps = []
    for page in refs:
        absente = page not in cadres
        if absente:
            faults += 1
            if len(cadres) < n_cadres:             
                cadres.append(page)
            else:                                 
                victime = ordre.popleft()
                cadres[cadres.index(victime)] = page  
            ordre.append(page)
        steps.append({"page": page, "frames": list(cadres), "fault": absente})
    return {"faults": faults, "steps": steps}


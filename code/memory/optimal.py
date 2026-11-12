"""
Remplacement de page optimal (OPT / Belady) : on retire la page
dont la prochaine utilisation est la plus lointaine (ou jamais).
"""


def optimal(refs, n_cadres):
    """Simule OPT. Renvoie {"faults": int, "steps": [{"page", "frames", "fault"}]}."""
    cadres = []
    steps = []
    faults = 0
    for i, page in enumerate(refs):
        fault = page not in cadres
        if fault:
            faults += 1
            if len(cadres) < n_cadres:
                cadres.append(page)
            else:
                futur = refs[i + 1:]
                # distance jusqu'à la prochaine utilisation (infini si jamais)
                def prochaine(p):
                    return futur.index(p) if p in futur else float("inf")
                victime = max(cadres, key=prochaine)
                cadres[cadres.index(victime)] = page
        steps.append({"page": page, "frames": list(cadres), "fault": fault})
    return {"faults": faults, "steps": steps}

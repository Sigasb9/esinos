"""
Ordonnancement SJF (plus court job d'abord), non préemptif.
Renvoie un Gantt : liste de (pid, debut, fin).
"""


def sjf(procs):
    """Choisit à chaque fin de processus le plus court parmi ceux arrivés. Renvoie le Gantt."""
    # TODO (Adam)
    restants = list(procs)                        # copie : on ne modifie pas la liste d'origine
    temps = 0                                      # horloge courante
    gantt = []
    while restants:                                # tant qu'il reste des processus à exécuter
        # "prêts" = déjà arrivés à l'instant `temps` (ils attendent le CPU)
        prets = [p for p in restants if p.arrival <= temps]   # déjà arrivés
        if not prets:                              # aucun prêt : IDLE jusqu'à la prochaine arrivée
            prochaine = min(p.arrival for p in restants)
            gantt.append(("IDLE", temps, prochaine))
            temps = prochaine
            continue                               # on recommence : maintenant il y a un prêt
        # SJF : on compare les burst. En cas d'égalité, celui arrivé le plus tôt passe d'abord.
        p = min(prets, key=lambda p: (p.burst, p.arrival))   # le plus court (égalité : le plus tôt arrivé)
        gantt.append((p.pid, temps, temps + p.burst))        # il tourne jusqu'au bout (non préemptif)
        temps += p.burst
        restants.remove(p)                         # terminé : on le retire de la liste
    return gantt

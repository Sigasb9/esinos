"""
TLB (cache de traduction) : taux de succès simulé et temps d'accès effectif (EAT).
La TLB est gérée en LRU.
"""


def taux_de_succes_tlb(refs, taille):
    """Simule une TLB LRU de `taille` entrées sur la suite de pages refs. Renvoie le taux de succès (0..1)."""
    if not refs:
        return 0.0
    tlb = []
    succes = 0
    for page in refs:
        if page in tlb:
            succes += 1
            tlb.remove(page)
        elif len(tlb) >= taille:
            tlb.pop(0)  # la plus anciennement utilisée
        tlb.append(page)
    return succes / len(refs)


def eat(h, t_tlb, t_mem):
    """Temps d'accès effectif : h·(t_tlb+t_mem) + (1−h)·(t_tlb+2·t_mem)."""
    return h * (t_tlb + t_mem) + (1 - h) * (t_tlb + 2 * t_mem)

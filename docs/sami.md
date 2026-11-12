# Sami — Chef de projet, architecture, mémoire, intégration

Tu es chef de projet : ton rôle est que **tout le monde** avance. Tu es aussi celui qui fusionne.

**Mes fichiers :** `process.py`, `gantt.py`, `main.py`, `code/memory/paging.py`, `code/memory/optimal.py`, `code/memory/tlb.py`, `code/filesystem/minifs.py` (bonus)
**Règle :** je modifie uniquement mes fichiers. Pour toucher à ceux d'un autre, je demande d'abord.
**Soutenance :** 15 min, le prof tire 4 cartes au hasard (2 code + 2 concept), sur **tout** le projet. Absent = 0.

---

## 1. Installation (une seule fois)
- [ ] Compte GitHub créé, pseudo envoyé à Sami, invitation **acceptée** (mail ou notifications GitHub)
- [ ] **Git for Windows** installé (git-scm.com) — ou **GitHub Desktop** (desktop.github.com), plus simple (boutons)
- [ ] **Python 3** installé (cocher « Add Python to PATH »), test : `python --version`
- [ ] **VS Code** installé
- [ ] Git sait qui tu es (terminal, une fois) :
```
git config --global user.name "Sami NOM"
git config --global user.email "email-de-ton-compte-github"
```
> Important : le prof voit **qui a commit quoi**. Commit toujours avec ton compte.

## 2. Télécharger le projet depuis GitHub (une seule fois)
**Terminal :**
```
git clone https://github.com/Sigasb9/esinos-os-project.git
cd esinos-os-project
code .
```
**GitHub Desktop :** `File > Clone repository` → onglet *URL* → colle le lien → *Clone*. Puis `Repository > Open in Visual Studio Code`.

**Récupérer le travail des autres (à chaque début de session) :**
```
git checkout main
git pull
```
GitHub Desktop : branche `main` puis bouton **Fetch origin / Pull origin**.

**Tester que tout marche :**
```
python code/main.py
python -m unittest discover -s code/tests -t code -v
```
(les tests de fichiers pas encore codés échouent avec `NotImplementedError` : normal)

---

## 3. Commit et envoyer son travail
**Une tâche = une branche. Jamais de commit direct sur `main`.**

**Terminal :**
```
git checkout -b feature/paging      # crée ta branche (1 fois)
# ... tu codes ...
git add .
git commit -m "feat: pagination et traduction d'adresse"
git push -u origin feature/paging
```
**GitHub Desktop :** `Current branch > New branch` → nom `feature/paging` → tu codes → en bas à gauche écris le message → **Commit to feature/paging** → **Publish branch** (ensuite : **Push origin**).

**Fin de tâche :** sur github.com, bouton vert **Compare & pull request** → 2 lignes (ce que j'ai fait / comment tester) → **Create pull request** → préviens Sami. Il relit et fusionne.

Messages de commit : `feat:` nouveau code · `fix:` correction · `docs:` documentation.
**Au moins 1 commit par session de travail.** Conflit (`<<<<<<<` dans un fichier) ? Ne force rien, appelle Sami. Perdu ? `git status`.

---

## 4. Mes tâches
### Tâche 0 — Mettre le dépôt en place (en premier)
1. Crée le dépôt public `esinos-os-project` sur GitHub (avec `.gitignore` Python).
2. Dans le dossier `esinos/` généré par Claude Code : `git remote add origin https://github.com/Sigasb9/esinos-os-project.git` puis `git push -u origin main` (ou *Publish repository* dans GitHub Desktop).
3. `Settings > Collaborators` : ajoute Ilias, Adam, Yassine.
4. `Settings > Branches > Add rule` sur `main` : exiger une pull request avant fusion.
5. Envoie le lien à l'équipe + leurs fichiers `guides/*.md`.
> `CLAUDE.md` est dans le dossier parent, hors du dépôt : copie-le dans `esinos/` si tu veux le versionner.
**Résultat attendu :** les 3 coéquipiers peuvent cloner et pousser une branche.

### Tâche 1 — Mes fichiers déjà codés (à comprendre ligne par ligne)
`process.py` (dataclass `Process`, `EXEMPLE`), `gantt.py`, `main.py` (menu, `lire_entier`), `paging.py`, `optimal.py`, `tlb.py` (géré en **LRU**).

### Tâche 2 — Vérifier mes résultats
| Quoi | Résultat attendu |
|---|---|
| `translate(1000, {0: 2, 3: 5})` (pages de 256 o) | **1512** (adresse 600 → page 2 absente → `PageFault`) |
| Optimal, 3 cadres, refs du TD | **9 défauts** |
| `eat(0.8, 20, 100)` | **140 ns** |
| `taux_de_succes_tlb([1,2,1,3,1,2], 2)` | **1/6** |

### Tâche 3 — Relire et fusionner les pull requests (toute la durée)
Avant de fusionner : `git pull`, `git checkout <branche>`, lance `python -m unittest discover -s code/tests -t code -v`, puis *Merge*. Vérifie le **format de retour** de chaque fonction (voir `CLAUDE.md`), surtout `metrics.calculer`.

### Tâche 4 — Intégration et gel du code
`python code/main.py` fonctionne avec tous les menus, tous les tests passent, plus aucun `NotImplementedError`. Après le gel : plus de code, seulement rapport, vidéo, répétitions.

### Tâche 5 — Bonus (si tout est fusionné)
Compléter `minifs.py` (`creer`, `lire`, `supprimer`, `afficher` ; `__init__` est déjà codé). Test : `creer("a.txt", "bonjour!!")` → inode `{"taille": 9, "blocs": [0, 1, 2]}`.

### Tâche 6 — Séances d'explication
Avant la soutenance, organise 4 × 10 min : chacun explique son code aux autres. Utilise le **quiz soutenance** pour vérifier que tout le monde est « Prêt ».

### Ce que je dois savoir expliquer à la soutenance
- [ ] Pagination : page, cadre, table des pages, `//` et `%`
- [ ] Défaut de page, mémoire virtuelle
- [ ] FIFO / LRU / Optimal et l'anomalie de Belady
- [ ] TLB et formule EAT
- [ ] Le code des 3 autres (le prof tire au hasard !)

---

## 5. Mon journal (à remplir au fur et à mesure)
But : quand on révisera, ce tableau dit **ce que j'ai fait et compris**. Remplis-le **le jour même**, en 2-3 lignes, avec tes mots.

| Tâche | Date | Ce que j'ai fait | Ce que j'ai compris / difficultés | À revoir |
|---|---|---|---|---|
| Dépôt GitHub |  |  |  |  |
| Paging / Optimal / TLB |  |  |  |  |
| Relecture des PR |  |  |  |  |
| Intégration |  |  |  |  |
| Bonus minifs |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

### Mes notes pour la soutenance (explique avec tes mots)
-
-
-

> Ce fichier est dans le dépôt (`docs/`). Pour le sauvegarder : `git add docs` → `git commit -m "docs: journal"` → `git push`.

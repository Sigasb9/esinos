# Ilias — Round Robin, Priority, LRU

Mon code `rr`, `priority`, `lru` est **ma** partie : le prof peut me demander de l'expliquer, mais aussi le code des trois autres.

**Mes fichiers :** `code/scheduler/rr.py`, `code/scheduler/priority.py`, `code/memory/lru.py`
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
git config --global user.name "Ilias NOM"
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
git checkout -b feature/round-robin      # crée ta branche (1 fois)
# ... tu codes ...
git add .
git commit -m "feat: ajout du Round Robin"
git push -u origin feature/round-robin
```
**GitHub Desktop :** `Current branch > New branch` → nom `feature/round-robin` → tu codes → en bas à gauche écris le message → **Commit to feature/round-robin** → **Publish branch** (ensuite : **Push origin**).

**Fin de tâche :** sur github.com, bouton vert **Compare & pull request** → 2 lignes (ce que j'ai fait / comment tester) → **Create pull request** → préviens Sami. Il relit et fusionne.

Messages de commit : `feat:` nouveau code · `fix:` correction · `docs:` documentation.
**Au moins 1 commit par session de travail.** Conflit (`<<<<<<<` dans un fichier) ? Ne force rien, appelle Sami. Perdu ? `git status`.

---

## 4. Mes tâches
Le fichier existe déjà dans le projet avec la bonne signature, un commentaire `# TODO` et `raise NotImplementedError` : **tu remplaces le `raise` par ton code**, tu ne changes pas le nom ni les paramètres de la fonction.

### Tâche 1 — Round Robin · branche `feature/round-robin`
**Idée :** chaque processus s'exécute au maximum un *quantum*, puis, s'il n'a pas fini, repasse à la fin de la file.
**Étapes :**
1. Relis ton cours sur le Round Robin.
2. Dans `rr.py`, complète `rr(procs, quantum)`. Elle **renvoie** un Gantt : liste de `(pid, début, fin)` (rien à afficher dedans).
3. Utilise une file (`collections.deque`) et un dictionnaire `restant` (temps restant de chaque processus).
4. **Règle à respecter :** un processus qui arrive pendant une tranche entre dans la file **avant** celui qui vient d'être interrompu. Écris-le en commentaire.
5. Si aucun processus n'est arrivé, le processeur attend : `("IDLE", début, fin)`.
6. Teste avec l'exemple et 2 quantums différents. Commit, push, pull request.

**Résultat attendu** (exemple P1(0,5) P2(1,3) P3(2,8) P4(3,6), quantum = 4) :
```
[("P1",0,4), ("P2",4,7), ("P3",7,11), ("P4",11,15), ("P1",15,16), ("P3",16,20), ("P4",20,22)]
```
Moyennes : attente **9.25**, séjour **14.75**. Le test `test_rr` doit passer.

### Tâche 2 — Priority · branche `feature/priority`
**Idée :** parmi les processus déjà arrivés, celui qui a la meilleure priorité passe en premier, sans être interrompu. **Plus petit nombre = priorité plus haute** (écris-le en commentaire).
**Étapes :** complète `priority(procs)` ; égalité de priorité → le premier arrivé ; gère le trou (`IDLE`) ; vérifie à la main sur 4-5 processus ; pull request.

**Résultat attendu** (exemple) :
```
[("P1",0,5), ("P3",5,13), ("P2",13,16), ("P4",16,22)]
```
Moyennes : attente **7.00**, séjour **12.50**. Le test `test_priority` doit passer.

### Tâche 3 — LRU · branche `feature/lru`
**Idée :** quand il n'y a plus de place, on retire la page **utilisée il y a le plus longtemps**.
**Étapes :**
1. Regarde `fifo.py` (Yassine) : même format de retour.
2. Complète `lru(refs, n_cadres)` → `{"faults": nombre, "steps": [{"page", "frames", "fault"}, ...]}`.
3. Astuce : garde les pages dans une liste de la moins récente à la plus récente. Page déjà présente → déplace-la à la fin. Défaut sans place → retire la première.
4. Pull request.

**Résultat attendu :** refs `7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1`, 3 cadres → **12 défauts** (FIFO = 15, Optimal = 9). Le test `test_defauts` doit passer.

### Tâche 4 — bonus (seulement si tout est fusionné)
Mini système de fichiers (`code/filesystem/minifs.py`). Parle-en à Sami avant.

### Ce que je dois savoir expliquer à la soutenance
- [ ] Différence Round Robin / Priority
- [ ] Ce qu'est un quantum (trop petit ? trop grand ?)
- [ ] La famine (starvation) et comment l'éviter (aging)
- [ ] Comment LRU choisit la page à retirer, et pourquoi il fait moins de défauts que FIFO ici
- [ ] Mon code ligne par ligne (`deque`, `restant`, la règle d'arrivée)

---

## 5. Mon journal (à remplir au fur et à mesure)
But : quand on révisera, ce tableau dit **ce que j'ai fait et compris**. Remplis-le **le jour même**, en 2-3 lignes, avec tes mots.

| Tâche | Date | Ce que j'ai fait | Ce que j'ai compris / difficultés | À revoir |
|---|---|---|---|---|
| Round Robin |  |  |  |  |
| Priority |  |  |  |  |
| LRU |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

### Mes notes pour la soutenance (explique avec tes mots)
-
-
-

> Ce fichier est dans le dépôt (`docs/`). Pour le sauvegarder : `git add docs` → `git commit -m "docs: journal"` → `git push`.

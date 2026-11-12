# Adam — FCFS, SJF, métriques, rapport

Tu es la personne qui connaît le mieux la **théorie** de l'ordonnancement : à toi de bien la maîtriser.

**Mes fichiers :** `code/scheduler/fcfs.py`, `code/scheduler/sjf.py`, `code/scheduler/metrics.py`, `report.pdf`
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
git config --global user.name "Adam NOM"
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
git checkout -b feature/fcfs-sjf      # crée ta branche (1 fois)
# ... tu codes ...
git add .
git commit -m "feat: ajout de FCFS et SJF"
git push -u origin feature/fcfs-sjf
```
**GitHub Desktop :** `Current branch > New branch` → nom `feature/fcfs-sjf` → tu codes → en bas à gauche écris le message → **Commit to feature/fcfs-sjf** → **Publish branch** (ensuite : **Push origin**).

**Fin de tâche :** sur github.com, bouton vert **Compare & pull request** → 2 lignes (ce que j'ai fait / comment tester) → **Create pull request** → préviens Sami. Il relit et fusionne.

Messages de commit : `feat:` nouveau code · `fix:` correction · `docs:` documentation.
**Au moins 1 commit par session de travail.** Conflit (`<<<<<<<` dans un fichier) ? Ne force rien, appelle Sami. Perdu ? `git status`.

---

## 4. Mes tâches
Le fichier existe déjà dans le projet avec la bonne signature, un commentaire `# TODO` et `raise NotImplementedError` : **tu remplaces le `raise` par ton code**, tu ne changes pas le nom ni les paramètres de la fonction.

### Tâche 1 — FCFS et SJF · branche `feature/fcfs-sjf`
**Idée :**
- **FCFS** : on exécute dans l'ordre d'arrivée.
- **SJF** (non préemptif) : quand le processeur se libère, on prend, parmi les processus **déjà arrivés**, celui qui a le plus petit burst.

**Étapes :**
1. Complète `fcfs(procs)` et `sjf(procs)`. Elles **renvoient** un Gantt : liste de `(pid, début, fin)`.
2. Si aucun processus n'est arrivé, le processeur attend : ajoute `("IDLE", début, fin)`.
3. Teste avec l'exemple (`EXEMPLE` dans `process.py`). Commit, push, pull request.

**Résultat attendu** :
```
FCFS : [("P1",0,5), ("P2",5,8), ("P3",8,16), ("P4",16,22)]
SJF  : [("P1",0,5), ("P2",5,8), ("P4",8,14), ("P3",14,22)]
Trou : fcfs([Process("P1", 3, 2)])  ->  [("IDLE",0,3), ("P1",3,5)]
```
Les tests `test_fcfs`, `test_sjf`, `test_trou_processeur` doivent passer.

### Tâche 2 — Métriques · branche `feature/metrics`
**Formules :** séjour = fin − arrivée · attente = séjour − burst.
**Étapes :**
1. Complète `calculer(procs, gantt)` dans `metrics.py`. La **fin** d'un processus = la fin de sa **dernière** tranche dans le Gantt (important pour Round Robin).
2. Elle renvoie `(resultats, attente_moyenne, sejour_moyen)`.
3. **Format imposé** de `resultats` (le menu en dépend) : un dictionnaire par processus, `{pid: {"pid", "arrivee", "burst", "fin", "sejour", "attente"}}`. Regarde le stub pour la forme exacte.
4. Pull request.

**Résultat attendu :** FCFS attente **5.75** / séjour **11.25** · SJF **5.25** / **10.75** · Round Robin q=4 **9.25** / **14.75** · Priority **7.00** / **12.50**. Le test `test_moyennes` doit passer.

### Tâche 3 — Rapport · fichier `report.pdf`
**Contenu :** 2 à 4 pages. Plan : introduction · architecture · ordonnanceur · mémoire · difficultés · liens avec le cours · conclusion.
**Étapes :** demande à chacun 5 lignes sur ses difficultés avant la fin du code · ajoute au moins 1 diagramme de Gantt et 1 tableau de défauts de page (copiés depuis le programme) · exporte en PDF · envoie à Sami.
**Résultat attendu :** `report.pdf` de 2 à 4 pages, avec des liens clairs avec le cours.

### Ce que je dois savoir expliquer à la soutenance
- [ ] FCFS contre SJF
- [ ] L'effet de convoi (un long processus bloque tous les autres)
- [ ] Formules : temps de séjour et temps d'attente
- [ ] Préemptif / non préemptif
- [ ] Mon code ligne par ligne (tri, `max`, gestion du trou IDLE)

---

## 5. Mon journal (à remplir au fur et à mesure)
But : quand on révisera, ce tableau dit **ce que j'ai fait et compris**. Remplis-le **le jour même**, en 2-3 lignes, avec tes mots.

| Tâche | Date | Ce que j'ai fait | Ce que j'ai compris / difficultés | À revoir |
|---|---|---|---|---|
| FCFS |  |  |  |  |
| SJF |  |  |  |  |
| Métriques |  |  |  |  |
| Rapport |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

### Mes notes pour la soutenance (explique avec tes mots)
-
-
-

> Ce fichier est dans le dépôt (`docs/`). Pour le sauvegarder : `git add docs` → `git commit -m "docs: journal"` → `git push`.

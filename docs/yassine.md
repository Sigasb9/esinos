# Yassine — FIFO, tests, README, vidéo

Commence par la tâche 1 : c'est la plus importante pour toi. Demande de l'aide à Sami après 30 min de blocage.

**Mes fichiers :** `code/memory/fifo.py`, `code/tests/`, `README.md`, `demo.mp4`
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
git config --global user.name "Yassine NOM"
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
git checkout -b feature/fifo      # crée ta branche (1 fois)
# ... tu codes ...
git add .
git commit -m "feat: ajout de FIFO"
git push -u origin feature/fifo
```
**GitHub Desktop :** `Current branch > New branch` → nom `feature/fifo` → tu codes → en bas à gauche écris le message → **Commit to feature/fifo** → **Publish branch** (ensuite : **Push origin**).

**Fin de tâche :** sur github.com, bouton vert **Compare & pull request** → 2 lignes (ce que j'ai fait / comment tester) → **Create pull request** → préviens Sami. Il relit et fusionne.

Messages de commit : `feat:` nouveau code · `fix:` correction · `docs:` documentation.
**Au moins 1 commit par session de travail.** Conflit (`<<<<<<<` dans un fichier) ? Ne force rien, appelle Sami. Perdu ? `git status`.

---

## 4. Mes tâches
Le fichier existe déjà dans le projet avec la bonne signature, un commentaire `# TODO` et `raise NotImplementedError` : **tu remplaces le `raise` par ton code**, tu ne changes pas le nom ni les paramètres de la fonction.

### Tâche 1 — FIFO · branche `feature/fifo`
**Idée :** la mémoire est découpée en *cadres*. Une page demandée qui n'est pas dans un cadre = **défaut de page**. S'il n'y a plus de place, FIFO retire la page présente **depuis le plus longtemps** (premier arrivé, premier sorti).
**Étapes :**
1. Relis ton cours (pagination, FIFO). Un point pas clair ? Demande à Sami.
2. Complète `fifo(refs, n_cadres)`. Elle renvoie `{"faults": nombre, "steps": [{"page", "frames", "fault"}, ...]}` : le nombre de défauts **et** l'état des cadres à chaque étape.
3. Astuce : une liste. Page absente et cadres pleins → `pop(0)` (retire la plus ancienne), puis `append(page)`.
4. Pull request.

**Résultat attendu :**
- refs `7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1`, 3 cadres → **15 défauts**
- **Belady** : refs `1 2 3 4 1 2 5 1 2 3 4 5` → **9** défauts avec 3 cadres, **10** avec 4 cadres (plus de cadres, plus de défauts !)

### Tâche 2 — Tests
Les fichiers `test_scheduler.py` et `test_memory.py` existent déjà. Ton travail :
1. Les lire et comprendre chaque test : un test = un exemple dont on connaît le résultat.
2. Ajouter au moins **2 tests à toi** (ex. un cas limite : un seul processus, 1 seul cadre).
3. Si un test échoue après le code de quelqu'un, ouvre un ticket dans l'onglet **Issues** de GitHub et préviens la personne.
4. Vérifier que `code/tests/__init__.py` existe.

**Résultat attendu :** cette commande lance tout et tout passe :
```
python -m unittest discover -s code/tests -t code -v
```

### Tâche 3 — README · fichier `README.md`
Contenu : description · installation · utilisation (`python code/main.py`) · exemples · répartition du travail.
**Résultat attendu :** quelqu'un qui n'a pas touché au projet arrive à le lancer avec ton seul README. Fais-le tester à une personne extérieure.

### Tâche 4 — Vidéo de démo · fichier `demo.mp4`
6 à 8 minutes, **caméra ouverte obligatoire** (le visage de chacun apparaît), chacun présente sa partie à tour de rôle. Répète une fois à blanc, ferme les notifications, grande police dans le terminal. Compresse sous **100 Mo** (GitHub refuse plus gros) et envoie à Sami.
**Résultat attendu :** la vidéo se lit sur un autre ordinateur et montre tout ce que le prof demande.

### Ce que je dois savoir expliquer à la soutenance
- [ ] La différence entre page et cadre
- [ ] Ce qu'est un défaut de page
- [ ] Comment FIFO choisit la page à retirer
- [ ] L'anomalie de Belady (l'exemple 9 → 10 défauts)
- [ ] Mon code ligne par ligne

---

## 5. Mon journal (à remplir au fur et à mesure)
But : quand on révisera, ce tableau dit **ce que j'ai fait et compris**. Remplis-le **le jour même**, en 2-3 lignes, avec tes mots.

| Tâche | Date | Ce que j'ai fait | Ce que j'ai compris / difficultés | À revoir |
|---|---|---|---|---|
| FIFO |  |  |  |  |
| Tests |  |  |  |  |
| README |  |  |  |  |
| Vidéo |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

### Mes notes pour la soutenance (explique avec tes mots)
-
-
-

> Ce fichier est dans le dépôt (`docs/`). Pour le sauvegarder : `git add docs` → `git commit -m "docs: journal"` → `git push`.

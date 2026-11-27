# TP3 — Intégration Continue avec FastAPI et GitHub Actions

## 1. Description du projet

Ce projet est une application web Python développée avec **FastAPI**.

Il permet d'effectuer plusieurs opérations mathématiques et de gérer des éléments à travers une API REST.

Ce TP consiste à ajouter une nouvelle fonctionnalité de soustraction, développer des tests unitaires et mettre en place une intégration continue avec GitHub Actions.

## 2. Technologies utilisées

- Python 3.12
- FastAPI : création de l'API REST
- Uvicorn : lancement du serveur
- Pytest : exécution des tests unitaires
- Pytest-cov : calcul de la couverture du code
- Pylint : analyse de la qualité du code
- Git et GitHub : gestion du code source
- GitHub Actions : automatisation des tests

## 3. Installation

Créer et activer un environnement virtuel :

```bash
python -m venv .venv
```

Sous Windows PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

Installer les dépendances :

```bash
pip install fastapi uvicorn pytest httpx pytest-cov pylint
```

## 4. Lancement de l'application

Exécuter la commande :

```bash
uvicorn main:app --reload
```

L'application sera accessible à :

http://127.0.0.1:8000

Documentation interactive Swagger :

http://127.0.0.1:8000/docs

## 5. Fonctionnalités de l'application

| Méthode HTTP | Endpoint | Description |
|---|---|---|
| GET | `/` | Affiche un message de bienvenue |
| GET | `/addition` | Additionne deux nombres |
| POST | `/multiply` | Multiplie deux nombres |
| POST | `/divide` | Divise deux nombres |
| GET | `/subtraction` | Soustrait deux nombres |
| DELETE | `/remove/{item_id}` | Supprime un élément |
| PUT | `/update/{item_id}` | Modifie un élément |

### Nouvelle fonctionnalité : soustraction

La fonctionnalité ajoutée dans ce TP permet de soustraire deux nombres entiers.

Exemple :

```text
GET /subtraction?a=10&b=5
```

Résultat attendu :

```json
{
  "result a-b=": 5,
  "developer": "Dev3"
}
```

## 6. Tests unitaires

Les tests sont développés dans le fichier `test_main.py`.

Ils permettent de vérifier le fonctionnement des différents endpoints de l'application.

Pour exécuter les tests :

```bash
pytest -v
```

**Résultat obtenu : 10 tests réussis.**

## 7. Code Coverage

La couverture du code permet de mesurer la partie du code exécutée pendant les tests.

Commande :

```bash
pytest --cov=main --cov-report=term-missing
```

**Résultat obtenu : 100 % de couverture sur `main.py`.**

L'objectif du TP, qui était d'atteindre une couverture supérieure à 90 %, est donc atteint.

## 8. Analyse de la qualité du code avec Pylint

Pylint permet de vérifier la qualité du code Python et de détecter les mauvaises pratiques.

Commande :

```bash
python -m pylint main.py test_main.py
```

**Résultat obtenu : 10/10.**

## 9. Intégration Continue avec GitHub Actions

Un workflow GitHub Actions est configuré dans :

```text
.github/workflows/ci.yml
```

À chaque `push` ou `pull request`, GitHub Actions exécute automatiquement :

1. La récupération du code source.
2. L'installation de Python et des dépendances.
3. L'exécution des tests unitaires avec Pytest.
4. Le calcul de la couverture du code.
5. L'analyse de la qualité avec Pylint.
6. La génération du rapport JUnit XML.

### Rapport JUnit XML

Le rapport est généré avec la commande :

```bash
pytest -v --junitxml=report.xml
```

Il est ensuite sauvegardé comme artefact GitHub sous le nom :

```text
rapport-junit
```

Cet artefact peut être téléchargé depuis la page d'exécution du workflow GitHub Actions.

## 10. Structure du projet

```text
TP3/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── main.py
├── test_main.py
├── README.md
├── requirements.txt
├── .gitignore
└── .gitlab-ci.yml
```

## 11. Conclusion

Ce TP a permis de développer une nouvelle fonctionnalité dans une application FastAPI, de créer des tests unitaires, de mesurer la couverture du code et d'améliorer sa qualité avec Pylint.

Enfin, l'intégration continue a été mise en place avec GitHub Actions afin d'automatiser les vérifications à chaque modification du projet.
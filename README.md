## Résumé

![circleCI-badge](https://img.shields.io/circleci/build/github/npaillasson/orange_county_lettings/master?token=c8a305dbec80d4bfbb68c6da7fce237fe5933620)
![docker-image-size](https://img.shields.io/docker/image-size/npaillasson/orange_county_lettings?label=docker%20image%20size&sort=date)
![docker-image-tag](https://img.shields.io/docker/v/npaillasson/orange_county_lettings?label=latest%20docker%20image%20tag&sort=date)
![last-commit](https://img.shields.io/github/last-commit/npaillasson/orange_county_lettings)

Site web d'Orange County Lettings

##technologies

Le site est développé à l'aide du framework [django](https://docs.djangoproject.com/fr/4.0/).
Les tests sont réalisés à l'aide du framework de test [pytest](https://docs.pytest.org/en/6.2.x/) et
la vérification du respect de la PEP8 est éfféctué à l'aide de [flake8](https://flake8.pycqa.org/en/latest/).

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  profiles_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### déploiement

Pour le développement et le deploiement en continue (CI/CD) nous utilisons [CircleCI](https://circleci.com/docs/) 
dans le cadre de ce projet. Le site est quand à lui hébérgé sur le service [heroku](https://devcenter.heroku.com/categories/reference)
et surveillé par [sentry](https://docs.sentry.io/)

Les détails de la pipeline sont disponible dans `.cicleci/config.yml`.

Lors d'un **git push** depuis la branch master du projet, les tests et le linter sont lancé, en cas de réussite, 
une image docker du projet est créer et est envoyé sur le registry `npaillasson/oc`


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
- `git clone https://github.com/npaillasson/orange_county_lettings.git`

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

#### CI/CD

Pour le développement et le déploiement en continu (CI/CD) nous utilisons [CircleCI](https://circleci.com/docs/) 
dans le cadre de ce projet. Le site est quant à lui hébergé sur le service [heroku](https://devcenter.heroku.com/categories/reference)
et surveillé par [sentry](https://docs.sentry.io/).

Les détails de la configuration de la pipeline sont disponibles dans `.cicleci/config.yml`.

##### Push depuis la branche master

Lors d'un **git push** depuis la branche master du projet, les tests et le linter sont lancés, en cas de réussite, 
une image docker du projet est créée et est envoyée sur le registre dockerhub `npaillasson/orange-county-lettings` et sur
le registre heroku. Après une conteneurisation et un envoi des images réussi sur les registres, le site est ensuite déployé sur Heroku.

##### Push depuis une autre branche que la branche master

Lors d'un **git push** depuis une autre branche que la branche master, seuls les tests et flake8 sont exécutés.

### Docker

Pour installer docker, vous pouvez vous référer à [la documentation](https://www.docker.com/). 
Il est possible de récupérer l'image docker de l'application à l'aide de la commande `docker pull npaillasson/orange_county_lettings:tagname`.
Les images sont taguées avec le hash du comite correspondant à leur création.

#### exécution de l'image docker en local

Le déploiement du site sur Heroku et un developpeur en local utilisent la même image docker pour lancer le site.
La version du site éxécutée dépend des variables d'environnement transmises au conteneur lors de son lancement.

Pour lancer le site en version de développement, utilisez la commande suivante :
```
% docker run -d -p 8000:8000 npaillasson/orange_county_lettings:tagname 
```

Si vous ne disposez pas de l'image en local, docker ira la télécharger sur le registre.

Pour lancer le site en version de production (même en local), utilisez la commande suivante :
```
% docker run -it -e ENV="PRODUCTION" -e PORT=8000 -e SECRET_KEY=<chaine de caractère servant de clé secrète> -p 8000:8000 npaillasson/orange_county_lettings:d09c975e9c338bad523f5b24f7a09cfc6703082d
```

Ici, on transmet des variables d'environnement au conteneur grâce à l'argument "**-e**",
ces variables seront utilisés pour lancer la version "production" du site. Les trois variables sont obligatoires,
en cas d'absence de l'une de ces variables, le site de production ne se lancera pas.

La selection de la version du site à lancer se fait grâce au script shell 'launch_cmd.sh' qui est appelé par l'instruction **CMD** 
au lancement du conteneur.

### Configuration de CircleCI

#### Prérecquis

* Disposer d'un compte sur [CircleCI](https://circleci.com/docs/)
* Suivre le dépot github du projet avec circleCI

#### Configuration

Configurer des variables d'environnement liées au projet :
  * DOCKER_HUB_ACCESS_TOKEN : contient le [token d'acces docker](https://docs.docker.com/docker-hub/access-tokens/) permettant de push l'image sur le registre.
  * DOCKER_HUB_USERNAME : contient le nom d'utilisateur du compte docker.
  * HEROKU_API_KEY : contient la clé API permettant de push l'image sur l'application heroku (pour créer un nouveau token d'accès depuis heroku CLI utiliser `heroku authorizations:create`)
  * HEROKU_APP_NAME : contient le nom de l'application (actuellement **oc-lettings-np**)

### Configuration de HEROKU

#### Prérecquis

* Disposer d'un compte sur [heroku](https://devcenter.heroku.com/)
* Disposer d'heroku CLI
* Utiliser l'application **oc-lettings-np** ou à défaut créer une nouvelle application à l'aide de la commande `$ heroku create <app-name>`
* Disposer d'un compte Sentry avec un projet correspondant à l'application à surveiller (En production, le site est suivi par le service [Sentry](https://docs.sentry.io/))

#### Configuration

Lors du déploiement, Heroku va lancer le conteneur docker avec l'image de l'application. Afin de lancer le serveur en 
mode 'production', il est nécessaire de configurer les variables d'environnement suivantes dans Heroku:
* ENV : "PRODUCTION"
* PORT : 8000
* SECRET_KEY : Une clé secrète utilisée en production seulement, [cliquer ici](#génération-clé-secrète) pour apprendre à générer une nouvelle clé secrète. **Pour des raisons de sécurité, il ne faut pas utiliser la clé utilisée en développement dans la mise en production. C'est elle qui est notamment utilisée pour créer les [tokens CSRF](https://docs.djangoproject.com/fr/4.0/ref/csrf/)**.
* SENTRY_DSN : Le [DSN sentry](https://docs.sentry.io/product/sentry-basics/dsn-explainer/) permettant de suivre les problèmes de l'application sur sentry

Pour configurer une variable d'environnement depuis heroku CLI, il faut utiliser la commande suivante `$ heroku config:set <variable_name>=<value>`.

Lors de la mise en production, l'adresse de l'application correspond à "https://**<app_name>**.herokuapp.com/".

#### Génération clé secrète

Dans une shell python :
```
>>> import random, string
>>> "".join([random.choice(string.printable) for _ in range(24)])
```
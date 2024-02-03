# Documentation du Projet AlecSync

## Introduction

AlecSync est une plateforme sociale innovante permettant aux utilisateurs de se connecter, de partager des messages et de suivre les activités de leurs amis. Cette documentation fournit un aperçu complet du projet AlecSync, y compris ses fonctionnalités, son architecture et ses dépendances.

## Fonctionnalités Principales

1. **Inscription et Connexion:**
   - Les utilisateurs peuvent s'inscrire sur la plateforme en fournissant leur nom, nom d'utilisateur, mot de passe et une image de profil.
   - Une fois inscrits, les utilisateurs peuvent se connecter en utilisant leur nom d'utilisateur et leur mot de passe.

2. **Profil Utilisateur:**
   - Chaque utilisateur a un profil qui affiche des informations telles que son nom, son nom d'utilisateur, sa date d'adhésion, le nombre de followers, et une liste des personnes qu'il suit.
   - Les utilisateurs peuvent également mettre à jour leur image de profil et leur mot de passe.

3. **Timeline:**
   - La timeline affiche les messages postés par l'utilisateur ainsi que ceux des personnes qu'il suit.
   - Les utilisateurs peuvent poster de nouveaux messages, consulter les messages existants, et interagir avec eux en aimant ou en commentant.

4. **Suggestions de Suivi:**
   - La plateforme suggère des utilisateurs à suivre en fonction des intérêts et des activités des utilisateurs actuels.
   - Les suggestions sont basées sur des algorithmes de recommandation qui analysent les interactions précédentes et les intérêts communs.

## Architecture Technique

1. **Frontend:**
   - Le frontend de l'application est développé en utilisant HTML, CSS et JavaScript.
   - Bootstrap est utilisé pour la mise en page et le style des composants frontend.
   - Les modèles Jinja2 sont utilisés pour générer dynamiquement les pages HTML avec des données provenant du backend.

2. **Backend:**
   - Le backend de l'application est construit en utilisant le framework Flask de Python.
   - Flask gère les routes, les requêtes HTTP, la logique métier et l'intégration avec la base de données.
   - SQLAlchemy est utilisé comme ORM (Object-Relational Mapping) pour interagir avec la base de données SQLite.

3. **Base de Données:**
   - La base de données SQLite est utilisée pour stocker les informations des utilisateurs, les messages, les relations de suivi, etc.
   - Elle est gérée et manipulée à l'aide de SQLAlchemy, offrant ainsi une abstraction efficace pour les opérations de lecture et d'écriture.

4. **Sécurité:**
   - La sécurité de l'application est renforcée par l'utilisation de tokens CSRF (Cross-Site Request Forgery) pour prévenir les attaques de type CSRF.
   - Les mots de passe des utilisateurs sont stockés de manière sécurisée en utilisant des techniques de hachage et de salage avec l'aide de la bibliothèque Werkzeug.

## Dépendances du Projet

1. Flask: Framework web léger pour le développement d'applications web en Python.
2. SQLAlchemy: Bibliothèque ORM pour la gestion des bases de données relationnelles en Python.
3. Bootstrap: Framework front-end pour la création de sites web et d'applications web responsives.
4. Jinja2: Moteur de modèle pour la génération de contenu dynamique dans les applications web Flask.
5. Werkzeug: Bibliothèque Python pour la gestion des mots de passe et la sécurité web.

## Guide de Démarrage Rapide pour AlecSync

### 1. Configuration de l'Environnement

Avant de commencer, assurez-vous d'avoir Python et pip installés sur votre système. Vous aurez également besoin d'un éditeur de texte ou d'un IDE pour modifier le code source.

### 2. Téléchargement du Code Source

- Clonez ou téléchargez le code source de l'application AlecSync depuis le référentiel GitHub.

### 3. Installation des Dépendances

- Ouvrez une fenêtre de terminal dans le répertoire du projet AlecSync.
- Exécutez la commande suivante pour installer les dépendances requises:
```bash
pip install -r requirements.txt
```
### 4. Configuration de la Base de Données

- L'application utilise SQLite comme base de données par défaut. Aucune configuration supplémentaire n'est requise.

### 5. Exécution de l'Application
- Dans le terminal, exécutez la commande suivante pour lancer l'application Flask:
```bash
python app.py runserver
```
- L'application AlecSync sera accessible à l'adresse suivante dans votre navigateur web: http://localhost:5000

### 6. Utilisation de l'Application
- Accédez à la page d'accueil de l'application dans votre navigateur.
- Vous pouvez vous inscrire en fournissant vos informations personnelles ou vous connecter si vous avez déjà un compte.
- Explorez les différentes fonctionnalités telles que la timeline, le profil utilisateur, les suggestions de suivi, etc.
- Pour poster de nouveaux messages, cliquez sur "Post New Message" dans la section timeline.

### 7. Personnalisation et Développement
- Vous pouvez personnaliser et étendre l'application en modifiant le code source selon vos besoins.
- Explorez les fichiers Python dans le répertoire app pour comprendre la logique de l'application.
- Les fichiers HTML dans le répertoire templates contiennent le code HTML généré dynamiquement à l'aide de Jinja2.

Amusez-vous bien à utiliser AlecSync!

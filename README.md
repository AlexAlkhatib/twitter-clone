# 💬 **AlecSync — Plateforme Sociale Interactive**

**AlecSync** est une plateforme sociale interactive que j’ai développée dans un cadre **personnel**, afin d’explorer la création d’applications web full-stack permettant aux utilisateurs de partager du contenu, d’interagir entre eux et de suivre l’activité de leurs amis.
Le projet met en pratique le développement backend avec **Flask**, la gestion de données avec **SQLAlchemy**, et l’intégration d’un frontend dynamique et responsive.


## 🎯 Objectifs du projet

* Concevoir une **application web complète** (frontend + backend + base de données)
* Mettre en place des fonctionnalités sociales modernes (timeline, follow system, interactions)
* Structurer un backend sécurisé et robuste avec Flask
* Créer une interface responsive intuitive avec Bootstrap
* Manipuler une base relationnelle via SQLAlchemy


## 📱 Fonctionnalités principales

### 🔐 Inscription & Connexion

* Création de compte avec image de profil
* Authentification sécurisée
* Hashing + salage des mots de passe (Werkzeug)

### 👤 Profil Utilisateur

* Informations : nom, username, date d’adhésion, followers/following
* Mise à jour de la photo de profil et du mot de passe

### 📰 Timeline (fil d’actualité)

* Messages de l’utilisateur + messages des comptes suivis
* Création de nouveaux posts
* Likes, commentaires, interactions

### 🤝 Suggestions de Suivi

* Recommandations d'utilisateurs basées sur :

  * intérêts communs
  * interactions précédentes
  * réseau existant


## 🧰 Stack Technique

### 🖥️ Frontend

* **HTML / CSS / JavaScript**
* **Bootstrap** pour une interface responsive
* **Jinja2** pour générer des templates dynamiques

### ⚙️ Backend

* **Flask** : gestion des routes, sessions, logique métier
* Sécurisation via **tokens CSRF**
* Système d’authentification robuste

### 🗄️ Base de données

* **SQLite** (simple, légère, intégrée)
* **SQLAlchemy ORM** (modèles, relations, requêtes sécurisées)

### 🔒 Sécurité

* CSRF protection (WTForms / Flask-CSRF)
* Hashing + salage des mots de passe (Werkzeug)
* Gestion des sessions utilisateurs


## 🧠 Compétences démontrées

✔ Développement full-stack complet (front + back + base de données)
✔ Gestion d’une architecture MVC dans Flask
✔ Création d’un système d’authentification sécurisé
✔ Développement d’une timeline interactive (logique backend + affichage dynamique)
✔ Implémentation d’un système de relations sociales (followers/following)
✔ Manipulation d'un ORM (SQLAlchemy)
✔ Design responsive & UX avec Bootstrap
✔ Structuration propre du code et gestion d’un projet complet


## 📂 Structure du projet

```
AlecSync/
 ├── app/
 │   ├── static/           # CSS, images, JS
 │   ├── templates/        # Pages HTML Jinja2
 │   ├── models.py         # Modèles SQLAlchemy
 │   ├── routes.py         # Routes Flask
 │   ├── forms.py          # Formulaires + validation
 │   └── utils.py          # Fonctions utilitaires
 ├── requirements.txt
 ├── app.py                # Point d’entrée Flask
 └── README.md
```


## 🚀 Guide de démarrage rapide

### 1️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2️⃣ Lancer l’application

```bash
python app.py
```

L’application sera disponible à l’adresse :

👉 **[http://localhost:5000](http://localhost:5000)**

### 3️⃣ Utiliser AlecSync

* Créer un compte
* Personnaliser son profil
* Poster des messages
* Suivre des utilisateurs
* Voir la timeline et interagir


## 🔧 Pistes d’amélioration

* API REST pour interagir avec une app mobile
* Ajout de WebSockets pour un fil d’actualité en temps réel
* Refonte UI en React / Vue.js
* Système de notifications
* Upload avancé d’images via un stockage cloud
* Passage à PostgreSQL + migrations avec Alembic


## 👤 À propos

Développeur passionné par la création d’applications web modernes, je conçois AlecSync pour approfondir mes compétences full-stack avec Python, Flask et SQLAlchemy.
GitHub : **[https://github.com/AlexAlkhatib](https://github.com/AlexAlkhatib)**


## 📄 Licence

MIT License  Copyright (c) 2025 Alex Alkhatib

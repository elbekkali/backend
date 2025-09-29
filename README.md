# Backend FastAPI - Agency Project

Ce dossier contient le backend de l'application développé avec **FastAPI**.

## Description

L’API backend est construite avec FastAPI et inclut :
- Gestion des utilisateurs et authentification
- Base de données PostgreSQL via SQLAlchemy
- Migrations avec Alembic
- Validation de données avancée avec Pydantic (support e-mail, etc.)
- Sécurité avec hashing bcrypt et JWT
- Support multipart pour fichiers

## Prérequis

- Python 3.10+  
- Environnement virtuel recommandé  
- Les dépendances sont listées dans `requirements.txt`

## Installation et exécution

1. Ouvre une invite de commandes (PowerShell ou CMD).

2. Place-toi dans le dossier backend du projet :

### `cd path/to/backend`

*(Adapter `path/to/backend` selon ton organisation)*

3. Active ton environnement virtuel (si tu en as un) :
- Sur Windows PowerShell :
  ```
  .\env\Scripts\activate
  ```
- Sur MacOS/Linux :
  ```
  source env/bin/activate
  ```

4. Installe ou mets à jour les dépendances (optionnel si déjà fait) :
  ```
  pip install -r requirements.txt
  ```

5. Lance le serveur FastAPI en mode développement avec rechargement automatique :
  ```
  uvicorn app.main:app --reload
  ```

6. Ouvre un navigateur sur :  
[http://127.0.0.1:8000](http://127.0.0.1:8000)  
pour accéder à l’API et sa documentation Swagger automatique :  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Base de données

Le backend utilise une base de données PostgreSQL distante, accessible ici :  
[https://console.neon.tech/app/projects/holy-bird-62895536/branches/br-late-leaf-a2446h9a/tables](https://console.neon.tech/app/projects/holy-bird-62895536/branches/br-late-leaf-a2446h9a/tables)  

*(Attention : un collaborateur devra disposer des accès nécessaires pour manipuler la base)*

---

## Remarques

- Veille à ajuster les chemins vers l’environnement virtuel selon ton installation locale.  
- Ce backend est conçu pour être utilisé avec le frontend React du projet Agency.  
- Pour toute question ou problème avec l’installation, contacter l’administrateur du projet.

---

Bonne exploration !

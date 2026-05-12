# Documentation d’utilisation — CRUD Bibliothèque Django

## Ajouter un livre

Accéder à l’URL :

```text
http://127.0.0.1:8000/myfirstapp/ajout/
```

Remplir le formulaire avec :

- le titre
- l’auteur
- la date de parution
- le nombre de pages
- le résumé

Puis cliquer sur :

```text
Envoyer les données
```

Le livre sera enregistré dans la base de données.

---

# Afficher tous les livres

Accéder à l’URL :

```text
http://127.0.0.1:8000/myfirstapp/
```

Cette page affiche la liste complète des livres enregistrés.

---

# Afficher un livre

Accéder à l’URL :

```text
http://127.0.0.1:8000/myfirstapp/affiche/<id>/
```

Exemple :

```text
http://127.0.0.1:8000/myfirstapp/affiche/1/
```

Cette page affiche les informations détaillées du livre correspondant à l’ID.

---

# Modifier un livre

Accéder à l’URL :

```text
http://127.0.0.1:8000/myfirstapp/update/<id>/
```

Exemple :

```text
http://127.0.0.1:8000/myfirstapp/update/1/
```

Le formulaire est pré-rempli avec les anciennes valeurs.

Modifier les informations souhaitées puis valider.

Les données du livre seront mises à jour dans la base.

---

# Supprimer un livre

Accéder à l’URL :

```text
http://127.0.0.1:8000/myfirstapp/delete/<id>/
```

Exemple :

```text
http://127.0.0.1:8000/myfirstapp/delete/1/
```

Le livre correspondant sera supprimé de la base de données.

---

# Lancer le serveur Django

Dans le terminal :

```bash
python manage.py runserver
```

Puis ouvrir :

```text
http://127.0.0.1:8000/
```
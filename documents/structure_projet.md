Voici comment ajouter une hiérarchie de fichiers en markdown :

```markdown
# Structure du projet

manim_site/
│
├── manim_project/
│   ├── migrations/
│   ├── static/               # Fichiers statiques (CSS, JS, etc.)
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   ├── templates/            # Fichiers HTML
│   │   └── manim_project/
│   │       ├── home.html
│   │       └── edit.html
│   ├── forms.py              # Gestion des formulaires (si nécessaire)
│   ├── urls.py               # Routes spécifiques à l'application
│   ├── views.py              # Logique des vues
│   └── utils/                # Fonctions utilitaires (par ex., génération de vidéos)
│       └── generate_video.py
│
├── manim_site/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py


```
Django est un framework web Python puissant et bien structuré, conçu pour développer rapidement des applications web. Il suit le principe "Don't Repeat Yourself" (DRY) et adopte une architecture Modèle-Vue-Contrôleur (MVC) légèrement adaptée en Modèle-Vue-Template (MVT).

## 1. Composants principaux de Django

- Modèle (Models) : Gère la structure de vos données et les interactions avec la base de données. Par exemple, un modèle représente une table dans la base de données.
- Vue (Views) : Contient la logique métier. Les vues en Django sont des fonctions ou des classes Python qui reçoivent des requêtes HTTP, exécutent la logique, puis renvoient une réponse HTTP.
- Template (Templates) : Définit la partie front-end de votre application. Les fichiers HTML (templates) affichent les données envoyées par les vues.
- URL Dispatcher : Mappe les URL entrantes aux vues correspondantes grâce à un fichier de configuration urls.py.

## 2. Comment fonctionne Django en pratique ?

- Requête : Un utilisateur saisit une URL dans son navigateur.
- URL Dispatcher : Django recherche dans urls.py la vue associée à cette URL.
- Vue : La vue effectue des opérations nécessaires (lecture/écriture en base de données, traitement de données, etc.).
- Modèle : Si nécessaire, la vue utilise les modèles pour interagir avec la base de données.
- Template : La vue rend un template HTML avec les données traitées et les renvoie au client.
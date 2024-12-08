# **Projet Django-Manim-Project**

## Membres du Groupe

- **Cinelli Esteban**  
- **Grodent Clément**  
- **Ricchieri Meven**  
- **Valiente Santiago**  

---

## **3. Description du Projet**

### **Contexte et Problématique**

Manim est une bibliothèque Python populaire pour produire des animations mathématiques et pédagogiques. Cependant, son utilisation nécessite des compétences en programmation Python, ce qui peut être un frein pour les enseignants, les étudiants, ou les créateurs de contenu ayant peu d'expérience technique.

De même, `matplotlib.animation` est un outil puissant pour créer des animations basées sur des graphiques, mais il reste largement inexploité pour des applications pédagogiques accessibles. 

Le projet vise à démocratiser l'accès à ces outils via une plateforme web intuitive qui offre plusieurs fonctionnalités :  
- La possibilité de soumettre et coder des scripts personnalisés pour Manim ou Matplotlib. 
- Une bibliothèque de scripts pré-codés permettant de générer rapidement des animations pédagogiques de base avec Manim ou Matplotlib.  
- Des options d'interaction où les utilisateurs peuvent entrer des paramètres spécifiques (comme des valeurs ou des configurations) pour personnaliser les animations.

### **Fonctionnalités Attendues**

1. **Soumission et Édition de Scripts**  
   Une interface web où les utilisateurs peuvent écrire ou copier-coller leurs scripts Manim ou Matplotlib personnalisés.  
   
2. **Bibliothèque de Scripts Pré-Codés**  
   Une sélection de scripts prêts à l'emploi pour réaliser des animations pédagogiques courantes. Par exemple, des animations de circuits électriques, de graphiques mathématiques, ou de phénomènes physiques.

3. **Personnalisation des Animations**  
   Pour les scripts pré-codés, l'utilisateur pourra entrer des valeurs ou paramètres (par exemple, les valeurs des résistances dans un circuit ou les données pour un graphique animé) afin de personnaliser les animations générées.

4. **Génération et Téléchargement de Vidéos**  
   Le backend traite les scripts soumis (Manim ou Matplotlib) et génère une vidéo, disponible au format `.mp4` pour téléchargement.

5. **Gestion des Fichiers**  
   Les vidéos générées seront accessibles pour téléchargement.

---

## **4. Objectifs du Projet**

### **Objectifs Techniques**

- Développer un site web basé sur Django.  
- Intégrer Manim et Matplotlib pour la génération de vidéos animées.  
- Mettre en place une bibliothèque de scripts pré-codés interactifs, c-à-d. paramétrables par l'utilisateur.  
- Gérer efficacement le stockage et la récupération des vidéos générées.  

### **Objectifs Fonctionnels**

- Fournir une interface utilisateur simple et accessible pour coder ou sélectionner des scripts.  
- Proposer des animations pédagogiques prêtes à l'emploi, paramétrables par l'utilisateur.  
- Permettre la génération de vidéos sans nécessiter d'installation locale des outils (Manim ou Matplotlib).  
- Offrir un rendu vidéo optimisé sous le format `.mp4`.  

---
## **5. Description Fonctionnelle**

### **Architecture du Système**

#### **Flux des Opérations**

1. L'utilisateur accède à une page web avec deux options principales :  
   - **Créer un script personnalisé :** Entrée d'un code Manim ou Matplotlib directement via l'éditeur intégré.  
   - **Utiliser un script pré-codé :** Sélection d'un script dans la bibliothèque et personnalisation des paramètres.  

2. Le script sélectionné ou créé est transmis au serveur Django.  
3. Le serveur identifie le moteur d'animation approprié (Manim ou Matplotlib) et exécute le script avec les paramètres fournis par l'utilisateur.  
4. Une vidéo est générée et stockée dans un répertoire spécifique.  
5. L'utilisateur peut :  
   - Télécharger la vidéo.  
   - Visualiser un aperçu directement sur le site.

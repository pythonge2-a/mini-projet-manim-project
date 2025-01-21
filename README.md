# **Django-Manim-Project**

## Group Members

- **Cinelli Esteban**  
- **Grodent Clément**  
- **Ricchieri Meven**  
- **Valiante Santiago**  

---

## **1. Project Description**

### **Context and Problem Statement**

Manim is a popular Python library for creating mathematical and educational animations. However, its use requires Python programming skills, which may be a barrier for teachers, students, or content creators with limited technical experience.

Similarly, `matplotlib.animation` is a powerful tool for creating graph-based animations but remains underutilized for accessible educational applications.

The project aims to democratize access to these tools through an intuitive web platform offering several features:  
- The ability to submit and write custom scripts for Manim or Matplotlib.  
- A library of pre-coded scripts to quickly generate basic educational animations using Manim or Matplotlib.  
- Interactive options where users can input specific parameters (e.g., values or configurations) to customize the animations.

### **Expected Features**

1. **Script Submission and Editing**  
   A web interface allowing users to write or copy-paste their custom Manim or Matplotlib scripts.  
   
2. **Library of Pre-Coded Scripts**  
   A selection of ready-to-use scripts for common educational animations, such as electrical circuits, mathematical graphs, or physical phenomena.  

3. **Animation Customization**  
   For pre-coded scripts, users can input values or parameters (e.g., resistance values in a circuit or data for an animated graph) to personalize the generated animations.  

4. **Video Generation and Download**  
   The backend processes the submitted (Manim or Matplotlib) scripts and generates a video, available for download in `.mp4` format.  

5. **File Management**  
   Generated videos will be accessible for download.

---

## **2. Project Objectives**

### **Technical Objectives**

- Develop a Django-based website.  
- Integrate Manim and Matplotlib for generating animated videos.  
- Implement a library of interactive, pre-coded scripts that are user-configurable.  
- Efficiently manage the storage and retrieval of generated videos.  

### **Functional Objectives**

- Provide a simple and accessible user interface for coding or selecting scripts.  
- Offer ready-to-use, customizable educational animations.  
- Enable video generation without requiring local installation of tools (Manim or Matplotlib).  
- Deliver optimized video rendering in `.mp4` format.  

---

## **3. Functional Description**

### **System Architecture**

#### **Operational Workflow**

1. The user accesses a web page with two main options:  
   - **Create a Custom Script:** Input Manim or Matplotlib code directly via the integrated editor.  
   - **Use a Pre-Coded Script:** Select a script from the library and customize its parameters.  

2. The selected or created script is sent to the Django server.  
3. The server identifies the appropriate animation engine (Manim or Matplotlib) and executes the script with the user-provided parameters.  
4. A video is generated and stored in a specific directory.  
5. The user can:  
   - Download the video.  
   - Preview it directly on the website.

---

## **4. Installation of the project**

1. Clone the repository:  
   ```bash
   git clone https://github.com/pythonge2-a/mini-projet-manim-project.git
2. Go to the directory with 
    ```bash
    cd mini-projet-manim-project
3. Install poetry venv with 
    ```bash 
    poetry install --no-root
4. Activate the venv with 
    ```bash 
    poetry shell
5. Check the installation of manim and django with 
    ```bash
    manim --version
    django-admin --version
6. Go to the manim_site directory with (first cmd for Windows / second cmd for linux)
    ```bash
    cd .\manim_site\ 
    cd manim_site/
7. Run the server with 
    ```bash 
    python manage.py runserver

---

## **5. Example for manim**

## Step 1: Importing Modules

```python
from manim import *
```

- **`from manim import *`** :  
  Cette ligne importe toutes les classes et fonctions de la bibliothèque **Manim**.  
  Cela permet d’utiliser directement des objets comme `Scene`, `MathTex`, et des animations comme `Write` ou `FadeIn`.

---

## Step 2: Creating a Class Inheriting from `Scene`

```python
class AnnotateMath(Scene):
```

- **`class AnnotateMath(Scene):`** :  
  - Crée une classe personnalisée pour définir notre animation.  
  - La classe hérite de `Scene`, qui est le canevas de base de Manim pour ajouter des objets et animations.

---

## Step 3: `construct` method

```python
def construct(self):
```

- **`construct(self)`** :  
  - Méthode obligatoire pour une `Scene`.  
  - Tout le contenu et les animations de la scène doivent y être définis.

---

## Step 4: Add a Math Equation

```python
formula = MathTex(r"a^2 + b^2 = c^2")
```

- **`MathTex`** : Permet de créer des équations en utilisant LaTeX.  
- **`r"a^2 + b^2 = c^2"`** :  
  - La chaîne représente le **théorème de Pythagore**.  
  - Le `r` indique qu’il s’agit d’une chaîne brute.

---

## Step 5: Add Annotation

```python
annotation = Text("Théorème de Pythagore").next_to(formula, DOWN)
```

- **`Text`** : Sert à afficher du texte classique, comme ici *"Théorème de Pythagore"*.  
- **`.next_to(formula, DOWN)`** :  
  - Positionne le texte juste en dessous de `formula`.  
  - `DOWN` est une constante Manim indiquant une direction vers le bas.

---

## Step 6: Adding Animations

### Animation de l’Équation
```python
self.play(Write(formula))
```

- **`self.play()`** : Lance une animation sur la scène.  
- **`Write(formula)`** : Fait apparaître l’équation comme si elle était écrite à la main.

### Animation de l’Annotation
```python
self.play(FadeIn(annotation))
```

- **`FadeIn(annotation)`** : Fait apparaître progressivement l'annotation sur la scène.

---

## Step 7: Break

```python
self.wait(2)
```

- **`self.wait(2)`** : Met la scène en pause pendant 2 secondes pour permettre au spectateur de visualiser le résultat final.

---

## Final result

```python
from manim import *

class AnnotateMath(Scene):
    def construct(self):
        formula = MathTex(r"a^2 + b^2 = c^2")
        annotation = Text("Théorème de Pythagore").next_to(formula, DOWN)

        self.play(Write(formula))
        self.play(FadeIn(annotation))
        self.wait(2)

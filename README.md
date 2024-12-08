# **Django-Manim-Project**

## Group Members

- **Cinelli Esteban**  
- **Grodent Clément**  
- **Ricchieri Meven**  
- **Valiante Santiago**  

---

## **3. Project Description**

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

## **4. Project Objectives**

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

## **5. Functional Description**

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

## Temporary Installation

1. Clone the repository:  
   ```bash
   git clone --branch M.Ricchieri git@github.com:pythonge2-a/mini-projet-manim-project.git
2. Go to the directory with 
    ```bash
    cd mini-projet-manim-project
3. Install poetry venv with 
    ```bash 
    poetry install --no-root
5. Activate the venv with 
    ```bash 
    poetry shell
6. Check the installation of manim and django with 
    ```bash
    manim --version
    django-admin --version
8. Go to the manim_site directory with 
    ```bash
    cd .\manim_site\
10. Run the server with 
    ```bash 
    python manage.py runserver`
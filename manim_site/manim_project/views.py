from django.shortcuts import render, redirect
from django.http import HttpResponse
from manim_project.utils.generate_video import generate_manim_video, generate_pre_coded_video
from os.path import join
from django.conf import settings




# Home
def home_view(request):
    return render(request, 'manim_project/home.html')



# Script edition
def edit_code_view(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        # TODO: Ajouter la logique pour traiter et générer une vidéo avec Manim

        return HttpResponse("Le code a été soumis avec succès !")
    return render(request, 'manim_project/edit.html')



# Video generation for user script
def generate_video_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        generate_manim_video(code)
        return redirect('result')
    return render(request, 'manim_project/edit.html')



# Video generation for pre-coded script
def generate_pre_coded_video_view(request):
    if request.method == 'POST':
        try:
            # Get the script name from the form
            script_name = request.POST.get('script_name')

            # Get additional parameters from the form
            params = {key: value for key, value in request.POST.items() if key not in ['csrfmiddlewaretoken', 'script_name']}

            # Construct the path to the script
            script_path = join(settings.MEDIA_ROOT, "pre_coded", script_name)

            # Generate the video with the provided parameters
            generate_pre_coded_video(script_path, **params)
            return redirect('result')
        
        except Exception as e:
            print(f"Erreur : {e}")
            return render(request, 'manim_project/pre_coded.html', {'error': str(e)})
    return render(request, 'manim_project/pre_coded.html')




# Result 
def result_view(request):
    return render(request, 'manim_project/result.html')





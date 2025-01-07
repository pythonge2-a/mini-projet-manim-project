from django.shortcuts import render, redirect
from django.http import HttpResponse
from manim_project.utils.generate_video import generate_manim_video, generate_pre_coded_video
from os.path import join
from django.conf import settings
import os




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
        video_id = generate_manim_video(code)
        return render(request, 'manim_project/result.html', {'video_id': video_id})
    return render(request, 'manim_project/edit.html')



# Video generation for pre-coded script with UUID
def generate_pre_coded_video_view(request):
    if request.method == 'POST':
        try:
            script_name = request.POST.get('script_name')
            params = {key: value for key, value in request.POST.items() if key not in ['csrfmiddlewaretoken', 'script_name']}
            script_path = join(settings.MEDIA_ROOT, "pre_coded", script_name)

            video_id = generate_pre_coded_video(script_path, **params)
            return render(request, 'manim_project/result.html', {'video_id': video_id})

        except Exception as e:
            print(f"Erreur : {e}")
            return render(request, 'manim_project/pre_coded.html', {'error': str(e)})
    return render(request, 'manim_project/pre_coded.html')




# Result 
def result_view(request):
    return render(request, 'manim_project/result.html')

def video_bank_view(request):
    return render(request, 'manim_project/video_bank.html')



# Get the script content for the video bank
def get_script(request):
    if request.method == 'POST':
        script_path = request.POST.get('script_path')
        full_path = os.path.join(settings.MEDIA_ROOT, script_path)
        
        with open(full_path, 'r') as file:
            script_content = file.read()
            
        request.session['script_content'] = script_content
        return redirect('edit_code')
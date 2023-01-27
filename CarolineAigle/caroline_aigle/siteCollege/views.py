from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'siteCollege/index.html')
def actions(request):
    return render(request, 'siteCollege/actions.html')
def unss(request):
    return render(request, 'siteCollege/unss.html')
def p_avenir(request):
    return render(request, 'siteCollege/p_avenir.html')
def p_citoyen(request):
    return render(request, 'siteCollege/p_citoyen.html')
def p_edu_art_cult(request):
    return render(request, 'siteCollege/p_edu_art_cult.html')
def p_sante(request):
    return render(request, 'siteCollege/p_sante.html')
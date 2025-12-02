from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def faq(request):
    return render(request, "faq.html")

def contact(request):
    return render(request, "contact.html")

def story(request):
    return render(request, "story.html")

def single_story(request):
    return render(request, "single_story.html")

def game(request):
    return render(request, "games.html")

def parent(request):
    return render(request, "parent.html")

def login_view(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html") 

def leaderboard(request):
    return render(request, "leaderboard.html")

def custom_admin(request):
    return render(request, "admin-page.html")
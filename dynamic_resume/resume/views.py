from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')
def addResume(request):
    return render(request, 'addResume.html')
def editResume(request):
    return render(request, 'editResume.html')
def viewResume(request):
    return render(request, 'viewResume.html')
def deleteResume(request):
    return redirect('home')
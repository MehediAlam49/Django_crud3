from django.shortcuts import render,redirect
from resume.models import *
# Create your views here.
def home(request):
    resumeData = resumeModel.objects.all()
    return render(request, 'home.html', {'resume': resumeData})
def addResume(request):
    if request.method == 'POST':
        resumeData = resumeModel(
            profileImage = request.FILES.get('profileImage'),
            fullName = request.POST.get('fullName'),
            profession = request.POST.get('profession'),
            description = request.POST.get('description'),
            city = request.POST.get('city'),
            country = request.POST.get('country'),
            phone = request.POST.get('phone'),
            projects = request.POST.get('projects'),
            followers = request.POST.get('followers'),
            likes = request.POST.get('likes'),
            about = request.POST.get('about'),
            facebook = request.POST.get('facebook'),
            github = request.POST.get('github'),
            linkedin = request.POST.get('linkedin'),
            department = request.POST.get('department'),
            university = request.POST.get('university'),
            grad_year = request.POST.get('grad_year'),
            institute = request.POST.get('institute'),
            progress = request.POST.get('progress'),
            html = request.POST.get('html'),
            css = request.POST.get('css'),
            react = request.POST.get('react'),
            vue = request.POST.get('vue'),
            python = request.POST.get('python'),
            django = request.POST.get('django'),
            photoshop = request.POST.get('photoshop'),
            sublime = request.POST.get('sublime'),
            npm = request.POST.get('npm'),
        )
        resumeData.save()
        return redirect('home')
    return render(request, 'addResume.html')
def editResume(request,id):
    resumeData = resumeModel.objects.get(id=id)
    if request.method == 'POST':
        resumeData.fullName = request.POST.get('fullName')
        resumeData.profession = request.POST.get('profession')
        resumeData.description = request.POST.get('description')
        resumeData.city = request.POST.get('city')
        resumeData.country = request.POST.get('country')
        resumeData.phone = request.POST.get('phone')
        resumeData.projects = request.POST.get('projects')
        resumeData.followers = request.POST.get('followers')
        resumeData.likes = request.POST.get('likes')
        resumeData.about = request.POST.get('about')
        resumeData.facebook = request.POST.get('facebook')
        resumeData.github = request.POST.get('github')
        resumeData.linkedin = request.POST.get('linkedin')
        resumeData.department = request.POST.get('department')
        resumeData.university = request.POST.get('university')
        resumeData.grad_year = request.POST.get('grad_year')
        resumeData.institute = request.POST.get('institute')
        resumeData.progress = request.POST.get('progress')
        resumeData.html = request.POST.get('html')
        resumeData.css = request.POST.get('css')
        resumeData.react = request.POST.get('react')
        resumeData.vue = request.POST.get('vue')
        resumeData.python = request.POST.get('python')
        resumeData.django = request.POST.get('django')
        resumeData.photoshop = request.POST.get('photoshop')
        resumeData.sublime = request.POST.get('sublime')
        resumeData.npm = request.POST.get('npm')

        picture = request.FILES.get('profileImage')
        if picture.profileImage is not None:
            resumeData.profileImage = picture
        resumeData.save()
        return redirect('home')
    return render(request, 'editResume.html', {'resume': resumeData})
def viewResume(request,id):
    resumeData = resumeModel.objects.get(id=id)
    return render(request, 'viewResume.html', {'resume': resumeData})
def deleteResume(request,id):
    return redirect('home')
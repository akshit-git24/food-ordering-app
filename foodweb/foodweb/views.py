from django.shortcuts import render

#creating views
def Homepage(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')
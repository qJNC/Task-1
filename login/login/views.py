from django.shortcuts import render

def home(request):
    if request.method=="POST":
        type=request.POST['type']

    return render(request,"index.html")


def register(request):
    
    if request.method=="POST":
        username=request.POST['username']
        end=request.POST['endname']
        email=request.POST['emailid']
        password=request.POST['passw']
        password=request.POST['confpass']
        password=request.POST['profile']
        address=request.POST['address']
    return render(request,"index1.html")

def login(request):
    
    if request.method=="POST":
        type=request.POST['type']
    return render(request,"loginform.html")


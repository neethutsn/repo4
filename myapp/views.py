from django.shortcuts import render

def masterpage(request):
    return render(request,'master.html')

def homepage(request):
    return render(request,'home.html')

def registerpage(request):
    return render(request,'register.html')

def admasterpage(request):
    return render(request,'adminmaster.html')

def usermasterpage(request):
    return render(request,'usermaster.html')

def signinpage(request):
    return render(request,'signin.html')

def catpage(request):
    return render(request,'category.html')

def adashpage(request):
    return render(request,'admindashboard.html')

def shoppage(request):
    return render(request,'shopmaster.html')

def indoorpage(request):
    return render(request,'indoor.html')

def outdoorpage(request):
    return render(request,'outdoor.html')

def floweringpage(request):
    return render(request,'flowering.html')

def giftpage(request):
    return render(request,'gift.html')

def bonsaipage(request):
    return render(request,'bonsai.html')

def cartpage(request):
    return render(request,'cart.html')

def profilepage(request):
    return render(request,'profile.html')

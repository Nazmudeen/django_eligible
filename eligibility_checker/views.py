from django.shortcuts import render

def home(request):
    return render(request,"index.html")

    """

def check_eligibility(request):
    age=request.GET["userage"]
    if int(age)<18:
        return render(request,'index.html',{"msg":"not eligible"})
    else:
        return render(request,'index.html',{"msg":"eligible"})    """
"""
def username(request):
    user=request.POST["user1"]
    return render(request,'index.html',{"name":user+"is"})   """  

def calculate(request):
    number1=request.GET["num1"]
    number2=request.GET["num2"]
    total=number1+number2
    return render(request,'index.html',{"sumvalue":"totel = "+str(total)})    



# Create your views here.

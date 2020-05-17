from django.shortcuts import render
def home(request):
    if request.method=='POST':
       return render(request,'bulb_on.html')
    else:
       return render(request,'bulb_off.html')

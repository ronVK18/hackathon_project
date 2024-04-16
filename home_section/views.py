from django.shortcuts import render,HttpResponse

# Create your views here.
def create(request, *args, **kwargs):
    return render(request,"home_section/log_in.html")

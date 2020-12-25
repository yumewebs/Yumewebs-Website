from django.shortcuts import render, HttpResponse

# Create your views here.
def contact(request):
    return render(request, "website/contact.html")

def services(request):
    return render(request, "services/services.html")

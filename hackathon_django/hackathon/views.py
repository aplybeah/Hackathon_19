from django.shortcuts import render,redirect

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")
def search_page(request):
    return render(request, "search.html")

def search_result(request, id):
    return render(request, "search_result.html")
    #write a redirect function with the POST from the form
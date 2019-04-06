from django.shortcuts import render,redirect
from .forms import SearchForm
from .data_set import rank_full

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")
def search_page(request):
    return render(request, "search.html")

def redirect_search(request):
    # response = redirect(r"/search/<int:id>")
    # return response
    if request.method == 'POST': 
        form = SearchForm(request.POST) 
        if form.is_valid():  
           form=form.save()
           return redirect('search_result', id=SearchForm.id)  
    else: 
            form = ContactForm()
    return render(request, 'search_result.html', {'form': form})

def search_result(request, id):
    return render(request, "search_result.html")
    #write a redirect function with the POST from the form
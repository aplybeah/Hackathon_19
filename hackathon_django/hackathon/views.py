from django.shortcuts import render,redirect
from .forms import SearchForm

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
           keyword= form.cleaned_data['keyword']
           post_date=form.cleaned_data['post_date']
           set_aside=form.cleaned_data['set_aside']
           return redirect('search/<int:id>')  
    else: 
            form = ContactForm()
    return render(request, 'search_result.html', {'form': form})

def search_result(request, id):
    return render(request, "search_result.html")
    #write a redirect function with the POST from the form


    #dataframe editing function calls two smaller functions on each row of dataframe
#Parses through the title and body of each post and assigns a score based on occurance number 
#of each term
def rank_full(df, search):  
    df['title_score'] = df['title'].map(lambda x: header_ranking(x, search))
    df['body_score'] = df['body'].map(lambda y: body_ranking(y, search))   
    df['total_score'] = df['title_score'] + df['body_score']
    
    df = df.sort_values(by=['total_score'], ascending=False, inplace= True)
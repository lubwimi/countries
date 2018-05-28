from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Country
from .forms import CountryForm

def home(request):
    greeting = "Welcome to Countries Application"
    
    if request.method == "POST":
        form = CountryForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return countries(request)
        else:
            form.errors
    else:
        form = CountryForm()
    
    
    context = {
        'greeting': greeting,
        'form': form,
    }
    
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {})

def countries(request):
    countries_list = Country.objects.all()
    
    paginator = Paginator(countries_list, 100)  # Show 100 countries per page
    page = request.GET.get('page')
    
    try:
        countries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        countries = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        countries = paginator.page(paginator.num_pages)
    
    context = {
        'countries': countries 
    }
    
    context_dict = {
        'countries': countries,
    }
    
    return render(request, 'countries.html', context_dict)

def your_country(request, country_id=1): # if no country suplied in the form take the first one
    context_dict = {
        'your_country': Country.objects.get(id=country_id)
    }
    
    return render(request, 'your_country.html', context_dict)

def search_country(request):
    if request.method == "POST":
        search_text = request.POST['search_text'] # ['search_text'] is a dictionary
    else:
        seach_text = ''
    
    countries = Country.objects.filter(country__contains=search_text) # __contains is a method in django
    
    context = {
        'countries' : countries,
    }
    
    return render(request, 'ajax_search.html', context)

def delete(request, country_id):
    try:
        obj = Country.objects.get(pk=country_id)
        obj.delete()
    except:
        pass
    return redirect("/countries/")

def feature(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return countries(request)
        else:
            form.errors
    else:
        form = CountryForm()
    
    
    context = {
        #'greeting': greeting,
        'form': form,
    }
    
    return render(request, 'feature.html', context)






from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TourForm
from .models import Tour
from django.core.paginator import Paginator
from django.db.models import Min, Max


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def all_tours(request):
    tours = Tour.objects.all()
    return render(request, 'main/all_tours.html', {'tours': tours})



def tour_type(request, tour_type_slug):

    tour_type_display = dict(Tour._meta.get_field('tour_type').choices).get(tour_type_slug, 'Unknown')
    tours = Tour.objects.filter(tour_type=tour_type_slug)
    if not tours.exists():
        return render(request, 'main/tour_not_found.html')

    paginator = Paginator(tours, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/tour_type.html', {
        'tour_type_display': tour_type_display,
        'tour_type_slug': tour_type_slug,
        'tours': page_obj,
    })


def create(request):
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TourForm()
        content = {
            'form': form
        }

    return render(request, 'main/create.html', content)

def tour_list(request):

    search_query = request.GET.get('search', '').strip()
    tours = Tour.objects.all()
    if search_query:
        search_query = search_query.capitalize()
        tours = Tour.objects.filter(title__icontains=search_query)


    price_range = Tour.objects.aggregate(min_price=Min('price'), max_price=Max('price'))
    countries = Tour.objects.values_list('country', flat=True).distinct()
    tour_types = Tour._meta.get_field('tour_type').choices
    selected_countries = request.GET.getlist('country')
    if selected_countries:
        tours = tours.filter(country__in=selected_countries)
    min_price = request.GET.get('min_price', price_range['min_price'])
    max_price = request.GET.get('max_price', price_range['max_price'])
    if min_price and max_price:
        tours = tours.filter(price__gte=min_price, price__lte=max_price)

    selected_tour_types = request.GET.getlist('tour_type')
    if selected_tour_types:
        tours = tours.filter(tour_type__in=selected_tour_types)

    paginator = Paginator(tours, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'tours': page_obj,
        'page_obj': page_obj,
        'price_range': price_range,
        'countries': countries,
        'tour_types': tour_types,
        'min_price': min_price,
        'max_price': max_price,
        'selected_countries': selected_countries,
        'selected_tour_types': selected_tour_types,
        'search_query': search_query,
    }

    return render(request, 'main/all_tours.html', context)



def tour_update(request, id=0):
    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:
        return render(request, 'main/tour_not_found.html')

    if request.method == 'GET':
        form = TourForm(instance=tour)
        return render(request, 'main/update.html', {'form': form, 'tour': tour})

    else:
        form = TourForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('home')


def tour_detail(request, id):
    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:
        return render(request, 'main/tour_not_found.html')

    tour_type_display = tour.get_display_for_tour_type()

    return render(request, 'main/tour_detail.html', {
        'tour': tour,
        'tour_type_display': tour_type_display
    })


def tour_delete(request, id=0):
    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:
        return render(request, 'main/tour_not_found.html')

    tour.delete()

    return redirect('all_tours')


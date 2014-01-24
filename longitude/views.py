from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from longitude.models import Brand, Location
from django.template import RequestContext, loader



# Create your views here.
def index(request):
    context = {}
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        brands = Brand.objects.filter(name__icontains=q)
        context['q'] = q
        context['brands'] = brands

    if request.method == 'POST' and request.POST.get('add_brand', None):
        add_brand = request.POST['add_brand']
        brands = Brand.objects.create(name=add_brand)


    if request.method == 'POST' and request.POST.get('delete_brand', None):
        print request.POST['delete_brand']
        delete_brand = request.POST['delete_brand']
        brands = Brand.objects.filter(name=delete_brand).delete()

    if 'all' in request.GET and request.GET['all']:
        all = request.GET['all']
        brands = Brand.objects.all()
        context['all'] = all
        context['brands'] = brands

    return render(request, 'longitude/index.html', context)


def detail(request, brand_pk):

    brand = Brand.objects.get(pk=brand_pk)
    locations = Location.objects.filter(brand=brand_pk)
    context = {
        'brand': brand,
        'locations': locations

    }
    if locations.exists():
        return render_to_response('longitude/detail.html', context)
    else:
        raise Http404("No Detail page found..")








from django.shortcuts import render
from django.views.generic import TemplateView, ListView #search
from django.db.models import Q #search
from products.models import *



def product(request, product_id):
    product = Product.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


    return render(request, 'products/product.html', locals())
#search
class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query)
        )
        return object_list

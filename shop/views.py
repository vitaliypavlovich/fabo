
import logging
from django.core.cache import cache
from django.shortcuts import render, redirect

from shop.models import Product

logger = logging.getLogger(__name__)



def product_view(request):
    title = request.GET.get('title')
    purchases__count = request.GET.get('purchases__count')
    result = cache.get(f"products-view-{title}-{purchases__count}")
    if result is not None:
        return result

    products = Product.objects.all()
    title = request.GET.get('title')
    if title is not None:
        products = products.filter(title__icontains=title)
    purchases__count = request.GET.get('purchases__count')
    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    response = render(request, "index.html", {"products": products})
    cache.set(f"products-view-{title}-{purchases__count}", response, 60 * 60)
    return response

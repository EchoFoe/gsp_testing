from django.shortcuts import render, get_object_or_404
from .models import Category, Offer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def offer_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(is_active=True)
    object_list = Offer.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        object_list = object_list.filter(category=category)
    paginator = Paginator(object_list, 8)
    page = request.GET.get('page')
    try:
        offers = paginator.page(page)
    except PageNotAnInteger:
        offers = paginator.page(1)
    except EmptyPage:
        offers = paginator.page(paginator.num_pages)

    return render(request, 'job/list.html', {'category': category,
                                             'categories': categories,
                                             'page': page,
                                             'offers': offers})


def offer_detail(request, id, slug):
    offer = get_object_or_404(Offer, id=id, slug=slug, available=True)
    return render(request, 'job/detail.html', {'offer': offer})

from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Promotion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def promotion_list(request, category_slug=None, subcategory_slug=None):
    category = None
    subcategory = None
    categories = Category.objects.filter(is_active=True)
    subcategories = SubCategory.objects.filter(is_active=True)
    object_list = Promotion.objects.filter(is_active=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        object_list = object_list.filter(category=category)
    if subcategory_slug:
        subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        object_list = object_list.filter(subcategory=subcategory)
    paginator = Paginator(object_list, 50)
    page = request.GET.get('page')
    try:
        promotions = paginator.page(page)
    except PageNotAnInteger:
        promotions = paginator.page(1)
    except EmptyPage:
        promotions = paginator.page(paginator.num_pages)

    return render(request, 'ad/list.html', {'category': category,
                                            'categories': categories,
                                            'subcategory': subcategory,
                                            'subcategories': subcategories,
                                            'page': page,
                                            'promotions': promotions})


def promotion_detail(request, id, slug):
    promotion = get_object_or_404(Promotion, id=id, slug=slug, is_active=True)
    return render(request, 'ad/detail.html', {'promotion': promotion})

from django.shortcuts import render, get_object_or_404
from .models import Category, Promotion, PromotionDetails
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def promotion_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(is_active=True)
    object_list = Promotion.objects.filter(is_active=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        object_list = object_list.filter(category=category)
    paginator = Paginator(object_list, 50)
    page = request.GET.get('page')
    try:
        promotions = paginator.page(page)
    except PageNotAnInteger:
        promotions = paginator.page(1)
    except EmptyPage:
        promotions = paginator.page(paginator.num_pages)
    return render(request, "reclame/list.html", {'category': category,
                                                 'categories': categories,
                                                 'promotions': promotions})


def promotion_detail(request, id, slug):
    promotion = get_object_or_404(Promotion, id=id, slug=slug, is_active=True)
    promotion_details_main = PromotionDetails.objects.filter(is_main=True, is_active=True)
    promotion_details_not_main = PromotionDetails.objects.filter(is_not_main=True, is_active=True)
    return render(request, 'reclame/detail.html', {'promotion': promotion,
                                                   'promotion_details_main': promotion_details_main,
                                                   'promotion_details_not_main': promotion_details_not_main,
                                                   })

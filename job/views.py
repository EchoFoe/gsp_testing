from django.shortcuts import render, get_object_or_404
from .models import Category, Offer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import OfferRegistrationForm
from utils.emails import SendingEmail


# from utils.emails import SendingEmail


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


def register_job(request):
    if request.method == 'POST':
        offer_form = OfferRegistrationForm(request.POST, request.FILES)
        if offer_form.is_valid():
            print(request.POST)
            print(offer_form.cleaned_data)
            print('yes')
            data = offer_form.cleaned_data
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            middle_name = data.get('middle_name')
            name = data.get('name')
            description = data.get('description')
            email = data.get('email')
            phone = data.get('phone')
            category = data.get('category')
            image = data.get('image')
            price = data.get('price')
            start_time = data.get('start_time')
            end_time = data.get('end_time')

            # new_offer = Offer.objects.create(first_name=first_name, last_name=last_name, middle_name=middle_name,
            #                                  email=email, phone=phone, name=name, start_time=start_time,
            #                                  end_time=end_time, image=image, description=description, price=price)

            new_offer = offer_form.save(commit=False)
            # Сохраним заказ в БАЗЕ
            new_offer.save()

            # Offer.objects.create(all(new_offer))

            email = SendingEmail()
            email.sending_email(type_id=1, new_offer=new_offer)
            email.sending_email(type_id=2, email=new_offer.email, new_offer=new_offer)
            return render(request, 'job/register_job_done.html', {'new_offer': new_offer})
    else:
        offer_form = OfferRegistrationForm()
    return render(request, 'job/register_job.html', {'offer_form': offer_form})

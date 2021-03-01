from django.shortcuts import render
from .models import Product
from . import engine

def my_view(request):
    Product.objects.all().delete()
    if 'search' in request.GET and request.GET['search']:
        search = request.GET['search']
        query=engine.driverwork(search)
        #print(query)
        for item in query:
            try:
                Product.objects.create(title=item[0], price=item[1], provider=item[2], url=item[3], img=item[4])
            except Exception:
                pass
    #Product.objects.create(title='Кто правит миром? | Хомский Ноам',price='666 ₽',provider='OZON', url='https://www.ozon.ru/product/kto-pravit-mirom-166282423',img='https://cdn1.ozone.ru/s3/multimedia-c/wc250/6008333076.jpg')
    return render(
        request,
        'pages/index.html',
        {
            'elements': Product.objects.all()
        }
    )

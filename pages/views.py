from django.shortcuts import render
from .models import Product
from .models import Stats
from . import engine
from django.db.models import F

def my_view(request):
    Product.objects.all().delete()
    error = ""
    first = ""
    link = ""
    last = ""
    text = ""
    if 'search' in request.GET and request.GET['search']:
        search = request.GET['search']
        try:
            obj = Stats.objects.get(querystring=search)
            #Stats.objects.filter(querystring__in=search).update(amount=F('amount')+1)
            obj.amount += 1
            obj.save()
        except Stats.DoesNotExist:
            Stats.objects.create(querystring=search, amount=1)
        query = engine.driverwork(search)
        error = engine.errorCheck(search)
        link = 'http://127.0.0.1:8000/?search='+search
        first = error[0]
        text = error[1]
        last = error[2]
        for item in query:
            try:
                Product.objects.create(title=item[0], price=item[1], provider=item[2], url=item[3], img=item[4])
            except Exception:
                pass
    return render(
        request,
        'pages/index.html',
        {
            'elements': Product.objects.all(),
            'exception': error,
            'first': first,
            'text': text,
            'last': last,
            'link': link
        }
    )

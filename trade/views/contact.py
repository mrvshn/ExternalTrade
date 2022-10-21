from django.shortcuts import render
from trade.models import Contact


def contact(request):
    model = Contact

    return render(request, 'trade/contact.html',
                  context={'name': 'Merve Sahin'})


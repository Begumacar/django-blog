from django.shortcuts import render

def anasayfa(request):
    context={
        'isim': 'Begüm Acar'
    }
    return render(request, 'pages/anasayfa.html', context=context)
from django.shortcuts import render

def iletisim(request):
    context={
        'key': 'başlı içerik naber'
    }
    return render(request, 'pages/iletisim.html', context=context)
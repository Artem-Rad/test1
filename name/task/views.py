from django.shortcuts import render, redirect
from .models import NameModel
from django.http import JsonResponse

def name(request):
    query = NameModel.objects.all()
    number = len(query) + 1
    if request.method == 'POST':
        res = request.POST.get('your_name')
        obj = NameModel(data={f'name{number}': res})
        obj.save()
        return redirect('name')
    else:
        con = {
            'number': number
        }
        return render(request, 'name.html', con)


def json_name(request):
    lis = []
    res = NameModel.objects.all()
    for ell in res:
        lis.append(ell.data)
    return JsonResponse(lis, safe=False)
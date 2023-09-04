from django.shortcuts import render


def django_urls(request):
    return render(request,'django_urls/index.html')

def item(request,check,id = 1):
    if id == 5:
        data = {'id':id , 'letter': 'five'}

    else:
        data = {'id':id}
    print(check)
    return render(request,'django_urls/item.html',data)

def sub_item(request,id,sub_id):
    if id == sub_id:
        data = {'id':id, 'sub_id':sub_id, 'message': 'both are same'}
    else:
        data = {'id':id, 'sub_id':sub_id}
    return render(request,'django_urls/sub-item.html',data)

def custom_year(request,year = 1996):
    data = {'year': year}
    return render(request,'django_urls/year.html',data)
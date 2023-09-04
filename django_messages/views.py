from django.shortcuts import render
from .forms import *
from django.contrib import messages

# def django_messages(request):
#     if request.method == "POST":
#         fm = StudentModelForm(request.POST)
#         if fm.is_valid():
#             name = fm.cleaned_data['name']
#             fm.save()
#             messages.add_message(request,messages.INFO,f'{name} is created')

#             messages.success(request, f" welcome {request.user}")
#     else:
#         fm = StudentModelForm()
#     return render(request,'messages/index.html',{'form':fm})

def django_messages(request):
    if request.method == "POST":
        fm = StudentModelForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            fm.save()

            # custom message tag from settings
            messages.error(request, f" welcome {request.user}")

            print(messages.get_level(request))

            messages.debug(request,'this is before debug message')
            messages.set_level(request,messages.DEBUG)
            messages.debug(request,'this is after debug message')

            print(messages.get_level(request))
    else:
        fm = StudentModelForm()
    return render(request,'messages/index.html',{'form':fm})



# research on get_messages()
# from django.contrib.messages import get
# storage = get_messages(request)
# for message in storage:
# do_somethig_with_the_messages(message)
from django.shortcuts import render
from .forms import UserForm,UserInfoForm
#from .forms import forms


# Create your views here.
def index(request):
    dict = {}
    return render(request, 'login_app/index.html', context=dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'profile_pic' in request.FILES:        #FOR ALL FILES
                user_info.profile_pic = request.FILES['profile_pic']
            user_info.save()

            registered = True

    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()


    user_form = UserForm()
    user_info_form = UserInfoForm()
    diction = {'user_form': user_form, 'user_info_form': user_info_form, 'registeres':registered}
    return render(request, 'login_app/register.html', context=diction)

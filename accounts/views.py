from django.shortcuts import render , redirect

from .forms import UserForm


# Create your views here.


class SignUp(generic.CreateView):
        form_class=UserCreationForm
        success_url=reverse_lazy("")
        template_name="registration/signup.html"




# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/products')

    else:
        user_form = UserForm()

    context = {'user_form' : user_form}

    return render(request , 'registration/register.html' , context)
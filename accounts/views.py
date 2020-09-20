from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import UserCreateForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('home_page')
    else:
        form = UserCreateForm()
    return render(request, 'registration/signup.html', {'form': form})

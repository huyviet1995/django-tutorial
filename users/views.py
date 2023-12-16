from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username + ' was created')
            messages.success(req, f'Account created for {username}!')
            return redirect('food:index')
    else:
        form = UserCreationForm()
    return render(req, 'users/register.html', {'form': form})


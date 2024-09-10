from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.forms import CustomUserCreationForm


# @login_required(login_url='/accounts/login')
# def profile(request):
#     return render(request, 'pages/profile.html')

@login_required(login_url='/accounts/login')
def update_user(request):
    user = request.user
    form = CustomUserCreationForm(instance=user)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/perfil', pk=user.id)

    return render(request, 'pages/profile.html', {'form': form})


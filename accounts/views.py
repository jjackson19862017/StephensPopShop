from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.template.context_processors import csrf

from products.views import all_products

from .forms import UserLoginForm, UserProfileForm, UserRegistrationForm


# Create your views here.
def index(request):
    """
    if the user is already logged in then goes to home
    """
    if request.user.is_authenticated:
        return redirect(reverse('products'))
    """A view that displays the index page"""
    return render(request, "index.html")

@login_required
def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('index')


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user}) 


def register(request):
    """Render the registration page, this will show up on the users profile page"""
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if registration_form.is_valid() and profile_form.is_valid():
            user = registration_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            
            profile.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    args = {'user_form': registration_form, 'profile_form': profile_form}
    return render(request, 'register.html', args)

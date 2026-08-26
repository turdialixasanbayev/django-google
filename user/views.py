from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, 'home.html')

def login_page(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('profile')
    return render(request, "login.html")

@login_required
def profile_page(request):
    social_account = request.user.socialaccount_set.get(
        provider="google"
    )

    google_data = social_account.extra_data

    context = {
        "name": google_data.get("name"), # full_name
        "picture": google_data.get("picture"), # picture
        "given_name": google_data.get("given_name"), # first_name
        "family_name": google_data.get("family_name"), # last_name
    }

    return render(request, "profile.html", context)

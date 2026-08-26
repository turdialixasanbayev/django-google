from django.shortcuts import render

from django.contrib.auth.decorators import login_required


def index_view(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, "login.html")

@login_required
def profile(request):
    social_account = request.user.socialaccount_set.get(
        provider="google"
    )

    google_data = social_account.extra_data

    context = {
        "name": google_data.get("name"),
        "picture": google_data.get("picture"),
        "given_name": google_data.get("given_name"),
        "family_name": google_data.get("family_name"),
    }

    return render(request, "profile.html", context)

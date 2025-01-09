from django.shortcuts import render, redirect
from .models import Hobby
from django.contrib.auth.decorators import login_required


@login_required
def add_hobby(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            hobby, created = Hobby.objects.get_or_create(name=name)
            request.user.hobbies.add(hobby)
            return redirect("profile")
    return render(request, "user_hobbies/add_hobby.html")

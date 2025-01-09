from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required

from django.db.models import Count
from django.core.paginator import Paginator

from .models import CustomUser, FriendRequest
from user_hobbies.models import Hobby



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('login')
        else:
            print(form.errors)  # Print the errors in the console for debugging
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('homepage')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def profile_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = CustomUserCreationForm(instance=request.user)
    return render(request, "users/profile.html", {"form": form})


@login_required
def similar_users_view(request):
    user_hobbies = request.user.hobbies.all()
    similar_users = (
        CustomUser.objects.filter(hobbies__in=user_hobbies)
        .exclude(id=request.user.id)
        .annotate(common_hobbies=Count("hobbies"))
        .order_by("-common_hobbies")
    )

    # Pagination
    paginator = Paginator(similar_users, 10)
    page = request.GET.get("page")
    users_page = paginator.get_page(page)

    return render(request, "users/similar_users.html", {"users": users_page})


@login_required
def send_friend_request(request, user_id):
    to_user = CustomUser.objects.get(id=user_id)
    FriendRequest.objects.get_or_create(from_user=request.user, to_user=to_user)
    return redirect("similar_users")

@login_required
def accept_friend_request(request, request_id):
    friend_request = FriendRequest.objects.get(id=request_id)
    if friend_request.to_user == request.user:
        request.user.friends.add(friend_request.from_user)
        friend_request.delete()
    return redirect("profile")


@login_required
def homepage_view(request):
    # Fetch most popular hobbies (ordered by user count)
    popular_hobbies = Hobby.objects.annotate(user_count=Count('customuser')).order_by('-user_count')[:10]

    # Find most similar users based on hobbies
    user_hobbies = request.user.hobbies.all()
    similar_users = (
        CustomUser.objects.filter(hobbies__in=user_hobbies)
        .exclude(id=request.user.id)
        .annotate(common_hobbies=Count('hobbies'))
        .order_by('-common_hobbies')[:10]
    )

    return render(request, 'users/homepage.html', {
        'popular_hobbies': popular_hobbies,
        'similar_users': similar_users,
    })


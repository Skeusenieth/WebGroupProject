from django.urls import path
from .views import signup, login_view, profile_view, similar_users_view, send_friend_request, accept_friend_request, \
    homepage_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path("profile/", profile_view, name="profile"),
    path("similar/", similar_users_view, name="similar_users"),
    path("send_request/<int:user_id>/", send_friend_request, name="send_request"),
    path("accept_request/<int:request_id>/", accept_friend_request, name="accept_request"),
    path('homepage/', homepage_view, name='homepage'),
]

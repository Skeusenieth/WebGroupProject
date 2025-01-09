from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    hobbies = models.ManyToManyField('user_hobbies.Hobby', blank=True)

    def __str__(self):
        return self.username


class FriendRequest(models.Model):
    from_user = models.ForeignKey(CustomUser, related_name="sent_requests", on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name="received_requests", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} -> {self.to_user}"

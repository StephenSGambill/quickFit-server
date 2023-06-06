from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.URLField(
        default="https://www.nicepng.com/png/detail/1011-10113425_profile-clipart-generic-user-circle.png"
    )
    motivation = models.CharField(max_length=50)
    public = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

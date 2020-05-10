from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'accounts'

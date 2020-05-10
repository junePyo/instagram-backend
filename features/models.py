from django.db import models
from user.models import Account


class Comment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    written_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'comments'

# validator for password?

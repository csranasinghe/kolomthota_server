
from django.db import models



class Message(models.Model):
    author = models.ForeignKey('accounts.Account', on_delete = models.PROTECT)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_20_messages():
        return Message.objects.order_by('-timestamp').all()[:20]
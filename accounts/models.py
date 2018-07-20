from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Account(AbstractUser):
    USER_TYPE_CHOICES = (
        ('BP', 'Berth Planner'),
        ('SA', 'Shipping Agent'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES,  max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'


class BerthPlanner(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL,
                                   related_name='account',
                                   on_delete=models.CASCADE,
                                   primary_key=True)

    def __str__(self):
        return str(self.account)






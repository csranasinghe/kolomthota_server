from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'BP':
            BerthPlanner.objects.create(account=instance)

@receiver(post_save, sender=Account)
def save_user_profile(sender, instance, **kwargs):
    instance.account.save()




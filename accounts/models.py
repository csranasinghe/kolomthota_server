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
                                   related_name='bp_account',
                                   on_delete=models.CASCADE,
                                   primary_key=True)

    def __str__(self):
        return str(self.account)


class ShippingAgent(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL,
                                   related_name='sa_account',
                                   on_delete=models.CASCADE,
                                   primary_key=True)
    shipping_line = models.ForeignKey('shipping_line.ShippingLine',
                                      on_delete=models.CASCADE,
                                      blank=True, default='')
    is_active_agent = models.BooleanField(default=False)

    def __str__(self):
        return str(self.account)


# # TODO: Add proper post_save signal handling
# @receiver(post_save, sender=Account)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.user_type == 'BP':
#             BerthPlanner.objects.create(bp_account=instance)
#         elif instance.user_type == 'SA':
#             ShippingAgent.objects.create(sa_account=instance)
#     else:
#         instance.account.save()
#

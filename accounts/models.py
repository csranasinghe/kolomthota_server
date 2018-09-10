from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Account(AbstractUser):
    USER_TYPE_CHOICES = (
        ('BP', 'Berth Planner'),
        ('SA', 'Shipping Agent'),
        ('ADMIN', 'System Admin'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES,  max_length=10)
    def __str__(self):
        return self.get_full_name()
    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'


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


def set_staff_superuser_status(sender, instance, **kwargs):
    if instance.user_type == 'BP':
        instance.is_staff = True
    elif instance.user_type == 'ADMIN':
        instance.is_staff = True
        instance.is_superuser = True


pre_save.connect(set_staff_superuser_status, sender=Account, dispatch_uid="set_staff_superuser_status")

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class Address(models.Model):
    name = models.CharField(max_length=256, blank=True)
    street_address = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    city_area = models.CharField(max_length=128, blank=True)
    postal_code = models.CharField(max_length=32, blank=True)
    phone = models.CharField(max_length=32, blank=True, default=32)

    def __str__(self):
        return '{0}/{1}'.format(self.phone, self.street_address)

    class Meta:
        verbose_name = '地址'
        verbose_name_plural = '多个地址'


class UserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, is_staff=True, is_superuser=True, **extra_fields)

    def create_user(self, email, password=None, is_staff=False, is_active=True, **extra_fields):
        email = UserManager.normalize_email(email)
        extra_fields.pop('username', None)
        user = self.model(email=email, is_active=is_active, is_staff=is_staff, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=256, blank=True)
    addresses = models.ManyToManyField(Address, blank=True, related_name='user_addresses')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return '{0}<{1}>'.format(self.name, self.email)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '多个用户'


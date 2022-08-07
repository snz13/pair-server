from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomsUserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(verbose_name='user name', max_length=100, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    date_of_birth = models.DateField(verbose_name='date of birth', null=True)
    is_active = models.BooleanField(default=True, verbose_name='is user active')
    is_admin = models.BooleanField(default=False, verbose_name='is user admin')

    first_name = models.CharField(verbose_name='first name', max_length=255, null=True)
    last_name = models.CharField(verbose_name='last name', max_length=255, null=True)

    objects = CustomsUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    @property
    def is_staff(self):
        return self.is_admin

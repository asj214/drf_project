from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from core.models import TimeStampModel, SoftDeleteModel


class UserManager(BaseUserManager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(UserManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if not self.alive_only:
            return super().get_queryset()
        return super().get_queryset().filter(deleted_at__isnull=True)

    def create_user(self, email, name, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), name=name, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email=email, password=password, name=name, )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, TimeStampModel, SoftDeleteModel):
    email = models.EmailField('이메일', max_length=255, unique=True)
    name = models.CharField('이름', max_length=100)
    is_staff = models.BooleanField('스태프 유무', default=False)
    is_superuser = models.BooleanField('슈퍼유저', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name',
    ]

    class Meta:
        db_table = 'users'
        ordering = ['-id']

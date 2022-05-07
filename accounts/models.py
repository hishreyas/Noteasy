from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Course(models.TextChoices):
    FYBCS = 'FY19', ('FYB.sc Computer science')
    SYBCS = 'SY19', ('SYB.sc Computer science')
    TYBCS = 'TY19', ('TYB.sc Computer science')


class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Student must have an user name')
        if not email:
            raise ValueError('Student must have an email address')

        user = self.model(email=self.normalize_email(email),username = username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email='admin@noteasy.com',password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, username = username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    username = models.TextField(max_length=120,unique= True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    course = models.CharField(max_length=5,choices=Course.choices)
    is_active = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
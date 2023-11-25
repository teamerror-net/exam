from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from useraccount.manager import UserManager #import from uauth apps


class UserAccount(AbstractBaseUser,PermissionsMixin):
    class Meta:
        verbose_name_plural = "STUDENT ACCOUNT"
    profile_pic = models.ImageField(upload_to='faces/', default='faces/profile.png')
    username = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    dept = models.CharField(max_length=100)
    studentId = models.CharField(verbose_name="ID",max_length=50,unique=True)
    email = models.EmailField(max_length=100,null=True, blank=True)
    phone = models.CharField(max_length=11)
    auth_token = models.CharField(max_length=500,null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'studentId'
    REQUIRED_FIELDS = ['username','first_name', 'last_name','dept','phone']

    objects = UserManager()

    def __str__(self):
        return str(self.studentId)
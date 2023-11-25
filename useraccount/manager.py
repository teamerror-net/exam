from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, studentId, password, **extra_fields):
        if not studentId:
            raise ValueError('Student id required')
        user = self.model(studentId = studentId, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, studentId, password, **extra_fields):
        user = self.create_user(studentId, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
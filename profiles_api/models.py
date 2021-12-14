from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


# Create your models here.

class UserProfileManger(BaseUserManager):
    """ manage of user profiles """
    def create_user(self,email,name,password=None):
        """ create a new user profile """
        if not email:
            raise ValueError('User must have an enter email address')

        email= self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self,email,name,password):
        """ cerate new super user with given details"""
        user =self.create_use(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ databse model for users in the system """
    email = models.EmailField(max_length=255,unique=True) # email id
    name = models.CharField(max_length=255) # name with charter max_length
    is_active = models.BooleanField(default=True) # permission system: user profile is acctivate or not
    is_staff = models.BooleanField(default=False) # this is one for user is staff user , which is access to django admin thats why we set flase.

    objects = UserProfileManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ retrieve full name of user """
        return self.name
    def get_short_name(self):
        """ retrieve short name of user """
        return self.name
    def __str__(self):
        """ Return string representation of our user """
        return self.email



class ProfileFeedItem(models.Model):

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __self__(self):

        return self.status_text

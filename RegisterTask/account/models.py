#from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		
		user = self.model(
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
		)
		user.is_active=True
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	email 			= models.EmailField(verbose_name="email", max_length=60, unique=True)
	name			= models.CharField(verbose_name='name',max_length=60,blank=False)
	Phone			= models.IntegerField(blank=False)
	date_joined		= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin		= models.BooleanField(default=False)
	is_active		= models.BooleanField(default=False)
	is_staff		= models.BooleanField(default=True)
	is_superuser	= models.BooleanField(default=False)
	profile_image	= models.ImageField(max_length=255, upload_to='profile_pics',blank=False)
	password 		= models.CharField(max_length = 240,default='dummyPswd')	
 
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = MyAccountManager()

	def __str__(self):
		return str(self.email)+str(self.name)+str(self.Phone)

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=3)

class SecretKey(models.Model):
    key = models.CharField(max_length=32)

class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')

class InsecureView(models.Model):
    def get(self, request):
        password = request.GET.get('password')
        return HttpResponse(f'Your password is: {password}')

class CommandInjectionView(models.Model):
    def post(self, request):
        command = request.POST.get('command')
        os.system(command)
        return HttpResponse('Command executed successfully')

class SQLInjectionView(models.Model):
    def get(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = User.objects.raw(f"SELECT * FROM auth_user WHERE username='{username}' AND password='{password}'")
        return HttpResponse(f'User: {user.username}')

class XSSView(models.Model):
    def get(self, request):
        message = request.GET.get('message')
        return HttpResponse(f'<p>{message}</p>')

class CSRFView(models.Model):
    def post(self, request):
        new_password = request.POST.get('new_password')
        user = request.user
        user.set_password(new_password)
        user.save()
        return HttpResponse('Password changed successfully')

from django.db import models

# Create your models here.


class UserConfig(models.Model):
    file_name = models.CharField(max_length=255)
    account = models.CharField(max_length=255, unique=True)
    server = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    investor = models.CharField(max_length=255)
    is_enable = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_configs():
        return UserConfig.objects.filter(is_deleted=False, is_enable=True)
    
    @staticmethod
    def get_configs_by_account_id(account_id):
        try:
            return UserConfig.objects.get(account=account_id, is_deleted=False, is_enable=True)
        except:
            return False
    
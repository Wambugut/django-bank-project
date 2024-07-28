from django.db import models
from django.contrib.auth.models import User

class Bank(models.Model):
    name = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=100)
    institution_number = models.CharField(max_length=100, default='UNKNOWN_INST_NUM')
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Replace 1 with the actual default user ID

    def str(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    transit_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(default='admin@utoronto.ca')
    capacity = models.PositiveIntegerField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)

    def str(self):
        return self.name 
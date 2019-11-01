from django.db import models

class People(models.Model):
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}님의 직업은 {self.job}이고 {self.address}에 삽니다.' 

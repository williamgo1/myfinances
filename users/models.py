from django.db import models


class UserFinance(models.Model):
    username = models.CharField(max_length=100, primary_key=True, verbose_name='Логин')
    name = models.CharField(max_length=20, blank=True, verbose_name='Имя')
    surname = models.CharField(max_length=20, blank=True, verbose_name='Фамилия')
    total_amount = models.FloatField(default=0, verbose_name='Общая сумма')

    def add(self, other):
        if isinstance(other, (int, float)):
            self.total_amount += other
        else:
            return NotImplemented

    def sub(self, other):
        if isinstance(other, (int, float)):
            self.total_amount -= other
        else:
            return NotImplemented


# class OperationHistory(models.Model):
#     operation_name = models.CharField(max_length=255)



# class PiggyBank(models.Model):
#     pass
from django.db import models

# Create your models here.

class account(models.Model):
    account_name = models.CharField(max_length=40, null=True)
    account_img = models.ImageField(upload_to='img/', default='img/no_image.png', null=True)
    description = models.CharField(max_length=100, null=True, default="-")

    def __str__(self):
        return self.account_name

class deposit(models.Model):
    index = models.CharField(max_length=10, null=True, default="입금")
    amount = models.IntegerField(null=True, default=0)
    deposit_account = models.ForeignKey(account, on_delete=models.PROTECT)

    created = models.DateTimeField(null=True)

    @property
    def inAndOut(self):
        if index == "입금":
            return self.amount
        elif index == "출금":
            return self.amount * (-1)
        return self.amount

    class Meta:
        ordering = ['-created']

class asset(models.Model):
    asset_account = models.ForeignKey(account, on_delete=models.PROTECT)
    current_amount = models.IntegerField(null=True, default=0)
    created = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created']


class data(models.Model):
    currentValue1 = models.IntegerField(null=True, default=0)
    currentValue2 = models.IntegerField(null=True, default=0)
    currentValue3 = models.IntegerField(null=True, default=0)
    currentValue4 = models.IntegerField(null=True, default=0)
    currentValue5 = models.IntegerField(null=True, default=0)
    currentValue6 = models.IntegerField(null=True, default=0)
    currentValue7 = models.IntegerField(null=True, default=0)

    futureValue1 = models.IntegerField(null=True, default=0)
    futureValue2 = models.IntegerField(null=True, default=0)
    futureValue3 = models.IntegerField(null=True, default=0)
    futureValue4 = models.IntegerField(null=True, default=0)
    futureValue5 = models.IntegerField(null=True, default=0)
    futureValue6 = models.IntegerField(null=True, default=0)
    futureValue7 = models.IntegerField(null=True, default=0)


    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created']
from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name="wallet_user",
        on_delete=models.CASCADE
    )
    name = models.CharField("Name", max_length=50)


class Operation(models.Model):
    class OperationType(models.TextChoices):
        INCOME = "Income"
        EXPENSE = "Expense"

    wallet = models.ForeignKey(
        to=Wallet,
        related_name="operation_wallet",
        on_delete=models.CASCADE
    )
    _type = models.CharField(
        "Operation type",
        choices=OperationType.choices,
        default=OperationType.INCOME,
        max_length=10
    )
    amount = models.BigIntegerField("Amount")
    comment = models.CharField("Comment", max_length=100, null=True)

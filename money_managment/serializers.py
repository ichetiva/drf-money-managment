from rest_framework import serializers

from money_managment.models import Wallet, Operation


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("id", "name",)


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ("id", "wallet", "_type", "comment", "amount",)

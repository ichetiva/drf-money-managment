from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from money_managment.models import Wallet
from money_managment.serializers import WalletSerializer, OperationSerializer


class CreateWalletAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WalletSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class UpdateWalletAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WalletSerializer

    def update(self, request, *args, **kwargs):
        wallet_id = int(request.data.get("id", None))
        if not wallet_id:
            return Response(
                {
                    "message": "Field 'id' (wallet id) is not found in data"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            db_wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist:
            return Response(
                {
                    "message": "Wallet not found"
                }, status=status.HTTP_404_NOT_FOUND
            )
        if not db_wallet:
            return Response(
                {
                    "message": f"Wallet with ID '{wallet_id}' is not found"
                }, status=status.HTTP_404_NOT_FOUND
            )
        if db_wallet.user != request.user:
            return Response(
                {
                    "message": "Forbidden for you"
                }, status=status.HTTP_403_FORBIDDEN
            )
        serializer = self.serializer_class(db_wallet, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class DeleteWalletAPIView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        wallet_id = int(request.data.get("id", None))
        if not wallet_id:
            return Response(
                {
                    "message": "Field 'id' (wallet id) is not found in data"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            db_wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist:
            return Response(
                {
                    "message": "Wallet not found"
                }, status=status.HTTP_404_NOT_FOUND
            )
        if not db_wallet:
            return Response(
                {
                    "message": f"Wallet with ID '{wallet_id}' is not found"
                }, status=status.HTTP_404_NOT_FOUND
            )
        if db_wallet.user != request.user:
            return Response(
                {
                    "message": "Forbidden for you"
                }, status=status.HTTP_403_FORBIDDEN
            )
        db_wallet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DetailWalletAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WalletSerializer

    def list(self, request, *args, **kwargs):
        wallet_id = int(request.GET.get("id", None))
        if not wallet_id:
            return Response(
                {
                    "message": "Field 'id' (wallet id) is not found in data"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            db_wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist:
            return Response(
                {
                    "message": "Wallet not found"
                }, status=status.HTTP_404_NOT_FOUND
            )
        if not db_wallet:
            return Response(
                {
                    "message": f"Wallet with ID '{wallet_id}' is not found"
                }, status=status.HTTP_404_NOT_FOUND
            )
        if db_wallet.user != request.user:
            return Response(
                {
                    "message": "Forbidden for you"
                }, status=status.HTTP_403_FORBIDDEN
            )
        serializer = self.serializer_class(db_wallet)
        return Response(serializer.data)


class CreateOperationAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OperationSerializer

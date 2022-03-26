from django.urls import path

from money_managment import views

urlpatterns = [
    # wallets
    path("wallets/create/", views.CreateWalletAPIView.as_view(), name="create-wallet"),
    path("wallets/edit/", views.UpdateWalletAPIView.as_view(), name="edit-wallet"),
    path("wallets/delete/", views.DeleteWalletAPIView.as_view(), name="delete-wallet"),
    path("wallets/get/", views.DetailWalletAPIView.as_view(), name="detail-wallet"),

    # operations
    path("operations/create/", views.CreateOperationAPIView.as_view(), name="create-operation"),
]

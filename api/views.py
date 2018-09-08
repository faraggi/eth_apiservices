from rest_framework import authentication, permissions, generics

from .models import Transaction
from .serializers import TransactionSerializer


class NewTransactionView(generics.CreateAPIView):
    serializer_class = TransactionSerializer


class TransactionView(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = Transaction.objects.all()
        TxHash = self.request.query_params.get('TxHash', None)
        if TxHash is not None:
            queryset = queryset.filter(TxHash=TxHash)
        return queryset

from rest_framework import authentication, permissions, generics

from .models import Transaction
from .serializers import TransactionSerializer


class NewTransactionView(generics.CreateAPIView):
    serializer_class = TransactionSerializer


class TransactionView(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication, )
    serializer_class = TransactionSerializer
    # permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        queryset = Transaction.objects.all()
        tx_hash = self.request.query_params.get('tx_hash', None)
        if tx_hash is not None:
            queryset = queryset.filter(tx_hash=tx_hash)
        return queryset

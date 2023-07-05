from rest_framework.views import APIView, Request, Response, status

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountView(APIView):
    def get(self, request: Request) -> Response:
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

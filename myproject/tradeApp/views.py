from rest_framework.views import APIView
from rest_framework.response import Response
from .models import trade
from .serialize import tradeSerializer

class tradeList(APIView):
    def get(self, request):
        trade1 = trade.objects.all()
        serialize = tradeSerializer(trade1, many = True)
        return Response(serialize.data)


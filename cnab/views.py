from rest_framework.generics import (ListCreateAPIView)
from cnab.models import Cnab
from cnab.serializers import CnabSerializer
from rest_framework.views import Response, status


class ListCreateCnabView(ListCreateAPIView):
    queryset = Cnab.objects.all()
    serializer_class = CnabSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        
        file = self.request.FILES['file']
        rows = file.readlines()
        try:
            for row in rows:
                
                decoded_row = row.decode("utf-8")
                Cnab.objects.bulk_create([
                            Cnab(transaction_type = decoded_row[0:1],
                            date = decoded_row[1:9],
                            value= int(decoded_row[9:19])/100,
                            CPF= decoded_row[19:30],
                            card= decoded_row[30:42],
                            hour= decoded_row[42:48],
                            owner= decoded_row[48:62],
                            store_name= decoded_row[62:81])
                            ])

        except:
            return Response('Invalid file type', status=status.HTTP_400_BAD_REQUEST)

        return Response('Successfully saved file', status=status.HTTP_201_CREATED)
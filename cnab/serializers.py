from rest_framework import serializers
from cnab.models import Cnab


class CnabSerializer(serializers.ModelSerializer):
    
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(CnabSerializer, self).__init__(many=many, *args, **kwargs)
        
    class Meta:
        model = Cnab
        fields = "__all__"
    
        read_only_fields = [
            "transaction_type",
            "date",
            "value",
            "CPF",
            "card",
            "hour",
            "owner",
            "store_name"]
        
        extra_kwargs = {'file': {'write_only': True}}
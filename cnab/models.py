from django.db import models
from django.core.validators import RegexValidator


class TransactionTypes(models.IntegerChoices):
    DEBITO = 1, "Débito"
    BOLETO = 2, "Boleto"
    FINANCIAMENTO = 3, "Financiamento"
    CREDITO = 4, "Crédito"
    EMPRESTIMO = 5, "Recebimento Empréstimo"
    VENDAS = 6, "Vendas"
    TED = 7, "Recebimento TED"
    DOC = 8, "Recebimento DOC"
    ALUGUEL = 9, "Aluguel"


class Cnab(models.Model):
    transaction_type = models.IntegerField(choices=TransactionTypes.choices)
    date = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{1,8}$')])
    value = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    CPF = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,11}$')])
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,6}$')])
    owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)

    file = models.FileField(upload_to='uploads/')

    class Meta:
        ordering = ["id"]


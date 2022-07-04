from django.db import models
import datetime as dt

class trade(models.Model):
    trader = models.CharField(max_length=25)
    counterparty = models.CharField(max_length=256)
    instrumentId = models.IntegerField
    instrumentName = models.CharField(max_length=256)
    tradeDateTime = models.DateTimeField(dt.datetime)
    tradeId = models.IntegerField

    def __str__(self):
        return self.trader


class TradeDetails(models.Model):
    buySellIndicator = models.CharField(max_length=5)
    price = models.IntegerField
    quantity = models.IntegerField
from django.contrib import admin
from .models import Region, Department, Arrondissement, Order, School, Cycle, Offer, Infrastructure
from .models import LetterAl, Sex, Detail, OldClass, StatusPsl, Personal, Appart

admin.site.register(Region)
admin.site.register(Department)
admin.site.register(Arrondissement)
admin.site.register(Order)
admin.site.register(School)
admin.site.register(Cycle)
admin.site.register(Offer)
admin.site.register(Infrastructure)
admin.site.register(LetterAl)
admin.site.register(Sex)
admin.site.register(Detail)
admin.site.register(OldClass)
admin.site.register(StatusPsl)
admin.site.register(Personal)
admin.site.register(Appart)

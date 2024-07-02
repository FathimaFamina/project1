from django.contrib import admin
from poll.models import Person
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=('id','fname','lname','city')

admin.site.register(Person,PersonAdmin)
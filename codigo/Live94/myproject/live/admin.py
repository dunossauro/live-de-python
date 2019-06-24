from django.contrib import admin
from .models import Live


@admin.register(Live)
class LiveAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'get_guest',
                    'like', 'unlike', 'like_frequence')
    search_fields = ('title', 'guest__first_name')

    def get_guest(self, obj):
        if obj.guest:
            return obj.guest.get_full_name()

    get_guest.short_description = 'Convidado'

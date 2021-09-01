from django.urls import path
from myproject.live import views as v


app_name = 'live'


urlpatterns = [
    path('', v.live_list, name='live_list'),
    path('<int:pk>/', v.live_detail, name='live_detail'),
    path('add/', v.LiveCreate.as_view(), name='live_add'),
    path('json/', v.live_json, name='live_json'),
]

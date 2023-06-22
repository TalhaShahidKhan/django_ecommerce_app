from django.urls import path
from purchase.views import purchase_start_view,purchase_stopped_view,purchase_success_view
urlpatterns = [
    path('start/',purchase_start_view,name="start"),
    path('success/',purchase_success_view,name="success"),
    path('stopped/',purchase_stopped_view,name="stopped"),
]
app_name = 'purchase'
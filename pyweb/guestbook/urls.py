from django.urls import path
from guestbook import views

urlpatterns = [
    path('',views.list),
    path('write',views.write),
    path('gb_insert',views.insert),
    path('passwd_check',views.passwd_check),
    path('gb_update',views.update),
    path('gb_delete',views.delete),
]
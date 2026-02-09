from django.urls import path
from . import views
urlpatterns = [
    path('catalog/', views.course_form),
    path('details/',views.course_details,name='coursedetails'),
    path('delete/<int:sid>',views.course_delete),
    path('update/<int:sid>',views.course_update),
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('foodcategory/',views.getCategories),
    path('foodcategory/create/',views.creatCategory),
    path('foodcategory/<str:pk>/',views.getCategorybyId),
    path('foodcategory/<str:pk>/update/',views.updateCategory),
    path('foodcategory/<str:pk>/delete/',views.deleteCategory)
]
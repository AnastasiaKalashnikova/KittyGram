from django.urls import path # type: ignore


from cats.views import cat_list, cat_detail

urlpatterns = [
   path('cats/', cat_list),
   path('cats/<int:pk>/', cat_detail)
]



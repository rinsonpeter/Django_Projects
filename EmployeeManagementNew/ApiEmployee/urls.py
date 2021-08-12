from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ApiEmployee.views import ViewDept

# urlpatterns = [
#     path('products/', Product.as_view()),
#     path('products/<int:pk>', ProductDetail.as_view()),
#     path('purchases/',Purchases.as_view())
# ]

urlpatterns = [
    path('department/', ViewDept.as_view()),
]
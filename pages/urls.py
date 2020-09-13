from django.urls import path
from pages import views
from accounts import views as accounts_views
from orders import views as orders_views
from shopcart import views as shopcart_views

urlpatterns = [
    path('', views.home_page_view, name="home_page"),
    #Products
    path('products/<int:category_id>', views.category_view, name="category"),
    path('products/detail/<int:product_id>', views.product_detail_view, name="product_detail"),
    #Accounts
    path('signup/', accounts_views.signup, name='signup'),
    #Orders
    path('orders/', orders_views.order_list, name='order_list'),
    path('orders/<int:id>', orders_views.order_detail, name='order_detail'),
    path('orders/order', orders_views.orderproduct, name='orderproduct'),
    #Shopcart
    path('shopcart/', shopcart_views.shopcart_list, name='shopcart_list'),
    path('addtocart/<int:id>', shopcart_views.shopcart_add, name='addtocart'),
    path('deletefromcart/<int:id>', shopcart_views.shopcart_delete, name='deletefromcart'),
]
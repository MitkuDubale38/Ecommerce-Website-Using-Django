from django.urls import path
from .views import home,SearchResultsView,Products,Product_Detail,ReviewProduct,cart_add,item_clear,item_increment,item_decrement,cart_clear,cart_detail,contact,orders


urlpatterns = [

    path('', home.as_view(), name="home"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('products/', Products.as_view(), name='products'),
    path('products/<int:pk>', Product_Detail.as_view(), name="product_detail"),
    path('Review/<int:pk>/',  ReviewProduct, name="review"),
    path('contact_us/',  contact, name="contact_us"),
    path('checkout/',  orders, name="checkout"),


    path('cart/add/<int:id>/',cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/',item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/',cart_detail,name='cart_detail'),

]
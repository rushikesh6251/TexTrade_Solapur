"""Online_Grocery_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from grocery.views import *
from django.conf.urls.static import static
from django.conf import settings
from grocery.views import create_order, payment_success
from grocery import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('signup',Signup,name="signup"),
	path('about/',About,name='about'),
	path('contact/',Contact,name='contact'),
    path('login',Login,name="login"),
    path('logout',Logout,name="logout"),
    path('view_vendors', view_vendors, name='view_vendors'),
    path("view_orders",view_orders, name="view_orders"),
    path('view_user',View_user,name="view_user"),
    path('add_product',Add_Product,name="add_product"),
    path('view_feedback', View_feedback, name='view_feedback'),
    path('view_orders', view_orders, name='view_orders'),
    path('view_product(?P<int:pid>)', View_product, name='view_product'),
    path('admin_view_product', Admin_View_product, name='admin_view_product'),
    path('vendor_view_product', vendor_view_product, name='vendor_view_product'),
    path('login_admin',Admin_Login,name="login_admin"),
    path('admin_viewBooking', Admin_View_Booking, name='admin_viewBooking'),
    path('view_categary/', View_Categary, name='view_categary'),
    path('add_categary', Add_Categary, name='add_categary'),
    path('add_cart(?P<int:pid>)', Add_Cart, name='add_cart'),
    path('delete_product(?P<int:pid>)', delete_product, name='delete_product'),
    path('delete_user(?P<int:pid>)', delete_user, name='delete_user'),
    path('delete_feedback(?P<int:pid>)', delete_feedback, name='delete_feedback'),
    path('cart', view_cart, name='cart'),
    path('payment(?P<total>[0-9]+)', payment, name='payment'),
    
    path('booking/<str:pid>/', Booking_order, name="booking_order"),

    path('process_booking/', process_booking, name="process_booking"), 
    path('review/<int:product_id>/', add_review, name='add_review'),
    path("payment/<int:total>/", payment, name="payment"),
    path('pay/', views.create_order, name='create_order'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path("booking-confirmation/", booking_confirmation, name="booking_confirmation"),
    path("product/<int:product_id>/review/", add_review, name="add_review"),
    path('delete_booking/(?P<str:pid>)/(?P<bid>[0-9]+)', delete_booking, name='delete_booking'),
    path('delete_admin_booking/(?P<str:pid>)/(?P<bid>[0-9]+)', delete_admin_booking, name='delete_admin_booking'),
    path('booking_detail/(?P<str:pid>)/(?P<bid>[0-9]+)', booking_detail, name='booking_detail'),
    path('admin_booking_detail/<str:pid>/<int:bid>/<int:uid>/', views.admin_booking_detail, name='admin_booking_detail'),

    path('vendor_view_booking_detail/(?P<str:pid>)/(?P<bid>[0-9]+)/(?P<uid>[0-9]+)', vendor_view_booking_detail, name='vendor_view_booking_detail'),

    path('signupvender', signupvender, name="signupvendor"),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    # path('add_review/<int:pid>/<int:bid>/', add_review, name='add_review'),

    path('Edit_status/(?P<str:pid>)/(?P<bid>[0-9]+)', Edit_status, name='Edit_status'),
    path('remove_cart(?P<int:pid>)', remove_cart, name='remove_cart'),
    path('booking(?P<str:pid>)', Booking_order, name="booking"),
    path('view_booking', View_Booking, name='view_booking'),
    path('profile', profile, name='profile'),
    path('edit_profile', Edit_profile, name='edit_profile'),
    # path('vendor_edit_profile', Vendor_Edit_profile, name='vendor_edit_profile'),
    path('delete_category(?P<int:pid>)', delete_category, name='delete_category'),
    path('admin_home', Admin_Home, name='admin_home'),
    path('change_password', Change_Password, name="change_password"),
    path('vendor_change_password', vendor_change_password, name="vendor_change_password"),
    path('send_feedback/(?P<pid>[0-9]+)', Feedback, name='send_feedback'),
	path('edit_category/<int:pid>',edit_category, name='edit_category'),
    path('edit_product/<int:pid>',edit_product, name='edit_product'),
    path('signupvender/', signupvender, name="signupvender"),
    path('loginvender/', loginvender, name="loginvender"),
    path('vendor_home',vendor_home,name="vendor_home"),
    path('view_orders',view_orders,name="view_orders"),     
    path('view_orders_vendor',view_orders_vendor,name="view_orders_vendor"),     

    path('product/<str:booking_id>/<int:product_id>/review/', views.add_review, name='add_review'),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

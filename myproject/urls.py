from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from shopping.views import home, signup_page, login_page, display, logout_page, products, product_details, add_details, Add_To_Cart, Cart_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("signup/", signup_page, name="signup"),
    path("login/", login_page, name="login"),
    path("display/", display, name="displaypage"),
    path("logout/", logout_page, name="logout"),
    path("products/", products, name="productpage"),
    path('product_details/<int:product_id>/', product_details, name='product_details'),
    path("add/", add_details, name="add_details"),
    path("cart/<int:id>/", Add_To_Cart, name="cart"),
    path("cart/", Cart_data, name="cartdata"),
]

# Serve static and media files in production
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

# For local development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

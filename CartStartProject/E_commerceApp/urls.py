from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    UserListCreate, UserRetrieveUpdateDestroy,
    CompanyListCreate, CompanyRetrieveUpdateDestroy,
    CustomerListCreate, CustomerRetrieveUpdateDestroy,
    SellerListCreate, SellerRetrieveUpdateDestroy,
    CategoryListCreate, CategoryRetrieveUpdateDestroy,
    ProductListCreate, ProductRetrieveUpdateDestroy,
    OrderListCreate, OrderRetrieveUpdateDestroy,
    OrderItemListCreate, OrderItemRetrieveUpdateDestroy,
    AddressListCreate, AddressRetrieveUpdateDestroy,
    ReviewListCreate, ReviewRetrieveUpdateDestroy,
    CartListCreate, CartRetrieveUpdateDestroy,
    CartItemListCreate, CartItemRetrieveUpdateDestroy,
    WishlistListCreate, WishlistRetrieveUpdateDestroy,
    WishlistItemListCreate, WishlistItemRetrieveUpdateDestroy,
    PaymentListCreate, PaymentRetrieveUpdateDestroy,
    CouponListCreate, CouponRetrieveUpdateDestroy,
    ShippingMethodListCreate, ShippingMethodRetrieveUpdateDestroy
)
from drf_yasg.views import get_schema_view as get_swagger_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_swagger_view(
    openapi.Info(
        title="E-Commerce API",
        default_version='v1',
        description="API documentation for E-Commerce application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@ecommerce.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

schema_view_redoc = get_swagger_view(
    openapi.Info(
        title="E-Commerce API",
        default_version='v1',
        description="API documentation for E-Commerce application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@ecommerce.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    # JWT Authentication URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # User URLs
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    
    # Company URLs
    path('companies/', CompanyListCreate.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroy.as_view(), name='company-detail'),
    
    # Customer URLs
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-detail'),
    
    # Seller URLs
    path('sellers/', SellerListCreate.as_view(), name='seller-list-create'),
    path('sellers/<int:pk>/', SellerRetrieveUpdateDestroy.as_view(), name='seller-detail'),
    
    # Category URLs
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),
    
    # Product URLs
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
    
    # Order URLs
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroy.as_view(), name='order-detail'),
    # path('orders/<int:pk>/pay/', OrderRetrieveUpdateDestroy.as_view({'post': 'pay'}), name='order-pay'),
    
    # Order Item URLs
    path('order-items/', OrderItemListCreate.as_view(), name='order-item-list-create'),
    path('order-items/<int:pk>/', OrderItemRetrieveUpdateDestroy.as_view(), name='order-item-detail'),
    
    # Address URLs
    path('addresses/', AddressListCreate.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', AddressRetrieveUpdateDestroy.as_view(), name='address-detail'),
    
    # Review URLs
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroy.as_view(), name='review-detail'),
    
    # Cart URLs
    path('carts/', CartListCreate.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartRetrieveUpdateDestroy.as_view(), name='cart-detail'),
    
    # Cart Item URLs
    path('cart-items/', CartItemListCreate.as_view(), name='cart-item-list-create'),
    path('cart-items/<int:pk>/', CartItemRetrieveUpdateDestroy.as_view(), name='cart-item-detail'),
    
    # Wishlist URLs
    path('wishlists/', WishlistListCreate.as_view(), name='wishlist-list-create'),
    path('wishlists/<int:pk>/', WishlistRetrieveUpdateDestroy.as_view(), name='wishlist-detail'),
    
    # Wishlist Item URLs
    path('wishlist-items/', WishlistItemListCreate.as_view(), name='wishlist-item-list-create'),
    path('wishlist-items/<int:pk>/', WishlistItemRetrieveUpdateDestroy.as_view(), name='wishlist-item-detail'),
    
    # Payment URLs
    path('payments/', PaymentListCreate.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroy.as_view(), name='payment-detail'),
    
    # Coupon URLs
    path('coupons/', CouponListCreate.as_view(), name='coupon-list-create'),
    path('coupons/<int:pk>/', CouponRetrieveUpdateDestroy.as_view(), name='coupon-detail'),
    
    # Shipping Method URLs
    path('shipping-methods/', ShippingMethodListCreate.as_view(), name='shipping-method-list-create'),
    path('shipping-methods/<int:pk>/', ShippingMethodRetrieveUpdateDestroy.as_view(), name='shipping-method-detail'),

    # API Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view_redoc.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
]

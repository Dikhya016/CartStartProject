from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
# import razorpay

from .models import *
from .serializers import *

# Razorpay client setup
# razorpay_client = razorpay.Client(auth=("YOUR_RAZORPAY_KEY_ID", "YOUR_RAZORPAY_KEY_SECRET"))

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username']
    

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class CompanyListCreate(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class CompanyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = StandardResultsSetPagination
   
    

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class SellerListCreate(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class SellerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'seller', 'company']
    ordering_fields = ['price', 'created_at']
    search_fields = ['name', 'description']
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    # @action(detail=True, methods=['post'])
    # def pay(self, request, pk=None):
    #     order = self.get_object()
    #     amount = int(order.total_amount * 100)  # Razorpay amount should be in paise
    #     payment = razorpay_client.order.create({"amount": amount, "currency": "INR", "payment_capture": "1"})
    #     order.razorpay_order_id = payment['id']
    #     order.save()
    #     return Response(payment)

class OrderItemListCreate(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class OrderItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class AddressListCreate(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class AddressRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class ReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class CartListCreate(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class CartRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class CartItemListCreate(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class CartItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class WishlistListCreate(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class WishlistRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class WishlistItemListCreate(generics.ListCreateAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class WishlistItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class PaymentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class CouponListCreate(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class CouponRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class ShippingMethodListCreate(generics.ListCreateAPIView):
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethodSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class ShippingMethodRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethodSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

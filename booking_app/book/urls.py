from django.urls import path
from .views import HotelListCreateView, RoomListView, BookingListCreateView, BookingDetailView,UserBookingListView

urlpatterns = [
    path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('rooms/', RoomListView.as_view(), name='room-list'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('mybookings/', UserBookingListView.as_view(), name='user-bookings'),
]
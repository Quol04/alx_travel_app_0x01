from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Listings.
    Provides CRUD operations.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Bookings.
    Provides CRUD operations.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

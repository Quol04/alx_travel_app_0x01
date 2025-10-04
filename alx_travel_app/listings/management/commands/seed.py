from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Clear old data
        Listing.objects.all().delete()

        # Create sample listings
        listings_data = [
            {"title": "Beachfront Villa", "description": "Beautiful villa by the beach", "price_per_night": 250, "location": "Mombasa"},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains", "price_per_night": 150, "location": "Mt. Kenya"},
            {"title": "City Apartment", "description": "Modern apartment in the city center", "price_per_night": 100, "location": "Nairobi"},
        ]

        for data in listings_data:
            Listing.objects.create(**data, available=True)

        self.stdout.write(self.style.SUCCESS("Successfully seeded listings"))

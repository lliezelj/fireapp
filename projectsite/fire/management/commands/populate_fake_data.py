from django.core.management.base import BaseCommand
from faker import Faker
from fire.models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions

class Command(BaseCommand):
    help = 'Populate database with fake data using Faker'

    def handle(self, *args, **options):
        fake = Faker()

        # Populate Locations table
        for _ in range(10):  # Generate 10 fake locations
            Locations.objects.create(
                name=fake.name(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )

        # Populate Incidents table
        for _ in range(10):  # Generate 10 fake incidents
            location = Locations.objects.order_by('?').first()  # Get a random location
            Incident.objects.create(
                location=location,
                date_time=fake.date_time(),
                severity_level=fake.random_element(elements=('Minor Fire', 'Moderate Fire', 'Major Fire')),
                description=fake.text()
            )

        # Populate FireStation table
        for _ in range(10):  # Generate 10 fake fire stations
            FireStation.objects.create(
                name=fake.company(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )

        # Populate Firefighters table
        for _ in range(10):  # Generate 10 fake firefighters
            Firefighters.objects.create(
                name=fake.name(),
                rank=fake.job(),
                experience_level=fake.random_element(elements=('Probationary Firefighter', 'Firefighter I', 'Firefighter II', 'Firefighter III', 'Driver', 'Captain', 'Battalion Chief')),
                station=fake.random_element(elements=('Station 1', 'Station 2', 'Station 3'))
            )

        for _ in range(10):  # Generate 10 fake fire trucks
            station = FireStation.objects.order_by('?').first()  # Get a random fire station
            FireTruck.objects.create(
                truck_number=fake.uuid4(),
                model=fake.word(),
                capacity=fake.random_int(min=1000, max=5000),
                station=station
            )

        
        for _ in range(10):  # Generate 10 fake weather conditions
            incident = Incident.objects.order_by('?').first()  # Get a random incident
            WeatherConditions.objects.create(
                incident=incident,
                temperature=fake.random_int(min=-10, max=40),
                humidity=fake.random_int(min=30, max=90),
                wind_speed=fake.random_int(min=0, max=30),
                weather_description=fake.sentence()
            )

        self.stdout.write(self.style.SUCCESS('Fake data populated successfully'))
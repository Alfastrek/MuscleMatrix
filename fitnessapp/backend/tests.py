from django.test import TestCase
from .models import Subscriber, Recommendation
from .views import RecommendationGenerator

class RecommendationGenerationTestCase(TestCase):
    def setUp(self):
        
        self.subscriber_build_muscle = Subscriber.objects.create(
            name="John", 
            goal="Build Muscle", 
            age=30,  
            weight=70.0,  
            height=170.0,  
            gender="Male"  
        )
        self.subscriber_lose_weight = Subscriber.objects.create(
            name="Alice", 
            goal="Lose Weight", 
            age=25, 
            weight=60.0, 
            height=160.0, 
            gender="Female"
        )
        self.subscriber_maintain_fitness = Subscriber.objects.create(
            name="Bob", 
            goal="Maintain Fitness", 
            age=35, 
            weight=75.0, 
            height=175.0, 
            gender="Male"
        )
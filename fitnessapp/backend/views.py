from django.shortcuts import render
from .models import Subscriber, Recommendation

class RecommendationGenerator:
    @staticmethod
    def generate_recommendations(subscriber_id):
        subscriber = Subscriber.objects.get(id=subscriber_id)
        recommendations = []

        # Generate workout recommendation
        workout_recommendation = RecommendationGenerator.generate_workout_recommendation(subscriber)
        recommendations.append(workout_recommendation)

        # Generate diet recommendation
        diet_recommendation = RecommendationGenerator.generate_diet_recommendation(subscriber)
        recommendations.append(diet_recommendation)

        # Save recommendations to database
        Recommendation.objects.bulk_create(recommendations)

    @staticmethod
    def generate_workout_recommendation(subscriber):
        # Determine workout plan based on subscriber's fitness goals
        if subscriber.goal == 'Build Muscle':
            workout_plan = "Day 1 (Chest and Triceps):\n- Bench press\n- Incline dumbbell press\n- Tricep dips\n- Skull crushers\n\n"
            workout_plan += "Day 2 (Back and Biceps):\n- Pull-ups\n- Bent-over rows\n- Bicep curls\n- Hammer curls\n\n"
            workout_plan += "Day 3 (Legs and Shoulders):\n- Squats\n- Deadlifts\n- Shoulder press\n- Lateral raises\n"
        elif subscriber.goal == 'Lose Weight':
            workout_plan = "Day 1 (Full Body):\n- Squats\n- Push-ups\n- Lunges\n- Rows\n- Planks\n\n"
            workout_plan += "Day 2 (Cardio):\n- Running or cycling\n- High-intensity interval training\n\n"
            workout_plan += "Day 3 (Rest or Active Recovery):\n- Yoga or Pilates\n- Light stretching\n"
        else:  # Maintain Fitness
            workout_plan = "Day 1 (Upper Body):\n- Push-ups\n- Pull-ups\n- Shoulder press\n- Rows\n- Bicep curls\n- Tricep dips\n\n"
            workout_plan += "Day 2 (Lower Body):\n- Squats\n- Lunges\n- Deadlifts\n- Calf raises\n- Leg curls\n\n"
            workout_plan += "Day 3 (Cardio):\n- Running or cycling\n- Swimming\n- Any cardio activity of choice\n"
        return Recommendation(subscriber=subscriber, recommendation_type='Workout Plan', recommendation_text=workout_plan)

    @staticmethod
    def generate_diet_recommendation(subscriber):
        # Determine diet plan based on subscriber's fitness goals
        if subscriber.goal == 'Build Muscle':
            diet_plan = "Meal 1 (Breakfast):\n- Protein-rich smoothie with banana, oats, protein powder, and almond milk\n\n"
            diet_plan += "Meal 2 (Snack):\n- Greek yogurt with berries and a handful of almonds\n\n"
            diet_plan += "Meal 3 (Lunch):\n- Grilled chicken breast with sweet potato and steamed broccoli\n\n"

        elif subscriber.goal == 'Lose Weight':
            diet_plan = "Meal 1 (Breakfast):\n- Egg white omelette with spinach and tomatoes\n\n"
            diet_plan += "Meal 2 (Snack):\n- Apple slices with peanut butter\n\n"
            diet_plan += "Meal 3 (Lunch):\n- Mixed greens salad with grilled chicken breast and balsamic vinaigrette\n\n"

        else:  
            diet_plan = "Meal 1 (Breakfast):\n- Whole grain toast with scrambled eggs and avocado\n\n"
            diet_plan += "Meal 2 (Snack):\n- Cottage cheese with pineapple chunks\n\n"
            diet_plan += "Meal 3 (Lunch):\n- Turkey and avocado wrap with whole wheat tortilla and mixed greens\n\n"

        return Recommendation(subscriber=subscriber, recommendation_type='Diet Plan', recommendation_text=diet_plan)


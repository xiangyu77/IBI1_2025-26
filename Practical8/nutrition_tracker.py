# nutrition_tracker.py
# IBI1 Practical 8: Nutrition Data Tracker

class food_item:
    """Represents a food item with name and nutritional values."""
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories   # in kcal
        self.protein = protein     # in grams
        self.carbs = carbs         # in grams
        self.fat = fat             # in grams


def daily_summary(items):
    """
    Calculate total nutrition for a list of food_item objects.
    Print summary and warnings if calories > 2500 or fat > 90g.
    """
    total_cal = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0

    for item in items:
        total_cal += item.calories
        total_protein += item.protein
        total_carbs += item.carbs
        total_fat += item.fat

    # Print report
    print("======== Daily Nutrition Summary ======")
    print(f"Total Calories: {total_cal:.1f} kcal")
    print(f"Total Protein:  {total_protein:.1f} g")
    print(f"Total Carbohydrates: {total_carbs:.1f} g")
    print(f"Total Fat:      {total_fat:.1f} g")

    # Warnings
    if total_cal > 2500:
        print(f"⚠️ Warning: Calorie intake exceeds 2500 kcal (actual: {total_cal:.1f})")
    if total_fat > 90:
        print(f"⚠️ Warning: Fat intake exceeds 90 g (actual: {total_fat:.1f})")


# Example usage (runs only when this script is executed directly)
if __name__ == "__main__":
    # Create some food items
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    pizza_slice = food_item("Pizza slice", 285, 12, 36, 10)
    chocolate_bar = food_item("Chocolate bar", 210, 2, 24, 13)

    # List of items consumed in 24 hours
    daily_meals = [apple, pizza_slice, chocolate_bar, pizza_slice]

    # Calculate and report
    daily_summary(daily_meals)
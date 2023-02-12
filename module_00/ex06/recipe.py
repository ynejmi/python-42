cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
                'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
                'prep_time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
                'prep_time': 15
    }
}


def print_recipe_names():
    print("Recipes:")
    for recipe in cookbook:
        print(recipe)


def print_recipe(recipe):

    if not recipe:
        print("Recipe name cannot be empty")
        return
    if recipe not in cookbook:
        print("Recipe not found")
    elif recipe in cookbook:
        print("Recipe for", recipe)
        print(" Ingredients list:", cookbook[recipe]['ingredients'])
        print(" To be eaten for", cookbook[recipe]['meal'])
        print(" Takes", cookbook[recipe]['prep_time'], "minutes of cooking")


def delete_recipe(recipe):
    if recipe not in cookbook:
        print("Recipe not found")
    else:
        del cookbook[recipe]


def add_recipe():
    recipe = input(">>> Enter a name: ")

    if recipe in cookbook:
        print("Recipe already exists")
        return

    if not recipe:
        print("Recipe name cannot be empty")
        return

    if not recipe.isalpha():
        print("Recipe name must be alpha")
        return

    if len(recipe) > 20:
        print("Recipe name must be less than 20 characters")
        return

    ingredients = []
    ingredient = input(">>> Enter ingredients: ")
    while ingredient:
        if not ingredient:
            print("Ingredient name cannot be empty")
            return

        if not ingredient.isalpha():
            print("Ingredient name must be alpha")
            return

        if len(ingredient) > 20:
            print("Ingredient name must be less than 20 characters")
            return

        ingredients.append(ingredient)
        ingredient = input()

    meal = input(">>> Enter a meal type: ")

    if not meal:
        print("Meal type cannot be empty")
        return

    if not meal.isalpha():
        print("Meal type must be alpha")
        return

    if len(meal) > 20:
        print("Meal type must be less than 20 characters")
        return

    prep_time = input(">>> Enter a preparation time: ")

    if not prep_time:
        print("Preparation time cannot be empty")
        return

    if not prep_time.isdigit():
        print("Preparation time must be digits")
        return

    if len(prep_time) > 5:
        print("Preparation time must be less than 5 characters")
        return
    # add to cookbook
    cookbook[recipe] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }

print("Welcome to the Python Cookbook !")
print("List of available option:")
print("1: Add a recipe")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit")
print("Please select an option:")
option = input(">> ")
while option != "5":
    if option == "1":
        add_recipe()
    elif option == "2":
        recipe = input("Please enter a recipe name to delete it:\n>> ")
        delete_recipe(recipe)
    elif option == "3":
        recipe = input("Please enter a recipe name to get its details:\n>> ")
        print_recipe(recipe)
    elif option == "4":
        print_recipe_names()
    else:
        print("Sorry, this option does not exist.")
        print("List of available option:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")

    print("Please select an option:")
    option = input(">> ")

print("Cookbook closed. Goodbye !")

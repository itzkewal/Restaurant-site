import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from restaurant.models import Category, MenuItem

def seed():
    # Create Categories
    apps, _ = Category.objects.get_or_create(name='Appetizers', slug='appetizers')
    mains, _ = Category.objects.get_or_create(name='Main Course', slug='mains')
    desserts, _ = Category.objects.get_or_create(name='Desserts', slug='desserts')
    drinks, _ = Category.objects.get_or_create(name='Drinks', slug='drinks')

    # Create Menu Items
    items = [
        {'name': 'Truffle Fries', 'category': apps, 'price': 12.99, 'description': 'Crispy fries tossed in truffle oil and parmesan.', 'image': 'menu_items/dish-1.png'},
        {'name': 'Bruschetta', 'category': apps, 'price': 10.50, 'description': 'Toasted bread topped with fresh tomatoes and basil.', 'image': 'menu_items/dish-2.png'},
        {'name': 'Ribeye Steak', 'category': mains, 'price': 34.99, 'description': 'Grain-fed ribeye grilled to perfection.', 'image': 'menu_items/dish-3.png'},
        {'name': 'Salmon Fillet', 'category': mains, 'price': 28.00, 'description': 'Pan-seared salmon with lemon butter sauce.', 'image': 'menu_items/dish-1.png'},
        {'name': 'Chocolate Lava Cake', 'category': desserts, 'price': 9.99, 'description': 'Warm chocolate cake with a molten center.', 'image': 'menu_items/dish-2.png'},
        {'name': 'Cheesecake', 'category': desserts, 'price': 8.50, 'description': 'Classic New York style cheesecake.', 'image': 'menu_items/dish-3.png'},
        {'name': 'Old Fashioned', 'category': drinks, 'price': 14.00, 'description': 'Bourbon, sugar, bitters, and orange peel.', 'image': 'menu_items/dish-1.png'},
    ]

    for item in items:
        MenuItem.objects.get_or_create(**item)

    print("Database seeded successfully!")

if __name__ == '__main__':
    seed()

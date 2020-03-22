from datetime import datetime
import random

from gallery.models import Category


def create_gallery(num=10):
    photo_list = []

    categories = Category.objects.all()

    for index in range(num):
        photo_list.append(
            {
                "pk": index,
                "title": "Photo Title",
                "image": f'https://source.unsplash.com/500x500/?nature{index}',
                "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "uploaded": datetime.now(),
                "category": random.choice(categories)
            }
        )

    return photo_list
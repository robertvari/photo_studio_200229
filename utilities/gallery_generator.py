from datetime import datetime


def create_gallery(num=10):
    photo_list = []

    for index in range(num):
        photo_list.append(
            {
                "title": "Photo Title",
                "image": f'https://source.unsplash.com/500x500/?nature{index}',
                "comment": "Photo comment",
                "uploaded": datetime.now()
            }
        )

    return photo_list
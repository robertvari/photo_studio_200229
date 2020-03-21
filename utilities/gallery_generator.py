def create_gallery(num=10):
    image_links = []

    for index in range(num):
        image_links.append(f'https://source.unsplash.com/500x500/?nature{index}')

    return image_links
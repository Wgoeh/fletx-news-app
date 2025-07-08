import random
IMAGES = [
    'https://cdn.dribbble.com/userupload/43273034/file/original-45fe1a1f6cd7427c3f2c6d536d81ff0f.jpg',
    'https://cdn.dribbble.com/userupload/15656345/file/original-e8705080f81f788f96d99e277034342f.jpg',
    'https://cdn.dribbble.com/userupload/43098102/file/original-52c1764e44918b9a54d70d982f70b9cb.jpg',
    'https://i.pinimg.com/736x/fe/f7/b3/fef7b3cbaeb59afc974ab04dd20741e6.jpg',
    'https://i.pinimg.com/736x/cf/12/b7/cf12b7007e8f69025dc5c389fc6a7cf4.jpg'
    'https://i.pinimg.com/736x/ac/c3/ba/acc3ba11c77639e59fbd120d451e0105.jpg',
    'https://i.pinimg.com/736x/10/d7/63/10d763bdddad5203a6afddcaf8fb114a.jpg',
    'https://i.pinimg.com/736x/92/e4/f4/92e4f49ab6efe52f10471c5b9f4d56c9.jpg',
    'https://alldotpy.github.io/FletX/assets/logo/fletx_t.png'
]

def with_random_img(article):
    """Generate article with random image"""

    article.url_to_image = random.choice(IMAGES)
    print(article.url_to_image)

    return article
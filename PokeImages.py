import requests

image_url = "https://cdn.bulbagarden.net/upload/6/6b/002MS.png"
img_data = requests.get(image_url).content
with open('images/ivysaur.jpg', 'wb') as handler:
    handler.write(img_data)
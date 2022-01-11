from PIL import Image

Photo = Image.open('C:/Users/ACER/Pictures/Pygame-Images/Terrorists/1/walk/1_terrorist_1_Walk_000.png')

changedPhoto = Photo.thumbnail((100, 100))
changedPhoto.show()
# changedPhoto.save("C:/Users/ACER/Pictures/Pygame-Images/Changed size of Terrorists")
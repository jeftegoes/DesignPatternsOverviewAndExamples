from lazy_bitmap import LazyBitmap


def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')


bmp = LazyBitmap('facepalm.jpg')
draw_image(bmp)

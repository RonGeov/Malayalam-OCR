from pgmagick import Image

img = Image()
img.density('600')

img.read('news.pdf')
img.backgroundColor('white')
img.write('news.tiff')



from PIL import ImageGrab
import datetime

d = datetime.datetime.now()
dt_now = d.strftime('%Y%m%d%H%M%S')

TARGET_NAME = ''

grabed_image = ImageGrab.grab()
grabed_image.save('images'+ str(dt_now) +'.jpg')

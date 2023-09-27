'''
In-Memory DB Image insertion Performance test
'''

import redis
import cv2
import numpy as np
import time
import io
from PIL import Image
import datetime

r = redis.StrictRedis.from_url('redis://default:nopass@127.0.0.1:6379/1')
img_path ="image.png"

img1 = cv2.imread(img_path, 1)
retval, buffer = cv2.imencode('.png', img1)

#img1_bytes = np.array(buffer).tostring()
start_time = datetime.datetime.now()
for i in range(8500):
    img1_bytes = np.array(buffer).tobytes()
    r.set(img_path, img1_bytes)
end_time = datetime.datetime.now()

elapsed_time_us = (end_time - start_time).microseconds
print(f"Elapsed time for set image into Redis : {elapsed_time_us} us")

# Decoding CV2
decoded = cv2.imdecode(np.frombuffer(img1_bytes, np.uint8), 1)
cv2.imwrite("cv2.png", decoded)

# Decoding PIL
image =  np.array(Image.open(io.BytesIO(img1_bytes))) 
cv2.imwrite("PIL.png", decoded)

# Reading Redis
img1_bytes_ = r.get(img_path)

# Decoding CV2+Redis
decoded = cv2.imdecode(np.frombuffer(img1_bytes_, np.uint8), 1)
cv2.imwrite("cv2_redis.png", decoded)

# Decoding PIL+Redis
img1_bytes_ = r.get(img_path)
decoded = np.array(Image.open(io.BytesIO(img1_bytes_))) 
cv2.imwrite("pil_redis.png", decoded)
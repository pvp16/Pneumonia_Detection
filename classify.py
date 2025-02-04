#code to classify 
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import matplotlib.pyplot as plt
model = load_model('trainedmodel.h5')
img = image.load_img('val/NORMAL/NORMAL2-IM-1430-0001.jpeg', target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
img_data = preprocess_input(x)
classes = model.predict(img_data)
plt.imshow(np.array(img))
if(classes[0][0]<=0 and classes[0][1]>0):

    print("lung infected with pneumonia") 
else:
    print("normal lung")
       

import streamlit as st

import cv2
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
def app():
  st.title(":hourglass_flowing_sand: Model Testing Page")
  
  def load_model():
    model=tf.keras.models.load_model('/content/drive/MyDrive/multi-page-app-main/apps/my_model.hdf5')
    return model
  
  with st.spinner('Model is being loaded..'):
    model=load_model()
  st.write("""
  # Cat and Dog Classification
  """
  )
  file = st.file_uploader("Please upload an image of cat or dog in", type=["jpg", "png"])
  st.set_option('deprecation.showfileUploaderEncoding', False)
  def import_and_predict(image_data, model):
        size = (180,180)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction
  if file is None:
      st.text("Please upload an image file")
  else:
      image = Image.open(file)
      st.image(image, use_column_width=True)
      prediction = import_and_predict(image, model)
      class_names=['Dog','Cat']
      st.write(prediction)
      string="This image most likely belongs to " +class_names[np.argmax(prediction)]
      st.success(string)
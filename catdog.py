from app import app
from tensorflow.keras.models import load_model
cat_dog = load_model("cat_dog_model.h5")

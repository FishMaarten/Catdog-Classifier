import os
import numpy as np
from PIL import Image
from app import app
from app.forms import UploadForm
from matplotlib.pyplot import imread
from tensorflow.keras.models import load_model

from flask import render_template, redirect, request, flash, url_for

@app.route("/", methods=["GET","POST"])
def index():
    form = UploadForm()
    if request.method == "POST":
        if request.files:
            upload = request.files["upload"].read()
            image = Image.frombytes('RGB', (128,128), upload, 'raw')
            image = np.array(image)
            cat_dog = load_model(os.environ.get("BASE_DIR") +"/cat_dog_model.h5")
            pred = cat_dog.predict(image.reshape(1,128,128,3))
            pred = "It's a" + (" dog!" if np.argmax(pred) else " cat!")
            return render_template("index.html", form=form, pred=pred)
    return render_template("index.html", form=form, pred="")

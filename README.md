# Cat or dog classification

**Author:** Maarten Fish  
Version.0.1 [changelog](https://github.com/FishMaarten/Catdog-Classifier/blob/master/resources/changelog.txt)

- **Goal:**  

Application allows user to **upload photo** of a *cat or dog*.  
A **pre-trained neural net predicts** the *class* of the animal.

**Extra**: keeps track of previous prediction score


- **Deployment:**  
**Flask** was used to handle the application [rendering](https://github.com/FishMaarten/Catdog-Classifier/blob/master/app/routes.py)
```py
@app.route("/", methods=["GET","POST"])
def index():
    form = UploadForm()
    if request.method == "POST":
        if request.files:
            upload = request.files["upload"].read()
            image = Image.frombytes('RGB', (128,128), upload, 'raw')
            cat_dog = load_model(os.environ.get("BASE_DIR") +"/cat_dog_model.h5")
            pred = cat_dog.predict(np.array(image).reshape(1,128,128,3))
            pred = "It's a" + (" dog!" if np.argmax(pred) else " cat!")
            return render_template("index.html", form=form, pred=pred)
    return render_template("index.html", form=form, pred="")
```
I learned some **java for event handling** the [index.html](https://github.com/FishMaarten/Catdog-Classifier/blob/master/app/templates/index.html)
```java
const fileField = document.getElementById("upload");                                  
fileField.addEventListener("change", (event) => {                                     
    document.getElementById("pet").style.display = "initial";                     
    document.getElementById("classify").style.display = "initial";                
    const files = event.target.files;                                             
});                                                                                   
fileField.onchange = function () {                                                    
    var reader = new FileReader();                                                        
    reader.onload = function (e) {                                                
        document.getElementById("pet").src = e.target.result;                         
    };                                                                                    
    reader.readAsDataURL(this.files[0]);                                                  
};
```
# Web application
- Try it yourself on the **heroku app  
https://catdog-classifier.herokuapp.com/**

![application screenshot](https://github.com/FishMaarten/Catdog-Classifier/blob/master/resources/catdog_screen.png)

# Technical
- **Model:** [Convolutional neural network (notebook)](https://github.com/FishMaarten/Catdog-Classifier/blob/master/resources/cat_dog.ipynb)

This model was chosen after *experimenting* on [custom convolution and pooling from scratch](https://github.com/FishMaarten/Catdog-Classifier/blob/master/resources/convolution_filter.ipynb)

It's a *simple but effective* net with an **input convolution** of only **6 kernels size 5x5**  
after which a **5x5 max pool** is applied with a **stride** of **3**

There are **2 more successive convolutions** after, with only **5 kernels each of size 3x3** followed by **another pool**

Finally the *convolution* is **flattened** and *fed forward* through 2 **dense hidden layers for classification** each with **47** *neurons*

```py
model = Sequential([
    Conv2D(6, 5, input_shape=(128,128,3), activation="relu"),
    MaxPooling2D(pool_size=5, strides=3),
    
    Conv2D(5, 3, activation="relu"),
    Conv2D(5, 3, activation="relu"),    
    MaxPooling2D(pool_size=5, strides=3),
    
    Flatten(),
    Dense(47, activation="relu"),
    Dense(47, activation="relu"),
    Dense(2, activation="softmax")
])
```
[Deeper dive](https://github.com/FishMaarten/Catdog-Classifier/blob/master/resources/tensorflow.ipynb) into tensorflow keras components and flow

- **Training:**

**Batch size 16 images running 50 epochs 25000 images each**  
First 3 epochs scored accuracy 63% 70% 73% respectively  
79% was reached after 15 epochs accuracy stalled around 80%  
Each epoch took aproximately 250 seconds totalling 3.5 hours  

- **Convolution:**

This technique takes a small, **2dim array called a kernel**;  
representing a **filter** that will be **walked across an image.**  
The resulting **condensed pixel** is the **sum of the multiples** of overlapping pixels.  
The kernel can **move across** in bigger steps called the **stride** resulting in a smaller output shape.

- **Max Pooling:**

**Pooling** is similar to convolution but the filter just returns the **highest pixel value under the shape.**  
This results in a smaller, **compressed image** depending on **pool size and stride**. 5x5 stride 3 ratio 3/5  

- **Visualization:**

![filters](https://github.com/FishMaarten/Catdog-Classifier/blob/master/resources/convolution.png)

![mnest digits](https://github.com/FishMaarten/Catdog-Classifier/blob/master/resources/mnest.png)

# Todo
- Accuracy tracker
- Object detection
- Database

# Contents
[**routes.py**](https://github.com/FishMaarten/Catdog-Classifier/blob/master/app/routes.py)
Web application renderer, core functionality  
[**index.html**](https://github.com/FishMaarten/Catdog-Classifier/blob/master/app/templates/index.html)
Html backend for the application  
[**catdog.py**](https://github.com/FishMaarten/Catdog-Classifier/blob/master/catdog.py)
Main flask app python script  
[**config.py**](https://github.com/FishMaarten/Catdog-Classifier/blob/master/config.py)
Configuration file for the flask  
[**training_logs.txt**](https://github.com/FishMaarten/Catdog-Classifier/blob/master/resources/training_logs.txt)
Epoch loss and accuracy

**Procfile** Tells heroku how to boot
```
web: gunicorn catdog:app
```
**requirements.txt** For dowloading pip packages
```
Flask==0.12.2
flask_wtf==0.14.3
PILLOW==7.2.0
numpy==1.18.5
matplotlib==3.3.1
gunicorn==20.0.4
tensorflow==2.3.0
Keras==2.4.3
```
# Changelogs

VERSION.0.1:

new file:   Procfile  
new file:   README.md  
new file:   app/__init__.py  
new file:   app/forms.py  
new file:   app/routes.py  
new file:   app/static/cat.png  
new file:   app/static/class.png  
new file:   app/static/dog.png  
new file:   app/static/upload.png  
new file:   app/static/wallpaper.jpg  
new file:   app/templates/index.html  
new file:   cat_dog_model.h5  
new file:   catdog.py  
new file:   config.py  
new file:   requirements.txt  
new file:   resources/cat_dog.ipynb  
new file:   resources/catdog_screen.png  
new file:   resources/changelog.txt  
new file:   resources/convolution.png  
new file:   resources/convolution_filter.ipynb  
new file:   resources/mnest.png  
new file:   resources/tensorflow.ipynb  
new file:   resources/training_logs.txt  

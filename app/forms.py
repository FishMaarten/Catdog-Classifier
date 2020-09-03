from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField

class UploadForm(FlaskForm):
    upload = FileField(
        "Choose a file...",
        render_kw = {"class": "upload"})
    classify = SubmitField(render_kw = {
        "style":"display: none;"})

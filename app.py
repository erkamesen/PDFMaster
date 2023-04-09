from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, send_file
from werkzeug.utils import secure_filename
import os
import time
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired

from utils.merge_pdf import PDFMaster


app = Flask(__name__)
app.config.from_pyfile("config.py")

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")



ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/merge-pdf", methods=["GET", "POST"])
def merge_pdf():
    form = UploadFileForm()
    if request.method == 'POST':
        _merger = PDFMaster()
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        file2 = request.files['file2']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            
            filename = secure_filename(file.filename)
            file.save(os.path.join(f"{app.config['UPLOAD_FOLDER']}/{_merger.current_time}", filename))
            
            filename2 = secure_filename(file2.filename)
            file2.save(os.path.join(f"{app.config['UPLOAD_FOLDER']}/{_merger.current_time}", filename2))
     
            

            filename_list = [filename, filename2]
            name = _merger.merge_pdf(filenames=filename_list)
            print(name)
            
            return send_from_directory("/home/erkam/Files/PDFMaster/utils", "result.pdf")
    else:
        return render_template("base.html", form=form)





"""
@app.route("/merge-pdf", methods=["GET", "POST"])
def merge_pdf():
    pass
"""



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
 
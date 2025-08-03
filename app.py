from flask import Flask, request, redirect, render_template

from speech2text import real_time_transcription

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/translate", methods=["GET"])
def translate():
    if request.method == "GET":
        return render_template('translate.html')

@app.route("/translate", methods=["POST"])
def transcript():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        print(request.files["file"])

        if "file" not in request.files:
            print("FIle not Found")
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            print("Empty File")
            return redirect(request.url)

        if file:
            print("Started Transcribing")
            file.save("speech.ogg")
            print(file, type(file) )
            transcript = real_time_transcription(file)
    return render_template('translate.html', transcript=transcript)

@app.route("/translator", methods=["GET", "POST"])
def translator():
    return render_template('translator.html')

if __name__ == '__main__':
    app.run(debug=True)

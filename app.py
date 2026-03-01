from flask import Flask, render_template, request, jsonify
import os

app = Flask(
    __name__,
    template_folder="web/templates",
    static_folder="web/static",
    static_url_path="/static"
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "video" not in request.files:
        return jsonify({"error": "No file selected"})

    file = request.files["video"]

    if file.filename == "":
        return jsonify({"error": "No file chosen"})

    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(save_path)

    return jsonify({"message": "Video uploaded successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
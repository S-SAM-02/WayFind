from pathlib import Path
import uuid

from flask import Flask, render_template, request, send_from_directory
from PIL import Image, UnidentifiedImageError
from werkzeug.utils import secure_filename

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/upload")
def upload_panorama():
    uploaded = request.files.get("panorama")
    if uploaded is None or not uploaded.filename:
        return render_template("index.html", error="Choose a panorama image first."), 400

    original_name = secure_filename(uploaded.filename)
    suffix = Path(original_name).suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        return render_template("index.html", error="Please upload a JPG or PNG image."), 400

    saved_name = f"{uuid.uuid4().hex}{suffix}"
    destination = UPLOAD_DIR / saved_name
    uploaded.save(destination)

    try:
        with Image.open(destination) as image:
            image.verify()
        with Image.open(destination) as image:
            width, height = image.size
            if width < 2 * height:
                destination.unlink(missing_ok=True)
                return render_template(
                    "index.html",
                    error="This image is unusually narrow for a 360° panorama. You can still use a wider equirectangular image."
                ), 400
    except (UnidentifiedImageError, OSError):
        destination.unlink(missing_ok=True)
        return render_template("index.html", error="The uploaded file is not a valid supported image."), 400

    return render_template(
        "index.html",
        image_url=f"/uploads/{saved_name}",
        image_dimensions=f"{width} × {height}",
        success="Panorama uploaded. Explore it below."
    )


@app.get("/uploads/<path:filename>")
def uploaded_file(filename):
    # Upload names are random UUIDs and never use a user-supplied path.
    return send_from_directory(UPLOAD_DIR, filename, max_age=0)


@app.errorhandler(413)
def file_too_large(_error):
    return render_template("index.html", error="The file is too large. Maximum size is 20 MB."), 413


if __name__ == "__main__":
    # Local development only. Use a production WSGI server when deploying.
    app.run(debug=True)

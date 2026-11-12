from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json()

    name = data.get("name", "").strip()
    phone = data.get("phone", "").strip()
    program = data.get("program", "").strip()

    if not name or not phone or not program:
        return jsonify({
            "success": False,
            "message": "Semua data harus diisi."
        }), 400

    # Untuk demo, data hanya dikembalikan.
    # Nantinya bisa disimpan ke database.
    return jsonify({
        "success": True,
        "message": f"Terima kasih, {name}! Konsultasi untuk program {program} berhasil dikirim."
    })


if __name__ == "__main__":
    app.run(debug=True)
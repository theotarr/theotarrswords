from flask import Flask, render_template, jsonify, request
from translator import latin_to_english, english_to_latin
from forms import get_forms

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/la_to_en", methods=["POST"])
def latin():
    if request.method == "POST":
        return jsonify({"translation": latin_to_english(request.get_json())}), 200, {"Access-Control-Allow-Origin": "*"}

@app.route("/en_to_la", methods=["POST"])
def english():
    if request.method == "POST":
        return jsonify({"translation": english_to_latin(request.get_json())}), 200, {"Access-Control-Allow-Origin": "*"}

# takes part of speech and part of def ie. "noun:canis"
@app.route("/forms", methods=["POST"])
def forms():
    return jsonify({"forms": get_forms(request.get_json())}), 200, {"Access-Control-Allow-Origin": "*"}

if __name__ == "__main__":
    app.run(debug=True)

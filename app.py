from flask import Flask, request, jsonify
from wordfreq import zipf_frequency


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/', methods=["POST"])
def main():
    words = request.form.get("words")
    res = {}
    for word in words:
        res[words] = zipf_frequency(word, 'en')
    return jsonify(res)


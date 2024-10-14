from flask import Flask, render_template, request
import flames

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("flames.html")

@app.route("/flam", methods=["POST"])
def main():
    name_1 = request.form["boy"]
    name_2 = request.form["girl"]

    get_length = flames.pros_data(name_1, name_2, [])
    flames_val = flames.flames(get_length)

    rel_word = flames.formate(flames_val)
    final = flames.result(flames_val)

    result = f"{"They" if flames_val != 2 else "There"} {rel_word} {final}"
    return render_template("flames.html", final_result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
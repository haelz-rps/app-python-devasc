import os

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.getenv("APP_PORT"))
    app.run(host="0.0.0.0", port=port)

#docker tag local-image:tagname new-repo:tagname
#docker push new-repo:tagname
#docker push haelz/abredes-devasc:tagname
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/image/<align>/<string:imgname>")
@app.route("/gallery/image/<align>/<string:imgname>")
def image(align, imgname):
    return render_template('image.html', imagename = imgname, alignment = align)

@app.route("/gallery/<urlname>")
def gallery(urlname):
    if urlname == "portraits":
        return render_template('portraits.html')
    elif urlname == "orders":
        return render_template('orders.html')
    elif urlname == "paintings":
        return render_template('paintings.html')
    return urlname


if __name__ == '__main__':
    app.run(debug=True)
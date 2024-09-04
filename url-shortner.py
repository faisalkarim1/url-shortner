from flask import Flask, request, redirect, render_template
import random
import string
app = Flask(__name__, template_folder='templates')




url_mapping = {}

def generate_short_url():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form.get('long_url')
    short_url = generate_short_url()
    url_mapping[long_url] = short_url
    return f"Shortened URL: {short_url}"

@app.route('/<short_url>')
def redirect_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url, code=302)
    else:
        return "URL not found."

if __name__ == '__main__':
    app.run(debug=True)
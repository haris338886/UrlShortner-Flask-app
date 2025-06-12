from flask import Flask, render_template, request, redirect, url_for
import random, string

app = Flask(__name__)

# In-memory database for short URLs
url_map = {}

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    if request.method == 'POST':
        original_url = request.form['original_url']
        code = generate_short_code()
        url_map[code] = original_url
        short_url = request.host_url + code
    return render_template('index.html', short_url=short_url)

@app.route('/<code>')
def redirect_to_original(code):
    original_url = url_map.get(code)
    if original_url:
        return redirect(original_url)
    return "<h3>URL not found!</h3>", 404

if __name__ == '__main__':
    app.run(debug=True)

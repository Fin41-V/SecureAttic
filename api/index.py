from flask import Flask, render_template, request

app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view-order')
def view_order():
    # This catches the [license_key] from Lemon Squeezy
    license_key = request.args.get('license_key', 'CHECK EMAIL')
    return render_template('view-order.html', license_key=license_key)

# This handles all your other pages (contact, documentation, etc.)
@app.route('/<path:path>')
def catch_all(path):
    if not path.endswith('.html'):
        path += '.html'
    return render_template(path)
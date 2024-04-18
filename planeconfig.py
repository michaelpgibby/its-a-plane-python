from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__, template_folder='.')

# Load the initial configuration from web_config.json
with open('web_config.json', 'r') as f:
    config_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', config=config_data)

@app.route('/update_config', methods=['POST'])
def update_config():
    if request.method == 'POST':
        # Convert brightness, min_altitude, and gpio_slowdown to integers
        new_config = request.form.to_dict()
        new_config['brightness'] = int(new_config.get('brightness', config_data['brightness']))
        new_config['min_altitude'] = int(new_config.get('min_altitude', config_data['min_altitude']))
        new_config['gpio_slowdown'] = int(new_config.get('gpio_slowdown', config_data['gpio_slowdown']))

        # Update the config_data dictionary with the new values
        config_data.update(new_config)

        # Save the updated config back to web_config.json
        with open('web_config.json', 'w') as f:
            json.dump(config_data, f, indent=4)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


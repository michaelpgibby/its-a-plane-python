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
        new_config['BRIGHTNESS'] = int(new_config.get('BRIGHTNESS', config_data['BRIGHTNESS']))
        new_config['MIN_ALTITUDE'] = int(new_config.get('MIN_ALTITUDE', config_data['MIN_ALTITUDE']))
        new_config['GPIO_SLOWDOWN'] = int(new_config.get('GPIO_SLOWDOWN', config_data['GPIO_SLOWDOWN']))

        # Update the config_data dictionary with the new values
        config_data.update(new_config)

        # Save the updated config back to web_config.json
        with open('web_config.json', 'w') as f:
            json.dump(config_data, f, indent=4)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


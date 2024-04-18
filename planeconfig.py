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
        new_config = request.form.to_dict()
        # Convert specific fields to integers if they exist
        for key in ['brightness', 'min_altitude', 'gpio_slowdown']:
            if key in new_config:
                try:
                    new_config[key] = int(new_config[key])
                except ValueError:
                    return f"Error: {key} must be an integer."
        # Update the config_data dictionary with the new values
        config_data.update(new_config)
        # Save the updated config back to web_config.json
        with open('web_config.json', 'w') as f:
            json.dump(config_data, f, indent=4)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


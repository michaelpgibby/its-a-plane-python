from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__, template_folder='.')

# Load the initial configuration from web_config.json
with open('web_config.json', 'r') as f:
    config_data = json.load(f)

@app.route('/')
def index():
    # Debug print to check types of values in config_data
    for key, value in config_data.items():
        print(f"Key: {key}, Value: {type(value)}")

    return render_template('index.html', config=config_data)

@app.route('/update_config', methods=['POST'])
def update_config():
    if request.method == 'POST':
        new_config = request.form.to_dict()

        # Ensure integer values for specific keys
        int_keys = ['MIN_ALTITUDE', 'GPIO_SLOWDOWN', 'BRIGHTNESS', 'LATITUDE', 'LONGITUDE']
        for key in int_keys:
            if key in new_config:
                try:
                    new_config[key] = int(float(new_config[key]))  # Convert to float first to handle values like '-81.234403'
                except ValueError:
                    # Handle invalid input gracefully
                    pass

        # Update the config_data dictionary with the new values
        config_data.update(new_config)

        # Ensure the ZONE_HOME and LOCATION_HOME values are formatted correctly
        if 'ZONE_HOME' in new_config and isinstance(new_config['ZONE_HOME'], str):
            new_config['ZONE_HOME'] = json.loads(new_config['ZONE_HOME'])
        
        if 'LOCATION_HOME' in new_config and isinstance(new_config['LOCATION_HOME'], str):
            new_config['LOCATION_HOME'] = json.loads(new_config['LOCATION_HOME'])

        # Save the updated config back to web_config.json
        with open('web_config.json', 'w') as f:
            json.dump(config_data, f, indent=4)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

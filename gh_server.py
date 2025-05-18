from flask import Flask, request, jsonify
from server.config import *
from llm_calls import *

app = Flask(__name__)


@app.route('/llm_call', methods=['POST'])
def llm_call():
    data = request.get_json()
    input_string = data.get('input', '')

    answer = classify_input(input_string)

    return jsonify({'response': answer})

@app.route('/gen_conc', methods=['POST'])
def handle_gen_conc():
    data = request.get_json()
    input_string = data.get('input', '')

    answer = generate_concept(input_string)

    return jsonify({'response': answer})


@app.route('/gen_spatial_prompt', methods=['POST'])
def gen_spatial_prompt():
    data = request.get_json()
    profile = data.get('profile', '')
    activity = data.get('activity', '')
    answer = generate_spatial_prompt(profile, activity)
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(debug=True)
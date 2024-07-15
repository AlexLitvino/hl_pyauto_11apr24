import csv
import logging
import os
import time
from enum import Enum

from flask import Flask, jsonify, request, send_file, redirect


class Operations(Enum):
    ADD = 'add'
    SUB = 'sub'
    MLP = 'mlp'
    DIV = 'div'


DATA_PATH = 'data'
STATISTICS_PATH = os.path.join(DATA_PATH, 'statistics.csv')


app = Flask(__name__)

logger = logging.getLogger()


def log_statistics(stat_file_path, stat_data):
    with open(stat_file_path, 'a') as csv_file:
        csw_writer = csv.writer(csv_file)
        csw_writer.writerow(stat_data)


@app.route('/')
def main():
    return redirect('/about', code=302)


@app.route('/api/v1/add')  # TODO: shorten url for lecture and make one general function to re-use for every endpoint
def add():
    args = request.args
    now = time.time()
    accuracy = 3
    try:
        op1 = float(args['op1'])
        op2 = float(args['op2'])
        result = op1 + op2
        result = round(result, accuracy)
        response = {'op1': op1, 'op2': op2, 'operation': Operations.ADD.value, 'result': result}
        stat_data = [now, 'SUCCESS', Operations.ADD.value, op1, op2, result]
        status_code = 200
    except Exception as e:
        response = {'error': 'Everything goes wrong:('}
        stat_data = [now, 'CRITICAL', e]
        status_code = 400
    finally:
        log_statistics(STATISTICS_PATH, stat_data)
        return jsonify(response), status_code


@app.route('/api/v1/sub')
def sub():
    args = request.args
    now = time.time()
    accuracy = 3
    try:
        op1 = float(args['op1'])
        op2 = float(args['op2'])
        result = op1 - op2
        result = round(result, accuracy)
        response = {'op1': op1, 'op2': op2, 'operation': Operations.SUB.value, 'result': result}
        stat_data = [now, 'SUCCESS', Operations.SUB.value, op1, op2, result]
    except Exception as e:
        response = {'error': 'Everything goes wrong:(', 'error_details': f'{e}'}
        stat_data = [now, 'CRITICAL', e]
    finally:
        log_statistics(STATISTICS_PATH, stat_data)
        return jsonify(response)


@app.route('/api/v1/mlp')
def mlp():
    args = request.args
    now = time.time()
    accuracy = 3
    try:
        op1 = float(args['op1'])
        op2 = float(args['op2'])
        result = op1 * op2
        result = round(result, accuracy)
        response = {'op1': op1, 'op2': op2, 'operation': Operations.MLP.value, 'result': result}
        stat_data = [now, 'SUCCESS', Operations.MLP.value, op1, op2, result]
    except Exception as e:
        response = {'error': 'Everything goes wrong:('}
        stat_data = [now, 'CRITICAL', e]
    finally:
        log_statistics(STATISTICS_PATH, stat_data)
        return jsonify(response)


@app.route('/api/v1/div')
def div():
    args = request.args
    now = time.time()
    accuracy = 3
    try:
        op1 = float(args['op1'])
        op2 = float(args['op2'])
        result = op1 / op2
        result = round(result, accuracy)
        response = {'a': op1, 'op2': op2, 'operation': Operations.DIV.value, 'result': result}
        stat_data = [now, 'SUCCESS', Operations.DIV.value, op1, op2, result]
    except Exception as e:
        response = {'error': 'Everything goes wrong:('}
        stat_data = [now, 'CRITICAL', e]
    finally:
        log_statistics(STATISTICS_PATH, stat_data)
        return jsonify(response)


@app.route('/about/')
def about():
    return send_file('templates/about.html')


if __name__ == '__main__':
    import os
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)

    port = 5000
    app.run(debug=False, port=port, host='0.0.0.0')

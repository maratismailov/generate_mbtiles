from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import subprocess
import os
from subprocess import Popen, PIPE
from subprocess import check_output
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return 'Hello 222world'


@app.route('/mbtiles/<id>')
def mbtiles(id):
    Process=subprocess.Popen(['./generateshapefile.sh', id], stdout=PIPE, stderr=PIPE)
    stdout, stderr = Process.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    filename = 'block_' + str(id) + '.mbtiles'
    os.system("qgis")
    os.rename(r'./main.mbtiles',filename)
    return send_file(filename, mimetype='application/x-sqlite3', as_attachment=True, attachment_filename=filename)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
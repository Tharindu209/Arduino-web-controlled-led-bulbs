from flask import Flask, render_template, Response, request
import serial
import time

serialcom = serial.Serial('/dev/cu.usbmodem1101', 9600) # change this to your own port
serialcom.timeout = 1

app = Flask(__name__)


def ledRedOn():
    serialcom.write(str('onRed').encode())
    
def ledRedOff():
	serialcom.write(str('offRed').encode())
 
def ledBlueOn():
    serialcom.write(str('onBlue').encode())
    
def ledBlueOff():
	serialcom.write(str('offBlue').encode())

def disconnect():
	serialcom.close()

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if 'on-red' in request.form.to_dict()['action']:
			ledRedOn()
		if 'on-blue' in request.form.to_dict()['action']:
			ledBlueOn()
		if 'off-red' in request.form.to_dict()['action']:
			ledRedOff()
		if 'off-blue' in request.form.to_dict()['action']:
			ledBlueOff()
		if 'dis' in request.form.to_dict():
			disconnect()

	return render_template('index.html')

if __name__ == "__main__":
    app.run()
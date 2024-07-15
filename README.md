# Web Controlled LED Bulbs using Arduino and Flask
=====================================================

This project allows you to control multiple LED bulbs remotely using a web interface. The system consists of an Arduino board connected to the LED bulbs, and a Flask web application that communicates with the Arduino board using serial communication.

## Hardware Requirements

* Arduino board (e.g. Arduino Uno)
* LED bulbs
* Breadboard and jumper wires
* Serial cable (USB to serial)

## Software Requirements

* Arduino IDE
* Python 3.x
* Flask web framework
* Serial library for Python

## How it Works

1. The Arduino board is connected to the LED bulbs and configured to receive serial commands.
2. The Flask web application is run on a computer connected to the same network as the Arduino board.
3. The user accesses the web interface using a web browser and sends commands to turn the LED bulbs on or off.
4. The Flask application receives the commands and sends them to the Arduino board using serial communication.
5. The Arduino board receives the commands and turns the corresponding LED bulbs on or off.

## Project Structure

* `app.py`: The Flask web application code
* `templates/index.html`: The web interface HTML file
* `webLED/webLED.ino`: The Arduino code

## Getting Started

1. Clone the repository and navigate to the project directory.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Upload the Arduino code to the Arduino board using the Arduino IDE.
4. Run the Flask application using `python app.py`.
5. Access the web interface using a web browser at `http://localhost:5000`.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
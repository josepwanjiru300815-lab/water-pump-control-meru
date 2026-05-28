from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)

# ======================================
# ESP32 IP
# ======================================
ESP32_IP = "192.168.137.164"

# ======================================
# STATES
# ======================================
pump_status = "OFF"
valve_status = "STOPPED"

# ======================================
# HOME
# ======================================
@app.route("/")
def home():

    return render_template("index.html")

# ======================================
# PUMP PAGE
# ======================================
@app.route("/pump")
def pump():

    global pump_status

    return render_template(
        "pump.html",
        pump_status=pump_status
    )

# ======================================
# VALVE PAGE
# ======================================
@app.route("/valve")
def valve():

    global valve_status

    return render_template(
        "valve.html",
        valve_status=valve_status
    )

# ======================================
# PUMP ON
# ======================================
@app.route("/pump/on")
def pump_on():

    global pump_status

    requests.get(f"http://{ESP32_IP}/pump/on")

    pump_status = "ON"

    return redirect("/pump")

# ======================================
# PUMP OFF
# ======================================
@app.route("/pump/off")
def pump_off():

    global pump_status

    requests.get(f"http://{ESP32_IP}/pump/off")

    pump_status = "OFF"

    return redirect("/pump")

# ======================================
# VALVE OPEN
# ======================================
@app.route("/valve/open")
def valve_open():

    global valve_status

    requests.get(f"http://{ESP32_IP}/valve/open")

    valve_status = "OPENING"

    return redirect("/valve")

# ======================================
# VALVE CLOSE
# ======================================
@app.route("/valve/close")
def valve_close():

    global valve_status

    requests.get(f"http://{ESP32_IP}/valve/close")

    valve_status = "CLOSING"

    return redirect("/valve")

# ======================================
# VALVE STOP
# ======================================
@app.route("/valve/stop")
def valve_stop():

    global valve_status

    requests.get(f"http://{ESP32_IP}/valve/stop")

    valve_status = "STOPPED"

    return redirect("/valve")

# ======================================
# RUN APP
# ======================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
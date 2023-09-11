import lib_path
from microdot import Microdot, send_file
import time
import leds


app = Microdot()


@app.route('/')
def index(request):
    return send_file('static/index.html')


@app.put('/colour')
def set_light(request):
    lights = request.json
    leds.set_all(
        red=lights["r"],
        green=lights["g"],
        blue=lights["b"],
        white_cold=lights["wc"],
        white_warm=lights["ww"],
    )
    return { "success": True }


def main():
    app.run(host='0.0.0.0', port=5000, debug=True, ssl=None)

    # This will never run
    while True:
        leds.flash_pwm()
        time.sleep(1)
        leds.flash()
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        leds.off()

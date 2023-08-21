import append_libs_path
from microdot import Microdot
import time
import leds


app = Microdot()


@app.route('/')
def index(request):
    return 'Hello, world!'


def main():
    app.run(host='0.0.0.0', port=5000, debug=True, ssl=None)

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

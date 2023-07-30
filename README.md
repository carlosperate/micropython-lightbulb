# micropython-lightbulb

Clone this repository and the micropython submodule.
Careful not to do a recursive submodule update, or it'll take a long time to complete.

```bash
git submodule update --init micropython
```

Pull the MicroPython submodules for the ESP8266 port:
```bash
docker run --rm -v $(pwd):$(pwd) -w $(pwd) larsks/esp-open-sdk make -C micropython/ports/esp8266 submodules
```

Build MicroPython's mpy-cross:
```bash
docker run --rm -v $(pwd):$(pwd) -w $(pwd) larsks/esp-open-sdk make -C micropython/mpy-cross
```

Build the project using the [larsks/esp-open-sdk](https://hub.docker.com/r/larsks/esp-open-sdk)
docker image:
```bash
docker run --rm -v $(pwd):$(pwd) -w $(pwd)/micropython-boards/ESP8285H16 larsks/esp-open-sdk make
```

Load:
```bash
python tools/esptool/esptool.py --port /dev/tty.usbserial-1440 erase_flash
```
```bash
python tools/esptool/esptool.py --port /dev/tty.usbserial-1440 --baud 1000000 write_flash --verify --flash_size=4MB -fm dio 0 micropython-boards/ESP8285H16/build/firmware-combined.bin
```

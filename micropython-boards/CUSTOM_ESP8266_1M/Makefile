# Makefile for custom MicroPython ESP8266 board.

################################################################################
# Define your settings here.

# The board name.
BOARD ?= CUSTOM_ESP8266_1M

# Location of MicroPython repository.
MICROPY_TOP ?= $(abspath ../../micropython)

################################################################################
# Define your targets here.

all: firmware

################################################################################
# Items below this line do not generally need to be changed.

BOARD_DIR = $(abspath .)
BUILD = $(abspath build)

include $(MICROPY_TOP)/py/mkenv.mk
include $(MICROPY_TOP)/py/mkrules.mk

firmware:
	$(Q)$(MAKE) -C $(MICROPY_TOP)/ports/esp8266 \
		PROJECT_TOP=$(abspath ../..) \
		BOARD=$(BOARD) \
		BOARD_DIR=$(BOARD_DIR) \
		BUILD=$(BUILD)

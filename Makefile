TITLE="EPIC UBNT_1101_DC_VOLTMETER"

PKG_NAME="UBNT_1101_DC_VOLTMETER"
PKG_VERSION="0.1"
PKG_RELEASE=1

MODULE_FILES=dc_voltmeter.py
MODULE_FILES_DIR=/usr/lib/python3.8/

.PHONY: all install

all: install

install:
	for f in $(MODULE_FILES); do cp $${f} $(MODULE_FILES_DIR); done

clean:
	for f in $(MODULE_FILES); do rm -f $(MODULE_FILES_DIR)$${f}; done

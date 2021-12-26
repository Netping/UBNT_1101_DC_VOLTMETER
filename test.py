#!/usr/bin/python3
from dc_voltmeter import *




def main():
	voltmeter=DC_V()
	print(voltmeter.Get('V_IN0'))

if __name__ == "__main__":
	main()

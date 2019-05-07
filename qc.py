#!/usr/bin/env python

from Quadcopter import Quadcopter
import os

os.nice(-10)

if __name__ == '__main__':
	Quadcopter().go()

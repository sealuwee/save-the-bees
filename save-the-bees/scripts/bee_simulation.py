'''
	This script will be the main script for creating
	executable commands for the simulation of CCD

	The main library I will be using will be SimPy, a 'discrete event simulation'
	for Python. There will also be an example simulation script in this
	scripts directory that will not be routed to the main functionality of this
	project.

'''
import numpy as np
import simpy
import collections as col

rint = np.random.randint
choice = np.random.choice

# simulation parameters

SIM_TIME_YEARS = 100 #this will represent the next 100 years.
SIM_TIME_MONTHS = 1200
STATES = ['CA']

# Initialize the amount of bees in our colonies.

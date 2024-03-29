import pandas as pd 
import numpy as np 
import scipy.stats as stats
import simpy
import random

RANDOM_SEED = 42
NEW_CUSTOMERS = 5
INTERVAL_CUSTOMERS = 10.0
MIN_PATIENCE = 1
MAX_PATIENCE = 3

def source(env, number, interval, counter):
	'''
		Source generates customers randomly
	'''
	for i in range(number):
		c = customer(env, 'Customer%02d' % i, counter, time_in_bank=12.0)
		env.process(c)
		t = random.expovariate(1.0 / interval)
		yield env.timeout(t)

def customer(env, name, counter, time_in_bank):
	'''
		Customer arrives, is served, and leaves.
	'''
	arrive = env.now
	print('%7.4f %s: Here I am' % (arrive, name))

	with counter.request() as req:
		patience = random.uniform(MIN_PATIENCE, MAX_PATIENCE)
		results = yield req | env.timeout(patience)

		wait = env.now - arrive

		if req in results:
			print('%7.4f %s: Wait %6.3f' % (env.now, name, wait))

			tib = random.expovariate(1.0 / time_in_bank)
			yield env.timeout(tib)
			print('%7.4f %s: Finished' % (env.now, name))

		else:
			print('%7.4f %s: RENEGED after %6.3f' % (env.now, name, wait))

print('Bank Renege')
random.seed(RANDOM_SEED)
env = simpy.Environment()
counter = simpy.Resource(env, capacity=1)
env.process(source(env, NEW_CUSTOMERS, INTERVAL_CUSTOMERS, counter))
env.run()

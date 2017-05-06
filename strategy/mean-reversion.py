from event import OrderEvent
import pandas as pd
import numpy as np
from statisticaltest import hurst #calculating hurst exponent

'''
Strategy note:
To do:
	- How to take different ticks
		- calculate hurst as test first, can get historical data
	- How ADF tests


'''
tick_distance = "5S"

class meanrevertstrat(object):
	def __init__():
		self.instrument = instrument
        self.units = units
        self.events = events
        self.ticks = 0
        self.data = pd.DataFrame()

	def calculate_signals(self, event):
		lookback = 20 # look back period length
		self.position = 0
		if event.type == "TICK":
            self.ticks += 1
            self.data = self.data.append(
                    pd.DataFrame({"ticks": [self.ticks], "time": [event.time], "ask": [event.ask]}))
           	resam = self.data.resample(tick_distance).last()
            resam["returns"] = np.log(resam["ask"]/resam["ask"].shift(1))
		
		linearstrat()
		pass

	def linearstrat():
		lookback = halflife # The look-back for the moving average and standard deviation can be set to equal the half-life.
		norm_dev = np.log(moving_avg)
		mktVal = -(y-movingAvg(y, lookback))/movingStd(y, lookback) # go look for movingAvg function on the website
		# Determine the normalized deviation from its moving average

		self.units = -norm_dev
		# Maintain the number of units in this asset negatively proportional to this normalized deviation
		pass

	
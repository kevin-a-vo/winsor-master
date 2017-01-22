#Author: Kevin Vo

from scipy.stats import mstats
import pandas as pd 
import numpy as np

class Winsor():
	def __init__(self):
		pass

	#This version replaces the outliers with the value
	#at the specified percentile. 
	def __using_mstats_df(self, df):
		return df.apply(self.__using_mstats, axis = 0)

	def __using_mstats(self, s):
		return mstats.winsorize(s, limits = [0.01, 0.01])

	def __winsorize(self, master):
		grouped = master.groupby(['item_id', 'quote_date'])
		master = grouped.apply(self.__using_mstats_df)
		return master

	#This replaces the values with NA
	def __winsorize_series(self, s, limits):
		#What does quantile accept?
		#quantile will accept a list, tuple and floats
		q = s.quantile(limits)
		if isinstance(q, pd.Series) and len(q) == 2:
			s[s < q.iloc[0]] = np.nan
			s[s > q.iloc[1]] = np.nan
		return s

	def winsorize(self, df, variables = None, limits = None,
					group = None, trim = False):
		
		#What happens if group is None?

		if type(variables) is str:
			variables = [variables,]

		for var in variables:
			grouped = df.groupby(group)[var]
			winsorSeries = grouped.apply(self.__winsorize_series, limits)
			df[var] = winsorSeries

		return df

#Do one thing and do it well

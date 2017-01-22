from winsor import Winsor
import pandas as pd

if __name__ == "__main__":
	data = pd.read_csv("price_quotes_2012_q3.csv")
	#The groupby function is robust to strings
	winObj = Winsor()
	data = winObj.winsorize(data, variables = ['price', 'stratum_weight'], limits = [0.05, 0.95], 
							group = ['item_id', 'quote_date'], trim = True)
	data.to_csv('comp_python.csv', index = False)


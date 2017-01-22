cd "users/kevinavo/Documents/winsor-master"
import delimited price_quotes_2012_q3.csv

ssc install winsor2
winsor2 price stratum_weight, replace cuts(5 95) trim by(item_id quote_date)
outsheet using "comp_stata.csv", comma replace
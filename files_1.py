from pandas import read_csv

data = read_csv('california_housing_test.csv')

print(data["median_house_value"].max(), data["median_house_value"].min())

#A

#Import pandas
#Read the provided CSV file ‘data.csv’.
import pandas as pd
df = pd.read_csv("data.csv")

#C

#Show the basic statistical description about the data.
#df.head()
df.describe()

#D

#Check if NULL values are there in the dataset
df.isnull().sum()
#D(i)

#Fill the NULL values with Mean
df = df.fillna(df.mean())
df
#verifying if there are any NULL values
df.isnull().sum()

#E

#Aggregation functions on 3 columns
result = df[['Duration','Pulse','Calories']].agg(['min', 'max','count','mean'])
print("Min, Max, Count and Mean values ")
result
#F

#Filtering with Calories between 500 and 1000
filter1 = df[(df.Calories >= 500) & (df.Calories <= 1000)]
filter1

#G

#Filtering the dataset with calories greater than 500 and pulse less than 100
filter2 = df[(df.Calories > 500) & (df.Pulse < 100)]
filter2


#H

#Showing all columns except Maxpulse in a new dataframe
df_modified = df.loc[:, df.columns!='Maxpulse']
df_modified

#I

#Deleting Maxpulse from main dataframe
del df["Maxpulse"]
df
#Existing datatypes of columns in dataframe
df.dtypes


#J

#Replacing the calories datatype
df.Calories = df.Calories.astype(int)
df.dtypes



#K

#Visualizing using scatter plot for the two columns (Duration and Calories).
import matplotlib.pyplot as plt
print(df.plot.scatter(x ='Duration', y= 'Calories'))
plt.show()


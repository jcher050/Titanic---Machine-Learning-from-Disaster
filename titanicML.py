

# linear algebra
# data processing, CSV file I/O (e.g. pd.read_csv)

import numpy as np 
import pandas as pd 

# Load the data from the titanic competition

titanic_data = pd.read_csv("../input/titanic/train.csv")
test_data = pd.read_csv("/kaggle/input/titanic/test.csv")


# Show the first five rows of the data
titanic_data.head()
test_data.head()

# Number of total passengers
total = len(titanic_data)
print(total)

# Number of passengers who survived
survived = (titanic_data.Survived == 1).sum()
print(survived)

# Number of passengers under 18
minors = (titanic_data.Age < 18).sum()
print(minors)

# TODO: Fill in the value of the survived_fraction variable
survived_fraction = survived/total

# Print the value of the variable
print(survived_fraction)

# TODO: Fill in the value of the minors_fraction variable
minors_fraction = minors/total

# Print the value of the variable
print(minors_fraction)


#Percentage of women who survived
women = titanic_data.loc[titanic_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women)

#Percentage of men who survived
men = titanic_data.loc[titanic_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("% of men who survived:", rate_men)
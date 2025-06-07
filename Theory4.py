🔸 16. What is inheritance in Python?
Answer:
Inheritance allows a class (child) to inherit attributes and methods from another class (parent).
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Inherited method
🔶 Python for Data Analysis Interview Questions
🔸 17. What libraries are used for data analysis in Python?
Answer:
pandas – data manipulation and analysis
numpy – numerical computations
matplotlib/seaborn – data visualization
scikit-learn – machine learning
statsmodels – statistical modeling

🔸 18. What is a DataFrame in pandas?
Answer:
A DataFrame is a 2D labeled data structure with rows and columns (like an Excel sheet or SQL table).

import pandas as pd
data = {'Name': ['A', 'B'], 'Age': [20, 25]}
df = pd.DataFrame(data)
print(df)
🔸 19. How do you read a CSV file in pandas?

import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
🔸 20. How to handle missing data in pandas?
df.isnull() – to detect

df.dropna() – to remove

df.fillna(value) – to fill

df.fillna(0, inplace=True)

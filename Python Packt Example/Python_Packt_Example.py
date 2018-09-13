
# from sklearn import datasets
# import pandas as pd
# iris = datasets.load_iris()
# df = pd.DataFrame(iris.data, columns=iris.feature_names)

import seaborn as sns
sns.set()

# Load the iris dataset
iris = sns.load_dataset("iris")

# Set the colour scheme
colours = ['#066082', '#b12acf', '#808080']

# This code will generate a joint plot using the Iris dataset.
sns_pairplot = sns.pairplot(iris, hue='species', size=2.5,palette=colours)

# Save the output to an image
sns_pairplot.savefig("Packtpairplotoutput.png")

print("Produced Pairplot Image")

# This code will generate a joint plot using the Iris dataset.
sns_jointplot = sns.jointplot(x="sepal_length", y="petal_length", data=iris);

# Save the output to an image
sns_jointplot.savefig("Packtjointplotoutput.png")

# Feedback success to the user
print("Produced Jointplot Image")

# This code will generate a linear regression plot using the Iris dataset.
sns_lmplot = sns.lmplot(x='sepal_length', # X-axis name
           y='petal_length', # Y-axis name
           data=iris, 
           fit_reg=True, # set to False if you don't need regression lines
           hue='species', # one colour per iris species
           scatter_kws={"s":100},
           size=8,
           palette=colours)

# Save the output to an image
sns_lmplot.savefig('PacktLinearRegression.jpeg', bbox_inches='tight')

# Feedback success to the user
print("Produced Linear Regression Image")

#End Script


import seaborn as sns
import matplotlib.pyplot as plt


df = iris = sns.load_dataset('iris')

# print(df.head())
# print(df.dtypes)
# print(df['species'].unique())
# print(df.columns)
# sns.heatmap(df.corr())
# sns.jointplot(x='petal_length',y='petal_width',data=df,kind='hex')

# sns.countplot('species',data=df)
# sns.barplot(x='petal_width',y='species',data=df)
# sns.boxplot(x='petal_width',y='species',data=df)


plt.show()
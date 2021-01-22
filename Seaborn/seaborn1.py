import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# print(df.head())

# predict tips based on other features
# print(df.dtypes)
# print(df.corr()) # cannot be done on categorical variables

# For non-categorical features: ##############################

# sns.heatmap(df.corr())

# sns.jointplot(x='tip',y='total_bill',data=df,kind='hex')
# sns.jointplot(x='tip',y='total_bill',data=df,kind='reg')

# more than 2 features, use pair plot
# sns.pairplot(df)
# sns.pairplot(df,hue='sex') # based on sex

# sns.displot(df['tip']) # make a histgram
# sns.displot(df['tip'],kde=False,bins=10) # kdu=True, we get y axis in terms of percentage

# For categorical features: ###########################33

# boxplot
# sns.boxplot('smoker','total_bill',data=df)
# sns.boxplot('smoker','total_bill',data=df,palette='rainbow')
# sns.boxplot(x='total_bill',y='day',hue='smoker',data=df)

# violinplot
# sns.violinplot(x='total_bill',y='day',data=df,palette='rainbow') ### what???


# countplot
# sns.countplot('sex',data=df) # pick out sex from df, and plot the counts of every single types
# sns.countplot(y='sex',data=df) # pick out sex from df, and plot the counts of every single types

# bar plot
# sns.barplot(y='total_bill',x='sex',data=df)





plt.show()








# %% [markdown]
# ### Python Intro

# %%


# %% [markdown]
# a // b 	Floor division 	Quotient of a and b, removing fractional parts
# 
# a % b 	Modulus 	Integer remainder after division of a by b
# 
# a ** b 	Exponentiation 	a raised to the power of b

# %% [markdown]
# ### Functions

# %% [markdown]
# #### Help Function

# %%
help(round)

# %% [markdown]
# #### Defining custom functions

# %%
def least_difference(a, b, c):
    """
    Return the smallest difference between any two numbers among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    # docstring (""" Text """) is shown if we call help(function)
    # The last line (>>>) indicates return upon running code
    
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(least_difference(1, 10, 100),
      least_difference(1, 10, 10),
      least_difference(5, 6, 7))

# %% [markdown]
# help(least_difference)

# %% [markdown]
# #### Default arguments

# %%
print(1, 2, 3, sep= ' < ') # the default sep is single space

# %%
def greet(who = "Sunzid"):
    print("Hello, ", who)
          
greet()
greet(who = "Hassan")
greet("Sunzid Hassan")

# %% [markdown]
# ### Functions applied to functions
# Functions that operate on other functions are called "higher-order functions". 

# %%
def mult_by_five(x):
    """ multiply input by 5"""
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep = '\n' # '\n' starts a new line
)

# %% [markdown]
# Sometimes, it's possible to pass functions inside other function. For example, we can pass a function in the max function as a key.

# %%
def mod_5(x):
    """Returns the remainder of x after dividing by 5"""
    return x % 5

print('Which number is the biggest?',
      max(100, 51, 14),
      'Which number is the biggest modulo 5?',
      max(100, 51, 14, key = mod_5),
      sep = '\n')

# %%
help(round)

# %% [markdown]
# ### Booleans

# %% [markdown]
# bool python variable has two values - True and False.
# 
# We use boolean operators to get T/F.
# 
# a == b - a is equal to b
# a <= b - a is less than or equal to b

# %%
x = True
print(x)
print(type(x))

# %%
True or True and False

# %%
# easy to understand code
# prepared_for_weather = (
#     have_umbrella 
#     or ((rain_level < 5) and have_hood) 
#     or (not (rain_level > 0 and is_workday))
# )

# %%
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is zero")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)

# %% [markdown]
# #### Use of colons and whitespaces to define seperate blocks of code.

# %%
def f(x):
    if x > 0:
        print("x is positive; x =", x)
        print("printed when x is positive; x =", x)
    print("Always printed, regardless of x's value; x =", x)

f(1)
f(0)

# %% [markdown]
# #### Boolean conversion
# 
# Just as int() converts floats into integer, bool() converts things into boolean.

# %%
print(bool(1)) # all numbers are treated as True, except 0
print(bool(0))

print(bool("asdf")) # all strings are treated as true, except empty string ""
print(bool(""))

# %%
# We can use non-boolean objects in if conditions and other places where a boolen would be expected. Python will implicitly treat them as their corresponding boolean value.

if 0:
    print(0)
elif "spam":
    print("spam")

# %%
def if_negative(number):
    return number < 0

if_negative(2)

# %%
True ^ False

# %% [markdown]
# Loops and list comprehensions

# %%
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    List = []
    for i in range(len(L)):
        List.append(L[i] > thresh)
    return List

# %%
L = [1, 2, 3]

L[0] > 2

# %%
len(L)

# %%
elementwise_greater_than([1, 2, 3], 2)

# %%
words = "it is closed."

# %%
words.replace(".","")
words.split()

# %%
help(str)

# %%
words.replace(".","").replace(",","").split()

# %%
words.split()


# %%
help(str.replace)


# %%
help(list)

# %%
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    index = []
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip(',.').lower() for token in tokens]
        if keyword.lower() in normalized:
            index.append(i)
    return index


# %%
def word_search(doc_list, keyword):
    indices = [] 
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

# %%
doc_list = ["The Learn Python Challenge Casino", "They bought a car, and a horse", "Casinoville?"]
keyword='Casino'

# %%
word_search(doc_list, keyword)

# %%
words = []
for i in range(len(doc_list)):
        words.append(doc_list[i].replace(",","").replace(".","").split())

# %%
for word in words:
    print(len(word))

# %%
help(str)

# %%
keyword.upper()

# %%
word[0].upper()

# %%
for item in doc_list:
    item.split()
    print(item, sep = ";")

# %%
item

# %% [markdown]
# ## Pandas

# %%
import pandas as pd

# %% [markdown]
# ### Dataframe

# %%
# this dataframe is generated by declaring dictionary whose keys are column names, and values are entries.
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})


# %%
pd.DataFrame({'Bob':['I liked it', 'It was awful'],
              'Sue':['Pretty good', 'Bland']},
             index=['Product A', 'Product B'])

# %% [markdown]
# ### Series

# %%
# A series is like a single column of dataframe. We can assign index names, but there is no column name. It instead has overall name.
pd.Series([1, 2, 3, 4],
         index= ['2015', '2016', '2017', '2018'],
          name = 'Product A')

# %%
# Reading data
# pd.read_csv('path.csv', index_col=0)

#writing data
# dataName.to_csv('fileName.csv', sep = )

# %% [markdown]
# ### Indexing in Python
# 
# In Python, we access attributes of an object with '.'. So title of a book can be book.title.
# Similarly we can access columns of a dataframe by using DataFrame.ColumnName
# 
# We can access values of a python dictionary with dictionaryName['columnName']. We can access dataframe columns the same way. Similarly, we can access specific data with dictionaryName['columnName'][rowNumber]

# %% [markdown]
# ### Indexing in Pandas
# iloc and loc is used for index based selection. It is a row-column selection, whereas rest of the Python is column-row selection.
# 
# iloc is used for number based selection:
# 
# reviews.iloc[:, 0] ; get all rows of the first column  
# reviews.iloc[:3, 0] ; get first 3 rows of the first column  
# reviews.iloc[1:3, 0] ; get 2-4th row of the first column  
# reviews.iloc[[0, 1, 2], 0] ; get first 3 rows of the first column  
# reviews.iloc[-5:] ; get last 5 rows of all columns  
# 
# loc is used for label based selection
# 
# reviews.loc[0, 'country'] ; get the first row of the'country' column's  
# reviews.loc[: , ['taster_name', 'taster_twitter_handle', 'points']] ; get all rows of the given columns  
# 
# To note:
# review.loc[0:10] returns 1st to 10th rows.  
# review.iloc[0:10] returns 1st to 11th rows.

# %%
# Set index = dataName.set_index("title")

# %%
# Conditional selection
# dataName.columnName == 'Name' # will return a clumn of T/F based on the data
# dataName.loc[dataName.columnName == 'Name'] # is equivalent to R's filter - it'll return the filtered dataframe
# dataName.loc[(dataName.col1 == 'Name') & (dataName.col2 >= 'Value')] # multi criteria filtering
# dataName.loc[(dataName.col1 == 'Name') & (dataName.col2 >= 'Value')] # show both of criteria 1 or 2

# %% [markdown]
# ### Pandas built in conditional selectors
# isin  
# Lets you select data whose value 'is in' a list of values (like multi-or condition).
# 
# dataName.loc[dataName.columnName.isin(['Name1', 'Name2'])]
# 
# isnull and notnull (is.na and !is.na in R)  
# dataName.loc[dataName.colName.notnull()]

# %% [markdown]
# ### Assignign data
# dataName['columnName'] = 'colValue'
# 
# dataName['colName'] = range(len(dataName), 0, -1)
# dataName['colName']

# %%
dataName.columnName.describe() # Statistics
dataName.columnName.mean()
dataName.columnName.unique() # array of unique values
dataName.columnName.value_counts() # how many times the unique entries repeated

#Map function: input > change > output
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

Doing the same thing with apply:
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

Direct approach:
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean

idxmax()

# %%
import pandas as pd

# %%
# Grouping data
dataName.groupby('colName').colName.count()
dataName.groupby('colName').colName.min()

# lambda - instant one expression function
dataName.groupby('colName').apply(lambda df: df.title.iloc[0])

# Group by more than one column, find max values of each group
dataName.groupby(['Col1', 'Col2']).apply(lambda df: df.loc[df.colName.idxmax()])

# run different functions with agg()
dataName.groupby(['Colname']).price.agg([len, min, max])

# Multi index operation
df = dataName.groupby(['col1', 'col2']).description.agg([len])

# %% [markdown]
# 
# 
# Multi-indices have several methods for dealing with their tiered structure which are absent for single-level indices. They also require two levels of labels to retrieve a value. Dealing with multi-index output is a common "gotcha" for users new to pandas.
# 
# However, in general the multi-index method you will use most often is the one for converting back to a regular index, the reset_index() method:

# %%
dataName.sort_vlaues(by = ['Col', 'col2'], ascending = False)

dataName.sort_index()

# %%
import pandas as pd

ckd = pd.read_excel('Input/MS Stock Report Summary on 20-July-22 (Closing Stock).xlsx',
                           sheet_name = "Stock Report", ra)
ckd.head()


# %%
from pandas import read_csv


cbu = read_csv('Input/20220721CKDStockDaysReport.csv')
cbu.head()

# %%
total_bike = cbu.OneMonth + cbu.OneWeek + cbu.TwoWeek + cbu.TwoMonth + cbu.OverTwoMonth
total_bike.to_csv('Output/totalBike.csv')

# %% [markdown]
# ### Data types
# 
# .dtype returns data type of object.  
# astype('float64') changes data type.
# 
# dataName[pd.isnull(dataName.colName)]
# dataName[pd.notnull(dataName.colName)]
# 
# fillna() for replacing NaN values.
# dataName.colName.fillna()
# 
# replace
# dataName.colName.replace("oldVal", "newVal")
# It can be used to replace: "Unknown", "Undisclosed", "Invalid"

# %% [markdown]
# ### Renaming and combining
# dataName.rename(columns={'oldName': 'newName'})
# 
# dataName.rename(index={0: 'newName', 1: 'newName2'})
# 
# 
# dataName.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

# %% [markdown]
# ### Combining dataframes
# concat(), join(), merge()
# 
# data with same fields: concat()
# 
# canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
# british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")
# 
# pd.concat([canadian_youtube, british_youtube])
# 
# left = canadian_youtube.set_index(['title', 'trending_date'])
# right = british_youtube.set_index(['title', 'trending_date'])
# 
# left.join(right, lsuffix='_CAN', rsuffix='_UK')

# %% [markdown]
# ## Data cleaning
# ### Handling missing values
# 
# dataName.dropna() # drop rows with missing values
# 
# #remove columns with at least one missing vlaue
# dataName.dropna(axis=1)
# 
# #fill na values
# dataName.fillna(0)
# dataName.fillna(method = 'bfill', axis = 0).fillna(0) #replace all na values with values directly after it, then replace remaining na values with 0

# %%
# modules we'll use
import pandas as pd
import numpy as np

# for Box-Cox Transformation
from scipy import stats

# for min_max scaling
from mlxtend.preprocessing import minmax_scaling

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

# set seed for reproducibility
np.random.seed(0)


# generate 1000 data points randomly drawn from an exponential distribution
original_data = np.random.exponential(size=1000)

# mix-max scale the data between 0 and 1
scaled_data = minmax_scaling(original_data, columns=[0])

# plot both together to compare
fig, ax = plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(scaled_data, ax=ax[1], kde=True, legend=False)
ax[1].set_title("Scaled data")
plt.show()

# normalize the exponential data with boxcox
normalized_data = stats.boxcox(original_data)

# plot both together to compare
fig, ax=plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(normalized_data[0], ax=ax[1], kde=True, legend=False)
ax[1].set_title("Normalized data")
plt.show()

# %%


# modules we'll use
import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# read in our data
landslides = pd.read_csv("../input/landslide-events/catalog.csv")

# set seed for reproducibility
np.random.seed(0)

landslides['date_parsed'] = pd.to_datetime(landslides['date'], format="%m/%d/%y")

landslides['date_parsed'] = pd.to_datetime(landslides['Date'], infer_datetime_format=True)

day_of_month_landslides = landslides['date_parsed'].dt.day
day_of_month_landslides.head()

# %% [markdown]
# ## Time Series
# ### Linear regression with time series

# %%
import pandas as pd

df = pd.DataFrame({'Hardcover':[139, 128, 172, 139, 191],
'Date': ['2000-04-01', '2000-04-02', '2000-04-03', '2000-04-04', '2000-04-05']}).set_index('Date')

df.head()

# %% [markdown]
# #### Lag features.
# We shift our observations of the target series, so they appear to have occured later in time. For example a 1-step lag is shifting values by 1 row, though multiple steps is possible too.
# 
# Linear regression with a lag feature produces the model. It shows if value of one record is correlated with value of the previous record.It indicates values can be predicted from previous observations.

# %%
df['Lag_1'] = df.Hardcover.shift(1)
df = df.reindex(columns=['Hardcover', 'Lag_1'])

df.head()

# %%
Time = pd.Series([0, 1, 2, 3, 4],
index=(['2000-04-01', '2000-04-02', '2000-04-03', '2000-04-04', '2000-04-05']),
name = 'Time')

df.join(Time)

# %%
from sklearn.linear_model import LinearRegression

# Training data
X = df.loc[:, ['Time']]  # features
y = df.loc[:, 'Hardcover']  # target

# Train the model
model = LinearRegression()
model.fit(X, y)

# Store the fitted values as a time series with the same time index as
# the training data
y_pred = pd.Series(model.predict(X), index=X.index)

# %% [markdown]
# ### Trend
# The slowest moving part of a serie, representing largest time scale of importance.
# 
# We can use moving average plot to see trend.
# 
# If the trend is linear, we'll use linear model.
# 
# target = m * time + c
# 
# If it's quadratic (e.g., a parabola), we just need to add the square of the dummy to the feature set.
# 
# target = a * time ** 2 + b * time + c
# Here, linear regression will learn the coefficients a, b and c.

# %%
# moving_average = dataName.rolling(
#     window=365,       # 365-day window
#     center=True,      # puts the average at the center of the window
#     min_periods=183,  # choose about half the window size
# ).mean()              # compute the mean (could also do median, std, min, max, ...)

# trend = dataName.rolling(
#     window=____,
#     center=____,
#     min_periods=6,
# ).____()

# ax = tunnel.plot(style=".", color="0.5")
# moving_average.plot(
#     ax=ax, linewidth=3, title="Tunnel Traffic - 365-Day Moving Average", legend=False,
# );

# %% [markdown]
# In Lesson 1, we engineered our time dummy in Pandas directly. From now on, however, we'll use a function from the statsmodels library called DeterministicProcess. Using this function will help us avoid some tricky failure cases that can arise with time series and linear regression. The order argument refers to polynomial order: 1 for linear, 2 for quadratic, 3 for cubic, and so on.
# A deterministic process, by the way, is a technical term for a time series that is non-random or completely determined, like the const and trend series are. Features derived from the time index will generally be deterministic.
# 

# %%
# from statsmodels.tsa.deterministic import DeterministicProcess

# dp = DeterministicProcess(
#     index=tunnel.index,  # dates from the training data
#     constant=True,       # dummy feature for the bias (y_intercept)
#     order=1,             # the time dummy (trend)
#     drop=True,           # drop terms if necessary to avoid collinearity
# )
# # `in_sample` creates features for the dates given in the `index` argument
# X = dp.in_sample()

# X.head()


# from sklearn.linear_model import LinearRegression

# y = tunnel["NumVehicles"]  # the target

# # The intercept is the same as the `const` feature from
# # DeterministicProcess. LinearRegression behaves badly with duplicated
# # features, so we need to be sure to exclude it here.
# model = LinearRegression(fit_intercept=False)
# model.fit(X, y)

# y_pred = pd.Series(model.predict(X), index=X.index)



# To make a forecast, we apply our model to "out of sample" features. "Out of sample" refers to times outside of the observation period of the training data. Here's how we could make a 30-day forecast:


# X = dp.out_of_sample(steps=30)

# y_fore = pd.Series(model.predict(X), index=X.index)

# y_fore.head()



# %%
# from statsmodels.tsa.deterministic import DeterministicProcess

# y = average_sales.copy()  # the target

# # YOUR CODE HERE: Instantiate `DeterministicProcess` with arguments
# # appropriate for a cubic trend model
# dp = DeterministicProcess(index=y.index, order=3)

# # YOUR CODE HERE: Create the feature set for the dates given in y.index
# X = dp.in_sample()

# # YOUR CODE HERE: Create features for a 90-day forecast.
# X_fore = dp.out_of_sample(steps = 90)


# # Check your answer
# q_3.check()

# %% [markdown]
# ### Seasonality
# Seasonal plot: a plot over a specific time period (time, days, weeks, months, years, etc.).
# 
# Seasonal indicators:
# 
# What is Seasonality?
# 
# We say that a time series exhibits seasonality whenever there is a regular, periodic change in the mean of the series. Seasonal changes generally follow the clock and calendar -- repetitions over a day, a week, or a year are common. Seasonality is often driven by the cycles of the natural world over days and years or by conventions of social behavior surrounding dates and times.
# 
# Seasonal patterns in four time series.
# 
# We will learn two kinds of features that model seasonality. The first kind, indicators, is best for a season with few observations, like a weekly season of daily observations. The second kind, Fourier features, is best for a season with many observations, like an annual season of daily observations.
# 
# Seasonal Plots and Seasonal Indicators
# 
# Just like we used a moving average plot to discover the trend in a series, we can use a seasonal plot to discover seasonal patterns.
# 
# A seasonal plot shows segments of the time series plotted against some common period, the period being the "season" you want to observe. The figure shows a seasonal plot of the daily views of Wikipedia's article on Trigonometry: the article's daily views plotted over a common weekly period.
# There is a clear weekly seasonal pattern in this series, higher on weekdays and falling towards the weekend.
# 
# Seasonal indicators
# 
# Seasonal indicators are binary features that represent seasonal differences in the level of a time series. Seasonal indicators are what you get if you treat a seasonal period as a categorical feature and apply one-hot encoding.
# 
# By one-hot encoding days of the week, we get weekly seasonal indicators. Creating weekly indicators for the Trigonometry series will then give us six new "dummy" features. (Linear regression works best if you drop one of the indicators; we chose Monday in the frame below.)
# 
# This allows linear regression to learn mean of the value of 1, and others will be 0.
# 
# Fourier features and the Periodogram
# 
# For long seasons with many observations, indicators are impractical. Fourier features capture the overall shape of the seasonal curve with few features.
# There can be frequencies for days, weeks, months, years - fourier helps us capture these.  
# The idea is to include in our training data periodic sine and cosine curves having same frequencies as the seasons we are trying to model.
# There are one pair for each potential frequency in the season starting with the longest - once per year, twice per year, three times per year etc.
# Linear regression learns the weights that will fit the seasonal component in the target series.
# 
# We can learn how many fourier pairs to include in our feature set with the help of periodogram.
# The periodgram tells you the strength of the frequencies in a time series.
# 
# If the periodgram drops after quarterly, we'll use 4 pairs. We'll use indicators for weeks.

# %% [markdown]
# ### Serial dependence
# In earlier lessons, we investigated properties of time series that were most easily modeled as time dependent properties, that is, with features we could derive directly from the time index. Some time series properties, however, can only be modeled as serially dependent properties, that is, using as features past values of the target series. The structure of these time series may not be apparent from a plot over time; plotted against past values, however, the structure becomes clear -- as we see in the figure below below.
# 
# Cycles
# One especially common way for serial dependence to manifest is in cycles. Cycles are patterns of growth and decay in a time series associated with how the value in a series at one time depends on values at previous times, but not necessarily on the time step itself. Cyclic behavior is characteristic of systems that can affect themselves or whose reactions persist over time. Economies, epidemics, animal populations, volcano eruptions, and similar natural phenomena often display cyclic behavior.
# 
# Lagged series and lag plots
# 
# When choosing lags to use as features, it generally won't be useful to include every lag with a large autocorrelation. In US Unemployment, for instance, the autocorrelation at lag 2 might result entirely from "decayed" information from lag 1 -- just correlation that's carried over from the previous step. If lag 2 doesn't contain anything new, there would be no reason to include it if we already have lag 1.
# 
# The partial autocorrelation tells you the correlation of a lag accounting for all of the previous lags -- the amount of "new" correlation the lag contributes, so to speak. Plotting the partial autocorrelation can help you choose which lag features to use.
# 
# Finally, we need to be mindful that autocorrelation and partial autocorrelation are measures of linear dependence. Because real-world time series often have substantial non-linear dependences, it's best to look at a lag plot (or use some more general measure of dependence, like mutual information) when choosing lag features. The Sunspots series has lags with non-linear dependence which we might overlook with autocorrelation.

# %%
from pathlib import Path
from warnings import simplefilter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

simplefilter("ignore")  # ignore warnings to clean up output cells

# Set Matplotlib defaults
plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True, figsize=(11, 5))
plt.rc(
    "axes",
    labelweight="bold",
    labelsize="large",
    titleweight="bold",
    titlesize=14,
    titlepad=10,
)
plot_params = dict(
    color="0.75",
    style=".-",
    markeredgecolor="0.25",
    markerfacecolor="0.25",
    legend=False,
)
%config InlineBackend.figure_format = 'retina'


# Load Tunnel Traffic dataset
data_dir = Path("D:/Python/Input")
tunnel = pd.read_csv(data_dir / "Tutorial/tunnel.csv", parse_dates=["Day"])
tunnel = tunnel.set_index("Day").to_period()

# %%
moving_average = tunnel.rolling(
    window=365,       # 365-day window
    center=True,      # puts the average at the center of the window
    min_periods=183,  # choose about half the window size
).mean()              # compute the mean (could also do median, std, min, max, ...)

ax = tunnel.plot(style=".", color="0.5")
moving_average.plot(
    ax=ax, linewidth=3, title="Tunnel Traffic - 365-Day Moving Average", legend=False,
);

# %%
from statsmodels.tsa.deterministic import DeterministicProcess

dp = DeterministicProcess(
    index=tunnel.index,  # dates from the training data
    constant=True,       # dummy feature for the bias (y_intercept)
    order=1,             # the time dummy (trend)
    drop=True,           # drop terms if necessary to avoid collinearity
)
# `in_sample` creates features for the dates given in the `index` argument
X = dp.in_sample()

X.head()

# %%


from sklearn.linear_model import LinearRegression

y = tunnel["NumVehicles"]  # the target

# The intercept is the same as the `const` feature from
# DeterministicProcess. LinearRegression behaves badly with duplicated
# features, so we need to be sure to exclude it here.
model = LinearRegression(fit_intercept=False)
model.fit(X, y)

y_pred = pd.Series(model.predict(X), index=X.index)



# %%


ax = tunnel.plot(style=".", color="0.5", title="Tunnel Traffic - Linear Trend")
_ = y_pred.plot(ax=ax, linewidth=3, label="Trend")



# %%


X = dp.out_of_sample(steps=30)

y_fore = pd.Series(model.predict(X), index=X.index)

y_fore.head()



# %%


ax = tunnel["2005-05":].plot(title="Tunnel Traffic - Linear Trend Forecast", **plot_params)
ax = y_pred["2005-05":].plot(ax=ax, linewidth=3, label="Trend")
ax = y_fore.plot(ax=ax, linewidth=3, label="Trend Forecast", color="C3")
_ = ax.legend()



# %%


# %% [markdown]
# ## Extra

# %% [markdown]
# ### Loop over datetime

# %%


# %%
import datetime
 
# consider the start date as 2021-february 1 st
start_date = datetime.date(2021, 2, 1)
 
# consider the end date as 2021-march 1 st
end_date = datetime.date(2021, 3, 1)
 
# delta time
delta = datetime.timedelta(days=1)
 
# iterate over range of dates
while (start_date <= end_date):
    print(start_date, end="\n")
    start_date += delta



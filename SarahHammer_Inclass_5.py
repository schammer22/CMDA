#Sarah Hammer
#In class 5, parts 1-3
#CMDA 3654

'''
Part 1 
'''

#The following code was executed in Terminal using iPython

#2.
import pandas

import numpy

import matplotlib

#used tab completion to browse functions for each package


#3.
pandas?
pandas.*ver*?

pandas.factorize?
pandas.factorize.*ver*?

pandas.stats?
pandas.stats.*ver*?

pandas.unique?
pandas.unique.*ver*?

pandas.save?
pandas.save.*ver*?

pandas.merge?
pandas.merge.*ver*?

#4 
#Ran the shortcut commands listed in the powerpoint
#• Ctrl-l (clear screen) 
#• Up-arrow; 
#• Down-arrow (scroll command history)
#• _i20 (refers to the input on line 20)
#• _20 (refers to the output on line 20)

#5
#Ran the magic commands listed in the powerpoint
# %reset (delete all objects you created)
# %run
# %paste
# %quickref (iPython Quick Reference Card)
# %timeit (computes average time of execution for a snippet of code)
# %hist (your input history)
# %pwd (returns current working directory)
# %cd directory_name (changes working directory to the named one)
# %ls (see all files in current working directory)

#6
#Ran the following code in iPython from in class 4_3
ten_things = "Apples Oranges Crows Telephone Light Sugar"
stuff = ten_things.split(' ')

print stuff[1]

#7
%xdel?
str.split?
re?
matplotlib.pylab?

#8
iPython --pylab
a = numpy.random.randn(100)
plot(a.cumsum())

numpy.random?
#generate random numbers

#9
numpy.cumsum?
#takes the cumulative sum of elements along an axis

#10
%timeit numpy.random.randn(100)
#100000 loops, best of 3: 5.37 µs per loop

%timeit numpy.random.randn(1000)
#10000 loops, best of 3: 40.7 µs per loop


%timeit numpy.random.randn(10000)
#1000 loops, best of 3: 390 µs per loop

'''
Part 2
'''

import numpy as np

#1
# Created a new ipython notebook “Inclass5_2”


#2
#Created two one-dimensional arrays with 5 elements of your choice. 
data1 = [6, 7.5, 8, 0 , 1]
data2 = [1, 2, 3.5, 7, 99]

#Displays array’s shape and type.
arr1 = np.array(data1)
arr2 = np.array(data2)
arr1.dtype
arr1.shape
arr2.dtype
arr2.shape

#3
#element-wise summation for the two arrays.
arrSum = arr1 + arr2
arrSum

#4
#element-wise product for the two arrays.
arrProduct = arr1 * arr2
arrProduct

#5 
#Create a 6X6 identity matrix.
imatrix = eye(6)
imatrix

#6
#Replaces all element on third row with value 5.
imatrix[2,] = 5
imatrix

#7 
#Replaces all elements that are not zero with value 6 using a boolean indexing and slicing.

#8
#Creates an empty 3 dimensional array, arr3 with shape (2,3,4), and elements of integer type.
arr3 = np.empty((2,3,4))
arr3

#9
#Display its number of dimensions, shape and type of each element.
arr3.dtype
arr3.shape
arr3.ndim

#10
#Gives the second element on the third dimension
#from the second group on the second dimension,
#from the first group on the first dimension the value 5.
arr3[0,1,1] = 5
arr3

#11
#Generates an array of 20 uniformly distributed random numbers with values between 0 and 1.
arr4 = rand(20)

#12
#Get the min, max, sum, mean, and standard deviation of the array in part 11.
arr4.min()
arr4.max()
arr4.sum()
arr4.mean()
arr4.std()

#13
#Replaces all elements less than 0.5 with 0 and all elements larger than 0.5 with 1 in the array from part 11 using “where” function.
arr4[arr4 < 0.5] = 0
arr4[arr4 > 0.5] = 1
arr4

#14
#Sorts the array in part 11.
arr4.sort()
arr4

#15
#Finds the unique values in the same array.
unique(arr4)

#16 
#Save your ipython notebook and download it as .py. Open it with your editor 
#(Notepad++ etc.) and make sure that there are correct and complete comments delimiting all your code and output.

'''
Part 3
'''

#1
#Go to quandl.com. Open an account. Go to the “Account Settings” and make note of your API Key.


#2
#Go to https://github.com/quandl/Python. Click on “Download ZIP”. Unzip folder and copy “setup.py” 
#and “Quandl” folders into your local folder where you run ipython. (EG: C:\Users\Denisa)


#3
#Create a new ipython notebook, In5_3. Import pandas module. Import Quandl module by “import Quandl”.
#    Since we already have the required NumPy and Pandas modules, it should work for you.
import pandas as pd
import Quandl as ql

#4
#Go to https://www.quandl.com/c/markets/bitcoin-data

#5
# You will import data for Bitcoin exchange rates to USD on different venues: Bitstamp, Bitfinex
# and LakeBTC. Go to:
#  https://www.quandl.com/BCHARTS/BITSTAMPUSD
# Click on “Python” Library on the right. The code you need to use to import data will show up. 
# Import only 2014 data to September30. Use your authentication key. Example code:
# bitstamp = Quandl.get("BITCOIN/BITSTAMPUSD", trim_start="2014-01-01", trim_end="2014-09- 30", authtoken="2_mykey_T")
# Import in separate DataFrames the data for Bitfinex and LakeBTC as well.

bitCharts = ql.get("BCHARTS/BITSTAMPUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="d2RqcjFpy3hu6apaVJrP")
bitFinex = ql.get("BAVERAGE/USD_BITFINEX", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="d2RqcjFpy3hu6apaVJrP")
lakeBTC = ql.get("BCHARTS/LAKEUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="d2RqcjFpy3hu6apaVJrP")

#6 
#View your three created pandas data frames using df_name.head(). What are the column names? 
#What is the frequency of data (daily/weekly/yearly Bitcoin prices)? Answer in comments

bitCharts.head()
bitFinex.head()
lakeBTC.head()

# bitCharts - Column Names: Open, High, Low, Close, Volume (BTC), Volume (Currency), Weighted Price
#           - Frequency: Daily
# bitFinex  - Column Names: Ask, Bid, Last, Volume (BTC), Volume (% of Total)
#           - Frequency: Daily
#lakeBTC    - Column Names: Open, High, Low, Close, Volume (BTC), Volume (Currency), Weighted Price
#           - Frequency: Daily

#7 
#Create three objects ind1, ind2, and ind3 containing the index of each of the created dataframes.
ind1 = bitCharts.index
ind2 = bitFinex.index
ind3 = lakeBTC.index

#8 
#Display ind1, ind2, ind3. How many elements are in each?

ind1
ind2
ind3

# ind1: 273
# ind2: 2
# ind3: 214

#9
#Display the .values attribute of each of ind1, ind2, ind3.

ind1.values
ind2.values
ind3.values

#What type of object is being displayed
#   for each? What dtype is each element of the displayed object?
#ind1: A date of dtype - datetime64[ns]
#ind2: A date of dtype - datetime64[ns]
#ind3: A date of dtype - datetime64[ns]

#10 
#Display the .columns attribute of each DataFrame

bitCharts.columns
bitFinex.columns
lakeBTC.columns

# How many columns do we have in each?
# bitCharts: 7
# bitFinex: 5
# lakeBTC: 7

#11
#Drop the variable showing BTC volume from each dataframe using the .drop method.
bitCharts.drop("Volume (BTC)", axis=1)
bitFinex.drop("Volume (BTC)", axis=1)
lakeBTC.drop("Volume (BTC)", axis=1)

#12
# Download your saved ipython notebook as .py, edit the content with your editor, add it to the
#  overall Inclass5 assignment marking it clearly as Part 5_3.


#13
#Upload your finalized Inclass 5 (containing the three parts from Mon, Wed and Frid) to Dropbox
#   and GitHub.

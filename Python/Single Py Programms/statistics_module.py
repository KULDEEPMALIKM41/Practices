from statistics import *

a = [1,10,3.5,4,6,7.3,4]
b = [2,2,3,8,9]

print("mean(a) - ",mean(a)) # The mean() method calculates the arithmetic mean of the numbers in a list.
print("mean(b) - ",mean(b)) 

print("median(a) - ",median(a)) # The median() method returns the middle value of numeric data in a list.
print("median(b) - ",median(b))

print("mode(a) - ",mode(a)) # The mode() method returns the most common data point in the list.
print("mode(b) - ",mode(b))

print("median_grouped(a) - ",median_grouped(a,interval=2)) # The median_grouped() method return the 50th percentile (median) of grouped continuous data
print("median_grouped(b) - ",median_grouped(b,interval=2)) # interval by default is 1. 

print("median_high(a) - ",median_high(a)) # The median_low() method returns the high middle value of numeric data in a list.
print("median_high(b) - ",median_high(b))

print("median_low(a) - ",median_low(a)) # The median_low() method returns the low middle value of numeric data in a list.
print("median_low(b) - ",median_low(b))

print("harmonic_mean(a) - ",harmonic_mean(a)) # The harmonic_mean() method returns the harmonic mean of data.
print("harmonic_mean(b) - ",harmonic_mean(b))

print("variance(a) - ",variance(a)) # The variance() method returns the sample variance of data.
print("variance(b) - ",variance(b))

print("stdev(a) - ",stdev(a)) # The stdev() method returns the square root of the sample variance.
print("stdev(b) - ",stdev(b))

    
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

# Exercises Part I

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato",
     "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# 1. Determine the number of elements in fruits. 

fruits.size #17 elements 

# 2. Output only the index from fruits.

fruits.index #RangeIndex(start=0, stop=17, step=1)

# 3. Output only the values from fruits.

fruits.values 

# 4. Confirm the data type of the values in fruits.

fruits.dtype #object

# 5. Output only the first five values from fruits. Output the last three values. Output two random values from fruits.

fruits.head(5)
fruits.tail(3)
fruits.sample(2)

# 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.

fruits.describe()

# 7. Run the code necessary to produce only the unique string values from fruits.

fruits.unique()

# 8. Determine how many times each unique string value occurs in fruits.

fruits.value_counts()

# 9. Determine the string value that occurs most frequently in fruits.

value_counts = fruits.value_counts()
value_counts.head(1) #kiwi

# 10. Determine the string value that occurs least frequently in fruits.

fruits.value_counts().nsmallest(n=1, keep='all')

# Exercises Part II

# 1. Capitalize all the string values in fruits.

fruits.str.capitalize()

# 2. Count the letter "a" in all the string values (use string vectorization).

fruits.str.count("a").sum() # 14 letter "a"

# 3. Output the number of vowels in each and every string value.

fruits.str.count('[aeiou]')

# 4. Write the code to get the longest string value from fruits.

max(fruits, key=len)

# 5. Write the code to get the string values with 5 or more letters in the name.

fruits[fruits.str.len() >= 5]

# 6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.

fruits[fruits.apply(lambda x: x.count('o') >= 2)]
# tomato, gooseberry

# 7. Write the code to get only the string values containing the substring "berry".

fruits[fruits.str.contains('berry')]
# strawberry, blueberry, blackberry, gooseberry

# 8. Write the code to get only the string values containing the substring "apple".

fruits[fruits.str.contains('apple')]
#3           pineapple, gala apple, honeycrisp apple

# 9. Which string value contains the most vowels?

fruits[max(fruits.str.count('[aeiou]'))]

# Exercises Part III

letters = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
)
letters = pd.Series(letters)

# 1. Which letter occurs the most frequently in the letters Series?
letters.describe()

# y is the top letter with freq of 13

# 2. Which letter occurs the Least frequently?
letters.value_counts()
# l is the least with frequency of 4 

# 3. How many vowels are in the Series?

letters.str.count('[aeiou]').sum()
# 34 vowels

# or using isin

letters.str.lower().isin(['a', 'e', 'i', 'o', 'u']).sum()

# 4. How many consonants are in the Series?

len(letters[letters.isin('aeiou') == False])


# 5. Create a Series that has all of the same letters but uppercased.

letters.str.capitalize()

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.

letters.value_counts().head(7).plot(kind='bar', ec='black')
plt.title('6 Most Common')
plt.show()

#### Use pandas to create a Series named exam_scores from the following list:

numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

numbers
# 1. What is the data type of the numbers Series?

numbers.dtype

# 2. How many elements are in the number Series?

numbers.size

# 3. Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.

numbers = numbers.str.replace('$', '').str.replace(',', '').astype('float')

# 4. Run the code to discover the maximum value from the Series.

numbers.max()

# 5. Run the code to discover the minimum value from the Series.

numbers.min()

# 6. What is the range of the values in the Series?

numbers.max() - numbers.min()

# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

numbers_binned = pd.cut(numbers, 4).value_counts()


# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

numbers_binned.plot(kind = 'bar', color = 'red', xlabel = 'USD', ylabel = 'Amount')
plt.title('Frequency')
plt.show()


### Use pandas to create a Series named exam_scores from the following list:

exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# 1. How many elements are in the exam_scores Series?

# 2. Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.

# 3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

# 4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.

# 5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.

# 6. Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.






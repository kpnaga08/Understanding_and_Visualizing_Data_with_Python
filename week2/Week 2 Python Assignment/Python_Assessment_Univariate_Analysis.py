Question 1
Using the NHANES data and the previous notebook, the following questions will be about the variable BPXSY2 (with missing values remove). Round your answer to the nearest tenth. (ex: 2.33 should be 2.3, 2.15 should be 2.2)

What is the median?

Answer: 122

Question 2

What is the mean?

Round your answer to the nearest tenth. (ex: 2.33 should be 2.3, 2.15 should be 2.2)

Answer: 124.8

Question 3
What is the standard deviation?

Round your answer to the nearest tenth. (ex: 2.33 should be 2.3, 2.15 should be 2.2)

Answer: 18.5

Question 4
What is the max?

Round your answer to the nearest tenth. (ex: 2.33 should be 2.3, 2.15 should be 2.2)

Answer: 238

Question 5
What is the Interquartile Range (IQR)?

Round your answer to the nearest tenth. (ex: 2.33 should be 2.3, 2.15 should be 2.2)

Answer: 22

Question 6
Which of these will return descriptive statistics for a numeric Series ‘s’?


Series.describe()
describe(s)
s.descriptive_stats()
s.describe()

Answer: s.describe()

Question 7
Select all that apply: Which will produce a histogram of the numeric Series ‘s’


sns.distplot(s)

sns.distplot(a=s)

sns.hist(a=s)

sns.hist(a=s).set(title="Histogram of s")

sns.hist(s)

sns.distplot(a=s).set(title="Histogram of s")

Answer: sns.distplot(s); sns.distplot(a=s); sns.distplot(a=s).set(title="Histogram of s") 

Question 8
How many rows of the DataFrame 'df' are shown with the following code: 

df.head()

Answer: 5

Question 9
What data is shown when the following code is run?

df.head(2)


Columns 1 and 2
Columns 0 and 1
Rows 1 and 2
Rows 0 and 1
All rows containing the value '2'

Answer: Rows 0 and 1
"""
Chapter 2 Exercises
Applied exercises in chapter 2 start with exercise 8
"""
import pandas as pd
import matplotlib.pyplot as plt

def exercise_8():
    """First applied exercise of ch 2"""
    print('Ch 2 | Exercise 8')
    print()
    # (a)
    college = pd.read_csv('data_sets/College.csv', header=0)

    # (b)
    print('college data frame')
    print(college.head())
    print()
    college.drop(college.columns[[0]], axis=1, inplace=True)

    # (c)
    # i.
    print()
    print(college.describe())

    # ii.
    print('Plotting pairs...')
    pd.plotting.scatter_matrix(college.iloc[:, : 10], alpha=0.2)
    plt.show()

    # iii.
    print()
    # college.boxplot(['Outstate', 'Private'])
    # plt.show()

    # vi.

    # v.

    # vi.

def exercise_9():
    """Second applied exercise from ch 2"""
    print('Ch 2 | Exercise 9')
    # Missing values are classified with a "?"
    auto = pd.read_csv('data_sets/Auto.csv', header=0, na_values='?')

    # Remove missing values
    auto.dropna(inplace=True)

    # (a) - (c)
    print('Qualitative Predictors:  name')
    print('''Quantitative Predictors: mpg, cylinders, displacement, horsepower,
        weight, acceleration, year, origin''')
    print(auto.describe())

    # (d)
    new_auto = auto.drop(auto.index[10:85])
    print()
    print(new_auto.describe())

    # (e)
    pd.plotting.scatter_matrix(auto.iloc[:, : 7], alpha=0.2)
    plt.show()
    """
    NOTES:
      - As Cylinders, Displacement, Horsepower, and Weight increase, MPG decreases
      - As Acceleration and Year increase, MPG also increases
      - There's a positive relationship between Horsepower, Cylinders and Displacement
      - The upper range of Displacement, Horsepower, and Weight disappear in later years
      - Interestingly, there's a negative relationship between Horsepower and Acceleration
         probably due to the positive relationship between Horsepower and Weight
    """

    # (f)
    """
    Yes, specifically weight, horsepower, displacement, and cylinders all have tighter groupings
      of their data points when compared to mpg, suggesting a strong relationship between those
      data points and mpg.
    """

def exercise_10():
    """Third applied exercise from ch 2"""
    boston = pd.read_csv('data_sets/Boston.csv', header=0, index_col=0)

    # (a)
    print(boston.info())
    print()

    # (b)
    pd.plotting.scatter_matrix(boston, alpha=0.2)
    plt.show()

    # (c)
    """
    NOTES:
      - Slight positive relationship between crim and lower status population
      - Slight negative relationship between crim and median value of occupied homes
      - Positive relationship between industrial acres and nitric oxcide concentration (NOX)
      - Negative relationship between industrial acres and distance from employment centers
      - Positive relationship between NOX and age of home
      - Negtive relationship between NOX and employment centers
      - Positive relationship between NOX and lower status population
      - Negative relationship between NOX and median home value
      - Negative relationship between rooms per dwelling and lower status pop
      - Positive relationship between rooms per dwelling and median home value
      - etc...
    """

    # (d)

    # (e)

    # (f)

    # (g)

    # (h)

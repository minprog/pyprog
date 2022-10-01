# Klimaatanalyse

![](../eca2csv/temperature.png)

Time to do real analysis. Write a program called `klimaat.py` that can read a file called `climate.csv` and print the following analysis from the data:

    CLIMATE ANALYSIS

    Data file
    -----------
    Filename: climate.csv
    First date: 01-01-1901
    Last date: 31-12-2019

    Basic information
    -----------------
    Lowest temperature: -11.4° on 26-01-1942
    Highest temperature: 37.5° on 25-07-2019
    Average temperature: 13.6°

    Extremes 2010-2019
    ------------------
    In 2010 the temperature varied between -6.1° on 02-12 and 34.4° on 09-07
    In 2011 the temperature varied between -0.1° on 31-01 and 32.2° on 28-06
    In 2012 the temperature varied between -5.1° on 03-02 and 33.0° on 19-08
    In 2013 the temperature varied between -2.8° on 17-01 and 34.0° on 02-08
    In 2014 the temperature varied between 1.0° on 3-12 and 32.9° on 19-07
    In 2015 the temperature varied between -1.3° on 23-01 and 33.1° on 01-07
    In 2016 the temperature varied between -0.8° on 29-12 and 32.9° on 20-07
    In 2017 the temperature varied between -1.9° on 18-01 and 31.9° on 27-05
    In 2018 the temperature varied between -4.6° on 28-02 and 35.7° on 26-07
    In 2019 the temperature varied between -1.1° on 24-01 and 37.5° on 25-07

    Longest heatwaves 2010-2019
    -----------------------------
    2010: ? days
    2011: ? days
    2012: ? days
    2013: ? days
    2014: ? days
    2015: ? days
    2016: ? days
    2017: ? days
    2018: ? days
    2019: ? days

## Instructions

- Use the file `climate.csv` that you generated in the previous assignment.

- You must load all data into a variable for further processing.

- It is not allowed to calculate all information in a single long function. This is slightly more efficient but disastrous for the readability of your code. Make sure that you perform each analysis in a separate functions.

- Also think about how you could split up your code into functions even more.

- Write doctests and ensure that all types are in order.

## Algorithmic hints

- A lot of this assignment is about finding largest and smallest values from all or parts of the data. The book provides some ideas about this in the section "Processing Whitespace-Delimited Data" (p. 192).

- It's fine to use some of the ugliest tricks to dig trough the data. Make sure that you get everything working first and only then consider making your code tidier and simpler.

# Preprocessing

![](temperature.png)

Let's contribute to the global climate discussions and analyse the large datasets that are [published](https://www.ecad.eu/dailydata/predefinedseries.php) by ECA (European Climate Assessment). We will limit the analysis to the maximum temperatures measures in De Bilt, Utrecht since 1901.

Take a look at [`climate.txt`](climate.txt) and read the description of how the data is encoded. The file does not have a standard format, but instead a format that is defined by ECA. Because of this, some preprocessing steps will need to be performed before we can do analyses on the data.

The goal is to get the ECA data file in a CSV format. Dit is a widely implemented standard that you can, for example, easily import into Excel, but can also be read using the many programming languages that offer data processing facilities. The CSV format assumes that data is in a tabular format, with many lines of data, each containing one or more fields.

The desired format is as follows. The first line needs to contain the *names* of all data fields (also called columns), separated by commas. All other lines contain data entries, where the fields are also separated by commas. Here's an example of a CSV file with just two columns.

![](telefoon.png)

Note: the operations in this assignment do sometimes resemble the examples from the book, but these certainly aren't copy-paste assignments. One different is that below, you need to define 4 functions that each open two files and read from those. In the book examples, files are opened in `main`, but that is not what is required here. Also, we will not use `StringIO` but just data files.

## Removing header lines

So before we start processing the data, take another good look at the ECA file called `climate.txt`. One thing to notice is that it has the header text containing information about the data format. It was great to understand how the file works, but not so great for automatically processing the data. In this case, there are not clear markers that help find where the data starts (like, for example, a line of dashes `------`). So we decide that the first preprocessing step is to remove the header text, leaving the column names and data.

![](step1.png)

**Assignment**

- Write, in a file called `eca2csv.py` a function that opens a **source** file, reads the data, skips the header text, and writes the result to a **target** file.

- Parameters of the function are: the names of the source and target files, plus the number of lines that need to be removed (e.g. 19). You need to decide on a name for the function and its parameters.

- It's not advisable to read in all lines of the file into a variable when you to data processing. For huge data files it's even impossible because these are larger than what fits in your computer's memory. Make sure to not do this.

- Study the examples from the book well. Employ the book's best practices, like using a `with` statement to open both files.

- Write in `main` a line of test code that calls the new function with source file name `climate.txt` and target file name `climate-noheader.txt`. Run your program and inspect whether the results are as expected.

## Data filteren
​
In the data you may notice that the year 2020 data is incomplete. Using those data when calculating statistics would yield distorted numbers. For examples, when calculating average temperatues per year, 2020 would be very cold indeed, because we only have temperatures for the first three months. The same would hold for statistics over multiple years, etc. So the next goal is to be able to remove some parts of the data (in our data file this would be 2020).

![](step2.png)

**Assignment**

- Write a function that reads a data file and saves a new data file where the data from a given year have been removed. The function that you write must be able to remove data from any year, so this would be a parameter for the function.

- In the data, the year can be found in the first four characters of a data line.

- The function must open and close the files as indicated by filenames provided in parameters.

- Write in `main` a line of test code that calls your function with source `climate-noheader.txt` and target `climate-noheader-no2020.txt`. Run your program and inspect the correctness of the results.

## Cleaning missing values

The data contains some "missing values": dates for which no measurements have been recorded. In the ECA data file these dates have a TX-value of 9999. These numbers can readily distort any calculations if we would interpret them as real temperatures. We will solve this by replacing the missing values by the avarage value of the previous and next days (rounded via the `round`-function).

The indicator for a missing value may differ between data files. Sometimes it would be `-1`, sometimes `0`, depending on the range of values that actual measurements could take. In this case `9999` can be used safely, because the odds of having temperatures of 999,9 degrees approach 0.

![](step3.png)

**Assignment**

- Write a function that reads a data file and saves a new data file where missing values are replace by the average value as described above.

- The function must have a parameter to indicate the value that is used as a "missing value".

- The function must open and close the files as indicated by filenames provided in parameters.

- Write in `main` a line of test code that calls your function with source `climate-noheader-no2020.txt` and target `climate-cleaned.txt`. Run your program and inspect the correctness of the results.

Hints:

- This problem is somewhat more involved than the other steps. You can use the "readline technique" from the book (page 181), but to calculate missing values you need access to *three consecutive lines*.

- This means that you should read one line at a time, as usual, but that you will need to keep track of the two previous lines of data too. To achieve that, you can save "old" temperature values while reading the data.

- Develop your algorithm on paper and thoroughly analyse its workings using an example dataset of just 6 lines.

## Converting to commas

As a final processing step, we need to replace the semicolons in the datafile (`;`) by commas (`,`).

**Assignment**

- Write a function that reads a data file and saves a new data file where semicolon separators are replaced by commas.

- The function must open and close the files as indicated by filenames provided in parameters.

- Write in `main` a line of test code that calls your function with source `climate-cleaned.txt` and target `climate.csv`. Run your program and inspect the correctness of the results.

## Testing

The testing code for all function should be in `main`. When the program is run, all of the *intermediate* files `climate-noheader.txt`, `climate-noheader-no2020.txt`, `climate-cleaned.txt` and `climate.csv` should be generated.

We haven't specified the names of your functions. This means that we cannot automatically test your functions individually, but we can only run the program and determine whether the right output files are generated.

To test, your program will be run using the ECA data file as linked in this assignment, but also using a slightly different data files, to see whether your program keeps working correctly when for example the "missing value" indicator isn't 9999 but -9999 (and other variations).

Other than that, all types will be checks. Doctests aren't useful here because the program only changes data files and functions return no values. Hence, doctests will not be checked.

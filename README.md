# sqlalchemy-challenge - sql-alchemy assignment - Data Analytics Bootcamp

### Description
This assignment aims at analysing the climate of Hawaii.

### Guide to Repository:
* The Resources folder contains the hawaii.sqlite database and two csv files - hawaii_measurements.csv and hawaii_stations.csv.
* The Images folder contains the expected output files for the assignment
* The Output_Images folder contains the output graphs generated as part of the assignment.
* climate_starter.ipynb is the jupyter notebook for Step 1 of the assignment -  Climate Analysis and Exploration for Precipitaion and Station Analysis
* app.py is the python file for Step 2 - Climate App
* temp_analysis_bonus_1_starter is the jupyter notebook for Bonus - Temperature Analysis I
* temp_analysis_bonus_2_starter is the jupyter notebook for Bonus - Temperature Analysis II

### Step a: Setting up in GitHub
Created the repository sqlalchemy-challenge. Cloned it to the local computer and updated the repository on a regular basis.

### Step 1 - Climate Analysis and Exploration
climate_starter.ipynb contains the precipitation analysis and station analysis by connecting to the sqlite database provided in the Resources folder.

#### Precipitation Analysis
Graph is plotted to depict the precipitation data for the last 12 months.

#### Station Analysis
Histogram is plotted for the most active station to depict the temperature observations for the last 12 months.

### Step 2 : Climate App
The app is added in app.py. It shows available routes in the home page.
Each route and the data displayed by them are as following.
* /api/v1.0/precipitation - displays the dates and precipitation values for the last 12 months.
* /api/v1.0/stations - displays all the stations available.
* /api/v1.0/tobs - displays the temperature observations of the most active station for the last year of data.
* /api/v1.0/start - displays the minimum temperature, the average temperature, and the maximum temperature for all dates greater than or equal to the start date.
or
* /api/v1.0/start/end - displays the minimum temperature, the average temperature, and the maximum temperature for dates between the start and end date inclusive.

### Step 3 : Bonus - Temperature Analysis I
* Compared June and December temperature data using independent t-test. A p value of 3.9025129038616655e-191 was obtained.
* Analysis - Here, the Null Hypothesis is that the two independent samples have identical average values.Since the p-value is less than 0.05, it indicates strong evidence against the null hypothesis and hence the null_hypothesis can be rejected because there is only 5% probability that the null hypothesis is correct. Thus, the difference in mean is statistically significant

### Step 4 : Bonus - Temperature Analysis II
* Plotted the bar graph for the average temperature for the period between 01-08-2017 and 07-08-2017. The error bar was plotted for the same period for the difference between maximum and minimum temperature.
* Plotted area graph to show the minimum, average and maximum temperatures for the same day and month in range (01-08-2017 and 07-08-2017) across all years .

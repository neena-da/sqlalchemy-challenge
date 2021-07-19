# sqlalchemy-challenge - sql-alchemy assignment - Data Analytics Bootcamp

### Description
This assignment aims at analysing and researching the database of employees from the 1980s and 1990s at Pewlett Hackard. The database contains 6 CSV files.

### Guide to Repository:
All the files are available in the folder EmployeeSQL. There is a gitignore file included to protect the database login details.
The data folder contains the 6 csv files.
The Output folders contains sql files with the queries, the ERD and the visualizations.
The Bonus question is solved in the EmployeeSQL_Bonus.ipynb file.

### Step a: Setting up in GitHub
Created the repository and folder EmployeeSQL. Cloned it to the local computer and updated the repository on a regular basis.

### Step 2 : ERD Diagram
* Sketched the ERD diagram using www.quickdatabasediagrams.com. Created the tables and listed the columns and types along with the primary keys, foreign keys and composie keys. Established the one to many and one to one relations between the tables.Two of the tables dept_emp and dept_manager are set up with composite keys as can be seen in the EmployeeSQL_Enterprise Relation Diagram.png in the Output folder.

### Step 3 : Importing data and Running Queries in Postgres
* Created database called EmployeeSQL in Postgres
* Created the 6 tables in the database using the CREATE TABLE statement, in order,  so that all the primary key/ foreign key relations are in alignment. The Create table queries are saved in EmployeeSQL_table_schemata.sql file in the Output folder.
* Imported data into the 6 tables using import function from the provided csv files.
* Ran query statements to get the desired outputs which is saved in EmployeeSQL_queries.sql file in the Output folder.


### Step 4 : Bonus
* Created an engine and connection between the Postgres database and jupyter notebook in jupyer notebook.
* Using pandas, matplotlib and sqlalchemy, created the below visualizations
	* Histogram plotted for the salary range of employees
	  Tables used : salary_data
	* Bar chart plotted for the average salary per job title 
	  Tables used : employee_data, salary_data, title_data
* Visualizations are saved in the Output folder.
* There are some inconsistencies that can be observed from the graphs, for example, verage salary for the senior staff and staff are higher when compared to the average salary of managers. This would make one question the authenticity of the data in the dataset

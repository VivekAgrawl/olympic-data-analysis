import pandas as pd
import warnings
warnings.filterwarnings("ignore")


#Task1
#Loading the data
def read_data_from_csv():
    df = pd.read_csv('dataset_olympics.csv')
    return df


#Task 2: Renaming the Columns
def data_cleaning():
    # Read data from a CSV file
    data = read_data_from_csv()

    # Create a copy of the data
    df = data.copy()

    # Dropping columns 'Height' and 'Weight'
    df = df.drop(columns = ['Height', 'Weight'], axis = 1)

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Replace missing values in the 'Medal' column with 'Medal-less'
    df['Medal'] = df['Medal'].fillna("Medal-less")

    # Replace missing values in the 'Age' column with the median age('24') from the dataset
    df['Age'] = df['Age'].fillna(24)

    # Save the cleaned dataset to a new CSV file named 'olympics_history_cleaned.csv'
    df.to_csv('olympics_history_cleaned.csv', index=False)

    # Return the cleaned dataset
    return df

#Do not Delete the Following function
def task_runner():
    data_cleaning()
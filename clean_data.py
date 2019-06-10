import pandas as pd

# use this function to remove rows with NULL, NAN or missing values from the dataset
def clean_data(filename):
    '''Loads a .csv file and "cleans" it by removing any rows with NaN values.'''

    df = pd.read_csv(filename)
    df.dropna(inplace=True)
    df.to_csv(filename)

if __name__ == '__main__':

    # define filepaths for the 2 datafiles based on my local system
    global_data = 'data/global_data.csv'
    city_data = 'data/city_data.csv'

    clean_data(global_data)
    clean_data(city_data)

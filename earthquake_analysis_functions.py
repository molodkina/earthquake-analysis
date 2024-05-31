import pandas as pd

def read_data(file_path):
    """
    Read earthquake data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pandas.DataFrame: DataFrame containing earthquake data.
    """
    data = pd.read_csv(file_path)
    return data


def filter_alaska(data):
    """
    Filter out earthquakes in Alaska, USA.
    
    Args:
        data (pandas.DataFrame): DataFrame containing earthquake data.
    
    Returns:
        pandas.DataFrame: DataFrame with Alaska, USA earthquakes removed.
    """
    filtered_data = data[~data['place'].str.contains('Alaska', case=False, na=False)]
    return filtered_data


def split_place(data):
    """
    Split the 'place' column by ',' and save the last part (country) to 'location'. 
    If it's not possible to extract the country information, save 'place' to 'location'.
    
    Args:
        df (pandas.DataFrame): DataFrame containing earthquake data.
    
    Returns:
        pandas.DataFrame: DataFrame with 'location' column added.
    """
    split_location = data['place'].str.rsplit(',', n=1, expand=True)
    data['location'] = split_location[1].str.strip().fillna('')
    data.loc[data['location'] == '', 'location'] = data['place'].str.strip()
    return data


def get_most_earthquakes(data, number_locations):
    """
    Get the territory/country with the most earthquakes.
    
    Args:
        data (pandas.DataFrame): DataFrame containing earthquake data.
        number_locations (int): Number of top locations to retrieve.
    
    Returns:
        pandas.DataFrame: DataFrame with top locations and earthquake counts.
    """
    eq_by_place = data['location'].value_counts().reset_index()
    eq_by_place.columns = ['location', 'numEQ']
    return eq_by_place.head(number_locations)


def get_top_magnitudes(data, number_locations):
    """
    Get the top locations with the highest magnitude earthquakes.
    
    Args:
        data (pandas.DataFrame): DataFrame containing earthquake data.
        number_locations (int): Number of top locations to retrieve.
    
    Returns:
        pandas.DataFrame: DataFrame with top locations and highest magnitude earthquakes.
    """
    top_magnitudes = data.sort_values(by='mag', ascending=True)
    top_three_magnitudes = top_magnitudes['mag'][-number_locations:]
    top_magnitude_data = data[data['mag'].isin(top_three_magnitudes)]
    sorted_top_magnitude_data = top_magnitude_data.sort_values(by='time', ascending=False)
    return sorted_top_magnitude_data[['location','mag', 'time']]


def calculate_risk_metric(data, number_locations):
    """ 
    Calculate risk metric for each location. To measure the magnitudes of earthquakes, we will use the Richter scale,
    which is a base-ten logarithmic scale.
    
    Args:
        data (pandas.DataFrame): DataFrame containing earthquake data.
        number_locations (int): Number of top risky locations to retrieve.
    
    Returns:
        pandas.DataFrame: DataFrame with top risky locations and their risk metrics.
    """
    data_subset = data[['location', 'mag']]
    data_subset['mag_10exp'] = 10 ** data_subset['mag']
    grouped_data = data_subset.groupby('location', as_index=False)['mag_10exp'].sum()
    sorted_grouped_data = grouped_data.sort_values(by='mag_10exp', ascending=False)
    sorted_grouped_data.columns = ['location', 'riskMetric']
    
    return sorted_grouped_data.head(number_locations)
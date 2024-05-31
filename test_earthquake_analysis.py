import unittest
import pandas as pd
from earthquake_analysis_functions import *

class TestEarthquakeFunctions(unittest.TestCase):

    def test_get_most_earthquakes(self):
        # Sample data
        data = pd.DataFrame({
            'location': [
                'Puerto Rico', 
                'Indonesia',
                'Greece', 
                'Japan', 
                'Puerto Rico', 
                'Puerto Rico',
                'Indonesia'
            ]
        })

        # Running the get_most_earthquakes function
        result = get_most_earthquakes(data, 2)

        # Extracting the number of earthquakes for the top 2 locations
        first_location_numEQ = result.iloc[0]['numEQ']
        second_location_numEQ = result.iloc[1]['numEQ']

        # Print to check values
        print("\nNumber of earthquakes in the location with the most earthquakes:", first_location_numEQ)
        print("Number of earthquakes in the second location:", second_location_numEQ)

        # Assert that the first count is greater than or equal to the second count
        self.assertGreaterEqual(first_location_numEQ, second_location_numEQ)

    def test_get_top_magnitudes(self):
        # Sample data
        data = pd.DataFrame({
            'location': [
                'Puerto Rico', 
                'Indonesia',
                'Greece', 
                'Japan', 
                'Puerto Rico', 
                'Puerto Rico',
                'Indonesia'
            ],
            'mag': [2.5, 3.0, 2.0, 4.0, 2.0, 3.5, 3.2],
            'time': [
                '2023-05-01T00:00:00Z',
                '2023-05-02T00:00:00Z',
                '2023-05-03T00:00:00Z',
                '2023-05-04T00:00:00Z',
                '2023-05-05T00:00:00Z',
                '2023-05-06T00:00:00Z',
                '2023-05-07T00:00:00Z'
            ]
        })

        # Running the get_top_magnitudes function
        result = get_top_magnitudes(data, 1)

        # Extracting the top magnitudes
        top_magnitude_result = result['mag'].values

        # Assert that the highest magnitude in the result are indeed the highest in the data
        top_magnitude_data = data['mag'].sort_values(ascending=False).head(1).values

        # Print to check values
        print("\nTop magnitudes in the result:", top_magnitude_result)
        print("Highest magnitudes in the data:", top_magnitude_data)

        # Assert that the magnitudes match
        self.assertTrue((top_magnitude_result == top_magnitude_data).all())

   
    def test_calculate_risk_metric(self):
        # Sample data
        data = pd.DataFrame({
            'location': [
                'Puerto Rico', 
                'Indonesia',
                'Greece', 
                'Japan', 
                'Puerto Rico', 
                'Puerto Rico',
                'Indonesia'
            ],
            'mag': [2.5, 3.0, 2.0, 4.0, 2.0, 3.5, 3.2]
        })

        # Running the calculate_risk_metric function
        result = calculate_risk_metric(data, 1)

        # Extracting the top risk metric
        top_risk_metric = result['riskMetric'].values

        # Calculate expected risk metrics manually
        top_mag = data['mag'].sort_values(ascending=False).head(1).values
        expected_risk_metric = 10 ** top_mag

        # Print to check values
        print("\nCalculated top risk metric:", top_risk_metric)
        print("Expected top risk metric:", expected_risk_metric)

        # Assert that the risk metrics match
        self.assertTrue((top_risk_metric == expected_risk_metric).all())

if __name__ == '__main__':
    unittest.main()

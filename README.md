# Earthquake Analysis

This project analyses earthquake data to identify the locations with the most earthquakes, the top magnitudes, and the riskiest locations based on a custom risk metric.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Testing](#testing)
4. [Project Structure](#project-structure)

## Installation

1. **Clone the repository:**

    ```bash
   git clone https://github.com/molodkina/earthquake-analysis.git
   cd earthquake-analysis
    ```

2. **Set up a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Place your earthquake data CSV file in the project directory.**

NOTE: a testing file 'file.csv' (earthquakes within the last 30 days as of 31 May 2024) is provided for your convenience.

2. **Run the script to perform the analysis with the argument containing the name of your file. An example command is:**

    ```bash
    python earthquake_analysis.py file.csv
    ```

## Testing

1. **To run the unit tests, execute the following command:**

    ```bash
    python -m unittest test_earthquake_analysis.py
    ```

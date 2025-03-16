import pandas as pd
import numpy as np

# Instantiate a dictionary of planetary data.
data = {'planet': ['Mercury', 'Venus', 'Earth', 'Mars',
                   'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
        'radius_km': [2440, 6052, 6371, 3390, 69911, 58232,
                     25362, 24622],
        'moons': [0, 0, 1, 2, 80, 83, 27, 14],
        'type': ['terrestrial', 'terrestrial', 'terrestrial', 'terrestrial',
                 'gas giant', 'gas giant', 'ice giant', 'ice giant'],
        'rings': ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes','yes'],
        'mean_temp_c': [167, 464, 15, -65, -110, -140, -195, -200],
        'magnetic_field': ['yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes']
        }

# Use pd.DataFrame() function to convert dictionary to dataframe.
planets = pd.DataFrame(data)

print(planets.groupby(['type']).sum(numeric_only=True))

# Group by type and magnetic_field and get the mean of the values
# in the numeric columns for each group.
planets.groupby(['type', 'magnetic_field']).mean()

# Group by type, then use the agg() function to get the mean and median
# of the values in the numeric columns for each group.
planets.groupby(['type']).agg(['mean', 'median'])

# Group by type and magnetic_field, then use the agg() function to get the
# mean and max of the values in the numeric columns for each group.
planets.groupby(['type', 'magnetic_field']).agg(['mean', 'max'])

# Define a function that returns the 90 percentile of an array.
def percentile_90(x):
    return x.quantile(0.9)

# Group by type and magnetic_field, then use the agg() function to apply the
# mean and the custom-defined `percentile_90()` function to the numeric
# columns for each group.
planets.groupby(['type', 'magnetic_field']).agg(['mean', percentile_90])
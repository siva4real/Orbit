from astropy.time import Time
import astropy.units as u
from astropy.coordinates import get_body, SkyCoord
import pandas as pd
from datetime import datetime, timedelta
import numpy as np


'''
Using astropy to get the positions of the Sun and Mars over a 10 year period as observed from Earth.
The positions are calculated for each hour over the 10 year period.
The results are saved to an Excel file.
'''

end_date = datetime.now()
start_date = end_date - timedelta(days=365.25 * 10)
dates = pd.date_range(start=start_date, end=end_date, freq='1h')

times = []
sun_ra = []
sun_dec = []
mars_ra = []
mars_dec = []

for date in dates :

    t = Time(date)
    
    sun = get_body('sun', t)
    sun_ra.append(sun.ra.hour) 
    sun_dec.append(sun.dec.deg) 
    
    mars = get_body('mars', t)
    mars_ra.append(mars.ra.hour) 
    mars_dec.append(mars.dec.deg) 
    
    times.append(date.strftime('%Y-%m-%d %H:%M:%S'))

df = pd.DataFrame({
    'Date': times,
    'Sun_RA_Hours': sun_ra,
    'Sun_Dec_Degrees': sun_dec,
    'Mars_RA_Hours': mars_ra,
    'Mars_Dec_Degrees': mars_dec
})

# Round numerical values to 8 decimal places
df = df.round({
    'Sun_RA_Hours': 8,
    'Sun_Dec_Degrees': 8,
    'Mars_RA_Hours': 8,
    'Mars_Dec_Degrees': 8
})

# Save to Excel file
output_filename = 'data/planetary_positions_raw.xlsx'
df.to_excel(output_filename, index=False)

print(f"Data has been saved to {output_filename}")
print(f"Number of entries: {len(df)}")
print("\nFirst few entries:")
print(df.head())
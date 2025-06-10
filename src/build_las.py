import lasio

from utils.read_data import read_data
from utils.units import units

data = read_data('data/WA1.txt')

# Check data format: float64
data.info()

# Create empty LAS file
las_file = lasio.LASFile()

# Setup metadata
well_name = 'WA1'
field_name = 'Test Field'
uwi = '123456789'
country = 'Test Country'

# Add metadata
las_file.well['WELL'] = lasio.HeaderItem('WELL', value=well_name)
las_file.well['FLD'] = lasio.HeaderItem('FLD', value=field_name)
las_file.well['UWI'] = lasio.HeaderItem('UWI', value=uwi)
las_file.well['CTRY'] = lasio.HeaderItem('CTRY', value=country)

# Check header
las_file.header

# Add depth curve
las_file.append_curve('DEPT', data['M__DEPTH'], unit='m')

# Loop through data adding curve and units to las file
for col, unit in zip(data.columns, units):
    if col != 'M__DEPTH':
        las_file.append_curve(col, data[col], unit=unit)

# Check curves added
las_file.curves

# Write LAS file ready for welly
las_file.write('notebooks/WA1_null.las')

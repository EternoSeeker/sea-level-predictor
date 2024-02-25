import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
import streamlit as st

# Year,CSIRO Adjusted Sea Level,Lower Error Bound,Upper Error Bound,NOAA Adjusted Sea Level
st.title('Sea Level Predictor')
st.write('This is a simple web app to predict the sea level rise in the future')

range = st.slider('Select a range of years', 1880, 2050, (1880, 2050))
st.write('You selected:', range)

df = pd.read_csv('epa-sea-level.csv')

if st.checkbox('Show Data'):
    st.write(df)

min_year = df['Year'].min()
max_year = df['Year'].max()
    
# starting year from min year in dataset
st.scatter_chart(df, x='Year', y='CSIRO Adjusted Sea Level', color='#00ffff')
fig = plt.figure()
plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'], s=8)


# Create first line of best fit
res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
# limit the x axis to a range
plt.xlim(range[0], range[1] + 10)
x1 = np.arange(range[0],range[1],1)
y1 = res1.intercept + res1.slope*x1
plt.plot(x1,y1,color='firebrick')

# Create second line of best fit
df2 = df[df['Year']>=2000]
res2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
x2 = np.arange(df2['Year'].min(),range[1],1)
y2 = res2.intercept + res2.slope*x2
plt.plot(x2,y2,color='mediumseagreen')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
# writing to the streamlit
st.pyplot(plt)

# Save plot 
# plt.savefig('sea_level_plot.png')

#return plt.gca()
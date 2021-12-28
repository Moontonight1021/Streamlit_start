#!python3

import streamlit as st
import pandas as pd

st.write("Here's out first attempt at using data to create a table:")

st.write(pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
}))

import numpy as np

#random data table
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)


#Plot a chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(chart_data)

#Plot a map
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, -122.4],
    columns=['lat','lon']
)

st.map(map_data)

# widget

x = st.slider('x')
st.write(x, 'squared is', x*x)

#!python3

import streamlit as st
import pandas as pd

st.write("Here's out first attempt at using data to create a table:")

st.write(pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
}))

import numpy as np

dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(chart_data)
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.header("Simulation Monte Carlo")

# Example: Estimation of π
points = 1000
x = np.random.rand(points)
y = np.random.rand(points)
inside = x**2 + y**2 <= 1

fig, ax = plt.subplots()
ax.scatter(x[inside], y[inside], color="blue", label="Inside")
ax.scatter(x[~inside], y[~inside], color="red", label="Outside")
ax.legend()
st.pyplot(fig)
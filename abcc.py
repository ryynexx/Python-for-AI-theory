# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Set the title of the dashboard
# st.title("Simple Data Dashboard")

# # Sidebar for user input
# st.sidebar.header("User Input")

# # Slider for selecting number of data points
# num_points = st.sidebar.slider("Number of Data Points", 1, 100, 50)

# # Generate random data
# data = pd.DataFrame({
#     'X': np.arange(num_points),
#     'Y': np.random.randn(num_points).cumsum()
# })

# # Display the data in a table
# st.subheader("Data Table")
# st.dataframe(data)

# # Create a line chart
# st.subheader("Line Chart")
# st.line_chart(data.set_index('X'))

# # Create a bar chart
# st.subheader("Bar Chart")
# fig, ax = plt.subplots()
# ax.bar(data['X'], data['Y'])
# st.pyplot(fig)

# # Add a footer
# st.write("This is a simple dashboard created using Streamlit.")



import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the dashboard
st.title("Enhanced Data Dashboard")

# Sidebar for user input
st.sidebar.header("User Input")

# User inputs for data generation
num_points = st.sidebar.slider("Number of Data Points", 1, 100, 50)
mean = st.sidebar.number_input("Mean", value=0.0)
std_dev = st.sidebar.number_input("Standard Deviation", value=1.0)

# Generate random data based on user input
data = pd.DataFrame({
    'X': np.arange(num_points),
    'Y': np.random.normal(loc=mean, scale=std_dev, size=num_points).cumsum()
})

# Display the data in a table
st.subheader("Data Table")
st.dataframe(data)

# Create a line chart
st.subheader("Line Chart")
st.line_chart(data.set_index('X'))

# Create a bar chart
st.subheader("Bar Chart")
fig_bar, ax_bar = plt.subplots()
ax_bar.bar(data['X'], data['Y'], color='skyblue')
ax_bar.set_title('Bar Chart of Y Values')
ax_bar.set_xlabel('X Values')
ax_bar.set_ylabel('Y Values')
st.pyplot(fig_bar)

# Create a scatter plot
st.subheader("Scatter Plot")
fig_scatter, ax_scatter = plt.subplots()
ax_scatter.scatter(data['X'], data['Y'], color='orange')
ax_scatter.set_title('Scatter Plot of Y Values')
ax_scatter.set_xlabel('X Values')
ax_scatter.set_ylabel('Y Values')
st.pyplot(fig_scatter)

# Create a histogram
st.subheader("Histogram")
fig_hist, ax_hist = plt.subplots()
ax_hist.hist(data['Y'], bins=10, color='purple', alpha=0.7)
ax_hist.set_title('Histogram of Y Values')
ax_hist.set_xlabel('Y Values')
ax_hist.set_ylabel('Frequency')
st.pyplot(fig_hist)

# Option to download the data as CSV
csv = data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Data as CSV",
    data=csv,
    file_name='generated_data.csv',
    mime='text/csv'
)

# Add a footer with additional information
st.write("This is an enhanced dashboard created using Streamlit.")
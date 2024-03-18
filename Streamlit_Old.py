"""
Created on Wed Mar 13 19:46:18 2024
@author: Singh AmanDeep Saini
"""

# =============================================================================
# Import Data
# =============================================================================

import streamlit as st
import pandas as pd

# Title for the Streamlit app
st.title('Data Story about Top Data Breaches')

# Explain what the data controversy about data breach
st.markdown("""
Data security and privacy are of huge concern.
Any data breach may cause not only financial and reputational losses,
but it also poses a threat to the breakdown of trust flowing from unauthorized access to information.
These all too often highlight not only the technical issues at stake here but also the aspect linked to ethical problems:
breaches infringe on the right to private life of the individual, mostly in the case of sensitive data.
""")

# Further explain what the data controversy about data breach
st.markdown("""
There are also questions about the ethical responsibility and accountability of organizations that have
been trusted with such confidential data. I will address such questions through an analysis of
"List of Top Data Breaches (2004 - 2021)" dataset from Kaggle.
""")

# Adding a link
st.markdown("""
For more details on the dataset, visit the [Kaggle Dataset](https://www.kaggle.com/datasets/hishaamarmghan/list-of-top-data-breaches-2004-2021).
""")

# Load the dataset
data_breaches = pd.read_csv('data_breaches.csv')

# Show the data
st.write("Here is a preview of the data breach dataset:")
st.write(data_breaches.head())

# Explain what the data is about
st.markdown("""
This dataset represents a list of data breaches from 2004 to 2021,
including the entities affected, the year of the breach, the number of records compromised,
the type of organization, and the method of the breach.
This analysis aims to provide insights into the scale and nature of data breaches over this period.
I will proceed with the data cleaning steps next...
""")

# Adding text to the sidebar

st.sidebar.title("About Me")
st.sidebar.info("""
I am a reliable, hardworking, and ambitious student who strives for perfectionism.
I am naturally elected to maintain a high standard of morality and professionalism.
I have an internal drive to be well-organized and consistent. My inquisitive nature
helps me to evaluate the situation without being emotionally affected. I am the ideal
candidate for work that necessitates precision and strong analytical capabilities.
""")
# =============================================================================



# =============================================================================
# Tidy Data
# =============================================================================

# Check for missing values in the dataset
missing_values = data_breaches.isnull().sum()

# Check data types of the columns
data_types = data_breaches.dtypes

# I will also check for any duplicate entries
duplicate_entries = data_breaches.duplicated().sum()

# I can also provide a summary of the 'Records' column to understand its distribution
records_summary = data_breaches['Records'].describe()

# Title with CSS for centering
st.markdown("<h1 style='text-align: center;'>Data Cleaning & Preperation</h1>",
            unsafe_allow_html=True)

# Data cleaning
with st.expander("Preliminary Data Cleaning"):

    # Expain what the data cleaning step shows
    st.markdown("""
The preliminary data cleaning process has revealed the following:
""")

    # Use columns to layout the elements side by side
    col1, col2, col3 = st.columns(3)

    # In the first column, display missing values
    with col1:
        st.write("Missing Values")
        missing_values = data_breaches.isnull().sum()
        st.write(missing_values)

    # In the second column, display data types
    with col2:
        st.write("Data Types")
        data_types = data_breaches.dtypes
        st.write(data_types)

    # In the third column, display summary of 'Records' column
    with col3:
        st.write("Records Summary")
        records_summary = data_breaches['Records'].describe()
        st.write(records_summary)

    # Explain key insights in bullet points
    st.markdown("""
1. There are no missing values in any of the columns, which means no null data handling is needed.
2. The Year column is listed as an object type, but it should be an integer for analysis purposes.
3. There are no duplicate entries, ensuring that each row represents a unique data breach.
4. The Records column is of numeric type (int64), and the summary shows a wide variation in the number of records affected by breaches, indicated by a large standard deviation.
""")

# Further data cleaning
with st.expander("Data Cleaning"):

    # Use columns to layout the elements side by side
    col1, col2 = st.columns(2)

    # Convert Year to integer
    data_breaches['Year'] = pd.to_numeric(data_breaches['Year'],
                                          errors='coerce')

    # In the first column, Check for and handle any inconsistencies in 'Method' column
    with col1:
        method_counts = data_breaches['Method'].value_counts()
        st.write("Count of Different Breach Methods")
        st.write(method_counts)

    # In the second column, Verify the changes made
    with col2:
        st.write("Data Types After Conversion")
        st.write(data_breaches.dtypes)

    # Expain what the data preperation step shows
    st.markdown("""
I have now converted the Year column to an integer for better analysis and standardize the
Method column entries if there's any inconsistency.
""")

# =============================================================================



# =============================================================================
# Transform Data
# =============================================================================

# Convert Year to integer rather than a float! (Just to ensure it is completed!)
data_breaches['Year'] = pd.to_numeric(data_breaches['Year'],
                                      errors='coerce')

# Clean and standardize the 'Method' column, if there are variations that essentially mean the same thing.
# Here I assume 'hacked' and 'HACKED' are the same and should be standardized.
data_breaches['Method'] = data_breaches['Method'].str.lower()

# Remove any rows with NA values (especially important after type conversion if there were invalid years)
data_breaches.dropna(subset=['Year'], inplace=True)

# Convert 'Year' to integer after dropping NA values
data_breaches['Year'] = data_breaches['Year'].astype(int)

# Check if any records need to be aggregated or if each row is indeed a unique breach event
# For simplicity, I assume each row is a unique event and does not require aggregation

# Further data cleaning
with st.expander("Data Preparation"):

    # First row
    col1, col3 = st.columns([1, 2])

    with col1:
        st.write("Cleaned Data Types")
        st.write(data_breaches.dtypes)

    with col3:
        st.write("Random 5 Rows of the Cleaned Data")
        st.dataframe(data_breaches.sample(5))

    # Second row
    col2 = st.columns(1)
    with col2[0]:
        st.write("Method Column Unique Values After Standardization")
        st.write(data_breaches['Method'].unique())

    # Expain my upcoming steps
    st.markdown("""
Next, I'll work on the code for creating the visualizations.
""")
# =============================================================================



# =============================================================================
# Further Transform Data After Visualization
# =============================================================================

# Function to capitalize each word in a string
def capitalize_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

# Apply the function to the 'Organization type' and 'Method' columns
data_breaches['Organization type'] = data_breaches['Organization type'].\
apply(lambda x: capitalize_each_word(str(x)))
data_breaches['Method'] = data_breaches['Method'].\
apply(lambda x: capitalize_each_word(str(x)))

# Now the organization types and methods will have each word capitalized
# Proceed with creating the sidebar filters as previously described

# Further data cleaning
with st.expander("Data Preparation After Visualization"):

    # Clarify my actions
    st.write("The Organization type and Methods will have now each word capitalized")
    st.dataframe(data_breaches.sample(10))
    st.markdown("""
After developing some initial graphs and integrating filter options into the Streamlit application,
I took a step back to review the interactivity and presentation of the data.
It was then I realized that the consistency in the formatting of the 'Organization type' and 'Method'
fields could significantly improve the user experience. While the initial visualizations provided valuable insights,
I noticed that the inconsistent capitalization could potentially lead to confusion or misinterpretation.
To address this, I decided to implement a cleaning step that ensures every first letter of the word is capitalized
and the rest are lowercased for each word in these fields. This not only enhances the aesthetic appeal of the
filters and graphs but also promotes clarity and professionalism in the data story I am aiming to tell.
""")
# =============================================================================



# =============================================================================
# Visualize Data
# =============================================================================

# Import visualization libraries
import plotly.express as px

# Title with CSS for centering
st.markdown("<h1 style='text-align: center;'>Data Visualization</h1>",
            unsafe_allow_html=True)

# Prepare the data for plotting
annual_records = data_breaches.groupby('Year')['Records'].sum().reset_index()
annual_records['Records'] = annual_records['Records'].astype(float) / 1e6  # Convert to millions
annual_records = annual_records.sort_values('Year')  # Sort years in ascending order

# Sidebar for filters
st.sidebar.header('Filter Options')

# Filter for years
years = sorted(annual_records['Year'].unique())
all_years_option = "All Years"
selected_years = st.sidebar.multiselect(
    'Select years:',
    options=[all_years_option] + years,
    default=[all_years_option]
)
if all_years_option in selected_years:
    selected_years = years

# Filter for organization types, sorted alphabetically
organization_types = sorted(data_breaches['Organization type'].unique())
all_org_types_option = "All Organization Types"
selected_org_types = st.sidebar.multiselect(
    'Select organization types:',
    options=[all_org_types_option] + organization_types,
    default=[all_org_types_option]
)
if all_org_types_option in selected_org_types:
    selected_org_types = organization_types

# Filter for methods, sorted alphabetically
methods = sorted(data_breaches['Method'].unique())
all_methods_option = "All Methods"
selected_methods = st.sidebar.multiselect(
    'Select methods:',
    options=[all_methods_option] + methods,
    default=[all_methods_option]
)
if all_methods_option in selected_methods:
    selected_methods = methods

# Apply all filters to the data
filtered_data = data_breaches[
    data_breaches['Year'].isin(selected_years) &
    data_breaches['Organization type'].isin(selected_org_types) &
    data_breaches['Method'].isin(selected_methods)
]
filtered_annual_records = filtered_data.groupby('Year')['Records'].\
    sum().reset_index()
filtered_annual_records['Records'] /= 1e6  # Convert to millions for the graph

# Create an interactive area plot using Plotly
fig = px.area(filtered_annual_records, x="Year", y="Records",
              title="Annual Overview: of Company Users Affected by Data Breaches",
              labels={"Records": "Company Users Affected (millions)"})

# Customize the layout of the Plotly graph
fig.update_traces(line=dict(color='#ff4b4b'),
                  fill='tozeroy', # Set line color to red and fill to zero
                  mode='lines+markers',
                  marker=dict(color='white', size=5))
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Company Users Affected (millions)",
    yaxis_type="log",  # Logarithmic scale
    xaxis=dict(tickmode='linear'),
    template="plotly_white"
)

# Display the Plotly graph in the Streamlit app
st.plotly_chart(fig)

# Expain my graph
st.markdown("""
The chart tells a long story of two huge peaks in 2013 with 3,469 million affected and the record year of 2019,
with 3,824 million users. These two years, therefore, definitely urge a much closer look, and a look that involves
more than just the company and its users:
1. Who were the company users affected and through what means did their data
get breached?

I will dive into these details to look at what those companies were and which methods led to their breaches, causing this huge user data exposure.
""")

# Graph 2

# We need to make sure the 'Records' column is in a suitable format for visualization
# For consistency with the provided image, we will use millions as the unit
filtered_data['Records (millions)'] = filtered_data['Records'] / 1e6

# Group data by Entity and Year and calculate the sum of records affected for each group
grouped_data = filtered_data.groupby(['Entity', 'Year'])['Records (millions)']\
    .sum().reset_index()

# Shorten the 'Entity' names to the first three words for the x-axis labels
grouped_data['Entity_short'] = grouped_data['Entity'].apply(lambda x: ' '.join(x.split()[:3]))

# Filter the data to include only the selected years
filtered_by_year = grouped_data[grouped_data['Year'].isin(selected_years)]

# Now we find the top 5 breaches for each selected year
top5_per_year = filtered_by_year.groupby('Year').apply(lambda x: x.nlargest(5, 'Records (millions)')).reset_index(drop=True)

# Create a bar chart with Plotly using the filtered top 5 data
fig_top5 = px.scatter(top5_per_year,
                      x='Year',
                      y='Records (millions)',
                      color='Entity_short',
                      size='Records (millions)',  # Size of points can represent the amount of records breached
                      title="Comparative Analysis: of Company User Breached by Entity and Selected Years",
                      labels={"Records (millions)": "Total Company Users Breached (millions)"},
                      hover_name='Entity',  # Show full entity name on hover
                      category_orders={"Year": selected_years})  # Ensure that only the selected years are shown

# Customizations for improved readability and aesthetics
fig_top5.update_layout(
xaxis_title="Year",
yaxis_title="Company Users Affected (millions)",
# legend_title="Company Entity",
xaxis={'categoryorder':'total descending'},
yaxis=dict(type='log'),  # Use a logarithmic scale due to the large range of values
margin=dict(l=0, r=0, t=100, b=150),  # Adjust margins to prevent cutting off labels
showlegend=False  # Hide the legend
)

# Display the Plotly graph in the Streamlit app
st.plotly_chart(fig_top5)

# Expain my graph
st.markdown("""
The graph of Comparative Analysis explains the Yahoo 2013 breach,
hence the reason why it reached such a huge number of over 300 billion users.
While 2019 brought multiple breaches at companies ranging from Facebook to Microsoft,
the biggest in terms of its likely ultimate cost was Yahoo. All these illustrate a
very different picture of the threat landscape, where the depth of breaches is
not measured in terms of the number of users but rather in the frequency and variety.

To fully understand a cybersecurity failure, should we focus on analyzing the methods
that enabled the root cause, since they likely created vulnerabilities that led to
widespread security breaches?
""")

# Shorten the 'Entity' names to the first three words for the x-axis labels
filtered_data['Entity_short'] = filtered_data['Entity'].apply(lambda x: ' '.join(x.split()[:3]))

# Filter the data to include only the selected years
filtered_by_year = filtered_data[filtered_data['Year'].isin(selected_years)]

# Now we find the top 5 breaches for each selected year
top5_method_per_year = filtered_by_year.groupby('Year').apply(lambda x: x.nlargest(3, 'Records (millions)')).reset_index(drop=True)

# Sort the top5_method_per_year DataFrame alphabetically by 'Entity_short'
top5_method_per_year.sort_values(by='Entity_short', inplace=True)

# Now, let's create the stacked bar chart with the sorted data
fig_method_entity_bar = px.bar(
    top5_method_per_year,
    x='Entity_short',  # Use 'Entity_short' for the x-axis
    y='Records (millions)',
    color='Method',  # Use 'Method' to color the bars
    title="Comparative Analysis: of Company User Breached by Method and Entity",
    labels={"Records (millions)": "Total Records Breached (millions)", "Entity_short": "Entity"},
    barmode='stack',  # Bars will be stacked on top of each other
    hover_name='Entity',  # Show full entity name on hover
)

# Customizing the layout
fig_method_entity_bar.update_layout(
    xaxis_title="Entity",
    yaxis_title="Total Records Breached (millions)",
    legend_title="Method",
    xaxis={'categoryorder': 'array', 'categoryarray': sorted(top5_method_per_year['Entity_short'].unique())},
    yaxis=dict(type='linear')  # Use linear scale for clarity with stacked bars
)

# Display the Plotly graph in the Streamlit app
st.plotly_chart(fig_method_entity_bar)

# Expain my graph
st.markdown("""
The 'Comparative Analysis' graph presents a detailed breakdown of data breaches by method.
It had a hacking incident from Yahoo in 2013, which ranks as the highest breach ever,
pointing towards a critical vulnerability even in the biggest technology companies.
2019 was one of the years when such a mixed bag—from accidentally public data exposure to
notably poor security and misconfigurations around the board—came to light.
Indeed, from this multi-faceted picture, a clear emphasis emerges on just
how greatly complicated the cybersecurity threats of the contemporary world have become.
""")


# =============================================================================
# Ethical Aspects
# =============================================================================

# Title with CSS for centering
st.markdown("<h1 style='text-align: center;'>Conclusion</h1>",
            unsafe_allow_html=True)

# My opinion and conclusion
st.markdown("""
Looking at big data breaches from the past years,
like the ones at Yahoo in 2013 and others at Facebook and Microsoft in 2019,
we see how big of a deal data security is. It's not just about numbers or stats;
it's about real people who have had their private information exposed.

The main point here is that companies that have our data need to take really good care of it.
They have to be responsible because when they mess up, it's not just a technical problem;
it's a matter of breaking trust with their users. The reasons for these breaches are varied – sometimes
it's because of weak security, and other times it's because of mistakes,
like accidentally sharing data that should've been kept private.
This shows that even big, well-known companies can struggle to keep our data safe.

So, the big takeaway from all this is that companies need to step up their game in
how they handle our personal information. They need to do a better job with their security and
also really think about how important it is to protect people's privacy. It's about doing the right
thing and making sure they're taking care of the trust that people put in them.
In today's world, where data leaks seem to happen all the time, this is a really important
reminder of why companies need to be super careful with our data.
""")
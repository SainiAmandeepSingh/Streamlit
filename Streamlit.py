"""
Date: 17/03/2024
@author: Singh AmanDeep Saini
"""

# =============================================================================
# Import & Load Data
# =============================================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# Title for the Streamlit app with CSS for centering
st.markdown("<h1 style='text-align: center;'>Data Breaches: A Data Story of Trust</h1>",
            unsafe_allow_html=True)

# Explain the data controversy about data breach
st.markdown("""
Data security and privacy are of huge concern.
Any data breach may cause not only financial and reputational losses,
but it also poses a threat to the breakdown of trust flowing from unauthorized access to information.
These all too often highlight not only the technical issues at stake here but also the aspect linked to ethical problems:
**breaches infringe on the right to the private life of the individual, mostly in the case of sensitive data.**

There are also questions about the ethical responsibility and accountability of organizations that have
been trusted with such confidential data. I will address such questions through an analysis of the
"***List of Top Data Breaches (2004 - 2021)***" dataset from Kaggle.
""")

# Data source of data breach
st.info("""
***For more details on the dataset,
visit the [Kaggle Dataset](https://www.kaggle.com/datasets/hishaamarmghan/list-of-top-data-breaches-2004-2021).***
""")

# Load the dataset
data_breaches = pd.read_csv('data_breaches.csv')

# Style the DataFrame Table with highlight rows
def highlight_rows(s):
    # Apply the red background to even rows
    return ['background-color: #FF4B4B'
            if row % 2 == 0
            else '' for row in range(len(s))]

# Apply the styling
data_breaches_style = data_breaches.head().style.apply(highlight_rows, axis=0)

# Display the styled DataFrame
st.markdown("<h5 style='text-align: center;'>Here is a preview of the data breach dataset</h5>",
            unsafe_allow_html=True)
st.dataframe(data_breaches_style)

# Explain the data controversy about data breach
st.markdown("""
In this data story, I will look at the data breach incidents not just as numbers
but as ethical dilemmas that impact real lives. I will analyze with my dataset the
broken societal trust, company responsibility, and the moral implications of
managing confidential user data.
""")
# =============================================================================



# =============================================================================
# Clean Data
# =============================================================================

# I will check for missing values in the dataset
missing_values = data_breaches.isnull().sum()

# I will check data types of the columns
data_types = data_breaches.dtypes

# I will also check for any duplicate entries
duplicate_entries = data_breaches.duplicated().sum()

# I can also provide a summary of the 'Records' column to understand its distribution
records_summary = data_breaches['Records'].describe()

# Data Cleaning & Preperation title with CSS for centering
st.markdown("<h2 style='text-align: center;'>Data Cleaning & Preperation</h2>",
            unsafe_allow_html=True)

# I will check data types of the columns
data_types = data_breaches.dtypes.apply(str)  # Convert data types to string before displaying

# Data cleaning
with st.expander("Data Cleaning"):

    # Expain what the data cleaning step shows
    st.markdown("<h6 style='text-align: center;'>The data cleaning process has revealed the following:</h6>",
                unsafe_allow_html=True)

    # Use columns to layout the elements side by side (3 columns)
    col1, col2, col3 = st.columns(3)

    # In the first column, I will display missing values
    with col1:
        st.write("Missing Values")
        missing_values = data_breaches.isnull().sum()
        st.write(missing_values)

    # In the second column, I will display summary of 'Records' column
    with col2:
        st.write("Records Summary")
        records_summary = data_breaches['Records'].describe()
        st.write(records_summary)

    # In the third column, display the data types as strings in a DataFrame
    with col3:
        st.write("Data Types")
        # Convert dtypes to strings and make a DataFrame
        data_types_df = pd.DataFrame(data_breaches.dtypes.astype(str), columns=['Type'])
        st.dataframe(data_types_df)

    # Expain the key insights of data cleaninig step
    st.info("""
1. There are no missing values in any of the columns, meaning no null data processing is required.
2. The Year column is shown as an object type, but for analysis purposes it must be an integer.
3. There are no duplicate entries, so each row represents a unique data breach.
4. The Records column is of type numeric (int64) and the summary shows a large variation in the number of
records affected by violations, indicated by a large standard deviation.
""")
# =============================================================================



# =============================================================================
# Prepare Data
# =============================================================================

# I will convert Year to integer rather than a float! (Just to ensure it is completed!)
data_breaches['Year'] = pd.to_numeric(data_breaches['Year'], errors='coerce').dropna().astype(int)

# I will also clean and standardize the 'Method' column in other words I will find out
# all the variations that essentially mean the same thing. For example, I assume
# 'hacked' and 'HACKED' are the same and should be standardized.
data_breaches['Method'] = data_breaches['Method'].str.lower().str.capitalize()

# I will remove any rows with NA values
# This is quite important especially after type conversion if there were invalid years
data_breaches.dropna(subset=['Year'], inplace=True)

# I will convert again the 'Year' to integer after dropping NA values
data_breaches['Year'] = data_breaches['Year'].astype(int)

# I will create a function that will capitalize each word in a string
def capitalize_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

# Convert any unsupported dtypes to string
for col in data_breaches.columns:
    if data_breaches[col].dtype not in [int, float]:
        data_breaches[col] = data_breaches[col].astype(str)

# I will apply this function to the 'Organization type' and 'Method' columns
data_breaches['Organization type'] = data_breaches['Organization type'].\
apply(lambda x: capitalize_each_word(str(x)))
data_breaches['Method'] = data_breaches['Method'].\
apply(lambda x: capitalize_each_word(str(x)))

# Further data cleaning
with st.expander("Data Preparation"):

    # Expain what the data preperation step shows
    st.markdown("<h6 style='text-align: center;'>The data preperation process has revealed the following:</h6>",
                unsafe_allow_html=True)

    # Creating two columns with a ratio of 1:2
    col1, col2 = st.columns([1,2])

    # First column
    with col1:
        # I will write a title for the data types section
        st.write("Cleaned Data Types")
        # Create a DataFrame from the dtypes and convert dtypes to strings
        data_types_df = pd.DataFrame(data_breaches.dtypes.astype(str), columns=['Data Type'])
        # Display the DataFrame with data types as strings
        st.dataframe(data_types_df)

    # Second column
    with col2:
        # I will write a title for the Capitalized section
        st.write("Capitalized First Letter for Organization type and Methods")
        # I will select specific columns from the dataframe
        selected_columns = ['Organization type', 'Method']
        # I will display a sample of 5 rows for the selected columns
        st.dataframe(data_breaches[selected_columns].sample(5))

    # Expain the key insights of data preperation step & my upcoming steps
    st.info("""
1. I have converted the 'Year' column from an object type to an integer to enhance the analysis.
2. I have also improved dataset readability and visual presentation by capitalizing the
first letter of each word in the 'Organization Type' and 'Method' columns.

These, in brief, are the very initial basic steps aimed at the generation of an
insightful data visualization for comprehensive analysis.
""")
# =============================================================================



# =============================================================================
# Sidebar Filtered Data
# =============================================================================

# Data Visualization title with CSS for centering
st.markdown("<h2 style='text-align: center;'>Data Visualization</h2>",
            unsafe_allow_html=True)

# Convert 'Year' to integer
data_breaches['Year'] = pd.to_numeric(data_breaches['Year'], errors='coerce').dropna().astype(int)

# Clean and standardize the 'Method' column
data_breaches['Method'] = data_breaches['Method'].str.lower().str.capitalize()

# Remove rows with NA values, which is important especially after type conversion if there were invalid years
data_breaches = data_breaches.dropna(subset=['Year'])

# Ensure 'Records' column is numeric and convert it to millions
data_breaches['Records'] = pd.to_numeric(data_breaches['Records'], errors='coerce').dropna()
data_breaches['Records'] = data_breaches['Records'] / 1e6

# I will prepare the data for filtering and plotting
annual_data_breaches = data_breaches.groupby('Year')['Records'].sum().reset_index()
annual_data_breaches['Records'] = annual_data_breaches['Records'].astype(float) / 1e6  # Convert to millions
annual_data_breaches = annual_data_breaches.sort_values('Year')  # Sort years in ascending order

# Sidebar header for filter options
st.sidebar.header('Data Story Filter Options')

# I will filter for years
years = sorted(annual_data_breaches['Year'].unique())
all_years_filter_option = "All Years"

# I will multiselect widget for selecting years, with a default option for all years
selected_filter_years = st.sidebar.multiselect(
    'Select Years:',
    options=[all_years_filter_option] + years,
    default=[all_years_filter_option]
)

# If "All Years" is selected, i will include all years in the filter
if all_years_filter_option in selected_filter_years:
    selected_filter_years = years

# I will filter for organization types, sorted alphabetically
organization_types = sorted(data_breaches['Organization type'].unique())
all_org_types_filter_option = "All Organization Types"

# I will multiselect widget for selecting organization types, with a default option for all types
selected_filter_org_types = st.sidebar.multiselect(
    'Select Organization Types:',
    options=[all_org_types_filter_option] + organization_types,
    default=[all_org_types_filter_option]
)

# If "All Organization Types" is selected, I will include all types in the filter
if all_org_types_filter_option in selected_filter_org_types:
    selected_filter_org_types = organization_types

# I will filter for methods, sorted alphabetically
methods = sorted(data_breaches['Method'].unique())
all_methods_filter_option = "All Methods"

# I will multiselect widget for selecting breach methods, with a default option for all methods
selected_filter_methods = st.sidebar.multiselect(
    'Select Data Breach Methods:',
    options=[all_methods_filter_option] + methods,
    default=[all_methods_filter_option]
)

# If "All Methods" is selected, I will include all methods in the filter
if all_methods_filter_option in selected_filter_methods:
    selected_filter_methods = methods

# I will finally apply all selected filters to the data
filtered_data = data_breaches[
    data_breaches['Year'].isin(selected_filter_years) &
    data_breaches['Organization type'].isin(selected_filter_org_types) &
    data_breaches['Method'].isin(selected_filter_methods)
]

# Sidebar header for About Me
st.sidebar.header('About Me')

# I will define a column layout
col1, col2 = st.sidebar.columns([1.5, 2])

# I will add my image to the left column
with col1:
    st.image("Me.jpg", width=122)

# I will add the text to the right column
with col2:
    st.error("""
    I am a dedicated student at HU pursuing a minor in Big Data & Design
    """)

# Sidebar header for Contact Me
st.sidebar.header('Contact Me')

# I will display my social media links with icons
st.sidebar.success("""
You can connect with me on:

[![LinkedIn](https://img.icons8.com/color/20/000000/linkedin.png)](https://www.linkedin.com/your_profile) LinkedIn

[![WhatsApp](https://img.icons8.com/color/20/000000/whatsapp.png)](https://wa.link/9ge1o6) WhatsApp

[![Facebook](https://img.icons8.com/color/20/000000/facebook-new.png)](https://www.facebook.com/singh.amandeep.saini.2e) Facebook
""")
# =============================================================================



# =============================================================================
# Visualize Data Graph 1
# =============================================================================

# I will group the filtered data by 'Year' and summing up 'Records' column, then converting to millions
graph1 = filtered_data.groupby('Year')['Records'].sum().reset_index()
graph1['Records'] /= 1e6  # Convert to millions for the graph

# I will create an interactive area plot using Plotly
fig = px.area(graph1, x="Year", y="Records",
              title="Annual Overview: Users Affected by Data Breaches",
              labels={"Records": "Users Affected (in millions)"})

# I will customize the layout of the Plotly graph
fig.update_traces(
    line=dict(color='#ff4b4b'),  # Setting the line color to red
    fill='tozeroy',  # Filling the area below the line
    mode='lines+markers',  # Displaying lines with markers
    marker=dict(color='white', size=5)  # Customizing marker color and size
)

# I will customize the layout for improved readability and aesthetics
fig.update_layout(
    xaxis_title="Year",
    title_x=0.3,  # Centering the title
    yaxis_title="Users Affected",
    plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
    paper_bgcolor="rgba(0,0,0,0)",  # Transparent background
    font=dict(color="white"),  # Text color
    yaxis_type="log",  # Using a logarithmic scale for the y-axis
    xaxis=dict(tickmode='linear'),  # Setting x-axis tick mode to linear
    template="plotly_white",  # Using the white template for the plot
    yaxis=dict(
        type='log',  # Using a logarithmic scale for the y-axis due to a large range of values
        tickvals=[0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000],  # Setting tick values
        ticktext=['500K', '1M', '2M', '5M', '10M', '20M', '50M', '100M', '200M', '500M', '1B', '2B', '5B'],  # Setting tick labels
    )
)

# I will display the Plotly graph in the Streamlit app
st.plotly_chart(fig)

# Expain my graph
st.markdown("""
The chart tells a long story of two huge peaks in 2013 with 3,469 million affected and the record year of 2019,
with 3,824 million users. These two years, therefore, definitely urge a much closer look, and a look that involves
more than just the company and its users:
""")

st.warning("""
***1. Who were the users affected and through what means did their data
get breached?***
""")

st.markdown("""
I will take a deep dive to see what those companies were and what methods made them
have big breaches in their systems that led to such huge exposure of user data.
""")
# =============================================================================



# =============================================================================
# Visualize Data Graph 2
# =============================================================================

# For consistency reasons I will use millions as the unit
filtered_data['Records (millions)'] = filtered_data['Records'] / 1e6

# I will group data by Entity and Year and then calculate the sum of records affected for each group
graph2_data = filtered_data.groupby(['Entity', 'Year'])['Records (millions)']\
    .sum().reset_index()

# I will shorten the 'Entity' names to the first three words for the x-axis labels for readability.
graph2_data['Entity_short'] = graph2_data['Entity'].apply(lambda x: ' '.join(x.split()[:3]))

# I will filter the data to include only the selected years based on my filter
graph2_data = graph2_data[graph2_data['Year'].isin(selected_filter_years)]

# I will now find the top 5 breaches for each selected year
graph2 = graph2_data.groupby('Year').apply(lambda x: x.nlargest(5, 'Records (millions)')).reset_index(drop=True)

# I will also calculate the sizes for the plot, with a cap for extremely large values such as (Yahoo)
max_size = 1000  # I will set a maximum size cap for extremely large breaches
scaled_sizes = graph2['Records (millions)'].apply(lambda x: min(x, max_size))

# I will create a scatter plot with Plotly using the filtered top 5 data
fig2 = px.scatter(
    graph2,
    x='Year',
    y='Records (millions)',
    color='Entity_short',
    size=scaled_sizes,  # Use scaled sizes with a cap
    title="Comparative Analysis: Users Affected by Data Breaches by Entity and Selected Years",
    labels={"Records (millions)": "Users Affected (in millions)",
            "Entity_short" : "Entity" ,
            "size" : "Size"},
    hover_name='Entity',  # Show full entity name on hover
    category_orders={"Year": selected_filter_years}  # Ensure that only the selected years are shown
)


# I will customize the layout for improved readability and aesthetics
fig2.update_layout(
    xaxis_title="Year",
    yaxis_title="Users Affected",
    title_x=0.1, # Center the title
    plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
    paper_bgcolor="rgba(0,0,0,0)",  # Transparent background
    font=dict(color="white"),  # Text color
    yaxis=dict(
        type='log',  # Use a logarithmic scale due to the large range of values
        tickvals=[0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000],
        ticktext=['500K', '1M', '2M', '5M', '10M', '20M', '50M', '100M', '200M', '500M', '1B', '2B', '5B'],
    ),
    legend_title="Entity",
    showlegend=True  # In case I wanted to hide the legend
)

# I will display the Plotly graph in the Streamlit app
st.plotly_chart(fig2)

# Expain my graph
st.markdown("""
The graph of Comparative Analysis explains the Yahoo 2013 breach,
hence the reason why it reached such a huge number of over 3 billion users.
While 2019 brought multiple breaches at companies ranging from Facebook to Microsoft,
the biggest in terms of its likely ultimate cost was Yahoo. All these illustrate a
very different picture of the threat landscape, where the depth of breaches is
not measured in terms of the number of users but rather in the frequency and variety.
""")

st.warning("""
***To fully understand a cybersecurity failure, should we focus on analyzing the methods
that enabled the root cause, since they likely created vulnerabilities that led to
widespread security breaches?***
""")
# =============================================================================



# =============================================================================
# Visualize Data Graph 3
# =============================================================================

# I will shorten the 'Entity' names to the first three words for the x-axis labels
filtered_data['Entity_short'] = filtered_data['Entity'].apply(lambda x: ' '.join(x.split()[:3]))

# I will filter the data to include only the selected years
graph3_data = filtered_data[filtered_data['Year'].isin(selected_filter_years)]

# I will now find the top 3 breaches for each selected year
graph3 = graph3_data.groupby('Year').apply(lambda x: x.nlargest(3, 'Records (millions)')).reset_index(drop=True)

# I will sort the graph3 DataFrame alphabetically by 'Entity_short'
graph3.sort_values(by='Entity_short', inplace=True)

# I will now create the stacked bar chart with the sorted graph3 DataFrame
fig3 = px.bar(
    graph3,
    x='Entity_short',  # Use 'Entity_short' for the x-axis
    y='Records (millions)',
    color='Method',  # Use 'Method' to color the bars
    title="Comparative Analysis: User Breached by Method and Entity",
    labels={"Records (millions)": "Users Affected (in millions)",
            "Entity_short": "Entity",
            "Method": "Data Breach Method"},
    barmode='stack',  # Bars will be stacked on top of each other
    hover_name='Entity',  # Show full entity name on hover
)

# I will customize the layout for a logarithmic scale with custom tick values for readability and scalability reasons
fig3.update_layout(
    xaxis_title="Entity",
    title_x=0.2, # Center the title
    yaxis_title="Users Affected",
    plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
    paper_bgcolor="rgba(0,0,0,0)",  # Transparent background
    font=dict(color="white"),  # Text color
    yaxis=dict(
        type='log',  # Use a logarithmic scale due to the large range of values
        tickvals=[0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000],
        ticktext=['500K', '1M', '2M', '5M', '10M', '20M', '50M', '100M', '200M', '500M', '1B', '2B', '5B']
    ),
    legend_title="Data Breach Method",
    xaxis={'categoryorder': 'array', 'categoryarray': sorted(graph3['Entity_short'].unique())}
)

# I will display the Plotly graph in the Streamlit app
st.plotly_chart(fig3)

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



# =============================================================================
# Data Perspective
# =============================================================================

# Personal Opinion title with CSS for centering
st.markdown("<h2 style='text-align: center;'>Data Perspectives</h2>",
            unsafe_allow_html=True)

# Personal View
st.markdown("""
I have thought a lot about data breaches at big companies like Yahoo, Facebook, and Microsoft.
The things that really get into me are not just the great sum of leaked data,
but how many has been lost in trust and the ethics that are linked to it.
"""
)

st.success("""
**Philosophical**:
***These data breaches was more than an email and phone number;
this was about people and the invasion of their personal world - life without their consent.***

**Ethically**:
Ethically speaking, I believe one has to rise beyond the social norms and legal
expectations with which these companies have failed to rise above.
***It's not just breaking rules; it's failing to protect basic rights to which people
should be entitled.***

**Economically**:
The data is valuable—maybe even tempting to exploit for personal profit.
***But at what cost? To me, there is an ethically sound way through which
data should be handled. It does not involve compromising privacy for financial gain.***

**Technologically**:
We are more connected than ever, and it is beautiful, but that comes with responsibility.
The technology that unites us should not be the one that brings risks upon us.
""")
# =============================================================================



# =============================================================================
# Conclusion
# =============================================================================

# Conclusion title with CSS for centering
st.markdown("<h2 style='text-align: center;'>Conclusion</h2>",
            unsafe_allow_html=True)

# Conclusion
st.info("""
In fact, looking at the big data breaches of the past years, for example,
those at Yahoo in 2013 and others at Facebook and Microsoft in 2019, one really
sees how big a deal data security really is. ***These are not numbers or statistics;
these are real individuals whose most private data has been exposed.***

The bottom line is that the companies with **our data really need good care.**
**They have to be responsible because, when they screw it up, that's not a technical glitch;
it's a betrayal of the user's trust.**

There could be many reasons: ***at times, security is weak,
and at other times, one shares, due to ignorance or by chance, what was meant to be kept secret.***
This shows that even reputable large companies find it difficult to keep our data safe.

***So, what is the most important conclusion from this data story?***

**Companies must raise the bar in how they treat our personal data.**
They really have to get their act together and reflect on what relevance it really
has to safeguard privacy. It is more about doing the right thing and making sure
they take care of the trust people place in them. ***In fact, today, it is almost a
daily occurrence that data breaches happen.***

This is a very good reminder to these companies to be super cautious with our data.

""")

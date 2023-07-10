import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime as dt
import plotly.express as px
import plotly
import pickle

# Data Exploring
def data_Capturing():
    #st.title("Customer Personality Analysis!")
    # Dataset
    st.subheader("Capturing Customer Information!")
    #st.write("These are the datasets.")
    data = pd.read_csv('C:/Users/ssude/sonyproject/sonyproject/MarketingCompaign.csv')
    st.write(data.head(5))
      

# Data Engineering
def data_Patterns():
    #st.write("Data Engineering page content goes here!")

    # Features
    st.subheader("Understanding Customer Data Patterns!")
    #st.write("Selected Features for the data Engineering as:")
    df = pd.read_csv('C:/Users/ssude/sonyproject/sonyproject/Inputdata.csv')
    st.write(df.head(5))

    #1. Age
    age = df.groupby("Age").agg({"Age": 'size', "TotalSpendings": ['sum', 'mean']})
    age.columns = ['TotalRecords', 'TotalAmount', 'AvgAmount']

    # Create a figure with three subplots
    fig1, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    # Plot histogram for TotalRecords
    axes[0].bar(age.index, age['TotalRecords'])
    axes[0].set_xlabel('Age Group')
    axes[0].set_ylabel('Total Records')
    axes[0].set_title('Total Records by Age Group')

    axes[1].bar(age.index, age['TotalRecords'])
    axes[1].set_xlabel('Age Group')
    axes[1].set_ylabel('Total Records')
    axes[1].set_title('Total Records by Age Group')

    axes[2].bar(age.index, age['TotalRecords'])
    axes[2].set_xlabel('Age Group')
    axes[2].set_ylabel('Total Records')
    axes[2].set_title('Total Records by Age Group')

    # Display the figure
    st.pyplot(fig1)

    # 2. Partners
    Partners = df.groupby("Partners").agg({"Partners": 'size', "TotalSpendings": ['sum', 'mean']})
    Partners.columns = ['TotalRecords', 'TotalAmount', 'AvgAmount']

    # Create a figure with three subplots
    fig2, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    # Plot histogram for TotalRecords
    axes[0].bar(Partners.index, Partners['TotalRecords'])
    axes[0].set_xlabel('Partners Group')
    axes[0].set_ylabel('Total Records')
    axes[0].set_title('Total Records by Partners Group')

    axes[1].bar(Partners.index, Partners['TotalRecords'])
    axes[1].set_xlabel('Partners Group')
    axes[1].set_ylabel('Total Records')
    axes[1].set_title('Total Records by Partners Group')

    axes[2].bar(Partners.index, Partners['TotalRecords'])
    axes[2].set_xlabel('Partners Group')
    axes[2].set_ylabel('Total Records')
    axes[2].set_title('Total Records by Partners Group')

    # Display the figure
    st.pyplot(fig2)

    # 3. Single
    Single = df.groupby("Single").agg({"Single": 'size', "TotalSpendings": ['sum', 'mean']})
    Single.columns = ['TotalRecords', 'TotalAmount', 'AvgAmount']

    # Create a figure with three subplots
    fig3, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    # Plot histogram for TotalRecords
    axes[0].bar(Single.index, Single['TotalRecords'])
    axes[0].set_xlabel('Single Group')
    axes[0].set_ylabel('Total Records')
    axes[0].set_title('Total Records by Singles Group')

    axes[1].bar(Single.index, Single['TotalRecords'])
    axes[1].set_xlabel('Single Group')
    axes[1].set_ylabel('Total Records')
    axes[1].set_title('Total Records by Singles Group')

    axes[2].bar(Single.index, Single['TotalRecords'])
    axes[2].set_xlabel('Single Group')
    axes[2].set_ylabel('Total Records')
    axes[2].set_title('Total Records by Singles Group')  

    # Display the figure
    st.pyplot(fig3)

    # 4. Children
    Children = df.groupby("Children").agg({"Children": 'size', "TotalSpendings": ['sum', 'mean']})
    Children.columns = ['TotalRecords', 'TotalAmount', 'AvgAmount']

    # Create a figure with three subplots
    fig4, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    # Plot histogram for TotalRecords
    axes[0].bar(Children.index, Children['TotalRecords'])
    axes[0].set_xlabel('Kids Group')
    axes[0].set_ylabel('Total Records')
    axes[0].set_title('Total Records by Kids Group')

    axes[1].bar(Children.index, Children['TotalRecords'])
    axes[1].set_xlabel('Kids Group')
    axes[1].set_ylabel('Total Records')
    axes[1].set_title('Total Records by Kids Group')

    axes[2].bar(Children.index, Children['TotalRecords'])
    axes[2].set_xlabel('Kids Group')
    axes[2].set_ylabel('Total Records')
    axes[2].set_title('Total Records by Kids Group')

    # Display the figure
    st.pyplot(fig4)

    # 5. Basic
    Basic = df.groupby("Basic").agg({"Basic": 'size', "TotalSpendings": ['sum', 'mean']})
    Basic.columns = ['TotalRecords', 'TotalAmount', 'AvgAmount']

    # Create a figure with three subplots
    fig5, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    # Plot histogram for TotalRecords
    axes[0].bar(Basic.index, Basic['TotalRecords'])
    axes[0].set_xlabel('Basic Education Group')
    axes[0].set_ylabel('Total Records')
    axes[0].set_title('Total Records by Basic Education Group')

    axes[1].bar(Basic.index, Basic['TotalRecords'])
    axes[1].set_xlabel('Basic Education Group')
    axes[1].set_ylabel('Total Records')
    axes[1].set_title('Total Records by Basic Education Group')

    axes[2].bar(Basic.index, Basic['TotalRecords'])
    axes[2].set_xlabel('Basic Education Group')
    axes[2].set_ylabel('Total Records')
    axes[2].set_title('Total Records by Basic Education Group')

    # Display the figure
    st.pyplot(fig5)

    # 6. Graduation
    Graduation = df.groupby("Graduation").agg({"Graduation": 'size', "TotalSpendings": ['sum', 'mean']})
    Graduation.columns = ['TotalRecords', 'TotalAmount', 'AvgAmount']


    # Create a figure with three subplots
    fig6, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    # Plot histogram for TotalRecords
    axes[0].bar(Graduation.index, Graduation['TotalRecords'])
    axes[0].set_xlabel('Graduation Education Group')
    axes[0].set_ylabel('Total Records')
    axes[0].set_title('Total Records by Graduation Education Group')

    axes[1].bar(Graduation.index, Graduation['TotalRecords'])
    axes[1].set_xlabel('Graduation Education Group')
    axes[1].set_ylabel('Total Records')
    axes[1].set_title('Total Records by Graduation Education Group')

    axes[2].bar(Graduation.index, Graduation['TotalRecords'])
    axes[2].set_xlabel('Graduation Education Group')
    axes[2].set_ylabel('Total Records')
    axes[2].set_title('Total Records by Graduation Education Group')

    # Display the figure
    st.pyplot(fig6)

    # 7.AdvanceEducation
    AdvanceEducation = df.groupby("AdvanceEducation").agg({"AdvanceEducation": 'size', "TotalSpendings": ['sum', 'mean']})
    AdvanceEducation.columns = ['TotalRecords', 'TotalAmount', 'AvgAmount']

    # Create a figure with three subplots
    fig7, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    # Plot histogram for TotalRecords
    axes[0].bar(AdvanceEducation.index, AdvanceEducation['TotalRecords'])
    axes[0].set_xlabel('Advance Education Group')
    axes[0].set_ylabel('Total Records')
    axes[0].set_title('Total Records by Advance Education Group')

    axes[1].bar(AdvanceEducation.index, AdvanceEducation['TotalRecords'])
    axes[1].set_xlabel('Advance Education Group')
    axes[1].set_ylabel('Total Records')
    axes[1].set_title('Total Records by Advance Education Group')

    axes[2].bar(AdvanceEducation.index, AdvanceEducation['TotalRecords'])
    axes[2].set_xlabel('Advance Education Group')
    axes[2].set_ylabel('Total Records')
    axes[2].set_title('Total Records by Advance Education Group')

    # Display the figure
    st.pyplot(fig7)

def data_Traits():
    #st.write("Understanding Customer Data Patterns!")

    # Model Training
    st.subheader("Extracting Customer Personality Traits!")
    #st.write("K-means Clustering model will show the different customer interests as follows:")

    Cdata = pd.read_csv('C:/Users/ssude/sonyproject/sonyproject/ClusterInfo.csv')
    st.write("Different Age groups exhibit varying levels of interest ")
    values = Cdata['Cluster']
    names = Cdata['AgeGroup']
    st.subheader("The Adults means the age between(20yrs to 60yrs are more purchasers)")

    fig8 = px.pie(Cdata, values=values, names=names, title='Age Groups')
    fig8.update_traces(textposition='inside', textinfo='percent+label')
    fig8.update_layout(title_font_size=50)
    st.plotly_chart(fig8)

    st.write("Different Marital Status groups exhibit varying levels of interest ")
    values = Cdata['Cluster']
    names = Cdata['Marital_Status']
    st.subheader("The small family size purchases are more")

    fig9 = px.pie(Cdata, values=values, names=names, title='Marital Status Groups')
    fig9.update_traces(textposition='inside', textinfo='percent+label')
    fig9.update_layout(title_font_size=50)
    st.plotly_chart(fig9)

    st.write("Different Education groups exhibit varying levels of interest ")
    values = Cdata['Cluster']
    names = Cdata['Education']
    st.subheader("The graduation level persons purchases are more")

    fig10 = px.pie(Cdata, values=values, names=names, title='Education Group')
    fig10.update_traces(textposition='inside', textinfo='percent+label')
    fig10.update_layout(title_font_size=50)
    st.plotly_chart(fig10)

    st.write("Different Kids groups exhibit varying levels of interest ")
    values = Cdata['Cluster']
    names = Cdata['Children'] 
    st.subheader("The families consists of 1 child purchases are more")
    fig11 = px.pie(Cdata, values=values, names=names, title='Kids Group')
    fig11.update_traces(textposition='inside', textinfo='percent+label')
    fig11.update_layout(title_font_size=50)
    st.plotly_chart(fig11)

def data_Personality_Profiles():
    st.subheader("Grouping Customers Based on Personality Profiles!")
    model = pickle.load(open('C:/Users/ssude/sonyproject/sonyproject/Model.pkl', 'rb'))

    Age = st.select_slider('Age', list(range(20, 101)), value=(20 + 101) // 2)
    Partners = st.select_slider('Partners', list(range(0, 3)), value=(0 + 3) // 2)
    Single = st.select_slider('Single', list(range(0, 3)), value=(0 + 3) // 2)
    Children = st.select_slider('Children', list(range(0, 4)), value=(0 + 4) // 2)
    Basic = st.select_slider('Basic', list(range(0, 3)), value=(0 + 3) // 2)
    Graduation = st.select_slider('Graduation', list(range(0, 3)), value=(0 + 3) // 2)
    Advance_Education = st.select_slider('Advance_Education', list(range(0, 3)), value=(0 + 3) // 2)
    Income = st.select_slider('Income', list(range(1700, 160001)), value=(1700 + 160001) // 2)
    TotalSpendings = st.select_slider('TotalSpendings', list(range(5, 2601)), value=(5 + 2601) // 2)
    PlaceSpendings = st.select_slider('PlaceSpendings', list(range(0, 51)), value=(0 + 51) // 2)
    WebEnrollment = st.select_slider('WebEnrollment', list(range(0, 21)), value=(0 + 21) // 2)
    MonthEnrollment = st.select_slider('MonthEnrollment', list(range(90, 141)), value=(90 + 141) // 2)
    Accepting_Cmps = st.select_slider('Accepting_Cmps', list(range(0, 6)), value=(0 + 6) // 2)
    Recency = st.select_slider('Recency', list(range(0, 101)), value=(0 + 101) // 2)
    Complain = st.select_slider('Complain', list(range(0, 3)), value=(0 + 3) // 2)
    Response = st.select_slider('Response', list(range(0, 3)), value=(0 + 3) // 2)

    



    if st.button('Predict'):
        makeprediction = model.predict([[Age, Partners, Single, Children, Basic, Graduation,
                                         Advance_Education, Income, TotalSpendings, PlaceSpendings,
                                         WebEnrollment, MonthEnrollment, Accepting_Cmps, Recency, Complain, Response]])
        output = round(makeprediction[0])
        st.success('Cluster Group is : {}'.format(output))
        
        # Display cluster name
        cluster_names = {
            0: 'Budget Conscious Shoppers',
            1: 'Esteemed Buyers',
            2: 'Regular Consumers',
            3: 'Discerning Buyers'
        }
        cluster_name = cluster_names.get(output)
        st.info('Category: {}'.format(cluster_name))


def main():
    
    menu = ["Data Capturing", "Data Patterns", "Data Traits", "Data Personality Profile"]
    choice = st.sidebar.selectbox("Select Page", menu)

    # Set CSS styles
    main_style = """
        <style>
        .main {
            padding: 10px;
            background-color: #F0F0F0;
            border: 5px solid #000000; /* Black border */
        }
        }
        </style>
    """
            
     
    # Set header and footer
    header = """
        <div>
            <h1 style='text-align: center; font-size: 36px; padding-bottom: 20px;'>Marketing Campaign Analysis</h1>
        </div>
    """

    footer = """
        <div style='text-align: center; padding-top: 20px;'>
            <h5>continue...</h5>
        </div>
    """


   
     # Apply styles and header/footer based on the selected page
    if choice == "Data Capturing":
        st.markdown(main_style, unsafe_allow_html=True)
        st.markdown(header, unsafe_allow_html=True)
        data_Capturing()
        st.markdown(footer, unsafe_allow_html=True)
    elif choice == "Data Patterns":
        st.markdown(main_style, unsafe_allow_html=True)
        st.markdown(header, unsafe_allow_html=True)
        data_Patterns()
        st.markdown(footer, unsafe_allow_html=True)
    elif choice == "Data Traits":
        st.markdown(main_style, unsafe_allow_html=True)
        st.markdown(header, unsafe_allow_html=True)
        data_Traits()
        st.markdown(footer, unsafe_allow_html=True)
    elif choice == "Data Personality Profile":
        st.markdown(main_style, unsafe_allow_html=True)
        st.markdown(header, unsafe_allow_html=True)
        data_Personality_Profiles()
        #st.markdown(footer, unsafe_allow_html=True)
        # Set background image and style


if __name__ == "__main__":
    main() 

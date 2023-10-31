import streamlit as st
import pandas as pd


with st.sidebar:

  st.title("AutoML 🤖")
  st.write("Transform your data into machine learning insights with a breeze.")

  # Upload CSV File
  uploaded_file = st.file_uploader("Upload your Dataset file")

if uploaded_file is not None:

  # setup tabs

  setup_tab, preprocess_tab, explore_tab, feature_tab, train_tab, deploy_tab = st.tabs(["Setup",
     "Preprocess", 
     "Explore", 
     "Select Features", 
     "Train", 
     "Deploy"
  ])

  # setup data

  with setup_tab:
    if uploaded_file.type == "text/csv":
      
      # view dataframe
      st.markdown("#### Dataframe")
      df_csv = pd.read_csv(uploaded_file)
      st.write(df_csv)

      # show dataframe shape

      st.markdown("#### Shape")
      df_shape = df_csv.shape
      st.markdown(f"The dataset has **{df_shape[0]} Rows** and **{df_shape[1]} Columns**")


      # show dataframe description
      st.markdown("#### Data Overview")
      st.write(df_csv.describe())

      # show dataframe column info

      st.markdown("#### Columns")
      df_columns = df_csv.columns
      info_dict = {
        "columns": df_columns,
        "Non Null Count": [],
        "Null Count": [],
        "Data Type": []
      }

      for col in df_columns:
        # calculate total values
        info_dict['Non Null Count'].append(len(df_csv[col]))
        info_dict['Null Count'].append(df_csv[col].isna().sum())
        info_dict['Data Type'].append(df_csv[col].dtype)

      st.table(info_dict)


  with preprocess_tab:
    st.write("Preprocess Data")

  with explore_tab:
    st.write("Explore Data")

  with feature_tab:
    st.write("Select Features")

  with train_tab:
    st.write("Train Model")

  with deploy_tab:
    st.write("Deploy Model")
import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 


st.title ("Titanic")
st.markdown ("Visualisation of Titanic Dataset")

selected_x_var = st.selectbox('X Variable' , 
                              ['age', 'fare',
                              'survived', 'parch'])

selected_y_var = st.selectbox('Y Variable' , 
                              ['age', 'fare',
                              'survived', 'parch'])
gender = st.radio('Gender', ['male' ,'female'])

Titanic_file = st.file_uploader ("Select a folder")
if Titanic_file is not None :
    Titanic_df = pd.read_csv(Titanic_file)
else :
    st.stop() # to prevent the entire app from running 

filteredbygender = Titanic_df.loc[Titanic_df ['sex']== gender]
st.write(filteredbygender)

# creating the scatter plot
sns.set_style ('darkgrid')
markers = {'Male' : 'X', 'Female' : '0'}

fig , ax = plt.subplots()
ax = sns.scatterplot(data= filteredbygender,
x = selected_x_var, y = selected_y_var,
hue = 'sex' , markers = markers)

plt.xlabel (selected_x_var)
plt.ylabel(selected_y_var)
plt.title('Scatterplot Titanic')
st.pyplot(fig)

import streamlit as st
st.header('Factorial App')
y=st.number_input('Enter a number',value=0)
bt=st.button('Result')

if bt:
    x=1
    for i in range(1,y+1):
      x=x*i
    st.subheader(x)
   

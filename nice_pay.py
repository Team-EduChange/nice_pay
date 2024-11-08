import streamlit as st

st.header('결제가 완료되었습니다.')

query_params = st.query_params
st.write(query_params)
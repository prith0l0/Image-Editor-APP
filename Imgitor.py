import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align: center';>Imgitor</h1>", unsafe_allow_html=True)
st.markdown("---")
image = st.file_uploader("Upload Your Image", type=["jpg","img","jpeg","pdf","raw","NEF"])
info=st.empty()
size=st.empty()
mode=st.empty()
format_=st.empty()
if image:
    img=Image.open(image)
    info.markdown(f"<h2 style='color:Black';>Information</h2>",unsafe_allow_html=True)
    size.markdown(f"<h6 style='color:#4CE2E4';>Size: {img.size}</h6>",unsafe_allow_html=True)
    mode.markdown(f"<h6 style='color:#4CE2E4'>Mode: {img.mode}</h6>",unsafe_allow_html=True)
    format_.markdown(f"<h6 style='color:#4CE2E4'>Format: {img.format}</h6>",unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center';>Resizeing</h2>",unsafe_allow_html=True)
    width=st.number_input("Width", value=img.width)
    height=st.number_input("Height", value=img.height)
    st.markdown("<h2 style='text-align: center';>Rotation</h2>",unsafe_allow_html=True)
    degree=st.number_input("Degree")
    st.markdown("<h2 style='text-align: center';>Filter</h2>",unsafe_allow_html=True)
    filters=st.selectbox("Filters", options=("None","Blur","Smooth","Detail","Sharpen","Smooth-More","Emboss","Contour","Edge-Enhance"))
    s_btn=st.button("Submit")
    if s_btn:
        editied=img.resize((width,height)).rotate(degree)
        Filtered=editied
        if filters != "None":
            if filters == "Blur":
                Filtered= editied.filter(BLUR)
            elif filters == "Smooth":
                Filtered= editied.filter(SMOOTH)
            elif filters == "Emboss":
                Filtered= editied.filter(EMBOSS)
            elif filters == "Detail":
                Filtered= editied.filter(DETAIL)
            elif filters == "Sharpen":
                Filtered= editied.filter(SHARPEN)
            elif filters == "Smooth-More":
                Filtered= editied.filter(SMOOTH_MORE)
            elif filters == "Contour":
                Filtered= editied.filter(CONTOUR)
            
        else:
            Filterd= editied.filter(EDGE_ENHANCE)
            
        st.image(Filtered)
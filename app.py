import streamlit as st

def main():
    """Basic CSS Shape Generator"""

    activities=["Design","About"]
    choice=st.sidebar.selectbox("Select Activity",activities)
    
    if choice == "Design":
        bgcolor = st.color_picker("Pick a Background Color")
        fontcolor=st.color_picker("Pick a Font Color","#ffffff")   

    
    
    html_temp="""
    <div style="background-color:{}; padding:10px">
    <h1 style="color:{};text-align:center">Basic CSS Shape Generator</h1>
    </div>
    """ 
    st.markdown(html_temp.format(bgcolor,fontcolor),unsafe_allow_html=True)

    

    if choice=="Design":
        st.subheader("Design")
        st.subheader("Modify the Shape")

        bgcolor2=st.sidebar.color_picker("Pick Bg Color")
        height = st.sidebar.slider("Height Size",10,200,50)
        width = st.sidebar.slider("Width Size",10,200,50)
        top_left_border=st.sidebar.number_input("Top Left Border",10,50,10)
        top_right_border=st.sidebar.number_input("Top Right Border",10,50,10)
        bottom_left_border=st.sidebar.number_input("Bottom Left Border",10,50,10)
        bottom_right_border=st.sidebar.number_input("Bottom Right Border",10,50,10)
        
        border_style=st.sidebar.selectbox("Border Style",["dotted","dashed","solid","double","groove","ridge","inset","outset","none","hidden"])
        border_color=st.sidebar.color_picker("Pick a Border Color","#654FEF")
        html_design = """
		<div style="height:{}px;width:{}px;background-color:{};border-radius:{}px {}px {}px {}px;border-style:{};border-color:{}">
		</div>
		"""

        st.markdown(html_design.format(bgcolor2,height,width,top_left_border,top_right_border,bottom_left_border,bottom_right_border,border_style,border_color),unsafe_allow_html=True)

        if st.checkbox("Result"):
            result_of_design=html_design.format(bgcolor2,height,width,top_left_border,top_right_border,bottom_left_border,bottom_right_border,border_style,border_color)
            st.code(html_design)
            st.code(result_of_design)
       
    if choice=="About":
        st.subheader("About")
        st.success("Created by Erdem Okutan")


if __name__ == "__main__":
    main()
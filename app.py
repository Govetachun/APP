import streamlit as st
import pandas as pd
import os
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import graphviz
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

st.set_page_config(
page_title = "Urban waste collection aid - UWC 2.0",
page_icon = "Active",
layout = "wide",
initial_sidebar_state='expanded',
)

#___ user authentication ___#

names = ["Bach","Admin"]
usernames = ["bbach","aadmin"]
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as f:
    hashed_passwords = pickle.load(f)

credentials = {"usernames":{}}

for un, name, pw in zip(usernames, names, hashed_passwords):
    user_dict = {"name":name,"password":pw}
    credentials["usernames"].update({un:user_dict})
authenticator = stauth.Authenticate(credentials,"sales_dashboard","abcdef", cookie_expiry_days=30)

pic1,signin = st.columns((6,4))

with signin:
    name,authentication_status ,username= authenticator.login("Login","main")

    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")
with pic1:
    if authentication_status != True:
        st.title("Urban waste collection aid - UWC 2.0")
        st.image("https://i.pinimg.com/originals/89/77/1c/89771c920c59c679a63a115dea5f9010.jpg")
if authentication_status == True:
    if os.path.exists('./dataset.csv'): 
        df = pd.read_csv('dataset.csv', index_col=None)
    if os.path.exists('./workshift.csv'): 
        wsh = pd.read_csv('workshift.csv', index_col=None)
    if os.path.exists('./capacity.csv'): 
        cap = pd.read_csv('capacity.csv', index_col=None)
    if os.path.exists('./routes1.csv'): 
        routes1 = pd.read_csv('routes1.csv', index_col=None)
    if os.path.exists('./routes2.csv'): 
        routes2 = pd.read_csv('routes2.csv', index_col=None)
    if os.path.exists('./routes3.csv'): 
        routes3 = pd.read_csv('routes3.csv', index_col=None)
    if os.path.exists('./vehicle.csv'): 
        vehicle = pd.read_csv('vehicle.csv', index_col=None)
    if os.path.exists('./vehicle_assigning.csv'): 
        vehicle_assigning = pd.read_csv('vehicle_assigning.csv', index_col=None)
    if os.path.exists('./MCP_assigning.csv'): 
        MCP_assigning = pd.read_csv('MCP_assigning.csv', index_col=None)

    with st.sidebar: 
        
        st.sidebar.title(f"Welcome {name}")
        choice = option_menu(menu_title = None, 
                            options = ["Dashboard","Calendar", "Vehicles","MCP","Assignment","Routes Planning","Chat","Working status now","Logout"],
                            default_index = 0,)
        st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
        st.title("Urban waste collection aid - UWC 2.0")
        
        

    # if choice == "Upload":
    #     st.title("Upload Your Dataset")
    #     file = st.file_uploader("Upload Your Dataset")
    #     if file: 
    #         df = pd.read_csv(file, index_col=None)
    #         df.to_csv('dataset.csv', index=None)
    #         st.dataframe(df)

    if choice == "Dashboard":
        st.title("Dashboard for the work day")
        col1, col2, col3 = st.tabs(['Morning','Afternoon','Evening'])
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        with col1:
            st.markdown("### Current status of garbage trucks in Morning")
            column1,column2,column3=st.columns(3)
            with column1:
                st.write('The vehicles status available')
                colors = ['gold', 'mediumturquoise', 'darkorange']
                value = df[:3].values[0]
                fig = go.Figure(data=[go.Pie(labels=['In use','In use','Available','In maintenance'], values=value,title="Vehicles")])
                fig.update_traces(hoverinfo='label+percent', textinfo='label+value', textfont_size=15,
                            marker=dict(colors=colors, line=dict(color='#000000', width=3)))

                st.write(fig)
            with column2:
                st.write("MCPs list status in Morning")
                fig3 = px.bar(cap,x="MCP",y="count",color="status")
                st.write(fig3)
            with column3:
                st.write("MCPs's janitors and collectors status in Morning")
                fig2 = go.Figure([go.Bar(x=['Collectors','Janitors'], y=[df['Collectors'].values[0], df['Janitors'].values[0]])])
                st.write(fig2)


            column4,column5_1,a,column5_2= st.columns((3,3,1,3))
            with column4:
                st.markdown("### Vehicle status")

                def highlight_survived(s):
                    return ['background-color: green']*len(s) if s.Available else ['background-color: red']*len(s)
                st.dataframe(vehicle.style.apply(highlight_survived, axis=1))
            with column5_1:
                st.markdown("### Assignment")
                fig5_1 = ff.create_table(MCP_assigning)
                st.write(fig5_1)
            with a:
                pass
            with column5_2:
                st.markdown("### Vehicle Assignment")
                fig5_2 = ff.create_table(vehicle_assigning)
                st.write(fig5_2)
                
        with col2:
            st.markdown("### Current status of garbage trucks in Afternoon")
            column6,column7,column8=st.columns(3)
            with column6:
                st.write('The vehicles status available')
                colors = ['lightgreen', 'royalblue', 'gold']
                value = df[:3].values[1]
                fig = go.Figure(data=[go.Pie(labels=['In use','In use','Available','In maintenance'], values=value,title="Vehicles")])
                fig.update_traces(hoverinfo='label+percent', textinfo='label+value', textfont_size=15,
                            marker=dict(colors=colors, line=dict(color='#000000', width=3)))

                st.write(fig)
            with column7:
                st.write("MCPs list status in Afternoon")
                fig3 = px.bar(cap,x="MCP",y="count",color="status")
                st.write(fig3)
            with column8:
                st.write("MCPs's janitors and collectors status in Morning")
                fig2 = go.Figure([go.Bar(x=['Collectors','Janitors'], y=[df['Collectors'].values[1], df['Janitors'].values[1]])])
                st.write(fig2)


            column9,column10_1,a,column10_2= st.columns((3,3,1,3))
            with column9:
                st.markdown("### Vehicle status")

                def highlight_survived(s):
                    return ['background-color: green']*len(s) if s.Available else ['background-color: red']*len(s)
                st.dataframe(vehicle.style.apply(highlight_survived, axis=1))
            with column10_1:
                st.markdown("### Assignment")
                fig5_1 = ff.create_table(MCP_assigning)
                st.write(fig5_1)
            with column10_2:
                st.markdown("### Vehicle Assignment")
                fig5_2 = ff.create_table(vehicle_assigning)
                st.write(fig5_2)
        with col3:
            st.markdown("### Current status of garbage trucks in Evening")
            column11,column12,column13=st.columns(3)
            with column11:
                st.write('The vehicles status available')
                colors = ['rgb(175, 49, 35)', 'darkorange', 'lightgreen']
                value = df[:3].values[2]
                fig = go.Figure(data=[go.Pie(labels=['In use','In use','Available','In maintenance'], values=value,title="Vehicles")])
                fig.update_traces(hoverinfo='label+percent', textinfo='label+value', textfont_size=15,
                            marker=dict(colors=colors, line=dict(color='#000000', width=3)))

                st.write(fig)
            with column12:
                st.write("MCPs list status in Evening")
                fig3 = px.bar(cap,x="MCP",y="count",color="status")
                st.write(fig3)
            with column13:
                st.write("MCPs's janitors and collectors status in Morning")
                fig2 = go.Figure([go.Bar(x=['Collectors','Janitors'], y=[df['Collectors'].values[2], df['Janitors'].values[2]])])
                st.write(fig2)


            column14,column15_1,a,column15_2= st.columns((3,3,1,3))
            with column14:
                st.markdown("### Vehicle status")

                def highlight_survived(s):
                    return ['background-color: green']*len(s) if s.Available else ['background-color: red']*len(s)
                st.dataframe(vehicle.style.apply(highlight_survived, axis=1))
            with column15_1:
                st.markdown("### Assignment")
                fig5_1 = ff.create_table(MCP_assigning)
                st.write(fig5_1)
            with column15_2:
                st.markdown("### Vehicle Assignment")
                fig5_2 = ff.create_table(vehicle_assigning)
                st.write(fig5_2)
        st.title("Route information")
        col4, col5, col6 ,col7= st.columns(4)
        with col4:
            st.info("Vehicle #1234")
            graph1 = graphviz.Digraph()

            for i in range(len(routes1)):
                graph1.edge(routes1['A'].values[i],routes1['B'].values[i])

            st.graphviz_chart(graph1)
        with col5:
            st.info("Vehicle #0001")
            graph2 = graphviz.Digraph()

            for i in range(len(routes2)):
                graph2.edge(routes2['A'].values[i],routes2['B'].values[i])

            st.graphviz_chart(graph2)
        with col6:
            st.info("Vehicle #0004")
            graph3 = graphviz.Digraph()

            for i in range(len(routes3)):
                graph3.edge(routes3['A'].values[i],routes3['B'].values[i])

            st.graphviz_chart(graph3)
        with col7:
            st.info("Vehicle #0007")
            graph1 = graphviz.Digraph()

            for i in range(len(routes1)):
                graph1.edge(routes1['A'].values[i],routes1['B'].values[i])

            st.graphviz_chart(graph1)
    elif choice == "Vehicles":
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.markdown('### Vehicle')
        col1, col2, col3 = st.columns(3)
        col1.metric("Vehicle number: 1234", "0km/h", "Available")
        col2.metric("Vehicle number: 2345", "20km/h", "-In use")
        col3.metric("Vehicle number: 3456", "40km/h", "-In use%")
        col4, col5, col6 = st.columns(3)
        col4.metric("Vehicle number: 1234", "70km/h", "-In use")
        col5.metric("Vehicle number: 2345", "0km/h", "Available")
        col6.metric("Vehicle number: 3456", "8km/h", "-In use")
        col7, col8, col9 = st.columns(3)
        col7.metric("Vehicle number: 1234", "30km/h", "-In use")
        col8.metric("Vehicle number: 2345", "22km/h", "-In use")
        col9.metric("Vehicle number: 3456", "0km/h", "Available")
        col10, col11, col12 = st.columns(3)
        col10.metric("Vehicle number: 1234", "30km/h", "-In use")
        col11.metric("Vehicle number: 2345", "22km/h", "Available")
        col12.metric("Vehicle number: 3456", "0km/h", "Available")
    elif choice == "MCP":
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.markdown("### MCPs's Goal")
        col1,col2,col3 = st.columns(3)
        with col1:
            st.markdown('### #MCP1 ')
            st.markdown('#####  268 Ly Thuong Kiet')
            age = st.slider('Capacity goal: 2 tons', 0, 100, 25)
            st.write( age, '% of the capacity goal - ',age/100*2, 'tons')
        with col2:
            st.markdown('### #MCP2 ')
            st.markdown('#####  114 To Hien Thanh')
            age2 = st.slider('Capacity goal: 5 tons', 0, 100, 26)
            st.write( age2, '% of the capacity goal - ',age2/100*5, 'tons')
        with col3:
            st.markdown('### #MCP1 ')
            st.markdown('#####  153 Nguyen Chi Thanh')
            age3 = st.slider('Capacity goal: 6 tons', 0, 100, 50)
            st.write( age3, '% of the capacity goal - ',age3/100*6, 'tons')
        col4,col5,col6 = st.columns(3)
        with col4:
            st.markdown('### #MCP4 ')
            st.markdown('#####  100 Tran Hung Dao')
            age4 = st.slider('Capacity goal: 3 tons', 0, 100, 70)
            st.write( age4, '% of the capacity goal - ',age4/100*3, 'tons')
        with col5:
            st.markdown('### #MCP5 ')
            st.markdown('#####  45 Nguyen Thai Hoc')
            age5 = st.slider('Capacity goal: 5 tons', 0, 100, 95)
            st.write( age5, '% of the capacity goal - ',age5/100*5, 'tons')
        with col6:
            st.markdown('### #MCP6 ')
            st.markdown('#####  34 Cong Hoa')
            age6 = st.slider('Capacity goal: 8 tons', 0, 100, 12)
            st.write( age6, '% of the capacity goal - ',age6/100*8, 'tons')
    elif choice == "Assignment":
        placeholder = st.empty()

        if "visibility" not in st.session_state:
            st.session_state.visibility = "visible"
            st.session_state.disabled = False
        col1 ,col2 = st.columns(2)
        with col1:
                st.markdown("### Assignment")

                with st.expander("Remove MCP task:"):
                    text_input = st.text_input(
                        "Enter the MCP you want to remove 👇",
                        label_visibility=st.session_state.visibility,
                        disabled=st.session_state.disabled,
                    )

                    if text_input:
                        st.write("You entered: ", text_input)
                        MCP_assigning = MCP_assigning[MCP_assigning['MCP ID'].str.contains(text_input) == False]
                        MCP_assigning.to_csv('MCP_assigning.csv',index=False)
                
                with st.expander("Add MCP task:"):
                    with st.form(key="form5",clear_on_submit=True):
                        MCP_ID = st.text_input("Enter MCP_ID task here 👇")
                        Janitor_1 = st.text_input("Enter  Janitor 1 here 👇")
                        Janitor_2 = st.text_input("Enter Janitor 2 here 👇")
                        submit_MCP = st.form_submit_button(label="Submit5")
                    if submit_MCP:
                        MCP_assigning = MCP_assigning.append({'MCP ID':MCP_ID,'Janitor 1':Janitor_1,'Janitor 2':Janitor_2},ignore_index=True)
                        MCP_assigning.to_csv('MCP_assigning.csv',index=False)
                fig5_1 = ff.create_table(MCP_assigning)
                st.write(fig5_1)
        with col2:
                st.markdown("### Vehicle Assignment")
                with st.expander("Remove vehicle task:"):
                    text_input2 = st.text_input(
                        "Enter the vehicle you want to remove 👇",
                        label_visibility=st.session_state.visibility,
                        disabled=st.session_state.disabled,
                    )

                    if text_input2:
                        st.write("You entered: ", text_input2)
                        vehicle_assigning = vehicle_assigning[vehicle_assigning['Vehicle ID'].str.contains(text_input2) == False]
                        vehicle_assigning.to_csv('vehicle_assigning.csv',index=False)
                
                with st.expander("Add vehicle task:"):
                    with st.form(key="form6",clear_on_submit=True):
                        Vehicle_ID = st.text_input("Enter Vehicle_ID task here 👇")
                        Collector = st.text_input("Enter Collector here 👇")
                        submit_vehicle = st.form_submit_button(label="Submit6")
                    if submit_vehicle:
                        vehicle_assigning = vehicle_assigning.append({'Vehicle ID':Vehicle_ID,'Collector':Collector},ignore_index=True)
                        vehicle_assigning.to_csv('vehicle_assigning.csv',index=False)
                fig5_2 = ff.create_table(vehicle_assigning)
                st.write(fig5_2)
    elif choice == "Calendar":
        to_do_monday = pd.read_csv('monday.csv',index_col=None)
        to_do_tuesday = pd.read_csv('tuesday.csv',index_col=None)
        to_do_wednesday = pd.read_csv('wednesday.csv',index_col=None)
        to_do_thursday = pd.read_csv('thursday.csv',index_col=None)
        to_do_friday = pd.read_csv('friday.csv',index_col=None)
        col1,col2,col3,col4,col5 = st.columns(5)
        if "visibility" not in st.session_state:
            st.session_state.visibility = "visible"
            st.session_state.disabled = False
        with col1:
            st.markdown("### Monday 🐷")
            st.markdown("""---""")
            st.write("To do |",len(to_do_monday.index)," tasks")


            with st.expander("Add task"):
                    with st.form(key="form1",clear_on_submit=True):
                        MCP_input1 = st.text_input("Enter your Monday task here 👇")
                        vehicle_input1 = st.text_input("Enter your Monday's vehicle here 👇")
                        time_input1 = st.text_input("Enter your Monday's time here 👇")
                        submit_button1 = st.form_submit_button(label="Submit1")
                    if submit_button1:
                        to_do_monday = pd.read_csv('monday.csv',index_col=None)
                        collector1 = ''
                        for k in range(0,len(vehicle_assigning)):
                            if vehicle_assigning['Vehicle ID'].values[k] in vehicle_input1:
                                collector1 += vehicle_assigning['Collector'].values[k]
                        append = {'Todo':MCP_input1,'Vehicle':vehicle_input1,'Collectors':collector1,'Time':time_input1}
                        to_do_monday = to_do_monday.append(append,ignore_index=True)
                        to_do_monday.to_csv('monday.csv',index=None)
                    
                    st.write("Fomula to input task: Name of MCP,ID of Vehicle (from #0000 to #0007)")
                    st.write("Ex: Go to MCP1,#0000")
                    st.write("Remember to delete the placeholder before delete task")

            with st.expander("Remove task"):
                    st.markdown("##### Double-Click the task to remove it from the to do list")
                    button_day = [None] * len(to_do_monday.index)
                    for i in range(0,len(to_do_monday.index)):
                        button_day[i] = st.button("Task " +str(i)+ " "+ to_do_monday['Todo'].values[i])
                    for i in range(0,len(to_do_monday.index)):
                        if button_day[i]:
                            to_do_monday= to_do_monday.drop(i)
                            to_do_monday.to_csv('monday.csv',index=None)
                    
            st.dataframe(to_do_monday)
        with col2:
            st.markdown("### Tuesday 🐑")
            st.markdown("""---""")
            st.write("To do |",len(to_do_tuesday.index)," tasks")

            with st.expander("Add task"):
                    with st.form(key="form2",clear_on_submit=True):
                        MCP_input2 = st.text_input("Enter your Tuesday task here 👇")
                        vehicle_input2 = st.text_input("Enter your Tuesday's vehicle here 👇")
                        time_input2 = st.text_input("Enter your Tuesday's time here 👇")
                        submit_button2 = st.form_submit_button(label="Submit2")
                    if submit_button2:
                        to_do_tuesday = pd.read_csv('tuesday.csv',index_col=None)
                        collector2 = ''
                        for k in range(0,len(vehicle_assigning)):
                            if vehicle_assigning['Vehicle ID'].values[k] in vehicle_input2:
                                collector2 += vehicle_assigning['Collector'].values[k]
                        append = {'Todo':MCP_input2,'Vehicle':vehicle_input2,'Collectors':collector2,'Time':time_input2}
                        to_do_tuesday = to_do_tuesday.append(append,ignore_index=True)
                        to_do_tuesday.to_csv('tuesday.csv',index=None)
                    
                    st.write("Fomula to input task: Name of MCP,ID of Vehicle (from #0000 to #0007)")
                    st.write("Ex: Go to MCP1,#0000")
                    st.write("Remember to delete the placeholder before delete task")

            with st.expander("Remove task"):
                    st.markdown("##### Double-Click the task to remove it from the to do list")
                    button_dayTues = [None] * len(to_do_tuesday.index)
                    for i in range(0,len(to_do_tuesday.index)):
                        button_dayTues[i] = st.button("Task " +str(i)+ " "+ to_do_tuesday['Todo'].values[i])
                    for i in range(0,len(to_do_tuesday.index)):
                        if button_dayTues[i]:
                            to_do_tuesday= to_do_tuesday.drop(i)
                            to_do_tuesday.to_csv('tuesday.csv',index=None)
                    
            st.dataframe(to_do_tuesday)
        with col3:
            st.markdown("### Wednesday 🍮")
            st.markdown("""---""")
            st.write("To do |",len(to_do_wednesday.index)," tasks")

            with st.expander("Add task"):
                    with st.form(key="form3",clear_on_submit=True):
                        MCP_input3 = st.text_input("Enter your Wednesday task here 👇")
                        vehicle_input3 = st.text_input("Enter your Wednesday's vehicle here 👇")
                        time_input3 = st.text_input("Enter your Wednesday's time here 👇")
                        submit_button3 = st.form_submit_button(label="Submit3")
                    if submit_button3:
                        to_do_wednesday = pd.read_csv('wednesday.csv',index_col=None)
                        collector3 = ''
                        for k in range(0,len(vehicle_assigning)):
                            if vehicle_assigning['Vehicle ID'].values[k] in vehicle_input3:
                                collector3 += vehicle_assigning['Collector'].values[k]
                        append = {'Todo':MCP_input3,'Vehicle':vehicle_input3,'Collectors':collector3,'Time':time_input3}
                        to_do_wednesday = to_do_wednesday.append(append,ignore_index=True)
                        to_do_wednesday.to_csv('wednesday.csv',index=None)
                    
                    st.write("Fomula to input task: Name of MCP,ID of Vehicle (from #0000 to #0007)")
                    st.write("Ex: Go to MCP1,#0000")
                    st.write("Remember to delete the placeholder before delete task")

            with st.expander("Remove task"):
                    st.markdown("##### Double-Click the task to remove it from the to do list")
                    button_dayWeds = [None] * len(to_do_wednesday.index)
                    for i in range(0,len(to_do_wednesday.index)):
                        button_dayWeds[i] = st.button("Task " +str(i)+ " "+ to_do_wednesday['Todo'].values[i])
                    for i in range(0,len(to_do_wednesday.index)):
                        if button_dayWeds[i]:
                            to_do_wednesday= to_do_wednesday.drop(i)
                            to_do_wednesday.to_csv('wednesday.csv',index=None)
                    
            st.dataframe(to_do_wednesday)
        with col4:
            st.markdown("### Thursday 🦄")
            st.markdown("""---""")
            st.write("To do |",len(to_do_thursday.index)," tasks")

            with st.expander("Add task"):
                    with st.form(key="form4",clear_on_submit=True):
                        MCP_input4 = st.text_input("Enter your Thursday task here 👇")
                        vehicle_input4 = st.text_input("Enter your Thursday's vehicle here 👇")
                        time_input4 = st.text_input("Enter your Thursday's time here 👇")
                        submit_button4 = st.form_submit_button(label="Submit4")
                    if submit_button4:
                        to_do_thursday = pd.read_csv('thursday.csv',index_col=None)
                        collector4 = ''
                        for k in range(0,len(vehicle_assigning)):
                            if vehicle_assigning['Vehicle ID'].values[k] in vehicle_input4:
                                collector4 += vehicle_assigning['Collector'].values[k]
                        append = {'Todo':MCP_input4,'Vehicle':vehicle_input4,'Collectors':collector4,'Time':time_input4}
                        to_do_thursday = to_do_thursday.append(append,ignore_index=True)
                        to_do_thursday.to_csv('thursday.csv',index=None)
                    st.write("Fomula to input task: Name of MCP,ID of Vehicle (from #0000 to #0007)")
                    st.write("Ex: Go to MCP1,#0000")
                    st.write("Remember to delete the placeholder before delete task")

            with st.expander("Remove task"):
                    st.markdown("##### Double-Click the task to remove it from the to do list")
                    button_dayThur = [None] * len(to_do_thursday.index)
                    for i in range(0,len(to_do_thursday.index)):
                        button_dayThur[i] = st.button("Tasks " +str(i)+ " "+ to_do_thursday['Todo'].values[i])
                    for i in range(0,len(to_do_thursday.index)):
                        if button_dayThur[i]:
                            to_do_thursday= to_do_thursday.drop(i)
                            to_do_thursday.to_csv('thursday.csv',index=None)
                    
            st.dataframe(to_do_thursday)
        with col5:
            st.markdown("### Friday 🍦")
            st.markdown("""---""")
            st.write("To do |",len(to_do_friday.index)," tasks")

            with st.expander("Add task"):
                    
                    with st.form(key="form5",clear_on_submit=True):
                        MCP_input5 = st.text_input("Enter your Friday task here 👇")
                        vehicle_input5 = st.text_input("Enter your Friday's vehicle here 👇")
                        time_input5 = st.text_input("Enter your Friday's time here 👇")
                        submit_button5 = st.form_submit_button(label="Submit5")
                    if submit_button5:
                        to_do_friday = pd.read_csv('friday.csv',index_col=None)
                        collector5 = ''
                        for k in range(0,len(vehicle_assigning)):
                            if vehicle_assigning['Vehicle ID'].values[k] in vehicle_input5:
                                collector5 += vehicle_assigning['Collector'].values[k]
                        append = {'Todo':MCP_input5,'Vehicle':vehicle_input5,'Collectors':collector5,'Time':time_input5}
                        to_do_friday = to_do_friday.append(append,ignore_index=True)
                        to_do_friday.to_csv('friday.csv',index=None)
                    st.write("Fomula to input task: Name of MCP,ID of Vehicle (from #0000 to #0007)")
                    st.write("Ex: Go to MCP1,#0000")
                    st.write("Remember to delete the placeholder before delete task")

            with st.expander("Remove task"):
                    st.markdown("##### Double-Click the task to remove it from the to do list")
                    button_dayFri = [None] * len(to_do_friday.index)
                    for i in range(0,len(to_do_friday.index)):
                        button_dayFri[i] = st.button("Tasks: " +str(i)+ " "+ to_do_friday['Todo'].values[i])
                    for i in range(0,len(to_do_friday.index)):
                        if button_dayFri[i]:
                            to_do_friday= to_do_friday.drop(i)
                            to_do_friday.to_csv('friday.csv',index=None)    
            st.dataframe(to_do_friday)
    elif choice == "Routes Planning":
        col1,col2,col3,col4,col5 = st.columns(5)
        if os.path.exists('./monday.csv'): 
            monday_task = pd.read_csv('monday.csv', index_col=None)
        if os.path.exists('./tuesday.csv'): 
            tuesday_task = pd.read_csv('tuesday.csv', index_col=None)
        if os.path.exists('./wednesday.csv'): 
            wednesday_task = pd.read_csv('wednesday.csv', index_col=None)
        if os.path.exists('./thursday.csv'): 
            thursday_task = pd.read_csv('thursday.csv', index_col=None)
        if os.path.exists('./friday.csv'): 
            friday_task = pd.read_csv('friday.csv', index_col=None)
        with col1:
            st.markdown("### Monday 🐷")
            st.markdown("""---""")
            graph1 = graphviz.Digraph()

            for i in range(1,len(monday_task)):
                graph1.edge(monday_task['Todo'].values[i-1],monday_task['Todo'].values[i])

            st.graphviz_chart(graph1)
            with st.expander("View Routes"):
                html_string = '<iframe src="https://www.google.com/maps/embed?pb=!1m40!1m12!1m3!1d31355.29001527989!2d106.67006038988386!3d10.779780858424584!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m25!3e0!4m5!1s0x317527c2f8f30911%3A0x36ac5073f8c91acd!2zTGFuZG1hcmsgODEsIDcyMEEgxJBp4buHbiBCacOqbiBQaOG7pywgVmluaG9tZXMgVMOibiBD4bqjbmcsIELDrG5oIFRo4bqhbmgsIFRow6BuaCBwaOG7kSBI4buTIENow60gTWluaCwgVmnhu4d0IE5hbQ!3m2!1d10.794875099999999!2d106.72187149999999!4m5!1s0x31752f16723e26b9%3A0xb02ca15ac61d5a35!2zMTAwIFRy4bqnbiBIxrBuZyDEkOG6oW8sIFBo4bqhbSBOZ8WpIEzDo28sIFF14bqtbiAxLCBUaMOgbmggcGjhu5EgSOG7kyBDaMOtIE1pbmg!3m2!1d10.7660734!2d106.6933469!4m5!1s0x31752ee539ad274d%3A0x55c67faa7644138a!2zMTUzIMSQxrDhu51uZyBOZ3V54buFbiBDaMOtIFRoYW5oLCBQaMaw4budbmcgOSAoUXXhuq1uIDUpLCBRdeG6rW4gNSwgVGjDoG5oIHBo4buRIEjhu5MgQ2jDrSBNaW5o!3m2!1d10.759146099999999!2d106.66614729999999!4m5!1s0x3175293095beb4bb%3A0x7ad6ebf12284bcdd!2zMzQgQ-G7mW5nIEjDsmEsIFBoxrDhu51uZyA0LCBUw6JuIELDrG5oLCBUaMOgbmggcGjhu5EgSOG7kyBDaMOtIE1pbmg!3m2!1d10.8011228!2d106.6601833!5e0!3m2!1svi!2s!4v1670943830438!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
                
                st.markdown(html_string, unsafe_allow_html=True)
                st.write("Click to open bigger: https://goo.gl/maps/CGdEgcxfngjt2zsS7")
        with col2:
            st.markdown("### Tuesday 🐑")
            st.markdown("""---""")
            graph2 = graphviz.Digraph()

            for i in range(1,len(tuesday_task)):
                graph2.edge(tuesday_task['Todo'].values[i-1],tuesday_task['Todo'].values[i])

            st.graphviz_chart(graph2)
            with st.expander("View Routes"):
                html_string = '<iframe src="https://www.google.com/maps/embed?pb=!1m46!1m12!1m3!1d31355.5659447004!2d106.66016018988253!3d10.777132308539617!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m31!3e0!4m5!1s0x31752f133765f339%3A0x99f29a2fa8faa1c!2zSDMgQnVpbGRpbmcsIMSQxrDhu51uZyBIb8OgbmcgRGnhu4d1LCBwaMaw4budbmcgNiwgUXXhuq1uIDQsIFRow6BuaCBwaOG7kSBI4buTIENow60gTWluaA!3m2!1d10.760323399999999!2d106.6990936!4m5!1s0x31752ec17709146b%3A0x54a1658a0639d341!2zMjY4IEzDvSBUaMaw4budbmcgS2nhu4d0LCBwaMaw4budbmcgMTQsIFF14bqtbiAxMCwgVGjDoG5oIHBo4buRIEjhu5MgQ2jDrSBNaW5o!3m2!1d10.772603!2d106.657698!4m5!1s0x31752ed0b789672f%3A0x53dad7885174e4e8!2zMTE0IFTDtCBIaeG6v24gVGjDoG5oLCBQaMaw4budbmcgMTUsIFF14bqtbiAxMCwgVGjDoG5oIHBo4buRIEjhu5MgQ2jDrSBNaW5o!3m2!1d10.7811823!2d106.6696664!4m5!1s0x31752f15a4882f8d%3A0xfff0b1f33162ce58!2zNDUgTmd1eeG7hW4gVGjDoWkgSOG7jWMsIEPhuqd1IMOUbmcgTMOjbmgsIFF14bqtbiAxLCBUaMOgbmggcGjhu5EgSOG7kyBDaMOtIE1pbmg!3m2!1d10.765834199999999!2d106.6963665!4m5!1s0x3175293095beb4bb%3A0x7ad6ebf12284bcdd!2zMzQgxJAuIEPhu5luZyBIw7JhLCBQaMaw4budbmcgNCwgVMOibiBCw6xuaCwgVGjDoG5oIHBo4buRIEjhu5MgQ2jDrSBNaW5oLCBWaeG7h3QgTmFt!3m2!1d10.8011228!2d106.6601833!5e0!3m2!1svi!2s!4v1670943667564!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
                
                st.markdown(html_string, unsafe_allow_html=True)
                st.write("Click to open bigger: https://goo.gl/maps/VV17gv7Rd3SoETfL7")
        with col3:
            st.markdown("### Wednesday 🍮")
            st.markdown("""---""")
            graph3 = graphviz.Digraph()

            for i in range(1,len(wednesday_task)):
                graph3.edge(wednesday_task['Todo'].values[i-1],wednesday_task['Todo'].values[i])

            st.graphviz_chart(graph3)
            with st.expander("View Routes"):
                html_string = '<iframe src="https://www.google.com/maps/embed?pb=!1m46!1m12!1m3!1d31355.77225284069!2d106.6573531398816!3d10.775151608625631!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m31!3e0!4m5!1s0x31752f3dbb8aca31%3A0x8228b5d49e722ad5!2zMTI4IMSQxrDhu51uZyBMw6ogTGFpLCBC4bq_biBUaMOgbmgsIFF14bqtbiAxLCBUaMOgbmggcGjhu5EgSOG7kyBDaMOtIE1pbmg!3m2!1d10.7695273!2d106.6920341!4m5!1s0x3175293095beb4bb%3A0x7ad6ebf12284bcdd!2zMzQgQ-G7mW5nIEjDsmEsIFBoxrDhu51uZyA0LCBUw6JuIELDrG5oLCBUaMOgbmggcGjhu5EgSOG7kyBDaMOtIE1pbmg!3m2!1d10.8011228!2d106.6601833!4m5!1s0x31752ec17709146b%3A0x54a1658a0639d341!2zMjY4IEzDvSBUaMaw4budbmcgS2nhu4d0LCBwaMaw4budbmcgMTQsIFF14bqtbiAxMCwgVGjDoG5oIHBo4buRIEjhu5MgQ2jDrSBNaW5o!3m2!1d10.772603!2d106.657698!4m5!1s0x31752f15a4882f8d%3A0xfff0b1f33162ce58!2zNDUgTmd1eeG7hW4gVGjDoWkgSOG7jWMsIEPhuqd1IMOUbmcgTMOjbmgsIFF14bqtbiAxLCBUaMOgbmggcGjhu5EgSOG7kyBDaMOtIE1pbmg!3m2!1d10.765834199999999!2d106.6963665!4m5!1s0x31752ee539ad274d%3A0x55c67faa7644138a!2zMTUzIE5ndXnhu4VuIENow60gVGhhbmgsIFBoxrDhu51uZyA5IChRdeG6rW4gNSksIFF14bqtbiA1LCBUaMOgbmggcGjhu5EgSOG7kyBDaMOtIE1pbmg!3m2!1d10.759146099999999!2d106.66614729999999!5e0!3m2!1svi!2s!4v1670943922021!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
                
                st.markdown(html_string, unsafe_allow_html=True)
                st.write("Click to open bigger: \https://goo.gl/maps/oC1n5sLhyYACqTvQ8")
        with col4:
            st.markdown("### Thursday 🦄")
            st.markdown("""---""")
            graph4 = graphviz.Digraph()

            for i in range(1,len(thursday_task)):
                graph4.edge(thursday_task['Todo'].values[i-1],thursday_task['Todo'].values[i])

            st.graphviz_chart(graph4)
            with st.expander("View Routes"):
                html_string = '<iframe src="https://www.google.com/maps/embed?pb=!1m40!1m12!1m3!1d31355.29001527989!2d106.67006038988386!3d10.779780858424584!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m25!3e0!4m5!1s0x317527c2f8f30911%3A0x36ac5073f8c91acd!2zTGFuZG1hcmsgODEsIDcyMEEgxJBp4buHbiBCacOqbiBQaOG7pywgVmluaG9tZXMgVMOibiBD4bqjbmcsIELDrG5oIFRo4bqhbmgsIFRow6BuaCBwaOG7kSBI4buTIENow60gTWluaCwgVmnhu4d0IE5hbQ!3m2!1d10.794875099999999!2d106.72187149999999!4m5!1s0x31752f16723e26b9%3A0xb02ca15ac61d5a35!2zMTAwIFRy4bqnbiBIxrBuZyDEkOG6oW8sIFBo4bqhbSBOZ8WpIEzDo28sIFF14bqtbiAxLCBUaMOgbmggcGjhu5EgSOG7kyBDaMOtIE1pbmg!3m2!1d10.7660734!2d106.6933469!4m5!1s0x31752ee539ad274d%3A0x55c67faa7644138a!2zMTUzIMSQxrDhu51uZyBOZ3V54buFbiBDaMOtIFRoYW5oLCBQaMaw4budbmcgOSAoUXXhuq1uIDUpLCBRdeG6rW4gNSwgVGjDoG5oIHBo4buRIEjhu5MgQ2jDrSBNaW5o!3m2!1d10.759146099999999!2d106.66614729999999!4m5!1s0x3175293095beb4bb%3A0x7ad6ebf12284bcdd!2zMzQgQ-G7mW5nIEjDsmEsIFBoxrDhu51uZyA0LCBUw6JuIELDrG5oLCBUaMOgbmggcGjhu5EgSOG7kyBDaMOtIE1pbmg!3m2!1d10.8011228!2d106.6601833!5e0!3m2!1svi!2s!4v1670943830438!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
                
                st.markdown(html_string, unsafe_allow_html=True)
                st.write("Click to open bigger: https://goo.gl/maps/CGdEgcxfngjt2zsS7")
        with col5:
            st.markdown("### Friday 🍦")
            st.markdown("""---""")
            graph5 = graphviz.Digraph()

            for i in range(1,len(friday_task)):
                graph5.edge(friday_task['Todo'].values[i-1],friday_task['Todo'].values[i])

            st.graphviz_chart(graph5)
            with st.expander("View Routes"):
                html_string = '<iframe src="https://www.google.com/maps/embed?pb=!1m46!1m12!1m3!1d31355.5659447004!2d106.66016018988253!3d10.777132308539617!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m31!3e0!4m5!1s0x31752f133765f339%3A0x99f29a2fa8faa1c!2zSDMgQnVpbGRpbmcsIMSQxrDhu51uZyBIb8OgbmcgRGnhu4d1LCBwaMaw4budbmcgNiwgUXXhuq1uIDQsIFRow6BuaCBwaOG7kSBI4buTIENow60gTWluaA!3m2!1d10.760323399999999!2d106.6990936!4m5!1s0x31752ec17709146b%3A0x54a1658a0639d341!2zMjY4IEzDvSBUaMaw4budbmcgS2nhu4d0LCBwaMaw4budbmcgMTQsIFF14bqtbiAxMCwgVGjDoG5oIHBo4buRIEjhu5MgQ2jDrSBNaW5o!3m2!1d10.772603!2d106.657698!4m5!1s0x31752ed0b789672f%3A0x53dad7885174e4e8!2zMTE0IFTDtCBIaeG6v24gVGjDoG5oLCBQaMaw4budbmcgMTUsIFF14bqtbiAxMCwgVGjDoG5oIHBo4buRIEjhu5MgQ2jDrSBNaW5o!3m2!1d10.7811823!2d106.6696664!4m5!1s0x31752f15a4882f8d%3A0xfff0b1f33162ce58!2zNDUgTmd1eeG7hW4gVGjDoWkgSOG7jWMsIEPhuqd1IMOUbmcgTMOjbmgsIFF14bqtbiAxLCBUaMOgbmggcGjhu5EgSOG7kyBDaMOtIE1pbmg!3m2!1d10.765834199999999!2d106.6963665!4m5!1s0x3175293095beb4bb%3A0x7ad6ebf12284bcdd!2zMzQgxJAuIEPhu5luZyBIw7JhLCBQaMaw4budbmcgNCwgVMOibiBCw6xuaCwgVGjDoG5oIHBo4buRIEjhu5MgQ2jDrSBNaW5oLCBWaeG7h3QgTmFt!3m2!1d10.8011228!2d106.6601833!5e0!3m2!1svi!2s!4v1670943667564!5m2!1svi!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
                
                st.markdown(html_string, unsafe_allow_html=True)
                st.write("Click to open bigger: https://goo.gl/maps/VV17gv7Rd3SoETfL7")
    elif choice == "Chat":
        st.markdown("### Chat")
        st.markdown("""---""")  
        st.markdown("### Contact me Tran Trung Nguyen via: https://www.facebook.com/trungnguyen.42")
        st.markdown("### Contact me Mai Minh Nhat via: https://www.facebook.com/zucczucczucc16.8")
    elif choice == "Working status now":
        st.markdown("### Working status now")
        st.markdown("""---""")
        
        # st.markdown("### Mai Minh Nhat")
        col1, col2, col3 = st.columns([3,6,1])

        with col1:
            st.write("")

        with col2:
            st.markdown("### Thursday 🍦, 15/12/2022")
            st.image("status.png", width=800)

        with col3:
            st.write("")
    elif choice == "Logout":
        st.markdown("### Logout")
        st.markdown("""---""")
        st.markdown("### Thank you for using our app")
        st.markdown("### See you again")
        st.markdown("### Bye")
        authenticator.logout("Logout")


import streamlit as st
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import graphviz
st.set_page_config(
page_title = "Urban waste collection aid - UWC 2.0",
page_icon = "Active",
layout = "wide",
initial_sidebar_state='expanded',
)


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
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Urban waste collection aid - UWC 2.0")
    choice = st.radio("Navigation", ["Dashboard","Calendar", "Vehicles","MCP","Tasks Assignment","Routes Planning"])
    st.info("UWC 2.0")

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
            fig2 = go.Figure([go.Bar(x=['Collectors','Janitors'], y=[df['Collectors'].values[0], df['Janitors'].values[0]])])
            st.write(fig2)


        column4,column5= st.columns((3,7))
        with column4:
            st.markdown("### Vehicle status")

            def highlight_survived(s):
                return ['background-color: green']*len(s) if s.Available else ['background-color: red']*len(s)
            st.dataframe(vehicle.style.apply(highlight_survived, axis=1))
        with column5:
            st.markdown("### Assignment")
            fig5 = ff.create_table(wsh)
            st.write(fig5)
            
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
            fig2 = go.Figure([go.Bar(x=['Collectors','Janitors'], y=[df['Collectors'].values[1], df['Janitors'].values[1]])])
            st.write(fig2)


        column9,column10= st.columns((3,7))
        with column9:
            st.markdown("### Vehicle status")

            def highlight_survived(s):
                return ['background-color: green']*len(s) if s.Available else ['background-color: red']*len(s)
            st.dataframe(vehicle.style.apply(highlight_survived, axis=1))
        with column10:
            st.markdown("### Assignment")
            fig5 = ff.create_table(wsh)
            st.write(fig5)
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
            fig2 = go.Figure([go.Bar(x=['Collectors','Janitors'], y=[df['Collectors'].values[2], df['Janitors'].values[2]])])
            st.write(fig2)


        column14,column15= st.columns((3,7))
        with column14:
            st.markdown("### Vehicle status")

            def highlight_survived(s):
                return ['background-color: green']*len(s) if s.Available else ['background-color: red']*len(s)
            st.dataframe(vehicle.style.apply(highlight_survived, axis=1))
        with column15:
            st.markdown("### Assignment")
            fig5 = ff.create_table(wsh)
            st.write(fig5)
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
    st.markdown('### Vehicle')
    col1,col2,col3 = st.columns(3)
    with col1:
        st.markdown('### #MCP1 ')
        st.markdown('#####  268 Ly Thuong Kiet')
        age = st.slider('Capacity', 0, 100, 25)
        st.write( age, '% of the capacity')
    with col2:
        st.markdown('### #MCP2 ')
        st.markdown('#####  114 To Hien Thanh')
        age2 = st.slider('Capacity', 0, 100, 26)
        st.write( age2, '% of the capacity')
    with col3:
        st.markdown('### #MCP1 ')
        st.markdown('#####  153 Nguyen Chi Thanh')
        age3 = st.slider('Capacity', 0, 100, 50)
        st.write( age3, '% of the capacity')
    col4,col5,col6 = st.columns(3)
    with col4:
        st.markdown('### #MCP4 ')
        st.markdown('#####  100 Tran Hung Dao')
        age4 = st.slider('Capacity', 0, 100, 70)
        st.write( age4, '% of the capacity')
    with col5:
        st.markdown('### #MCP5 ')
        st.markdown('#####  45 Nguyen Thai Hoc')
        age5 = st.slider('Capacity', 0, 100, 95)
        st.write( age5, '% of the capacity')
    with col6:
        st.markdown('### #MCP6 ')
        st.markdown('#####  34 Cong Hoa')
        age6 = st.slider('Capacity', 0, 100, 12)
        st.write( age6, '% of the capacity')
elif choice == "Tasks Assignment":

    
    col1 ,col2,col3 = st.columns(3)
    with col1:
        st.markdown('### Vehicle assigning')
        st.dataframe(vehicle_assigning)
    with col2:
        st.markdown('### MCPs assigning')
        st.dataframe(MCP_assigning)
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
                text_input = st.text_input(
                        "Enter your Monday task here 👇",
                        label_visibility=st.session_state.visibility,
                        disabled=st.session_state.disabled
                    )
                if text_input:
                    to_do_monday = pd.read_csv('monday.csv',index_col=None)
                    st.write("You entered: ", text_input)
                    # to_do_monday.loc[len(to_do_monday.index)] = [text_input]
                    to_do1 = ''
                    vehicle1 = ''
                    collector1 = ''
                    i = 0
                    j = 0
                    k = 0  
                    for i in range(0,len(text_input)):
                        if text_input[i] == ',':
                            break
                        to_do1+= text_input[i]
                    
                    for j in range(i+1,len(text_input)):
                        
                        if text_input[j] == ',':
                            break
                        vehicle1 += text_input[j]
                    
                    for k in range(0,len(vehicle_assigning)):
                        if vehicle_assigning['Vehicle ID'].values[k] in vehicle1:
                            collector1 += vehicle_assigning['Collector'].values[k]
                    #t.write(text_input[i],text_input[j], text_input[k])
                    append = {'Todo':to_do1,'Vehicle':vehicle1,'Collectors':collector1}
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
                text_input2 = st.text_input(
                        "Enter your Tuesday task here 👇",
                        label_visibility=st.session_state.visibility,
                        disabled=st.session_state.disabled
                    )
                if text_input2:
                    to_do_tuesday = pd.read_csv('tuesday.csv',index_col=None)
                    st.write("You entered: ", text_input2)
                    # to_do_monday.loc[len(to_do_monday.index)] = [text_input]
                    to_do2 = ''
                    vehicle2 = ''
                    collector2 = ''
                    i = 0
                    j = 0
                    k = 0  
                    for i in range(0,len(text_input2)):
                        if text_input2[i] == ',':
                            break
                        to_do2+= text_input2[i]
                    
                    for j in range(i+1,len(text_input2)):
                        
                        if text_input2[j] == ',':
                            break
                        vehicle2 += text_input2[j]
                    
                    for k in range(0,len(vehicle_assigning)):
                        if vehicle_assigning['Vehicle ID'].values[k] in vehicle2:
                            collector2 += vehicle_assigning['Collector'].values[k]
                    #t.write(text_input[i],text_input[j], text_input[k])
                    append = {'Todo':to_do2,'Vehicle':vehicle2,'Collectors':collector2}
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
                text_input3 = st.text_input(
                        "Enter your wednesday task here 👇",
                        label_visibility=st.session_state.visibility,
                        disabled=st.session_state.disabled
                    )
                if text_input3:
                    to_do_wednesday = pd.read_csv('wednesday.csv',index_col=None)
                    st.write("You entered: ", text_input3)
                    # to_do_monday.loc[len(to_do_monday.index)] = [text_input]
                    to_do3 = ''
                    vehicle3 = ''
                    collector3 = ''
                    i = 0
                    j = 0
                    k = 0  
                    for i in range(0,len(text_input3)):
                        if text_input3[i] == ',':
                            break
                        to_do3+= text_input3[i]
                    
                    for j in range(i+1,len(text_input3)):
                        
                        if text_input3[j] == ',':
                            break
                        vehicle3 += text_input3[j]
                    
                    for k in range(0,len(vehicle_assigning)):
                        if vehicle_assigning['Vehicle ID'].values[k] in vehicle3:
                            collector3 += vehicle_assigning['Collector'].values[k]
                    #t.write(text_input[i],text_input[j], text_input[k])
                    append = {'Todo':to_do3,'Vehicle':vehicle3,'Collectors':collector3}
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
                text_input4 = st.text_input(
                        "Enter your thursday task here 👇",
                        label_visibility=st.session_state.visibility,
                        disabled=st.session_state.disabled
                    )
                if text_input4:
                    to_do_thursday = pd.read_csv('thursday.csv',index_col=None)
                    st.write("You entered: ", text_input4)
                    # to_do_monday.loc[len(to_do_monday.index)] = [text_input]
                    to_do4 = ''
                    vehicle4 = ''
                    collector4 = ''
                    i = 0
                    j = 0
                    k = 0  
                    for i in range(0,len(text_input4)):
                        if text_input4[i] == ',':
                            break
                        to_do4+= text_input4[i]
                    
                    for j in range(i+1,len(text_input4)):
                        
                        if text_input4[j] == ',':
                            break
                        vehicle4 += text_input4[j]
                    
                    for k in range(0,len(vehicle_assigning)):
                        if vehicle_assigning['Vehicle ID'].values[k] in vehicle4:
                            collector4 += vehicle_assigning['Collector'].values[k]
                    #t.write(text_input[i],text_input[j], text_input[k])
                    append = {'Todo':to_do4,'Vehicle':vehicle4,'Collectors':collector4}
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
                text_input5 = st.text_input(
                        "Enter your friday task here 👇",
                        label_visibility=st.session_state.visibility,
                        disabled=st.session_state.disabled
                    )
                if text_input5:
                    to_do_friday = pd.read_csv('friday.csv',index_col=None)
                    st.write("You entered: ", text_input5)
                    # to_do_monday.loc[len(to_do_monday.index)] = [text_input]
                    to_do5 = ''
                    vehicle5 = ''
                    collector5 = ''
                    i = 0
                    j = 0
                    k = 0  
                    for i in range(0,len(text_input5)):
                        if text_input5[i] == ',':
                            break
                        to_do5+= text_input5[i]
                    
                    for j in range(i+1,len(text_input5)):
                        
                        if text_input5[j] == ',':
                            break
                        vehicle5 += text_input5[j]
                    
                    for k in range(0,len(vehicle_assigning)):
                        if vehicle_assigning['Vehicle ID'].values[k] in vehicle5 :
                            collector5 += vehicle_assigning['Collector'].values[k]
                    #t.write(text_input[i],text_input[j], text_input[k])
                    append = {'Todo':to_do5,'Vehicle':vehicle5,'Collectors':collector5}
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
    with col2:
        st.markdown("### Tuesday 🐑")
        st.markdown("""---""")
        graph2 = graphviz.Digraph()

        for i in range(1,len(tuesday_task)):
            graph2.edge(tuesday_task['Todo'].values[i-1],tuesday_task['Todo'].values[i])

        st.graphviz_chart(graph2)
    with col3:
        st.markdown("### Wednesday 🍮")
        st.markdown("""---""")
        graph3 = graphviz.Digraph()

        for i in range(1,len(wednesday_task)):
            graph3.edge(wednesday_task['Todo'].values[i-1],wednesday_task['Todo'].values[i])

        st.graphviz_chart(graph3)
    with col4:
        st.markdown("### Thursday 🦄")
        st.markdown("""---""")
        graph4 = graphviz.Digraph()

        for i in range(1,len(thursday_task)):
            graph4.edge(thursday_task['Todo'].values[i-1],thursday_task['Todo'].values[i])

        st.graphviz_chart(graph4)
    with col5:
        st.markdown("### Friday 🍦")
        st.markdown("""---""")
        graph5 = graphviz.Digraph()

        for i in range(1,len(friday_task)):
            graph5.edge(friday_task['Todo'].values[i-1],friday_task['Todo'].values[i])

        st.graphviz_chart(graph5)

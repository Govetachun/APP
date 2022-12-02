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
st.set_page_config(
page_title = "Real-Time Data Dashboard",
page_icon = "Active",
layout = "wide",
)
with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("UWC for task assignment")
    choice = st.radio("Navigation", ["Upload","Dashboard","Calendar", "MCP","Tasks Assignment","Routes Planning"])
    st.info("UWC")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

elif choice == "Dashboard":
    st.title("Dashboard for the work day")
    col1, col2, col3 = st.columns(3)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    with col1:
        st.info("Current status of garbage trucks in Morning")
        colors = ['gold', 'mediumturquoise', 'darkorange']
        value = df[:3].values[0]
        fig = go.Figure(data=[go.Pie(labels=['In use','In use','Available','In maintenance'], values=value)])
        fig.update_traces(hoverinfo='label+percent', textinfo='label+value', textfont_size=15,
                    marker=dict(colors=colors, line=dict(color='#000000', width=3)))

        st.write(fig)
        df1 = pd.DataFrame()
        fig2 = ff.create_table(df1)
        teams=['Morning']
        y1 = [df['Collectors'].values[0]]
        y2 = [df['Janitors'].values[0]]
        trace1 = go.Bar(x=teams, y=y1, xaxis='x2', yaxis='y2',
                marker=dict(color='#0099ff'),
                name='Collectors')
        trace2 = go.Bar(x=teams, y=y2, xaxis='x2', yaxis='y2',
                marker=dict(color='#404040'),
                name='Janitors')
        fig2.add_traces([trace1, trace2])
        fig2['layout']['xaxis2'] = {}
        fig2['layout']['yaxis2'] = {}
        fig2.layout.yaxis2.update({'anchor': 'x2'})
        fig2.layout.xaxis2.update({'anchor': 'y2'})
        fig2.layout.yaxis2.update({'title': 'people'})

        st.write(fig2)

        st.info("Assignment")
        st.dataframe(wsh)

        st.info("MCPs list")
        fig3 = px.bar(cap,x="MCP",y="count",color="status", title="MCPs list status in Morning")
        st.write(fig3)


    with col2:
        st.info("Current status of garbage trucks in Afternoon")
        colors = ['red', 'green', 'blue']
        value = df[:3].values[1]
        fig = go.Figure(data=[go.Pie(labels=['In use','In use','Available','In maintenance'], values=value)])
        fig.update_traces(hoverinfo='label+percent', textinfo='label+value', textfont_size=15,
                    marker=dict(colors=colors, line=dict(color='#000000', width=3)))

        st.write(fig)
        df1 = pd.DataFrame()
        fig2 = ff.create_table(df1)
        teams=['Afternoon']
        y1 = [df['Collectors'].values[1]]
        y2 = [df['Janitors'].values[1]]
        trace1 = go.Bar(x=teams, y=y1, xaxis='x2', yaxis='y2',
                marker=dict(color='#0099ff'),
                name='Collectors')
        trace2 = go.Bar(x=teams, y=y2, xaxis='x2', yaxis='y2',
                marker=dict(color='#404040'),
                name='Janitors')
        fig2.add_traces([trace1, trace2])
        fig2['layout']['xaxis2'] = {}
        fig2['layout']['yaxis2'] = {}
        fig2.layout.yaxis2.update({'anchor': 'x2'})
        fig2.layout.xaxis2.update({'anchor': 'y2'})
        fig2.layout.yaxis2.update({'title': 'people'})

        st.write(fig2)

        st.info("Assignment")
        st.dataframe(wsh)
        
        st.info("MCPs list")
        fig3 = px.bar(cap,x="MCP",y="count",color="status", title="MCPs list status in Afternoon")
        st.write(fig3)
    with col3:
        st.info("Current status of garbage trucks in Evening")
        colors = ['lightgreen','goldenrod',"magenta"]
        value = df[:3].values[2]
        fig = go.Figure(data=[go.Pie(labels=['In use','In use','Available','In maintenance'], values=value)])
        fig.update_traces(hoverinfo='label+percent', textinfo='label+value', textfont_size=15,
                    marker=dict(colors=colors, line=dict(color='#000000', width=3)))

        st.write(fig)
        df1 = pd.DataFrame()
        fig2 = ff.create_table(df1)
        teams=['Evening']
        y1 = [df['Collectors'].values[2]]
        y2 = [df['Janitors'].values[2]]
        trace1 = go.Bar(x=teams, y=y1, xaxis='x2', yaxis='y2',
                marker=dict(color='#0099ff'),
                name='Collectors')
        trace2 = go.Bar(x=teams, y=y2, xaxis='x2', yaxis='y2',
                marker=dict(color='#404040'),
                name='Janitors')
        fig2.add_traces([trace1, trace2])
        fig2['layout']['xaxis2'] = {}
        fig2['layout']['yaxis2'] = {}
        fig2.layout.yaxis2.update({'anchor': 'x2'})
        fig2.layout.xaxis2.update({'anchor': 'y2'})
        fig2.layout.yaxis2.update({'title': 'people'})

        st.write(fig2)

        st.info("Assignment")
        st.dataframe(wsh)
        
        st.info("MCPs list")
        fig3 = px.bar(cap,x="MCP",y="count",color="status", title="MCPs list status in Evening")
        st.write(fig3)
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
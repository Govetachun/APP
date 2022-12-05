import csv
def today():
    header = ['Time', 'In use', 'Available', 'In maintenance','Collectors','Janitors']
    data = [
        ['Morning', 3, 4, 5,3,12],
        ['Afternoon', 4, 2, 6, 4, 14],
        ['Evening', 3, 5, 4, 3, 10]
    ]

    with open('today.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
today()

def workshift():
    header = ['Vehicle', 'Collector', 'MCP', 'Jantitor 1','Janitor 2','Janitor 3']
    data = [
        ['#1234', 'Nguyen Van A','MCP 1','Tran Van A','Tran Van B','Tran Thi X'],
        ['#0001', 'Nguyen Van B','MCP 2','Tran Van C','Tran Van D','Tran Thi Y'],
        ['#0004', 'Nguyen Van C','MCP 3','Tran Van E','Tran Van F','Tran Thi Z'],
        ['#0005', 'Nguyen Van G','MCP 4','Tran Van E','Tran Van F','Tran Thi Z'],
        ['#0006', 'Nguyen Van H','MCP 5','Tran Van E','Tran Van F','Tran Thi Z'],
        ['#0007', 'Nguyen Van I','MCP 6','Tran Van E','Tran Van F','Tran Thi Z']
    ]

    with open('workshift.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
workshift()
def capacity():
    header = ['MCP', 'status','count']
    data = [
        ['MCP 1', 'Full',4],
        ['MCP 1', 'Available',16],
        ['MCP 2', 'Full',5],
        ['MCP 2', 'Available',15],
        ['MCP 3', 'Full',19],
        ['MCP 3', 'Available',6],
        ['MCP 4', 'Full',10],
        ['MCP 4', 'Available',10],
        ['MCP 5', 'Full',12],
        ['MCP 5', 'Available',18],
    ]

    with open('capacity.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
capacity()
def routes1():
    header = [ 'A','B']
    data = [
        [ 'Quan 1','Quan 2'],
        [ 'Quan 2','Quan 3'],
        [ 'Quan 3', 'Quan 5'],
        [ 'Quan 5','Quan 12'],
        [ 'Quan 12','Quan 4'],
        [ 'Quan 4','Quan 1']
    ]

    with open('routes1.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
routes1()
def routes2():
    header = [ 'A','B']
    data = [
        [ 'Quan 1','Quan 2'],
        [ 'Quan 2','Quan 3'],
        [ 'Quan 3', 'Quan 5'],
        [ 'Quan 5','Quan 12'],
        [ 'Quan 12','Quan 1'],
    ]

    with open('routes2.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
routes2()

def routes3():
    header = [ 'A','B']
    data = [
        [ 'Quan 1','Quan 2'],
        [ 'Quan 2','Quan 3'],
        [ 'Quan 3', 'Quan 5'],
    ]

    with open('routes3.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
routes3()
def vehicle():
    header = [ 'ID','Available','Current location']
    data = [
        [ '#1234',1,'MCP 1'],
        [ '#0001',1,'MCP 3'],
        [ '#0004',0, 'MCP 5'],
        [ '#2345', 1,'MCP 1'],
        [ '#3456',0, 'Station 3'],
        [ '#4567',0, 'Station 11'],
        [ '#5678',1, 'Station 5'],
        [ '#9787',0, 'MCP 2'],
    ]

    with open('vehicle.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
vehicle()

def vehicle_assigning():
    header = [ 'Vehicle ID','Collector']
    data = [
        [ '#0000','Nguyen Van A'],
        [ '#0001','Nguyen Van B'],
        [ '#0002', 'Nguyen Van C'],
        [ '#0003', 'Nguyen Van D'],
        [ '#0004', 'Nguyen Van E'],
        [ '#0005', 'Nguyen Van F'],
        [ '#0006', 'Nguyen Van G'],
        [ '#0007', 'Nguyen Van H'],
    ]

    with open('vehicle_assigning.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
vehicle_assigning()
def MCP_assigning():
    header = [ 'MCP ID','Janitor 1', 'Janitor 2']
    data = [
        [ 'MCP 1','Nguyen Van A','Tran Van A'],
        [ 'MCP 2','Nguyen Van B','Tran Van B'],
        [ 'MCP 3', 'Nguyen Van C','Tran Van C'],
        [ 'MCP 4', 'Nguyen Van D','Tran Van D'],
        [ 'MCP 5', 'Nguyen Van E','Tran Van E'],
        [ 'MCP 6', 'Nguyen Van F','Tran Van F'],
        [ 'MCP 7', 'Nguyen Van F','Tran Van F'],
        [ 'MCP 8', 'Nguyen Van F','Tran Van F'],
    ]

    with open('MCP_assigning.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
MCP_assigning()
import pandas as pd
def create_dataframe(days):
    dict = {'Todo':[],
            'Vehicle':[],
            'Collectors':[]}
    df_day = pd.DataFrame(dict)
    df_day.to_csv(days+'.csv',index=None)
    return df_day
    
monday = 'monday'
tuesday = 'tuesday'
wednesday = 'wednesday'
thursday = 'thursday'
friday = 'friday'
to_do_monday = create_dataframe(monday)
to_do_tuesday = create_dataframe(tuesday)
to_do_wednesday= create_dataframe(wednesday)
to_do_thursday = create_dataframe(thursday)
to_do_friday = create_dataframe(friday)
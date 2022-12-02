import csv

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

header = ['Vehicle', 'Collector', 'MCP', 'Jantitor 1','Janitor 2']
data = [
    ['#1234', 'Nguyen Van A','MCP 1','Tran Van A','Tran Van B'],
    ['#0001', 'Nguyen Van B','MCP 2','Tran Van C','Tran Van D'],
    ['#0004', 'Nguyen Van C','MCP 3','Tran Van E','Tran Van F']
]

with open('workshift.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

header = ['MCP', 'status','count']
data = [
    ['MCP 1', 'Full',4],
    ['MCP 1', 'Available',16],
    ['MCP 2', 'Full',5],
    ['MCP 2', 'Available',15],
    ['MCP 3', 'Full',19],
    ['MCP 3', 'Available',1],
]

with open('capacity.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

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
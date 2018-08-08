alient_0 = {'color': 'green', 'points': 5}
alient_1 = {'color': 'red', 'points': 15}
alient_2 = {'color': 'white', 'points': 25}
alient = [alient_0, alient_1, alient_2]
print(alient_0['color'])
alient_0['x_pos'] = 0
alient_0['y_pos'] = 25
print(alient_0)
del alient_0['points']
print(alient_0)
print(alient)

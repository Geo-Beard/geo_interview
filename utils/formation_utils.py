import csv


def formation_dict_maker(data_file_path):
    formations_dict = {}
    with open(data_file_path, 'r') as file:
        next(file)
        fields = ['biozone', 'top_m', 'base_m']
        for row in csv.DictReader(file, fieldnames=fields):
            formations_dict[row['biozone']] = [float(row['top_m']),
                                               float(row['base_m'])]
    return formations_dict


def formation_midpoint_maker(formation_dict):
    formation_midpoints = []
    for key, value in formation_dict.items():
        formation_midpoints.append(value[0] + (value[1]-value[0])/2)
    return formation_midpoints

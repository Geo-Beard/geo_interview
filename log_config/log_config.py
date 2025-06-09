def build_config(well):
    config = {}
    for log_name in well.head(0):
        # if log_name == 'M__DEPTH':
        #     config[log_name] = {"data": well[log_name]}
        if log_name == 'GR':
            config[log_name] = {"data": well[log_name],
                                "xlim": (0, 150),
                                "xticks": [0, 50, 100, 150],
                                "color": "green"}
        if log_name == 'ILM':
            config[log_name] = {"data": well[log_name],
                                "xlim": (0.2, 2000),
                                "xticks": [0.1, 1, 10, 100, 1000],
                                "color": "red"}
        if log_name == 'ILD':
            config[log_name] = {"data": well[log_name],
                                "xlim": (0.2, 2000),
                                "xticks": [0.1, 1, 10, 100, 1000],
                                "color": "blue"}
        if log_name == 'LL8':
            config[log_name] = {"data": well[log_name],
                                "xlim": (0.2, 2000),
                                "xticks": [0.1, 1, 10, 100, 1000],
                                "color": "green"}
        if log_name == 'NPHI':
            config[log_name] = {"data": well[log_name],
                                "xlim": (1.95, 2.95),
                                "xticks": [1.95, 2.45, 2.95],
                                "color": "red"}
        if log_name == 'RHOB':
            config[log_name] = {"data": well[log_name],
                                "xlim": (45, -15),
                                "xticks": [45, 15, -15],
                                "color": "blue"}
    return config

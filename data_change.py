def data_assign(data,data1):
    # for d1 in data1.items():
    #     print(d1)
    # print("\n")
    # for d in data:
    #     print(d)
    for d1 in data1.items():
        for d in data:
            if d1[0]==d['name']:
                for col in (d['columns']):
                    print(col['name'])
                    print(d1)
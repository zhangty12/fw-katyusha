
def data_params(filename):
    y = []
    X = []
    for line in open(filename, 'r').readlines():
        features = line.split()
        y.append(int(features[0]))
        data = []
        for field in features[1:]:
            tmp = field.split(':')
            data.append((int(tmp[0]), float(tmp[1])))
    return X, y

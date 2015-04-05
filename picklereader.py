import pickle, os

# Defines (should be set in a conf file)
iwd_data_path = 'signaldata/'
result_data_path = 'result/'
pickle_data_ext = '.pkl'

def save_obj(obj, name, path = iwd_data_path):
    if not name.endswith(pickle_data_ext): name = name + pickle_data_ext
    joinedpath =  os.path.abspath(os.path.join(path,name))
    print joinedpath
    with open(joinedpath, 'wb') as filehandle:
        pickle.dump(obj, filehandle, pickle.HIGHEST_PROTOCOL)
    print "CREATE", name, "has successfully been created in", path

def load_obj(name, path = iwd_data_path):
    data = []
    if not name.endswith(pickle_data_ext): name = name + pickle_data_ext
    joinedpath =  os.path.abspath(os.path.join(path,name))
    print joinedpath
    try:
        with open(joinedpath, 'rb') as filehandle:
            data = pickle.load(filehandle)
    except IOError:
        return False
    print "READ", name, "has succesfully been read from", path
    return data
        
def result_read(name):
    try:
        with open(result_data_path + name + ".txt", "r") as filehandle:
            return filehandle.read()
    except IOError:
        return False
        
def result_write(name, data):
    with open(result_data_path + name + '.txt', 'wb') as filehandle:
        filehandle.write(data)
    print "CREATE", name, "has successfully been created in", result_data_path
import os



def get_files(ipath):
    sfiles= []
    for (root,dirs,files) in os.walk(ipath, topdown=True):
        for file in files:
            if '.wav' in file:
                sfile = root +'\\'+ file
                sfiles.append(sfile)
    return sfiles



parth =''
files = get_files(parth)
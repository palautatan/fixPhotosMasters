# FINDS DIRECTORIES
def listdirz(path):
	'''
	Input:		path: Path of Photos Library Masters folder, i.e. "/Users/USER/Desktop/Masters"
					nested: Boolean; True to lok forward one step up in the directories
	Output: Files within one level of the Masters folder directory
	Dependencies:	Libraries: os
							Functions: listdir_nh()
	'''
    files = [item for sublist in [path+"/"+str(x) for x in listdir_nh(path)] for item in sublist]
    return files



# FINDS ALL DIRECTORIES IN MASTERS FOLDER
def recursivedirz(path):
	'''
	Input: Path of Photos Library Masters folder, i.e. "/Users/USER/Desktop/Masters"
	Output: All files (photos, videos) within the given Masters folder
	Dependencies:	Libraries: os
							Functions: listdir_nh(), listdirz()
	'''
    files = [listdirz(x) for x in [listdirz(x) for x in [listdirz(x) for x in [listdirz(x) for x in listdirz(path)]]]]
    return files
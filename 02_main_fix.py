# EDIE ESPEJO
# CLEAN IPHOTO MASTERS
# 2017-06-27


# INPUT: A "MASTERS" FOLDER FROM A PHOTOS LIBRARY PACKAGE (MAC)
# OUTPUT: FOLDERS MATCHING THE FORMAT YYYY-MM-DD
# PURPOSE: CONVERTS FOLDERS PER SECOND TO FOLDERS PER DAY


# FUTURE:		main():				1. Check for efficiency difference between if not folder exists and try/except
#											2. Way to vectorize the creation of folders
#											3. Make importable to command line or as an executable
#					recursivedirz():	Check for another way to kill the sublists


# LISTDIR_NH FUNCTION
def listdir_nh(path):
    '''
    Input: Path of directory (string)
    Output: Non-hidden files within given directory (list of strings)
    Dependencies: os Library
    '''
    from os import listdir
    files = listdir(path)
    parsed = [file for file in files if not file.startswith(".")]
    return parsed



# FINDS DIRECTORIES
def listdirz(path):
	'''
	Input: Path of Photos Library Masters folder, i.e. "/Users/USER/Desktop/Masters"
	Output: Files within one level of the Masters folder directory
	Dependencies:	Libraries: os
							Functions: listdir_nh()
	'''
    start = path+"/"
    files = [start+str(x) for x in listdir_nh(path)]
    return files



# FINDS ALL DIRECTORIES IN MASTERS FOLDER
def recursivedirz(path):
	'''
	Input: Path of Photos Library Masters folder, i.e. "/Users/USER/Desktop/Masters"
	Output: All files (photos, videos) within the given Masters folder
	Dependencies:	Libraries: os
							Functions: listdir_nh(), listdirz()
	'''
    years = listdirz(path)
    months = [x for x in [listdirz(x) for x in years]]
    unlisted_months = [item for sublist in months for item in sublist]
    days = [listdirz(x) for x in unlisted_months]
    unlisted_days = [item for sublist in days for item in sublist]
    final_folders = [listdirz(x) for x in unlisted_days]
    unlisted_final_folders = [item for sublist in final_folders for item in sublist]
    all_photos = [listdirz(x) for x in unlisted_final_folders]
    return([item for sublist in all_photos for item in sublist])

# MAIN FUNCTION
def main(path, new_location):
	'''
	Input: 	path: Path of Photos Library Masters folder, i.e. "/Users/USER/Desktop/Masters"
				new_location: Path of desired new location, i.e. "/Users/USER/Pictures"
	Output: No file output -- reformats Masters folder
	Dependencies: 	Libraries: os
							Functions: listdir_nh(), listdirz(), recursivedirz()
	'''
    # ACQUIRE ALL FILE NAMES IN THE MASTERS FOLDER
    all_files = recursivedirz(path)
    folders_created = []
    
    # FOR EACH NAMED FILE IN MASTERS FOLDER
    for this_file in all_files:
    	# OBTAIN DOWNLOAD DATE
		yyyymmdd = this_file.split("/")[-2].split("-")[0]
		folder_name = "-".join([yyyymmdd[0:4], yyyymmdd[4:6], yyyymmdd[6:8]])
		folder_name = new_location+"/"+folder_name
		
		# TRY TO MAKE THE FOLDER
        try:
            os.makedirs(folder_name)
            folders_created.append(folder_name)
        except:
            print("The folder named"+folder_name+" exists. This program will continue to reformat the Masters folder.")
        # SAVE FILE BY ITS FILENAME UNDER A FOLDER WITH FORMAT YYYY-MM-DD
        filename = this_file.split("/")[-1]
        os.rename(this_file, folder_name+"/"+filename)
    
    # PRINT SUMMARY
    print(str(len(folders_created))+" were created under "+new_location+".")
    print("Folders: " + "\n".join(folders_created))
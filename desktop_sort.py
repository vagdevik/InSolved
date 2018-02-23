import os

def get_files(dir):
	dir_files = []
	subdirs = [x[0] for x in os.walk(dir)]
	for subdir in subdirs:
		files = os.walk(subdir).next()[2]
		if (len(files) > 0):
			for file in files:
				dir_files.append(subdir + "/" + file)
	return dir_files

def desktop_sort(source, target_folder, Files):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    folders = []
    for f in Files:
        extension = f.split('.')[-1]
        if not extension in folders and extension != 'desktop':
            folders.append(extension)
            path = target_folder + '/' + str(extension)
            if not os.path.exists(path):
                os.makedirs(path)
        if extension!='desktop':
            des = target_folder + '/' + extension
            os.popen('cp '+ f + ' ' + des)

source = '/Desktop/source'
target_folder = '/Documents/target_folder'
Files = get_files(source)
desktop_sort(source, target_folder, Files)

import os

directories = ['Desktop', 'Documents', 'Downloads', 'Music']

def get_files(dir):
	dir_files = []
	subdirs = [x[0] for x in os.walk(dir)]
	for subdir in subdirs:
		files = os.walk(subdir).next()[2]
		if (len(files) > 0):
			for file in files:
				dir_files.append(subdir + "/" + file)
	return dir_files

def retrieve_files(directories):
    global filewise_sizes
    files = []
    file_sizes = []
    for directory in directories:
        file_list = get_files(directory)
        file_size_list = []
        for f in file_list:
            file_size = os.stat(f).st_size/(1048576.0)
            file_size_list.append(file_size)
        files += file_list
        file_sizes += file_size_list
    filewise_sizes = zip(file_sizes, files)
    filewise_sizes.sort()
    return filewise_sizes[::-1]

first_N = 4
filewise_sizes = retrieve_files(directories)
for i in range(first_N):
	file_name = filewise_sizes[i][1]
	size = filewise_sizes[i][0]
	print file_name, size

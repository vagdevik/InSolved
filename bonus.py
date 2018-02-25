import os
import humanize

def get_size(filename):
    st = os.stat(filename)
    return st.st_size

def list_files(dir):
	r = []
	subdirs = [x[0] for x in os.walk(dir)]
	for subdir in subdirs:
		files = os.walk(subdir).next()[2]
		if (len(files) > 0):
			for file in files:
				r.append(subdir + "/" + file)
	return r

def get_folderwise_sizes(list_of_directories):
	global folder_sizes_in_bytes, folder_sizes
	folder_sizes_in_bytes = []
	folder_sizes = []
	for folder in list_of_directories:
		size = 0
		dir_files = list_files(folder)
		for f in dir_files:
			size += get_size(f)
		folder_sizes_in_bytes.append(size)
		size_in_MB = humanize.naturalsize(size)
		folder_sizes.append(size_in_MB)
#	print folder_sizes

def get_typewise_sizes(list_of_directories):
	global out
	out = []
	for folder in list_of_directories:
		files_type_sizes = {}
		dir_files = list_files(folder)
		for f in dir_files:
			if len(f.split('/')[-1].split('.')) != 1:
				extension = f.split('.')[-1]
				if not extension in files_type_sizes and extension != 'desktop' :
					files_type_sizes[str(extension)] = 0
				if extension != 'desktop':
					files_type_sizes[str(extension)]+=get_size(f)
		out.append(files_type_sizes)
	for folder in out:
		for typ in folder:
			folder[typ] = humanize.naturalsize(folder[typ])
	
list_of_directories = ['/home/abhishek/Desktop']
get_folderwise_sizes(list_of_directories)
get_typewise_sizes(list_of_directories)
count = 0
for folder in out:
    length = ' |  Folder: ' + str(list_of_directories[count]) + ' | ' + folder_sizes[count]
    print '-'*len(length)
    print length
    print '-'*len(length)
    maximum = 0
    for typ in folder:
        if len(typ) > maximum:
            maximum = len(typ)
    maximum += 4
    for typ in folder:
        l = maximum - len(typ)
        print ' |  ' + typ + ' '*l + '|' + '  ' + str(folder[typ])
    print '-'*len(length)

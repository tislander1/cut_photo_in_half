from PIL import Image
from os import listdir, makedirs
from os.path import isfile, join, exists
mypath = 'photos'
filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def add_suffix_to_filename(filename, suffix):
    #get two file names (left and right)
    filename_with_suffix = filename.split('.')
    filename_with_suffix.insert(-1, '_' + suffix)
    filename_with_suffix = ''.join(filename_with_suffix[0:-1]) + '.' + filename_with_suffix[-1]
    return filename_with_suffix

for filename in filenames:
    im = Image.open(mypath + '/' + filename)
    full_width, height = im.size
    half_width = full_width//2
    im_left = im.crop((0, 0, half_width, height))
    im_right = im.crop((half_width, 0, full_width, height))

    #get two file names (left and right)
    filename_left = add_suffix_to_filename(filename, 'left')
    filename_right = add_suffix_to_filename(filename, 'right')
    if not exists(mypath + '/output/'):
        makedirs(mypath + '/output/')

    im_left.save(mypath + '/output/' + filename_left)
    im_right.save(mypath + '/output/' + filename_right)
    x = 2
x = 2
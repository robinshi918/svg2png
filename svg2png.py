import os
import os
import shutil
import sys
import getopt

TARGET_SIZE = [100, 200, 300]
INKSCAPE = '/usr/local/bin/inkscape '
SRC_FOLDER = '/Users/yunshi/work/iconlibrary'
TARGET_BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))


def append_path_separator(folder_path):
    if str(folder_path).endswith('/'):
        return folder_path
    else:
        return folder_path + '/'

def get_svg_in_folder(folder_name):
    if os.path.exists(folder_name):
        svg_files = [f for f in os.listdir(folder_name) if os.path.isfile(os.path.join(folder_name, f)) and str(f).lower().endswith('svg')]
        print svg_files
        print len(svg_files)
        return svg_files
    else:
        print "folder", folder_name, " not exist"

def convert(size, src_file):
    '''
    convert a single svg to png for given size
    '''
    target_folder = os.path.join(TARGET_BASE_FOLDER, str(size))
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    base_name = os.path.splitext(src_file)[0]
    target_file_name = append_path_separator(target_folder) + base_name + ".png"
    src_file_name = append_path_separator(SRC_FOLDER) + src_file
    cmdline = INKSCAPE + "--export-png " + target_file_name + " -w " + str(size) + " " + src_file_name

    print "CONVERTING", src_file, "--->", target_file_name
    os.system(cmdline)

def cleanup():
    for s in TARGET_SIZE:
        target_folder = append_path_separator(TARGET_BASE_FOLDER) + str(s)
        if os.path.exists(target_folder):
            shutil.rmtree(target_folder)

def convert_all():
    cleanup()
    file_list = get_svg_in_folder(SRC_FOLDER)
    for f in file_list:
        for s in TARGET_SIZE:
            convert(s, f)

def print_help():
    print 'Usage: svg2png.py -i <src_folder> -s <output_size_array> [-o <output_folder>]'
    print '    -i        source folder that contains the svg files'
    print '    -s        target size array'
    print '    -o        output folder'
    print '              [Optional]if not provided, output is set to current folder where'
    print '              this script locates'
    print '    -h        print this help'
    print '\nexample:'
    print '    python svg2png.py -i /Users/shiyun/iconlibrary -s 100,200,300 -o .'
    print '    Command reads all svg files from folder /Users/shiyun/iconlibrary, convert'
    print '    into 3 different target dimensions and save into separate folders. '
    print '    Target folders(./100/, ./200/ and ./300/) are created under current folder(.)'
    print "\nATTENTION: This script requires 'inkscape' to do the real conversion. "
    print "Please install 'inkscape' before running this script"
    print "HOW-TO install 'inkscape' by Homebrew. Note: Installation of 'inkscape' may"
    print "take 20 min, so please be patient."
    print "    brew install caskformula/caskformula/inkscape"

########################################################################
########################################################################

def main(argv):
    global TARGET_SIZE
    global SRC_FOLDER
    global TARGET_BASE_FOLDER
    src_folder = ''
    size_array = ''
    target_folder = ''
    try:
        opts, args = getopt.getopt(argv,"hi:s:o:")
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-i"):
            print '-i'
            print arg
            src_folder = str(arg).strip()
        elif opt in ("-s"):
            print '-s'
            print arg
            size_array = str(arg).strip()
        elif opt in ("-o"):
            target_folder = str(arg).strip()
            TARGET_BASE_FOLDER = target_folder
        else:
            print_help()
            sys.exit()
    
    if src_folder == '' or size_array == '':
        print_help()
        sys.exit()
    
    TARGET_SIZE = size_array.split(',')
    SRC_FOLDER = src_folder
    # print 'source folder is "' + str(SRC_FOLDER)
    # print 'size array is "' + str(TARGET_SIZE)
    # print 'target_base_folder' + TARGET_BASE_FOLDER

    convert_all()

if __name__ == "__main__":
    main(sys.argv[1:])

print '\n\n===============CONVERT DONE===============\n\n'


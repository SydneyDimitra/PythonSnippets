"""
Script to rename files based on pattern.
test_string = "ab_1010v01.pdf"
renaming to: "ab_1010_v01.pdf"
"""
def get_new_filename(filename):
    """Rename file."""
    import re
    pattern = "(?P<prefix>[A-Za-z]{2}_[0-9]{4,5})(?P<suffix>v[0-9].*)"
    match = re.match(pattern, filename)
    if match:
        new_name = match.group('prefix') + '_' + match.group('suffix')
        print filename, ">>>", new_name
        return new_name

def main(source_path):
    """Get files from given filepath """
    import glob
    files = glob.glob(source_path + '/*')
    #files = glob.glob(source_path + '*.pdf')
    for old_path in files:
        split_list = old_path.split("/")
        name = split_list[-1]
        print "NAME:", name
        new_name = get_new_filename(name)
        if new_name:
            split_list[-1] = new_name
            joiner = "/"
            new_path = joiner.join(split_list)
            print old_path, "--->", new_path
            os.rename(old_path, new_path)
        else:
            continue

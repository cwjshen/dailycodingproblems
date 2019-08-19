# This problem was asked by Google.

# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

# Note:

# The name of a file contains at least a period and an extension.

# The name of a directory or sub-directory will not contain a period.

# SOME ASSUMPTIONS I WOULD ASK DURING THE INTERVIEW:    
# Can I assume that there will only ever be one root level directory?
# Can I assume that the input file system string is valid / forms a valid directory tree?

def longest_file_path(file_system_string):
    # If empty string, return 0
    if not file_system_string:
        return 0
    # if not a base directory and not a file
    if '\\' not in file_system_string and '.' not in file_system_string:
        return 0
    # Base directory will be whatever comes before the first occurence of a new line
    if '\n' in file_system_string:
        base_dir = file_system_string[:file_system_string.find('\n')]
    else:
        base_dir = file_system_string
    current_path = base_dir
    current_longest_path = current_path
    prev_num_tabs = 0
    for i in range(len(file_system_string)):
        if file_system_string[i] == '\n':
            curr_num_tabs = 0
            begin_index = 0
            end_index = len(file_system_string)
            for j in range(i+1, len(file_system_string)):
                if file_system_string[j] == '\t':
                    curr_num_tabs += 1
                    begin_index = j + 1
                if file_system_string[j] == '\n':
                    end_index = j 
                    break
            if curr_num_tabs > prev_num_tabs:
                current_path = current_path + '/' + file_system_string[begin_index:end_index]
                prev_num_tabs = curr_num_tabs
            else:
                # backtrack by difference in number of tabs + 1 
                # e.g. if curr tabs == prev tabs, you need to backtrack by one '/'
                # if the curr tabs == 1 and prev tabs == 2 you need to backtrack by two '/'s
                num_backtracks = prev_num_tabs - curr_num_tabs + 1
                for i in range(num_backtracks):
                    # Cut off string by last find of '/' for the number of times you need to backtrack
                    current_path = current_path[:current_path.rfind('/')]
                # After cutting off the amount backtracked, add the current path
                prev_num_tabs = curr_num_tabs
                current_path = current_path + '/' + file_system_string[begin_index:end_index]
        if len(current_path) > len(current_longest_path):
            current_longest_path = current_path
    return len(current_longest_path)

a = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\tsubdir3"
b = "dir\n\tsubdir1\n\t\tsubsubdir1\n\tsubdir2"
c = "a.txt"
print(c)
print(longest_file_path(c))

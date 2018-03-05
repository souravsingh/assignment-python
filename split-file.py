import os, sys

filename, suffix = os.path.splitext(sys.argv[1])
print("Running the splitting command on file {} to files with {} lines".format(sys.argv[1], sys.argv[2]))
os.system("split {} -l {} {}-part -d --verbose --additional-suffix {}".format(sys.argv[1], sys.argv[2], filen, suffx))
print("File splitting done.")

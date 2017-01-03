import glob
import gzip

rawlist = glob.glob("*.txt")
gzlist = []

for file in rawlist:
    out_name = file + '.gz'
    f_in = open(file, 'rb')
    f_out = gzip.open(out_name, 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()
    gzlist.append(out_name)

print rawlist
print gzlist

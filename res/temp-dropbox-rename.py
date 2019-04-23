
API_key = '9U1wxIXa0DAAAAAAAAAAPNDpjxf4SAqRI9W2n4S1Vi880A2mKiATYxdnv0HUX5vE'
dbx = dropbox.Dropbox(API_key)
files = dbx.files_list_folder('').entries

def sorter(f):
    s = f.name
    i, j = s.index('_')+1, s.index('k')
    return float(s[i:j])
files.sort(key=sorter)

j = 0
for file in files:
    if 'metadata' in file.name:
        continue
    outname = '/data/cdb/{:03x}-{}'.format(j+0x29,file.name)
    print(outname)

    m, c = dbx.files_download(path=file.path_display)
    with open(outname, 'wb') as fo:
        fo.write(c.content)
    j +=1


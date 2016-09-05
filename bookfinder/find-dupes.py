# dupFinder.py
import os, sys
import hashlib
import argparse as ap
 
def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups
 
 
# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]
 
 
def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
 
 
def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical. The name could differ, but the content is identical')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')
 
    else:
        print('No duplicate files found.')
 
 
def deleteDups(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Removing dupes:')
        print('___________________')
        for file_paths in results:
            iterfiles = iter(file_paths)
            next(iterfiles)
            for subresult in iterfiles:
                print('\t\tRemoving %s' % subresult)
                os.remove(subresult)
        print('___________________')

    else:
        print('No duplicate files found.')
 
 
if __name__ == '__main__':
    
    parser = ap.ArgumentParser(description="Find duplicate files. ")
    parser.add_argument("--sources", nargs="+", help="list of directories to look for duplicates")
    parser.add_argument("--delete", action="store_true", help="Delete all duplicates. [Optional]")
    
    args, leftovers = parser.parse_known_args()

    if args.sources is not None:
            dups = {}
            folders = args.sources
            for i in folders:              
                if not i.startswith('.'):
                    # Iterate the folders given
                    if os.path.exists(i):                     
                        # Find the duplicated files and append them to the dups
                        joinDicts(dups, findDup(i))
                    else:
                        print('%s is not a valid path, please verify' % i)
                        sys.exit()        
                printResults(dups)
                if args.delete:                        
                    deleteDups(dups)
       
    else:
        print('Usage: python find-dupes.py --sources[source1, source2, source3...N]')
    
    
# importing os module
import os

directory = os.getcwd()

for count, mapname in enumerate(os.listdir(directory)):
    directory2 = directory+"/"+mapname
    for count2, filename2 in enumerate(os.listdir(directory2)):
        file_name, file_ext = os.path.splitext(filename2)

        if file_ext == '.txt':
            old = directory2 + '/' + filename2
            new = directory2 + '/' + mapname + '_DonkeySim_waypoints.txt'
            os.renames(old,new)

        elif file_ext == '.csv':

            if file_name == mapname + '_map_waypoints':
                old = directory2 + '/' + filename2
                new = directory2 + '/' + mapname + '_centerline.csv'
                os.renames(old, new)

            elif file_name == mapname + '_raceline':
                removefile = directory2 + '/' + filename2
                os.remove(removefile)

            elif file_name == mapname + '_raceline_newconv':
                old = directory2 + '/' + filename2
                new = directory2 + '/' + mapname + '_raceline.csv'
                os.renames(old, new)

        elif file_ext == '.pgm':
            removefile = directory2 + '/' + filename2
            os.remove(removefile)


        # rename() function will
        # rename all the files
        #os.rename(src, dst)



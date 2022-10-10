import os
import shutil
rootdir = '.'

for dirs in os.listdir(rootdir):
    if(not os.path.isfile(dirs) and not dirs.startswith(".")):
        shutil.make_archive(dirs, 'zip', dirs)
        os.rename(dirs+".zip", dirs+".mcaddon")
        shutil.rmtree(dirs)
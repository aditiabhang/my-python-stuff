### Absolute Path and Relation path in files

- Files have a name and a path.
- The root folder is the lowest folder.
- In a file path, the folders and filename are separated by backslashes on Windows and forward slashes on Linux and Mac.
- Use the os.path.join() function to combine folders with the correct slash.
- The current working directory is the oflder that any relative paths are relative to.
- os.getcwd() will return the current working directory.
- os.chdir() will change the current working directory.
- Absolute paths begin with the root folder, relative paths do not.
- The . folder represents "this folder", the .. folder represents "the parent folder".
- os.path.abspath() returns an absolute path form of the path passed to it.
- os.path.relpath() returns the relative path between two paths passed to it.
- os.makedirs() can make folders.
- os.path.getsize() returns a file's size.
- os.listdir() returns a list of strings of filenames.
- os.path.exists() returns True if the filename passed to it exists.
- os.path.isfile() and os.path.isdir() return True if they were passed a filename or file path.

-------------------------------------------------------------

### Reading & writing plain text files:

- The **open()** function will return a file object which has reading and writing –related methods.

        >>> helloFile = open('/Users/aditiabhang/My_Workspace/Python/my-python-stuff/automate-boring-stuff-with-python/simple_hello.txt')
        >>> helloFile.read()
        "Hello Aditi..!! How are you and how awesomely successful and beloved is you life right now!?\nI'm sure all the blessing are growing on you every day and night!\nStay Awesome!!!\n"

- Pass **‘r'** (or nothing) to open() to open the file in read mode. Pass **‘w'** for write mode. Pass **‘a'** for append mode.
- Opening a nonexistent filename in write or append mode will create that file.
- Call **read()** or **write()** to read the contents of a file or write a string to a file.

        >>> helloFile = open('/Users/aditiabhang/My_Workspace/Python/my-python-stuff/automate-boring-stuff-with-python/simple_hello2.txt', 'w')
        >>> helloFile.write('Helllooo YOUniverse!!!')
        22
- Call **readlines()** to return a list of strings of the file's content.

        >>> helloFile.readlines()
        ['Hello Aditi..!! How are you and how awesomely successful and beloved is you life right now!?\n', "I'm sure all the blessing are growing on you every day and night!\n", 'Stay Awesome!!!\n']

- Call **close()** when you are done with the file.

        >>> helloFile.close()

- The shelve module can store Python values in a binary file.
- The **shelve.open()** function returns a dictionary-like shelf value.

        >>> import shelve
        >>> shelfFile = shelve.open('mydata')
        >>> shelfFile['dogs'] = ['Tommy','Sally','Bolt','Hira']
        >>> shelfFile.close()
        >>> shelfFile = shelve.open('mydata')
        >>> shelfFile['dogs']
        ['Tommy', 'Sally', 'Bolt', 'Hira']

        >>> shelfFile = shelve.open('mydata')
        >>> list(shelfFile.keys())
        ['dogs']
        >>> list(shelfFile.values())
        [['Tommy', 'Sally', 'Bolt', 'Hira']]

-------------------------------------------------------------

### Copying & Moving files and folders

- We import **shutil** module does the job of copying and moving, or delete files.
- To copy and/or rename a file: **shutil.copy('from_path','to_path')**
- To copy an entire folder: **shutilcopytree('from_path','to_path')**
- Move function: **shutil.move'from_path','to_path')**
- To rename a folder, we simply move it but give a different name to the destination path: **shutil.move'from_path','to_path_with_new_name')**

-------------------------------------------------------------

### Deleting files or folder:

- **os.unlink()** will delete a file.
- **os.rmdir()** will delete a folder (but the folder must be empty).
- **shutil.rmtree()** will delete a folder and *all its contents*.
- Deleting can be dangerous, so do a "dry run" first.
- **send2trash.send2trash()** will send a file or folder to the recycling bin.
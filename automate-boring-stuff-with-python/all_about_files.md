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
- Pass *‘r'* (or nothing) to open() to open the file in read mode. Pass **‘w'** for write mode. Pass **‘a'** for append mode.
- Opening a nonexistent filename in write or append mode will create that file.
- Call **read()** or **write()** *to read the contents of a file or write a string to a file.
- Call **readlines()** to return a list of strings of the file's content.
- Call **close()** when you are done with the file.
- The shelve module can store Python values in a binary file.
- The **shelve.open()** function returns a dictionary-like shelf value.

### Working form the outside of the IDLE

- The shebang line tells your computer that you want to run the script using Python 3.
- On Windows, you can bring up the Run dialog by pressing Win+R.
- A batch file can save you a lot typing by running multiple commands.
- The batch files you'll make will look like this:

    ```
            @py C:\Users\Al\MyPytonScripts\hello.py %*
            @pause
    ```

- You'll need to add the MyPythonScripts folder to the PATH environment variable first.
- Command-line arguments can be read in the sys.argv list. (Import the sys module first)
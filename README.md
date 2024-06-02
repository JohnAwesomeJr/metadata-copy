# metadata-copy
copy date meta data from files in one folder to files that have the same name in another folder

This script copies metadata, such as creation and modification dates, from files in one folder to matching files in another folder, even if the file types differ. For example, if you have compressed videos in .mp4 format and the original videos in .MOV format, the script will transfer the original dates to the new files. It works for any file type, ensuring that the historical information of your files is preserved accurately after any transformations.

How to Use the Metadata Copy Script
Install Dependencies:
Run: ```pip install pywin32 pyexiftool```

Run the Script:
```python3 copy.py```

When prompted, enter the path to the source folder (original files).
Enter the path to the destination folder (new files).
The script will find matching files in both folders and copy the metadata from the original files to the new files.

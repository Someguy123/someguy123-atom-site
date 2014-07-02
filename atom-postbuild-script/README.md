## Atom Post-Build Script

# LICENSE
This script is licensed under the MIT license, the same as the original Someguy123 Atom Builds website.

# Dependencies

 - [Mega.PY by richardsaurus](https://github.com/richardasaurus/mega.py)
 - [WinRAR Command-line Tools](http://www.rarlab.com/download.htm)
 - [Python 2.7](http://python.org/)

# Information


This script is used to publish builds to MEGA. 

Current Todo: If someone were to enhance this script to automatically pull in newer version tags from git when detected, and only run if there was a new version, that would simplify the build process a ton.

The current process this script will follow is the following:

 1. Login to MEGA (can take email and pass as two params, no params is anonymous)
 2. Build the JSON object
 3. Read the package.json file and extract the version, load into the JSON object
 4. Use WinRAR command line tools to package up the Atom directory
 5. Calculate the MD5 hash of the file and then add it to the JSON object
 6. Upload the file to MEGA
 7. Output the JSON to the console to be placed inside builds.json for the Atom Builds Site

# To use it:

- Build atom using `.\script\build`
- Place the python script in `%TEMP%\atom-build` (the script will NOT be deleted, you can re-build newer versions of Atom and run the script again without problems).
- CD into the `%TEMP%\atom-build` directory, and then Run the python script using `python upload.py`, and it will produce a rar, upload to MEGA, and then output the JSON for `builds.json`


On successful completion, it will output JSON similar to the following:


	{
	  "date": "2014-07-02",
	  "url": "https://mega.co.nz/#!09JX0SZa!R01zLCHrVESkmoL1LcX9xF9ITTARK6NEBSbGOGZJzkc",
	  "md5": "96a39ee1d43a930e4aa43c953653c783",
	  "title": "Atom Build 0.107.0-a92eed5"
	}
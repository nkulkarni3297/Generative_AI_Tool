For this project virtual enviroenment is already created to you need to activate virtual environment first. For activating the virtual environment follow the below steps.

1. Open the project folder in Visual Studio Code/ CMD of local machine. It should look like this
	\path\to\pdf_poc>

If the project is opened in Visual Studio Code, open new terminal (by default it will start powershell terminal). To change it to CMD terminal, click on the ˅ (down arrow) sign next to powershell written on the top of terminal window in VSC and click the Command Prompt.
It will start a new CMD terminal within the same project folder path. Ensure the path is correct as above.

2. On Visual Studio Code/CMD type the following command
	\path\to\pdf_poc>poc_iqvia\scripts\activate

This command ensures the virtual environment is activated.

It should look like below
	(poc_iqvia) \path\to\pdf_poc>

Before Running the Project ensure you install all packages mentioned in requirements.txt file. 
To directly install all packages at once directly run the below command

pip install -r requirements.txt

once all packages are installed you are ready to run the script. For running the script type

python app_main.py

If everything works fine without any error then you should see a url with the below message

* Serving Flask app 'app_main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 436-384-159

Copy the http url and paste it in the browser.
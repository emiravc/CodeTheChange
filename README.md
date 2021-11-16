# P2P Zen Bot
This readme belongs to Hackathon CodeTheChange 2021, we have implemented a telegram bot that gives you Mental Health Recommendations. This project is under construction at the moment.

In order for our bot to work! You will have to work with our database directory in order to run this directory with our Django database menu/navigation program [P2P Zen](https://github.com/emiravc/P2P-Zen-Bot).

The program will be ran through `__main__.py`. Make sure to do the following commands before running our files:

## Installing Pip and Dependecies
Cancel changes
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py // Pip installation

python get-pip.py

pip help // To check installation
```

Few dependecies will needed as well therefore run the following command:

```
pip install python-decouple
```

In case pip still does not work giving error of :

`'pip' is not recognized as an internal or external command, operable program or batch file`.

This is because pip is installed to `C:\Python34\Scripts\pip`

Use the command `setx`to add the path of pip to Scripts file:`setx PATH "%PATH%;C:\Python34\Scripts" `

In order to use this bot information inside `prodil.ini.sample` has to be filled and name of this file needs to be changed to `prodil.ini`.

After neccessary dependecies are connected with [P2P Zen Database](https://github.com/emiravc/P2P-Zen-Bot), this bot can be executed order to run with `python -m prodil`

# 2021 Hackathon Code The Change TEJBarbarians

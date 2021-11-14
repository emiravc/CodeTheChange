# CodeTheChange

This readme belongs to Hackathon CodeTheChange 2021, we have implemented a telegram bot that gives you Mental Health Recommendations. This project is under construction at the moment.

The program will be ran through `__main__.py`. Make sure to do the following commands before running our files:

## Installing Pip and Dependecies

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

After neccessary dependecies are connected with `navigation`, this bot can be executed order to run with `python -m prodil`

# 2021 Hackathon Code The Change TEJBarbarians

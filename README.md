# 105 Game
This project emulate the 105 Premium d'Oro 90's slot machine

# RULES

 - The target of this game is to obtain 21 on each slot

 - Draw a card
 - Add the card to a slot content.
 - If the total of the slot is greater than *21* you lose the game
 - If the card drawn is "A" it's value is *1* if the value in the slot
   is lower that 11 otherwise its value is *11*. The slot start to flash 
   (if wasn't flashing before)
 - If in a slot you add more than 5 cards its value goes to *21* (but its 
   inner value is the one you reached by adding the cards so you can continue
   to add cards until you reach 21)
 - ...

## Python Environment
### Linux
#### To create the python envirnoment:
```bash
$ source create_python_venv_linux.sh
```

#### To activate the python environment
```bash
$ source .linux_env/bin/activate
```

#### To deactivate the python environment
```bash
$ deactivate
```

#### Run the program
After the python env activation
```bash
$ python main.py
```

### Windows Powershell
#### To create the python envirnoment:
```shell
$ .\create_python_venv_win.sh
```

#### To activate the python environment
```shell
$ .\activate_win_venv.ps1
```

#### To deactivate the python environment
```shell
$ deactivate
```

#### Run the program
After the python env activation
```shell
$ python main.py
```

#### Create a Windows executable
```shell
$ .\create_exe.ps1
```

## Software Requirements
 - python 
 - pip python module
 - venv python module

## Start the application with a different language in linux
 ```bash
 $ LANG=it_IT.UTF-8 python main.py
 $ LANG=en_US.UTF-8 python main.py 
 ```

## Create .po translation file
 ```bash 
 $ xgettext main.py 
 ```
 This will create a `message.po` file in the root directory (if there are any message to translate).

 Rename this file in `main.po` and copy it in the language directory `files/locale/<LANG>/LC_MESSAGES`

## Create .mo translation file from .po
 ```bash
 $ msgfmt files/locale/<LANG>/LC_MESSAGES/main.po -o files/locale/<LANG>/LC_MESSAGES/main.mo
 ```

 Example:
 ```bash
 $ msgfmt files/locale/it_IT/LC_MESSAGES/main.po -o files/locale/it_IT/LC_MESSAGES/main.mo
 ```

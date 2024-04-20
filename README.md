
# P/V Shadowing Calculator Software

A simple desktop utility with UI to calculate the minimum distance between panels to avoid shading in the case of single, double and/or triple panel system.


## Appendix

This is a semestrial project for the subject "EEN445 - Renewable Energy Resources" of Cyprus University of Technology.


## Installation

This project uses Python Poetry Dependency Manager. 
(https://python-poetry.org/docs/)

Prior to installing Poetry, make sure you run the most recent Python3 version of binaries. 

Windows - Open Powershell and run the following command:
```bash
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Linux, macOS, Windows (WSL) - Open Terminal and run the following command:
```
curl -sSL https://install.python-poetry.org | python3 -
```

Next you have to add Poetry executable to the path. The default location of installation of Poetry is:

Windows - "%APPDATA%\pypoetry"
macOS - "~/Library/Application Support/pypoetry"
Linux/UNIX - "~/Library/Application Support/pypoetry"

    
## Run Locally

Clone the project

```bash
  git clone https://github.com/suprch4rg3d/EEN445-PV_Calculator_Software
```

Go to the project directory

```bash
  cd App
```
Create a virtual environment using Poetry by running the command
```bash
  poetry shell
```
Do not forget to change the kernel in your code editor to point to the newly generated virtual environment

Install dependencies

```bash
  poetry install 
```

Run the application

```bash
  poetry run python interface.py
```


## Authors

- [@suprch4rg3d](https://github.com/suprch4rg3d)
- [@charalampo-smichaelide-s](https://github.com/Charalampo-sMichaelide-s)
- [@ca-kampouridis](https://github.com/ca-kampouridis)




# updaten
uv self update

# initialize
initialize app project without creating an app directory:

# alle gefundenen python versioenn anzeigen 
uv python list 

# die anzeigen, die er in dem projekt / dir aktuell ranzieht 
uv python find 

# eine von uv verwaltete (managed python) pthon version installieren nach ~/.local/bin
# uv refers to Python versions it installs as managed Python
uv pthon install <version>
uv pthon install 3.12


# normal sollte uv immer ein venv in einem projekt automatisch machen aber hier noch command
uv venv --python 3.11.6

# run script without building the hole project 
# ann wird das projekt nicht gebuildet u nur das (vom projekt unabhängige) skript ausgeführt
uv run --no-project example.py

# uvx —-ersetzt —-> uv tool run
# das geht alles bombenschnell
uv tool install ruff
which ruff
uvx ruff check
which ruff -> zeigt nix :)
uv tool upgrade --all

uv add <dependency>

# aktiviert venv und lässt projekt laufen
uv run 

# run flask
uv run flask --app main run

# make the server publicly available
$ flask run --host=0.0.0.0

# debug mode mit auto-reloading enablen
# AUFPASSEN! es ist von relevanz von welchen directory aus man 'uv run flas --app <appname> run' aufruft!!
flask --app hello run --debug
uv run flask --app main run --debug

# show help for flask cli
 uv run flask --help

# custom click command for flask CLI
flask --app flaskr init-db


# cluquiz-backend
cluquiz flask backend to serve various frontend clients

17.12.2025 note ->
start the app via :
uv run flask --app cluquiz run --debug --reload
uv run flask --app cluquiz run 

or for docker (loopback address cannot be published)
docker run --name myflask -p 5000:5000 myflask --host=0.0.0.0 --port=5000


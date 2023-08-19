
[1] - Start the server (API : http://127.0.0.1:8000/)
[2] - Start client app


[1] - Start the server
## Create a virtual environment :
```
cd api
python -m venv env
```
## Activate the virtual environment :

`source env/bin/activate`

## [get an key](https://platform.openai.com/account/api-keys)

`export OPENAI_API_KEY='sk-brHeh...A39v5iXsM2'`

or add to .env file

`OPENAI_API_KEY=YOUR_API_KEY'`

## Installation:

### install requirements :
use `pip3 on a mac`
`pip install -r requirements.txt`

### install whisper model
`pip install git+https://github.com/openai/whisper.git`

### install server [uvicorn ASGI server](https://www.uvicorn.org/)
`pip install "uvicorn[standard]`

## Start the server:
`uvicorn main:app --reload`

## Test API with curl:

```
curl -X POST "http://localhost:8000/generate" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"prompt\":\"Once upon a time\"}"
```

[2] Start the React client application

## Installation:
```
cd client
npm install
```

## Start the app
`npm start`
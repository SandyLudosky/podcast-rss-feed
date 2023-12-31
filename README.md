
### [1] - Configure and start the server
### [2] - Start client app

=========================================================

## [1] - Configure and start the server
### ➢ Create a virtual environment :
```
cd api
python -m venv env
```
### ➢ Activate the virtual environment :

`source env/bin/activate`

### ➢ [get an key](https://platform.openai.com/account/api-keys)

`export OPENAI_API_KEY='sk-brHeh...A39v5iXsM2'`

or add to .env file

`OPENAI_API_KEY=YOUR_API_KEY'`

## Installation:

### ➢ install requirements :
use `pip3 on a mac` or `pip on windows`
- `pip install -r requirements.txt`

### ➢ [install whisper model](https://github.com/openai/whisper)
`pip install git+https://github.com/openai/whisper.git`

### ➢ install server [uvicorn ASGI server](https://www.uvicorn.org/)
`pip install "uvicorn[standard]`

### ➢ Start the server:
`uvicorn main:app --reload`

### ➢ Test API with curl:

```
curl http://127.0.0.1:8000/
```

add your API key to the header
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY" -d '{
    "rss": "rss-url"
}' http://127.0.0.1:8000/transcribe/

```

## [2] - Start client app

### ➢ Installation:
```
cd client
npm install
```

### ➢ Start the app
`npm start`


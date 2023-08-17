
## Create a virtual environment :
```
python -m venv env
```
## Activate the virtual environment :
```
source env/bin/activate
```
## Installation:

`pip install -r requirements.txt`

## install whisper model
`pip install git+https://github.com/openai/whisper.git`
## [get an key](https://platform.openai.com/account/api-keys)

`export OPENAI_API_KEY='sk-brHeh...A39v5iXsM2'`

## install server [uvicorn ASGI server](https://www.uvicorn.org/)

`pip install "uvicorn[standard]`

## Start the server:
`uvicorn main:app --reload`
npmbuild:
	npm run build

flaskrun:
	python backend.py

all: npmbuild flaskrun

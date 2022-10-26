build:
	docker build -t usage-api .

run:
	docker run -it --rm  -p 5000:5000 usage-api
all: run

build:
	@g++ -o main main.cpp -std=c++23 -Wall

run: build
	./main

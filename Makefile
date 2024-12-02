all: run

build:
	@g++ -o main main.cpp -std=c++23 -Wall -Wextra -Werror -pedantic -pedantic-errors

run: build
	./main

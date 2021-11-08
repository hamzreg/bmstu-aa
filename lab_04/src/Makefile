CC := g++
FLAGS := -pthread
TARGET := app.exe


.PHONY: run clean

$(TARGET) : main.cpp graph.cpp
	$(CC) $(FLAGS) -o $@ $^

clean:
	$(RM) -rf *.exe
run:
	./app.exe


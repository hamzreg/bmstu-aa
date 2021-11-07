CC := g++
TARGET := app.exe


.PHONY: run clean

$(TARGET) : main.cpp graph.cpp
	$(CC) -o $@ $^

clean:
	$(RM) -rf *.exe
run:
	./app.exe


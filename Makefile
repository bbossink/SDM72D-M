CC = gcc
#CFLAGS  = -O2 -Wall -g -I/usr/local/include/modbus
CFLAGS  = -O2 -Wall -g `pkg-config --cflags libmodbus`
#LDFLAGS = -O2 -Wall -g -L/usr/local/lib -lmodbus
LDFLAGS = -O2 -Wall -g `pkg-config --libs libmodbus`

SDM = sdm72d-m
%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

${SDM}: sdm72d-m.o 
	$(CC) -o $@ sdm72d-m.o $(LDFLAGS)
	chmod 4711 ${SDM}

strip:
	strip ${SDM}

clean:
	rm -f *.o ${SDM}

install: ${SDM}
	install -m 4711 $(SDM) /usr/local/bin

uninstall:
	rm -f /usr/local/bin/$(SDM)

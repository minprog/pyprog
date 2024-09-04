DIA    = $(shell find -name '*.dia')
DIAPNG = $(patsubst %.dia,%.png,$(DIA))

%.png: %.dia
	dia --export $@ $<

all:  $(DIAPNG)

clean:
	rm -rf $(DIAPNG)

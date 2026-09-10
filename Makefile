# Local development, in a replica of the CI environment. Requires Docker (with Compose v2).
#
#   make dev        live site at http://localhost:4000 + live decks at http://localhost:4200
#                   Browse the site at :4000 (decks included, under /slides/). :4200 is for a
#                   deck you are editing -- open it directly, http://localhost:4200/unit-01.html.
#   make site       the production build into _site/ (Jekyll, decks, PDFs, content gate)
#   make pdf        re-render decks and PDFs only
#   make instructor decks with speaker notes -> _instructor-slides/ (never published)
#   make shell      a shell inside the container
#   make image      (re)build the image; needed after changing Gemfile, slides/requirements.txt,
#                   or the Dockerfile
#   make clean      remove build outputs
#
# Everything runs as your own uid/gid so the files it writes are yours.
export UID := $(shell id -u)
export GID := $(shell id -g)
COMPOSE := docker compose
RUN     := $(COMPOSE) run --rm --no-deps jekyll

.PHONY: dev site pdf instructor shell image clean

dev: image
	$(COMPOSE) up

site: image
	$(RUN) tools/build_site.sh

pdf: image
	$(RUN) tools/build_slides.sh --pdf

instructor: image
	$(RUN) tools/build_slides.sh --instructor

shell: image
	$(RUN) bash

image:
	$(COMPOSE) build

clean:
	rm -rf _site _instructor-slides .jekyll-cache .jekyll-metadata slides/_freeze slides/.quarto .deck-export-cache

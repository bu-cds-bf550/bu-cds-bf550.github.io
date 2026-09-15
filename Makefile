# Local development, in a replica of the CI environment. Requires Docker (with Compose v2).
#
#   make dev        live site at http://localhost:4000 + live decks at http://localhost:4200
#                   Browse the site at :4000 (decks included, under /slides/). :4200 is for a
#                   deck you are editing -- open it directly, http://localhost:4200/unit-01.html.
#   make site       the production build into _site/ (Jekyll, decks, PDFs, content gate)
#   make deck DECK=unit-02-2
#                   one deck at http://localhost:4200/unit-02-2.html, live-reloading, with
#                   drag-and-resize editing on (--profile authoring) and speaker notes shown.
#                   Faster than `make dev`, which re-renders all fifteen decks. What you drag
#                   is written back into slides/unit-02-2.qmd. NEVER publish this build: the
#                   editable filter embeds the whole source, notes included, in the HTML.
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

.PHONY: dev deck site pdf instructor shell image clean

dev: image
	$(COMPOSE) up

# One deck, with the editable plugin, on the slides service because that is the one publishing
# :4200. The preview lock holds a PID that means nothing in a fresh container (dev.sh explains
# why), so clear it first.
deck: image
	@test -n "$(DECK)" || { echo "usage: make deck DECK=unit-02-2" >&2; exit 2; }
	@test -f slides/$(DECK).qmd || { echo "no such deck: slides/$(DECK).qmd" >&2; exit 2; }
	$(COMPOSE) run --rm --no-deps --service-ports slides bash -c \
	  'rm -f slides/.quarto/preview/lock; \
	   quarto preview slides/$(DECK).qmd --profile authoring --no-browser --host 0.0.0.0 --port 4200'

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

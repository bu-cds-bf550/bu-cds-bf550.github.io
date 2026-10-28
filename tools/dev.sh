#!/usr/bin/env bash
# The three live-reload watchers `make dev` runs (one per compose service; see compose.yaml).
#
#   tools/dev.sh jekyll      serve the site at :4000, rebuilding on every edit, browser auto-refresh
#   tools/dev.sh slides      render slides/ on every edit and serve the decks at :4200 with reload
#   tools/dev.sh tutorials   the same for tutorials/, the tutorial decks, at :4201
#
# Browse the site at :4000 -- it serves the whole site, decks included, at /slides/ and
# /tutorials/. Use :4200 and :4201 only for a deck you are editing (:4200/unit-01.html,
# :4201/scikit-learn.html): their roots are _site/slides/ and _site/tutorials/, so the site page
# Jekyll writes there loads without styling, its /assets/... links pointing above the root.
#
# All three write into _site/. Jekyll keeps _site/slides and _site/tutorials across its rebuilds
# (`keep_files`) and never reads slides/ or tutorials/ (`exclude`), so the watchers do not trip
# over each other. Runs on the host too, if you have the tools installed.
set -euo pipefail
cd "$(dirname "$0")/.."

case "${1:-}" in
  jekyll)
    # No `--incremental`. It regenerates only pages whose own source file changed, so an edit to
    # _data/, _includes/, or _layouts/ -- which every page reads but none of them *is* -- updates
    # nothing: the rebuild reports success in milliseconds and _site keeps the stale sidebar. A
    # full build of this site is ~0.5s, so incremental bought no time it did not cost in
    # confusion. `keep_files: slides` still protects the decks the slides watcher writes.
    args=(--host 0.0.0.0 --port 4000 --livereload --livereload-port 35729 --watch)
    [[ "${JEKYLL_FORCE_POLLING:-0}" == "1" ]] && args+=(--force_polling)
    exec bundle exec jekyll serve "${args[@]}" ;;
  slides|tutorials)
    # `quarto preview` on the project renders every deck once, then re-renders a deck when its
    # source changes and reloads any browser tab showing it. One port per project.
    project="$1"
    port=4200; [[ "$project" == tutorials ]] && port=4201
    #
    # The preview lock holds the PID of the process owning it. In a fresh container that number
    # means nothing -- the PID namespace restarts at 1 -- so quarto "terminates the existing
    # preview server" by killing whatever wears that PID now, reliably itself: the service exits
    # 1 with no message. No preview survives a container start, so the lock is stale by
    # definition here. On the host, where the PID may be a real running preview, leave it alone.
    [[ -f /.dockerenv ]] && rm -f "$project/.quarto/preview/lock"
    exec quarto preview "$project" --no-browser --host 0.0.0.0 --port "$port" ;;
  *)
    echo "usage: tools/dev.sh jekyll|slides|tutorials" >&2; exit 2 ;;
esac

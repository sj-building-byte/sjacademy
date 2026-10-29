#!/bin/zsh
# Copy staged fixes over the originals. Each original is backed up first to
# SEO_Fixes_2026_09_30/backup_originals/<same path>. New files are copied into place.
set -euo pipefail
echo "Already applied on 2026-09-30, and the folder has since been reorganised. Not re-running."; exit 1
ROOT="${0:A:h:h:h}"
STAGED="$ROOT/SEO_Fixes_2026_09_30/staged"
BACKUP="$ROOT/SEO_Fixes_2026_09_30/backup_originals"

cd "$STAGED"
for f in A_Level_Hubs/*.html O_Level_Hubs/*.html HTML_Tools_and_Drafts/*.html; do
  if [[ -f "$ROOT/$f" ]]; then
    mkdir -p "$BACKUP/${f:h}"
    cp -p "$ROOT/$f" "$BACKUP/$f"
  fi
  cp "$f" "$ROOT/$f"
  echo "applied $f"
done
mkdir -p "$ROOT/New_Pages"
cp New_Pages/*.html "$ROOT/New_Pages/"
cp Yoast_Metadata_Changes.csv "$ROOT/SEO_Docs/Yoast_Metadata_Changes_2026_09_30.csv"
echo "done. originals backed up in $BACKUP"

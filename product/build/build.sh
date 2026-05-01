#!/usr/bin/env bash
## Job Hunter's Bundle — PDF build script
## Usage:
##   ./build.sh smoke   # render Module 1 only (smoke test)
##   ./build.sh full    # render full bundle (all 5 modules)
##   ./build.sh m3      # render Module 3 only (for M3 P12 emoji test)
##
## Output goes to ./output/ (gitignored).
## Requires: pandoc, xelatex (MacTeX), font-noto-color-emoji.

set -euo pipefail

cd "$(dirname "$0")"

## Make sure xelatex is on PATH (MacTeX installs to /Library/TeX/texbin)
export PATH="/Library/TeX/texbin:/opt/homebrew/bin:$PATH"

mode="${1:-smoke}"
mkdir -p output
product_dir="$(cd .. && pwd)"

case "$mode" in
  smoke)
    inputs=("$product_dir/module-01-resume.md")
    output="output/smoke-module-01.pdf"
    ;;
  m3)
    inputs=("$product_dir/module-03-interview.md")
    output="output/module-03.pdf"
    ;;
  full)
    inputs=(
      "$product_dir/module-01-resume.md"
      "$product_dir/module-02-cover-letter.md"
      "$product_dir/module-03-interview.md"
      "$product_dir/module-04-linkedin.md"
      "$product_dir/module-05-salary-negotiation.md"
    )
    output="output/job-hunters-bundle.pdf"
    ;;
  *)
    echo "Unknown mode: $mode (expected: smoke | m3 | full)" >&2
    exit 1
    ;;
esac

echo "==> Building [$mode] → $output"

pandoc \
  --defaults=defaults.yaml \
  -o "$output" \
  "${inputs[@]}"

echo "==> Done: $output"
ls -lh "$output"

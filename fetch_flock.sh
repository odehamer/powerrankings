#!/usr/bin/env bash
# Saves Flock Fantasy's expert dynasty and redraft rankings as small JSON files the trade page can read.
set -euo pipefail
trap 'rm -f flock_*.json.tmp' EXIT

for format in SUPERFLEX ONEQB REDRAFT REDRAFT_SF; do
  out="flock_$(echo "$format" | tr '[:upper:]' '[:lower:]').json"
  curl -sf "https://api.flockfantasy.com/rankings?format=${format}&pickType=hybrid" \
    | jq '{
        updated: (now | todate),
        players: [
          .data[] | select(.isDraftPick | not)
        ] | to_entries | map({
          fantasyCalcId: .value.fantasyCalcId,
          name: .value.playerName,
          position: .value.position,
          rank: (.key + 1),
          positionRank: .value.averagePositionalRank,
          tier: .value.averageTier
        }) | map(select(.fantasyCalcId != null))
      }
      | if (.players | length) < 100 then error("too few players") else . end' \
    > "$out.tmp"
  mv "$out.tmp" "$out"
done

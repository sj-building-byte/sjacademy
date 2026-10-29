#!/bin/bash
# usage: build/inspect.sh <video> <outdir> <times...>  -> grid of frames at given times
V=$1; O=$2; shift 2; mkdir -p $O; rm -f $O/tx-*.png; ins=""; n=0
for t in "$@"; do ffmpeg -y -loglevel error -ss $t -i $V -frames:v 1 -vf scale=216:384 $O/tx-$n.png; ins="$ins -i $O/tx-$n.png"; n=$((n+1)); done
lay=$(python3 -c "print('|'.join(f'{(i%9)*216}_{(i//9)*384}' for i in range($n)))")
ffmpeg -y -loglevel error $ins -filter_complex "xstack=inputs=$n:layout=$lay:fill=black" $O/grid.png

#!/usr/bin/env bash
set -e

if [[ $# < 2 ]]; then
    echo "Provide width and height arguments"
    exit 1
fi

WIDTH=$1
HEIGHT=$2

if [[ ($WIDTH < 3) || ($HEIGHT < 3)]]; then
    echo "Make sure that both width and height are greater than 3!"
    exit 1
fi

echo "Drawing a box $HEIGHT X $WIDTH size"


function draw_vertical() {
    ((height = $2 - 2))
    ((width = $1 - 2))
    for ((i=1;i<=height;i++)); do
        echo -n "|"
        for ((j=1;j<=width;j++)); do echo -n " "; done
        echo "|"
    done
}

function draw_horizontal() {
    echo -n "+"
    # for i in $(seq 1 $WIDTH)
    ((width = $1 - 2))
    for ((i=1;i<=width;i++)); do echo -n "-"; done
    echo "+"
}


draw_horizontal $WIDTH
draw_vertical $WIDTH $HEIGHT
draw_horizontal $WIDTH

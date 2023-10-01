#!/bin/bash

marco () {
    tempVar=$(pwd)
    export tempVar
    echo $tempVar
}

polo () {
    cd $tempVar
}  
#!/usr/bin/sh

# Build the container

main() {
  docker build -t vcwild/livedivulgator .
}

main

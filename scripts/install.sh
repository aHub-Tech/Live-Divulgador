#!/bin/bash

# prepare development environment to work with the project
# execute: sh ops/scripts/develop.sh

source $(dirname "$0")/lib.sh

default_dir="$(pwd)"
venv_dir="$default_dir/venv"

# terminal color
color_default="\e[39m"
color_error="\e[31m"
color_ok="\e[32m"
color_header="\e[34m"

# functions
print_header() {
  echo
  echo -e "--$color_header $1 $color_default"
}

print_check() {
  status=$?
  if [ $status -eq 0 ]
  then
    echo -e "[$color_ok v $color_default] $1"
  else
    echo -e "[$color_error x $color_default] $1"
  fi
}

main() {
  print_header "Preparing python virtual environment"

  python3 -m venv "$venv_dir" >/dev/null 2>&1
  print_check "venv initialization $venv_dir"

  $venv_dir/bin/pip install --upgrade pip >/dev/null 2>&1
  print_check "pip upgrade"

  $venv_dir/bin/pip install setuptools_scm >/dev/null 2>&1
  print_check "pip install setuptools_scm"

  # install local development build
  echo -e "      ... installing livedivulgator bot component"
  $venv_dir/bin/pip install -e .[dev] >/dev/null 2>&1
  print_check "bot installation"

  # check installation
  echo -e "      ... checking CLI"
  $venv_dir/bin/divulgator --help >/dev/null 2>&1
  print_check "divulgator development installation"
}

# main
main

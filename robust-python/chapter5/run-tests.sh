#!/bin/bash
set -euxo pipefail

run_typechecker() {
    find . -maxdepth 1 -name '*.py' | \
        xargs --verbose -I{} mypy {}
    
}

run_pytest() {
    find . -maxdepth 1 -name '*.py' | \
        xargs --verbose -I{} pytest -v {}
}


run_typechecker
run_pytest


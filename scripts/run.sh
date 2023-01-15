#! /bin/bash
GIT_ROOT=$(git rev-parse --show-toplevel)

set -e

pushd "${GIT_ROOT}" > /dev/null


printf "Starting Advent of Code solver \n" && \
poetry run python -m adventofcode


SUCCESS=$?

popd > /dev/null

exit $SUCCESS
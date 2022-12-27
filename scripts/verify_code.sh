#! /bin/bash
GIT_ROOT=$(git rev-parse --show-toplevel)

set -e

pushd "${GIT_ROOT}" > /dev/null


printf "Formating imports with isort \n" && \
isort AOC && \
printf "Format code with black \n" && \
black AOC && \
printf "Lint code with mypy \n" && \
mypy AOC && \
printf "Lint code with pylint \n" && \
pylint AOC


SUCCESS=$?

popd > /dev/null

exit $SUCCESS
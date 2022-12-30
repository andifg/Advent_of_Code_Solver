#! /bin/bash
GIT_ROOT=$(git rev-parse --show-toplevel)

set -e

pushd "${GIT_ROOT}" > /dev/null


printf "Formating imports with isort \n" && \
isort adventofcode && \
printf "Format code with black \n" && \
black adventofcode && \
printf "Lint code with mypy \n" && \
mypy adventofcode && \
printf "Lint code with pylint \n" && \
pylint adventofcode


SUCCESS=$?

popd > /dev/null

exit $SUCCESS
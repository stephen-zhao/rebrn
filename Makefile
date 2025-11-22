
.PHONY: all build publish publish-test clean test bump-version install-uv

all: build

install-uv:
	@command -v uv >/dev/null 2>&1 || curl -LsSf https://astral.sh/uv/install.sh | sh

test:
	uv run pytest -s

build:
	uv build

publish:
	uv publish

publish-test:
	uv publish --repository testpypi

clean:
	rm -rf ./build ./*.egg-info ./dist

bump-version:
	uv run bump-my-version bump $(PART)
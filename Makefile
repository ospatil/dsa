THEME_VERSION := v0.25.0
THEME := hugo-geekdoc
BASEDIR := docs
THEMEDIR := $(BASEDIR)/themes

.PHONY: doc
doc: doc-assets doc-build

.PHONY: doc-assets
doc-assets:
	mkdir -p $(THEMEDIR)/$(THEME)/ ; \
	curl -sSL "https://github.com/thegeeklab/$(THEME)/releases/download/${THEME_VERSION}/$(THEME).tar.gz" | tar -xz -C $(THEMEDIR)/$(THEME)/ --strip-components=1

.PHONY: doc-build
doc-build:
	cd $(BASEDIR); hugo

.PHONY: clean
clean:
	rm -rf $(THEMEDIR) && \
	rm -rf $(BASEDIR)/public

.PHONY: dev
dev:
	cd docs && \
	hugo server -D --baseURL http://localhost/

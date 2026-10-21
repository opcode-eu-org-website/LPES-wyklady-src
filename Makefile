# Copyright (c) 2019-2021 Robert Ryszard Paciorek <rrp@opcode.eu.org>
# 
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

MAINDIR     := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
OUTDIR      := $(MAINDIR)/output-www
TEXBUILDDIR := $(MAINDIR)/tmp-build
LIBFILESDIR := $(MAINDIR)/OpCode.eu.org/OpCode-core/lib

include $(shell if [ ! -f "$(MAINDIR)/OpCode.eu.org/OpCode-core/Makefile" ]; then \
	git submodule update --quiet --init "$(MAINDIR)/OpCode.eu.org" > /dev/null; \
	cd "$(MAINDIR)/OpCode.eu.org" && make > /dev/null; \
fi; echo "$(MAINDIR)/OpCode.eu.org/OpCode-core/Makefile")

.PHONY: help init installDependencies all
help:
	@echo 
	@echo See README.md
	@echo 

init: | checkout-submodules $(MAINDIR)/LPES-video/GoogleCloudTextToSpeach.py
	mkdir -p "$(TEXBUILDDIR)" "$(OUTDIR)"
	cd $(MAINDIR)/OpCode.eu.org && ln -fs $(MAINDIR)/output-www $(MAINDIR)/tmp-build . && make init

installDependencies:
	cd $(MAINDIR)/OpCode.eu.org && $(SUDO_CMD) make installDependencies

all:
	$(MAKE) buildAll
	@ [ "$(MAINDIR)" = "$(PWD)" ] && (cd LPES-booklets && $(MAKE) -f ../Makefile buildAll) || true
	@ [ "$(MAINDIR)" = "$(PWD)" ] && (cd LPES-video    && $(MAKE) -f ../Makefile buildAll) || true

$(MAINDIR)/LPES-video/GoogleCloudTextToSpeach.py:
	echo "token = ''" > $(MAINDIR)/LPES-video/GoogleCloudTextToSpeach.py

#
# addionals files
#

include $(wildcard $(MAINDIR)/LPES*/Makefile)

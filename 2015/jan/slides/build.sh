#!/bin/bash

pandoc -s -o slides.html -t dzslides --normalize --mathml --no-highlight --tab-stop=2 --data-dir=. slides.md


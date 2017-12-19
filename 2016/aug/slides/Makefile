all: slides.html

%.html: %.md
	pandoc -s -o $@ -t dzslides --normalize --mathml --no-highlight --tab-stop=2 --data-dir=. $<


IMAGES = thinking

minify: $(addprefix resources/, $(addsuffix .svg, $(IMAGES)))
	$(foreach IMAGE, $^, \
		scour -q -i $(IMAGE) -o $(IMAGE).min --create-groups --enable-id-stripping --enable-comment-stripping --enable-viewboxing --remove-metadata --set-precision=3; \
		mv $(IMAGE).min $(IMAGE); \
	)

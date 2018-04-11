`color-coder` takes an _n_-dimensional vector and returns a color.
Obviously, vectors live in a much larger space than the 3-dimensional space of colors,
so we will have to sacrifice some information.

`color-coder` takes a sample of vectors and  identifies the one-dimensional subspace
with the most variation in it (using PCA / SVD).
Then it maps it to a `[0, 1]` interval and builds the empirical
cumulative distribution function of the samples projected onto this subspace.
It is used later during color encoding in order to ensure a uniform distribution within
the `[0, 1]` interval.

Thus, similar vectors are mapped to similar colors while using the hue spectrum to its fullest.

__TL;DR:__ It works well if you have a bunch of samples and want to encode vectors similar to them.

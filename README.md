[![Codacy Badge](https://api.codacy.com/project/badge/Grade/21036c862fbb4305ba01fe57ab793af6)](https://www.codacy.com/app/mp4096/color-coder?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mp4096/color-coder&amp;utm_campaign=Badge_Grade)

# Color coder :rainbow:

`color-coder` takes an _n_-dimensional vector and returns a color.
Obviously, vectors live in a much larger space than the 3-dimensional space of colors,
so we will have to sacrifice some information.

## TL;DR summary
It works well if you have a bunch of samples and want to encode vectors similar to them.
Similar vectors are mapped to similar colors while using a color spectrum to its fullest.

## The math behind it

`color-coder` takes a sample of vectors and  identifies the one-dimensional subspace
with the most variation in it (using PCA / SVD).
Then it projects the samples onto this subspace and rescales them into a `[0, 1]` interval.
Next, it builds the empirical cumulative distribution function of the results,
which is used later during color encoding in order to ensure that colors are distributed
_uniformly_ within the `[0, 1]` interval.
This value can be used directly as hue or as an input for a colormap.
The latter is especially relevant if you want to have a perceptionally uniform
or a colorblind-accessible colormap.

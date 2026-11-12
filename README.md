![Intro scenery: the two oval portraits close up as a hand holds a magnifier over one face, enlarging a single eye, the matching portrait waiting beside it and the crimson ribbon at the top edge](intro-banner.png)

# analyze-code-similarity

![Wordmark banner: a studio wall of sepia portraits in walnut frames under one long brass light, the matching oval pair hung at the centre with a crimson ribbon bow above them, further single portraits ranked dimmer along the wall on both sides and a desk with a bound album below](banner.png)

<p align="center"><img src="logo.png" alt="analyze-code-similarity logo: two oval walnut framed sepia portraits of the same sitter side by side on a slate surface, her hair loose in the first and pinned up in the second, with a crimson ribbon bow tied above the frames" width="200"></p>

![Animated themed scene](scene.svg)

Compares two files and reports a similarity score based on common tokens or lines.

## Install
```sh
git clone https://github.com/ShadowGuard-AI/analyze-code-similarity
cd analyze-code-similarity
```
Standard library only. There are no third party requirements to install.


![Minor divider](sep-light.svg)

## Usage
```sh
python3 main.py FILE1 FILE2 [-m token|line] [-t THRESHOLD] [-v]
```


![Major divider](sep-heavy.svg)

## Parameters
- `FILE1`: path to the first file.
- `FILE2`: path to the second file.
- `-h`: show help message and exit.
- `-m`, `--mode`: comparison mode, `token` (default) or `line`.
- `-t`, `--threshold`: similarity threshold from 0.0 to 1.0. Default: 0.7. Scores below the threshold are reported as dissimilar.
- `-v`, `--verbose`: enable verbose logging.


![Minor divider](sep-light.svg)

## Verified behavior
- Identical files score 1.0000 and are reported similar, in both token and line mode.
- Unrelated files score 0.0000 and are reported dissimilar.
- A missing input file exits 1.
- A threshold outside 0.0 to 1.0 prints a message and exits 1.
- The code compares with `>=`, so a score exactly on the threshold counts as similar.
- Limits, from the code: token mode splits on whitespace only, so punctuation stays attached and case counts. Line mode uses sets, so duplicate lines collapse and line order is ignored.


![Minor divider](sep-light.svg)

## License
MIT License, see LICENSE.

> Logbook entry: the threshold comparison uses greater than or equal, so a score sitting exactly on the threshold counts as similar. A missing input file exits 1, and a threshold outside 0.0 to 1.0 prints a message and exits 1.
> Logbook entry: token mode splits on whitespace only, so punctuation stays attached and case counts. Line mode uses sets, so duplicate lines collapse and line order is ignored.

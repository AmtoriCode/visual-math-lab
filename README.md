# Solving $\int x^2\,dx$ with Manim

A visual and written explanation of why

$$
\int x^2\,dx = \frac{x^3}{3}+C.
$$

## View online

**Interactive project page:** https://amtoricode.github.io/manim-integral-x2/

The page includes the complete 720p animation and a link to the full seven-page companion paper.

## Repository contents

| File | Description |
|---|---|
| [`integral-x2-explainer.mp4`](integral-x2-explainer.mp4) | 53-second Manim animation (720p, 30 FPS) |
| [`integral-x2-paper.pdf`](integral-x2-paper.pdf) | Seven-page illustrated companion paper |
| [`integral-x2-paper.tex`](integral-x2-paper.tex) | LaTeX source for the paper |
| [`manim_script.py`](manim_script.py) | Manim Community Edition source |
| [`plan.md`](plan.md) | Narrative and visual design plan |
| [`index.html`](index.html) | GitHub Pages presentation site |

## What the explanation covers

1. The meaning of an antiderivative
2. Accumulated area under $y=x^2$
3. A Riemann-sum derivation of $a^3/3$
4. The power rule for integration
5. Why the constant of integration is necessary
6. Verification by differentiation
7. The Fundamental Theorem of Calculus
8. Common mistakes and generalizations

## Render the animation

Requires Python 3.10+, Manim Community Edition, LaTeX, and FFmpeg.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
manim -qm manim_script.py \
  Scene1_Question Scene2_Geometry Scene3_PowerRule Scene4_Verify
```

## Compile the paper

```bash
pdflatex integral-x2-paper.tex
pdflatex integral-x2-paper.tex
```

## License

The project source is released under the MIT License.

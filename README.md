# Visual Math Lab

A growing, math-only library of visual explanations. Each question can become a reusable lesson with animation, written derivation, source code, and downloadable materials.

## Website

**https://amtoricode.github.io/visual-math-lab/**

Use the question box to search published lessons. If no lesson matches, it opens a pre-filled GitHub lesson request. Questions asked in the associated Hermes chat can also be developed and added to this same library.

## Published lessons

| Topic | Question | Lesson |
|---|---|---|
| Calculus | How do we solve $\int x^2\,dx$? | [Open lesson](lessons/integral-x2/) |

## Structure

```text
index.html                 General math homepage and question interaction
lessons.json               Searchable lesson catalog
lessons/
  integral-x2/
    index.html             Lesson page
    integral-x2-explainer.mp4
    integral-x2-paper.pdf
    integral-x2-paper.tex
    manim_script.py
    assets/
```

## Adding the next math question

1. Create `lessons/<slug>/`.
2. Add a lesson page and any video, paper, source, and images.
3. Add one metadata object to `lessons.json`.
4. The homepage automatically makes the lesson searchable.
5. Commit and push; GitHub Pages republishes the library.

## Local preview

```bash
python3 -m http.server 8765
```

Then visit `http://localhost:8765`.

## Rendering Manim lessons

Requires Python 3.10+, Manim Community Edition, LaTeX, and FFmpeg.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## License

MIT

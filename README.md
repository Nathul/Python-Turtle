TURTLE ART PROJECTS
====================

This collection contains 4 Python scripts:
- 3 Turtle graphics-based generative art scripts
- 1 Sketch script using the sketchpy library to render a drawing of Tony Stark (Robert Downey Jr.)

---------------------------------------------------
REQUIREMENTS
---------------------------------------------------
✅ Python 3.x

📦 Required Libraries:
- turtle (built-in with Python)
- colorsys (standard)
- re (standard)
- tqdm → install with: pip install tqdm
- svgpathtools → install with: pip install svgpathtools
- sketchpy → install with: pip install sketchpy
- geocoder (optional; not required unless used elsewhere)

To install additional dependencies:
    pip install tqdm svgpathtools sketchpy

---------------------------------------------------
📁 FILE DESCRIPTIONS
---------------------------------------------------

1️⃣ Turtle-1.py
➤ Generates an infinite spiral pattern using HSV colors that shift over time.
➤ Continuously loops and evolves using forward/turn logic.

▶ HOW TO RUN:
    python Turtle-1.py
✴ Close the turtle window manually to stop.

---

2️⃣ Turtle-2.py
➤ Creates a colorful evolving spiral with circles and directional changes.
➤ Uses HSV color model with changing sizes and directions.

▶ HOW TO RUN:
    python Turtle-2.py

---

3️⃣ Turtle-3.py
➤ Converts an SVG file into a Turtle drawing.
➤ Extracts paths and fill colors to draw using Turtle graphics.

📁 Ensure your SVG file (e.g., iron.svg) is in the same folder.

▶ HOW TO RUN:
    python Turtle-3.py

🛠️ To change the SVG:
Edit this line at the bottom of the script:
    pen = sketch_from_svg('your_file.svg', scale=80)

⚠ Notes:
- Only SVGs with path + fill are supported.
- Stroke-only SVGs will be skipped.
- Complex SVGs may take time to render.

---

4️⃣ tony_stark_sketch.py
➤ Uses sketchpy to render a sketch of Robert Downey Jr. (Tony Stark).
➤ Loads the pre-built sketch from sketchpy’s library.

▶ HOW TO RUN:
    python  turtle-4.py

📦 Library used: sketchpy
✴ The drawing window opens automatically and starts rendering.

---

👨‍🎨 AUTHOR
Created by: Nathul.S

TURTLE ART PROJECTS
====================

This collection contains 3 Python scripts using the Turtle graphics module to create vibrant and animated generative art. One script also supports rendering SVG files into Turtle drawings.

--------------------
REQUIREMENTS
--------------------
To run these scripts, you need:

✅ Python 3.x  
✅ The following Python libraries:
   - turtle (comes with Python)
   - colorsys (standard)
   - tqdm (install via pip)
   - svgpathtools (install via pip)
   - re (standard)
   - svg.path (installed with svgpathtools)

To install additional dependencies:
> pip install tqdm svgpathtools

--------------------
FILE DESCRIPTIONS
--------------------

1️⃣ **Turtle-1.py**
   ➤ Generates an infinite spiral pattern using HSV colors that change over time.
   ➤ Continuously loops and evolves the shape using forward and turning logic.

   HOW TO RUN:
   > python Turtle-1.py  
   (Close the Turtle window manually to stop it.)

---

2️⃣ **Turtle-2.py**
   ➤ Creates a colorful evolving spiral with circles and directional changes.
   ➤ Uses the HSV color model to vary colors, with size and direction changes in each loop.

   HOW TO RUN:
   > python Turtle-2.py

---

3️⃣ **Turtle-3.py**
   ➤ Converts an SVG file into a Turtle graphics sketch.
   ➤ Extracts path and fill color from an SVG and draws it with Turtle.

   📁 Make sure your SVG file (e.g., `iron.svg`) is in the same folder.

   HOW TO RUN:
   > python Turtle-3.py

   You can change the SVG file by editing this line at the bottom of the script:
   > pen = sketch_from_svg('your_file.svg', scale=80)

--------------------
NOTES
--------------------
- Turtle graphics windows must be closed manually unless coded otherwise.
- Turtle-3 requires valid SVGs with `fill` paths (strokes only will be skipped).
- Long or complex SVGs may take time to render due to path sampling.

--------------------
AUTHOR
--------------------
Created by: [Nathul.S]

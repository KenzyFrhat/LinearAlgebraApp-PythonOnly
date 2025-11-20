LinearAlgebraApp
=================
PyQt6 desktop application for basic linear algebra operations with clear step-by-step logs.

Features
- Matrix input: choose rows × columns; GUI generates a table for matrix input
- Operations: REF (row echelon form), RREF (reduced row echelon form), Transpose, Inverse
- Steps: REF and RREF show step-by-step operations using Fraction arithmetic for exactness
- Clean modular structure for learning and extension

Run (recommended):
1. python -m venv .venv
2. .\.venv\Scripts\activate    (Windows) or source .venv/bin/activate (macOS/Linux)
3. pip install -r requirements.txt
4. python run.py

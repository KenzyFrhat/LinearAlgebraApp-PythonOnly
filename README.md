# 🎓 **LinearAlgebraApp — PyQt6 Desktop Application**  
*A modern educational tool for Linear Algebra with REF, RREF, Transpose, and Inverse operations.*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyQt-6.6-blue?logo=qt&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
</p>

<p align="center">
  <b>Clean UI</b> • <b>Step-by-step explanations</b> • <b>Exact arithmetic</b> • <b>Perfect for students</b>
</p>

---

# 🌟 **Overview**

**LinearAlgebraApp** is a clean, modern PyQt6 desktop application designed to help students **learn and visualize foundational matrix operations**:

- 🔹 Row Echelon Form (**REF**)  
- 🔹 Reduced Row Echelon Form (**RREF**)  
- 🔹 **Transpose**  
- 🔹 Matrix **Inverse** (with singular matrix detection)  

The app uses **exact arithmetic with Fractions**, providing precise calculations and step-by-step logs for every transformation.

---

# ✨ **Features**

### 🎛️ 1. Dynamic Matrix Input  
- Select rows & columns  
- Editable grid (Excel-like)  
- Clean number formatting  
- English numerals enforced  

### 🧠 2. Exact Ref/Rref Calculations  
- Uses `fractions.Fraction` for precision  
- No floating-point errors  
- Perfect for academic demonstrations  

### 🪜 3. Step-by-Step Logs  
Watch every row operation, pivot, swap, and elimination.  
Ideal for:

- Homework checking  
- Understanding Gaussian elimination  
- Visualizing transformations  

### 🔄 4. Transpose  
Instant row↔column swap.

### 🔁 5. Inverse (Gauss–Jordan method)  
- Full elimination on `[A | I]`  
- Extracts `A⁻¹` when invertible  
- Clear error message for singular matrices  

### 🎨 6. Modern PyQt6 GUI  
- Clean, minimal theme  
- Organized layout  
- Professional look & feel  
- Designed for clarity and learning  

---

# 🖼️ **Screenshots (Add your images here)**

<p align="center">
  <img src="docs/screenshot_main.png" width="70%" />
</p>

<p align="center">
  <img src="docs/screenshot_steps.png" width="70%" />
</p>

---

# 🗂️ **Project Structure**

```bash
LinearAlgebraApp/
│
├── app/
│   ├── gui/            # PyQt6 GUI (widgets, windows)
│   ├── core/           # Linear algebra logic (REF, RREF, etc.)
│   ├── utils/          # Helpers (formatting, parsing)
│   └── app.py          # Main application entry point
│
├── run.py              # Easy launcher
├── requirements.txt
└── README.md
```

---

# 🚀 **Installation & Usage**

### 1️⃣ Clone the repo
```bash
git clone https://github.com/yourusername/LinearAlgebraApp.git
cd LinearAlgebraApp
```

### 2️⃣ Create & activate virtual environment
```bash
python -m venv .venv
```

**Windows:**
```powershell
.\.venv\Scriptsctivate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ (Windows only) Fix Qt plugin issue if needed  
If you get this error:  

> Could not find the Qt platform plugin "windows"

Run:
```powershell
setx QT_QPA_PLATFORM_PLUGIN_PATH ".\.venv\Lib\site-packages\PyQt6\Qt6\plugins\platforms"
```

Restart your terminal.

### 5️⃣ Run the app
```bash
python run.py
```

---

# 🧮 **Math Behind the App**

### 🔵 REF  
Performs forward elimination with row swaps, scaling, and elimination.

### 🔵 RREF  
Full Gauss–Jordan elimination: pivots normalized to 1, zeroing above & below.

### 🔵 Transpose  
Creates a new matrix where rows become columns.

### 🔵 Inverse  
Uses augmented matrix method `[A | I] → [I | A⁻¹]`  
If `A` is singular, user gets a friendly explanation.

---

# 🧪 **Testing**
*(Optional but recommended if you expand the project)*

```
tests/
├── test_ref.py
├── test_rref.py
├── test_inverse.py
└── test_transpose.py
```

---

# 📌 **Roadmap / Future Features**

✔ Export steps as PDF  
✔ Dark mode theme  
✔ Determinant & rank calculator  
✔ Eigenvalues & eigenvectors  
✔ 3D visualizations  
✔ Matrix multiplication  

---

# 🤝 **Contributing**

Pull requests are welcome!

---

# 📄 **License**

MIT License.

---

# 💬 **Contact**

Feel free to reach out with questions or suggestions!

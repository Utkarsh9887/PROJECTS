# TrashTracker

**TrashTracker** is a Python-based waste management system designed to help categorize, track, and manage various types of waste such as:
- E-waste
- Hazardous waste
- Organic waste
- Recyclable and non-recyclable waste
- Industrial waste

## 📁 Project Structure

```
TRASHTRACKER/
│
├── create_db.py             # Initializes the database
├── Interface.py             # Main GUI interface (likely built with Tkinter)
├── e_waste.py               # Handles E-waste management
├── hazardous.py             # Handles hazardous waste tracking
├── industrial_waste.py      # Industrial waste operations
├── non_recyclable.py        # Logic for non-recyclable items
├── recyclable.py            # Recyclable materials logic
├── organic.py               # Manages organic waste
├── segregation.py           # Waste segregation module
├── category.py              # Waste categories
├── ims.db                   # SQLite database file
├── download.png             # UI asset (icon or image)
```

## 🛠 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

> Minimal dependency: `Pillow` (for image handling)

## 🚀 How to Run

1. Ensure you have Python 3 installed.
2. Run the main interface:
```bash
python Interface.py
```

## 📌 Notes

- This app appears to use **Tkinter** for the GUI.
- SQLite is used as the database backend.
- Internal logic is split across several modular `.py` files for clarity and maintainability.

## 📃 License

This project is for educational/demo purposes. Add your license here.

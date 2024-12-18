import os
import sys
import tkinter as tk

def fix_tcl_paths():
    python_path = sys.executable
    base_path = os.path.dirname(python_path)
    
    # Set the correct paths
    os.environ['TCL_LIBRARY'] = os.path.join(base_path, 'tcl', 'tcl8.6')
    os.environ['TK_LIBRARY'] = os.path.join(base_path, 'tcl', 'tk8.6')
    
    # Try to initialize tkinter
    try:
        root = tk.Tk()
        root.destroy()
        print("Tkinter initialization successful!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = fix_tcl_paths()
    if success:
        print(f"TCL_LIBRARY: {os.environ.get('TCL_LIBRARY')}")
        print(f"TK_LIBRARY: {os.environ.get('TK_LIBRARY')}")

        


from pathlib import Path

folder = Path(__file__).parent

print("=== Ransomware Attack Simulation ===")
print("SAFE DEMONSTRATION - NO FILES WILL BE CHANGED")
print()

for name in ("myfile.txt", "sample2.txt"):
    file_path = folder / name
    if file_path.is_file():
        print(f"[SIMULATED] Target identified: {name}")
    else:
        print(f"[SKIPPED] File not found: {name}")

print()
print("[SIMULATED] Ransomware warning:")
print("Your files would be at risk in a real attack.")
print("This demonstration does not encrypt or modify files.")
print()
print("Simulation complete.")
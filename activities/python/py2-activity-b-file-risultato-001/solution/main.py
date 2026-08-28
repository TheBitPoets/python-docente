from pathlib import Path


testo = Path("misure.txt").read_text(encoding="utf-8")
valori = [int(riga) for riga in testo.splitlines() if riga.strip() != ""]
totale = sum(valori)

Path("risultato.txt").write_text(f"{totale}\n", encoding="utf-8")

import matplotlib.pyplot as plt
import numpy as np

# Namen der Entwicklungsphasen
phases = ['Anforderungen', 'Design', 'Programmierung', 'Entwicklungstests', 'Akzeptanztests', 'Betrieb']

# Kostenfaktor für Fehlerbehebung
factors = [1, 5, 10, 25, 50, 500]

# X-Achsenpositionen
x = np.arange(len(phases))

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Horizontale Gitterlinien (zuerst, damit sie hinter den Balken liegen)
ax.yaxis.grid(True, linestyle='--', alpha=0.7, zorder=0)

# Balken (zorder > Grid)
bars = ax.bar(x, factors, width=0.6, color='orange', zorder=3)

# Achsenbeschriftung
ax.set_ylabel('Durchschnittlicher Kostenfaktor')
ax.set_xticks(x)
ax.set_xticklabels(phases)

plt.tight_layout()

# Diagramm speichern (optional)
plt.savefig("figures/cost_of_failure.png", dpi=300)

# Diagramm anzeigen
#plt.show()

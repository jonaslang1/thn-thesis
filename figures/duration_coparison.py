import matplotlib.pyplot as plt
import numpy as np

# Namen der Microservices
services = ['Instanz-Management', 'Regel', 'Reporting', 'Proxy', 'Nutzeroberfläche']

# Messdaten (10 Messungen je Service & Testtyp)
contract_measurements = [
    [83, 84, 77, 79, 80, 79, 84, 80, 82, 82],  # Instanz-Management
    [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],  # Regel
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],           # Reporting
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14], # Proxy
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]  # Nutzeroberfläche
]

integration_measurements = [
    [258, 260, 255, 248, 250, 244, 250, 259, 249, 243],  # Instanz-Management
    [25, 25, 25, 25, 25, 25, 25, 25, 25, 25],  # Regel
    [18, 18, 18, 18, 18, 18, 18, 18, 18, 18],  # Reporting
    [22, 22, 22, 22, 22, 22, 22, 22, 22, 22],  # Proxy
    [19, 19, 19, 19, 19, 19, 19, 19, 19, 19]   # Nutzeroberfläche
]

# Durchschnitt berechnen und runden (auf ganze Zahlen)
contract_times = [round(np.mean(times)) for times in contract_measurements]
integration_times = [round(np.mean(times)) for times in integration_measurements]

# X-Achsenpositionen
x = np.arange(len(services))
width = 0.35

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, contract_times, width, label='Contract Tests', color='skyblue')
bars2 = ax.bar(x + width/2, integration_times, width, label='Integrationstests', color='lightcoral')

# Beschriftung
ax.set_ylabel('Durchschnittliche Ausführungsdauer (s)')
ax.set_xticks(x)
ax.set_xticklabels(services)
ax.legend()

# Werte anzeigen
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(bars1)
autolabel(bars2)

plt.tight_layout()

# Diagramm speichern
plt.savefig("figures/testing_duration_comparison.png", dpi=300)
# Diagramm anzeigen
#plt.show()

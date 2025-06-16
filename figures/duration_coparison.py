import matplotlib.pyplot as plt
import numpy as np

# Namen der Microservices
services = ['Instanz-Management', 'Regel', 'Reporting', 'Proxy', 'Nutzeroberfläche']

# Messdaten (10 Messungen je Service & Testtyp)
contract_measurements = [
    [72, 81, 77, 73, 74, 79, 73, 80, 82, 82],  # Instanz-Management
    [44, 41, 34, 31, 30, 33, 39, 31, 32, 31],  # Regel
    [44, 43, 38, 38, 37, 38, 38, 40, 34, 38],  # Reporting
    [48, 38, 39, 47, 42, 42, 41, 43, 45, 44],  # Proxy
    [22, 25, 22, 23, 24, 20, 21, 23, 21, 22]   # Nutzeroberfläche
]

integration_measurements = [
    [258, 260, 255, 248, 250, 244, 250, 259, 249, 243],  # Instanz-Management
    [ 54,  48,  49,  49,  46,  50,  58,  47,  51,  56],  # Regel
    [ 84,  74,  67,  67,  63,  68,  69,  69,  67,  65],  # Reporting
    [284, 274, 291, 288, 289, 304, 293, 301, 300, 314],  # Proxy
    [234, 285, 266, 254, 251, 257, 262, 267, 249, 261]   # Nutzeroberfläche
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

# Latex Tabelle erstellen
# Contract Measurements Table
print("\\begin{table}[ht]")
print("\\centering")
print("\\caption{Contract-Test-Messwerte pro Service}")
print("\\label{tab:contract_measurements}")
print("\\begin{tabular}{l|" + "c" * 10 + "}")
print("\\toprule")
print("Service & " + " & ".join([f"M{i+1}" for i in range(10)]) + " \\\\")
print("\\midrule")
for s, row in zip(services, contract_measurements):
    print(f"{s} & " + " & ".join(str(val) for val in row) + " \\\\")
print("\\bottomrule")
print("\\end{tabular}")
print("\\end{table}\n")

# Integration Measurements Table
print("\\begin{table}[ht]")
print("\\centering")
print("\\caption{Integrationstest-Messwerte pro Service}")
print("\\label{tab:integration_measurements}")
print("\\begin{tabular}{l|" + "c" * 10 + "}")
print("\\toprule")
print("Service & " + " & ".join([f"M{i+1}" for i in range(10)]) + " \\\\")
print("\\midrule")
for s, row in zip(services, integration_measurements):
    print(f"{s} & " + " & ".join(str(val) for val in row) + " \\\\")
print("\\bottomrule")
print("\\end{tabular}")
print("\\end{table}")
import pandas as pd
import matplotlib.pyplot as plt

# Örnek veri seti
data = {
    "Kategori": ["A", "B", "C", "D"],
    "Satış": [200, 150, 300, 250]
}
df = pd.DataFrame(data)


# Grafik çizimi
plt.bar(df["Kategori"], df["Satış"])
plt.title("Kategori Bazında Satış")
plt.xlabel("Kategori")
plt.ylabel("Satış Miktarı")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. VERİ SETİNİ OLUŞTURMA (Hata riskini sıfırlamak için manuel veri)
data = {
    'Yaş': [25, 32, 47, 51, 62, 23, 39, 45, 50, 55],
    'Kolesterol': [180, 210, 240, 250, 280, 190, 220, 230, 260, 270],
    'Kalp_Riski': ['Düşük', 'Düşük', 'Yüksek', 'Yüksek', 'Yüksek', 'Düşük', 'Düşük', 'Yüksek', 'Yüksek', 'Yüksek'],
    'Günlük_Adım': [10000, 8000, 5000, 4000, 3000, 12000, 9000, 6000, 3500, 2500]
}

df = pd.DataFrame(data)

# 2. GÖRSELLEŞTİRME: Yaş vs Kolesterol (Risk Durumuna Göre)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Yaş', y='Kolesterol', hue='Kalp_Riski', s=100, palette='RdYlGn_r')

plt.title('Yaş ve Kolesterol İlişkisi (Sağlık Analizi)')
plt.xlabel('Yaş')
plt.ylabel('Kolesterol Seviyesi')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 3. VERİYİ KONTROL ET
print("Analiz Edilen Veri Tablosu:")
print(df)
import plotly.express as px

# İnteraktif Grafik Oluşturma
fig = px.scatter(df, x="Yaş", y="Kolesterol", color="Kalp_Riski",
                 size="Günlük_Adım", hover_data=['Yaş'],
                 title="Sağlık Metrikleri İnteraktif Analizi")

# Grafiği tarayıcıda açar
fig.show()
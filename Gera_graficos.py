import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# CONFIGURAÇÕES
# -------------------------------
ARQUIVO = "dados_imu_inicial.csv"

# -------------------------------
# LEITURA DO CSV
# -------------------------------
df = pd.read_csv(ARQUIVO)

# Verifica se existe coluna 'tempo_s'
if "tempo_s" in df.columns:
    t = df["tempo_s"]
else:
    # Se não existir, cria a partir do índice (assume TS=0.2 s)
    TS = 0.2
    t = range(len(df))
    t = [x*TS for x in t]

'''
# -------------------------------
# PLOT 1: Aceleração (gX, gY, gZ)
# -------------------------------
plt.figure(figsize=(10,5))
plt.plot(t, df["gX"], label="gX", color="r")
plt.plot(t, df["gY"], label="gY", color="g")
plt.plot(t, df["gZ"], label="gZ", color="b")
plt.xlabel("Tempo [s]")
plt.ylabel("Aceleração [g]")
plt.title("Valores de Aceleração (IMU)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# PLOT 2: Ângulos (angleX, angleY, angleZ)
# -------------------------------
plt.figure(figsize=(10,5))
plt.plot(t, df["angleX"], label="Angle X", linestyle="--", color="r")
plt.plot(t, df["angleY"], label="Angle Y", linestyle="--", color="g")
plt.plot(t, df["angleZ"], label="Angle Z", linestyle="--", color="b")
plt.xlabel("Tempo [s]")
plt.ylabel("Ângulo [°]")
plt.title("Ângulos calculados pela IMU")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# PLOT 3: Pitch e Roll
# -------------------------------
plt.figure(figsize=(10,5))
plt.plot(t, df["pitch"], label="Pitch", color="m")
plt.plot(t, df["roll"], label="Roll", color="c")
plt.xlabel("Tempo [s]")
plt.ylabel("Ângulo [°]")
plt.title("Pitch e Roll")
plt.legend()
#plt.ylim(-1, 1)
plt.grid(True)
plt.tight_layout()
plt.show()
'''

# Cria uma figura com 3 subplots em linha
fig, axes = plt.subplots(1, 3, figsize=(15, 5))


# -------------------------------
# PLOT 1: Acceleration (gX, gY, gZ)
# -------------------------------
axes[0].plot(t, df["gX"], label="gX", color="r")
axes[0].plot(t, df["gY"], label="gY", color="g")
axes[0].plot(t, df["gZ"], label="gZ", color="b")
axes[0].set_xlabel("Time [s]")
axes[0].set_ylabel("Acceleration [g]")
axes[0].set_title("Acceleration Values (IMU)")
axes[0].legend()
axes[0].grid(True)

# -------------------------------
# PLOT 2: Angles (angleX, angleY, angleZ)
# -------------------------------
axes[1].plot(t, df["angleX"], label="Angle X", linestyle="--", color="r")
axes[1].plot(t, df["angleY"], label="Angle Y", linestyle="--", color="g")
axes[1].plot(t, df["angleZ"], label="Angle Z", linestyle="--", color="b")
axes[1].set_xlabel("Time [s]")
axes[1].set_ylabel("Angle [°]")
axes[1].set_title("Angles Computed by IMU")
axes[1].legend()
axes[1].grid(True)

# -------------------------------
# PLOT 3: Pitch and Roll
# -------------------------------
axes[2].plot(t, df["pitch"], label="Pitch", color="m")
axes[2].plot(t, df["roll"], label="Roll", color="c")
axes[2].set_xlabel("Time [s]")
axes[2].set_ylabel("Angle [°]")
axes[2].set_title("Pitch and Roll")
#plt.ylim(-1, 1)
axes[2].legend()
axes[2].grid(True)

# Ajusta layout
plt.tight_layout()
plt.show()

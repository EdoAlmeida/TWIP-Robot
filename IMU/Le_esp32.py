import serial
import csv
import time

# -------------------------------
# CONFIGURAÇÕES
# -------------------------------
PORTA = "COM7"          # altere para sua porta serial
BAUDRATE = 115200
TIMEOUT = 1
TS = 0.2                # intervalo de amostragem em segundos
TEMPO_TOTAL = 60       # tempo total de aquisição em segundos
ARQUIVO = "dados_imu.csv"

# -------------------------------
# FUNÇÃO PRINCIPAL
# -------------------------------
def main():
    try:
        ser = serial.Serial(PORTA, BAUDRATE, timeout=TIMEOUT)
        time.sleep(2)  # aguarda inicialização do ESP32

        # Ler cabeçalho do ESP32
        cabecalho = ser.readline().decode().strip().split(",")
        cabecalho = ["tempo_s"] + cabecalho  # adiciona coluna de tempo

        n_amostras = int(TEMPO_TOTAL / TS)

        with open(ARQUIVO, mode="w", newline="") as f:
            escritor = csv.writer(f)
            escritor.writerow(cabecalho)

            print(f"Iniciando aquisição por {TEMPO_TOTAL} segundos...")

            for i in range(n_amostras):
                linha = ser.readline().decode(errors="ignore").strip()
                if not linha:  # pula linhas vazias
                    continue

                dados = linha.split(",")
                if len(dados) != len(cabecalho)-1:
                    continue  # pula linhas incompletas

                tempo_relativo = round(i * TS, 3)
                escritor.writerow([tempo_relativo] + dados)
                f.flush()

                print(f"{tempo_relativo:.2f} s | " + ", ".join(dados))

            print("Aquisição finalizada!")

    except Exception as e:
        print(f"Erro: {e}")

# -------------------------------
if __name__ == "__main__":
    main()

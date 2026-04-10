# 🚀 Automated Crypto Trading Bot (Binance Spot)

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Binance](https://img.shields.io/badge/Exchange-Binance-yellow.svg)

## 📌 Descripción
Este es un bot de trading sistemático desarrollado en Python para operar en el mercado Spot de Binance. El sistema utiliza un algoritmo basado en el cruce de Medias Móviles Exponenciales (EMA) y una gestión de riesgo avanzada con Stop Loss dinámico para maximizar ganancias y proteger el capital de forma automática.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.14
* **Librería de Conexión:** `ccxt` (para interactuar con la API de Binance).
* **Análisis de Datos:** `pandas` para el cálculo de indicadores técnicos.
* **Gestión de Tiempo:** `time` para el control de ciclos de monitoreo.

## 📈 Estrategia Técnica
El bot opera bajo una lógica de seguimiento de tendencia:
1. **Señal de Compra:** Se activa cuando la **EMA 9** cruza por encima de la **EMA 21** (Cruce de Oro).
2. **Señal de Venta:** Se activa por cruce inverso o mediante el **Stop Loss Dinámico**.
3. **Gestión de Riesgo:** - **Stop Loss Inicial:** 1.5% del precio de entrada.
   - **Trailing Stop:** El nivel de protección se ajusta automáticamente a medida que el precio sube, asegurando ganancias latentes.

## ⚙️ Configuración e Instalación
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)

Instalar las dependencias necesarias:

Bash
pip install ccxt pandas
Configurar tus credenciales de API en las variables API_KEY y SECRET_KEY.

Ejecutar el bot:

Bash
python bot.py
   

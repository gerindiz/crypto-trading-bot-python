# 🚀 Automated Crypto Trading Bot (Binance Spot) v2.0

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Binance](https://img.shields.io/badge/Exchange-Binance-yellow.svg)
![Twilio](https://img.shields.io/badge/Notifications-Twilio-red.svg)

<img width="1192" height="956" alt="bot python" src="https://github.com/user-attachments/assets/60a7a158-3de4-46f7-8377-2798072421f0" />

## 📝 Descripción
Este es un bot de trading sistemático desarrollado en Python para operar en el mercado Spot de Binance. El sistema utiliza un algoritmo basado en el cruce de Medias Móviles Exponenciales (EMA) y una gestión de riesgo avanzada con **Trailing Stop Loss dinámico** y **notificaciones en tiempo real vía WhatsApp**.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.14+
* **Librería de Conexión:** `ccxt` (para interactuar con la API de Binance).
* **Análisis de Datos:** `pandas` para el cálculo de indicadores técnicos.
* **Notificaciones:** `twilio` para alertas automatizadas a WhatsApp.
* **Persistencia:** CSV Logging para auditoría de operaciones.

## 📈 Estrategia Técnica
El bot opera bajo una lógica de seguimiento de tendencia:
1. **Señal de Compra:** Se activa cuando la **EMA 9** cruza por encima de la **EMA 21** (Cruce de Oro).
2. **Señal de Venta:** Se activa por cruce inverso o mediante el **Stop Loss Dinámico**.
3. **Gestión de Riesgo:** * **Stop Loss Inicial:** 1.5% del precio de entrada.
    * **Trailing Stop:** El nivel de protección se ajusta automáticamente a medida que el precio sube, asegurando ganancias latentes.
    * **Profit Target:** Alerta automática al alcanzar un **8% de ganancia**.

## 📱 Sistema de Alertas & Reportes
* **WhatsApp en Vivo:** Notificaciones inmediatas en cada ejecución de compra, venta o cumplimiento de objetivos.
* **Reportes Quincenales:** Generación automática de un resumen de rendimiento los días 1 y 15 de cada mes a las 10:00 AM.
* **Registro Histórico:** Almacenamiento local en `historial_posicion.csv` con datos de precio y porcentaje de ganancia minuto a minuto.

## ⚙️ Configuración e Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/gerindiz/crypto-trading-bot-python.git](https://github.com/gerindiz/crypto-trading-bot-python.git)

## ⚙️ Configuración e Instalación
1. Clonar el repositorio:
   ```bash
   git clone (https://github.com/gerindiz/crypto-trading-bot-python.git)

Instalar las dependencias necesarias:

Bash
pip install ccxt pandas
Configurar tus credenciales de API en las variables API_KEY y SECRET_KEY.

Ejecutar el bot:

Bash
python bot.py
   

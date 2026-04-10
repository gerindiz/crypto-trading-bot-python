import ccxt
import pandas as pd
import time
import math

# =========================================================
# CONFIGURACIÓN NIVEL PROFESIONAL - MODO SEGURIDAD
# =========================================================
API_KEY = 'TU_API_KEY_AQUI'
SECRET_KEY = 'TU_SECRET_KEY_AQUI'

# CAMBIO CLAVE: Iniciamos en True para que reconozca tu compra anterior
posicion_abierta = True 
precio_entrada = 72094.0   # Precio al que compraste hoy
max_precio_alcanzado = 72094.0 

# ESTRATEGIA: 1.5% de riesgo inicial con Trailing Stop
stop_loss_inicial = 0.015  
take_profit_objetivo = 0.08 # 8% de ganancia

def truncar(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def obtener_datos():
    v_ohlcv = exchange.fetch_ohlcv(simbolo, timeframe='1h', limit=100)
    df = pd.DataFrame(v_ohlcv, columns=['fecha', 'open', 'high', 'low', 'close', 'volume'])
    df['ema_9'] = df['close'].ewm(span=9, adjust=False).mean()
    df['ema_21'] = df['close'].ewm(span=21, adjust=False).mean()
    return df

print("🛡️ Iniciando Bot: Modo Continuidad (Posición Detectada)")
print(f"📊 Precio de entrada registrado: ${precio_entrada}")

while True:
    try:
        df = obtener_datos()
        u_precio = df['close'].iloc[-1]
        u_ema9 = df['ema_9'].iloc[-1]
        u_ema21 = df['ema_21'].iloc[-1]

        # --- LÓGICA DE COMPRA (Solo si cerramos la actual) ---
        if u_ema9 > u_ema21 and not posicion_abierta:
            if u_precio > u_ema9:
                print(f"🚀 SEÑAL CONFIRMADA: Comprando a ${u_precio}")
                exchange.create_market_buy_order(simbolo, cantidad_usdt / u_precio)
                precio_entrada = u_precio
                max_precio_alcanzado = u_precio
                posicion_abierta = True

        # --- LÓGICA DE VENTA PRO (TRAILING STOP) ---
        elif posicion_abierta:
            # Actualizamos el pico más alto para que el SL suba
            if u_precio > max_precio_alcanzado:
                max_precio_alcanzado = u_precio
            
            # El Stop Loss dinámico siempre está 1.5% debajo del máximo precio visto
            stop_loss_dinamico = max_precio_alcanzado * (1 - stop_loss_inicial)

            # Consultamos saldo real para evitar errores de precisión
            saldo_actual = exchange.fetch_balance()
            btc_total = saldo_actual['total'].get('BTC', 0)
            btc_para_vender = truncar(btc_total, 5) 

            # 1. Ejecución de Trailing Stop Loss (Protección)
            if u_precio <= stop_loss_dinamico:
                print(f"🛡️ TRAILING STOP ACTIVADO. Protegiendo en ${u_precio}")
                if btc_para_vender > 0:
                    exchange.create_market_sell_order(simbolo, btc_para_vender)
                    posicion_abierta = False
                    ganancia = ((u_precio/precio_entrada)-1)*100
                    print(f"✅ Venta cerrada. Rendimiento de la operación: {ganancia:.2f}%")

            # 2. Take Profit Objetivo (8%)
            elif u_precio >= (precio_entrada * (1 + take_profit_objetivo)):
                print(f"🎯 OBJETIVO ALCANZADO (+8%). Vendiendo a ${u_precio}")
                if btc_para_vender > 0:
                    exchange.create_market_sell_order(simbolo, btc_para_vender)
                    posicion_abierta = False

            # 3. Salida por Cruce (Seguridad extra si la tendencia muere)
            elif u_ema9 < u_ema21:
                print(f"📉 Tendencia debilitada (Cruce bajista). Cerrando a ${u_precio}")
                if btc_para_vender > 0:
                    exchange.create_market_sell_order(simbolo, btc_para_vender)
                    posicion_abierta = False

        # El monitor ahora te muestra el SL que te va siguiendo
        print(f"[{time.strftime('%H:%M:%S')}] BTC: ${u_precio:.2f} | EMA9: {u_ema9:.1f} | SL Dinámico: ${stop_loss_dinamico:.2f}")
        time.sleep(60)

    except Exception as e:
        print(f"⚠️ Error: {e}")
        time.sleep(10)
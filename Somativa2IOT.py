# TRABALHO FINAL FUNDAMENTOS DA INTERNET DAS COISAS 
#Aluno : Divansir de Ramos Scrobut Júnior
#Curso : Análise e desenvolvimento de sistemas
#PUC-PR 2023,20/09/2023

import dht
import machine
import time
import urequests
import network

# Função para conectar-se à rede Wi-Fi
def conectar_wifi(ssid, password):
    # Cria uma instância de WLAN e a ativa
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    # Conecta-se à rede Wi-Fi especificada com o SSID e senha fornecidos
    wifi.connect(ssid, password)
    
    # Aguarda até que o dispositivo esteja conectado à rede Wi-Fi
    while not wifi.isconnected():
        pass

# Função para ler o sensor DHT11
def ler_sensor_dht(pin):
    # Configura o pino onde o sensor DHT11 está conectado
    dht_pin = machine.Pin(pin)
    # Cria uma instância do sensor DHT11
    dht_sensor = dht.DHT11(dht_pin)
    # Realiza uma medição do sensor
    dht_sensor.measure()
    # Obtém a temperatura e umidade medidas pelo sensor
    temperatura = dht_sensor.temperature()
    umidade = dht_sensor.humidity()
    return temperatura, umidade

# Função para controlar o relé
def controlar_rele(pin, estado):
    # Configura o pino onde o relé está conectado como saída (OUT)
    relay_pin = machine.Pin(pin, machine.Pin.OUT)
    # Define o estado do relé (1 para ligar, 0 para desligar)
    relay_pin.value(estado)
    return estado

# Função para enviar dados para o ThingSpeak
def enviar_para_thingspeak(api_key, temperatura, umidade, rele_estado):
    # URL da API do ThingSpeak para enviar dados
    url = "https://api.thingspeak.com/update"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    # Formata os dados a serem enviados (API key, temperatura, umidade e estado do relé)
    data = "api_key={}&field1={}&field2={}&field3={}".format(api_key, temperatura, umidade, rele_estado)
    # Envia os dados para o ThingSpeak usando uma solicitação POST
    response = urequests.post(url, headers=headers, data=data)
    response.close()

# Configuração da rede Wi-Fi
ssid = "NOMEDOWIFI"  # SSID da rede Wi-Fi
password = "SENHADOWIFI"   # Senha da rede Wi-Fi
conectar_wifi(ssid, password)

# Configuração dos pinos do sensor DHT11 e do relé
dht_pin = 4    # Pino onde o sensor DHT11 está conectado
relay_pin = 2  # Pino onde o relé está conectado

# Chave da API do ThingSpeak
thingspeak_api_key = "APIKEY"

# Intervalo de leitura e envio de dados para o ThingSpeak (em segundos)
intervalo_leitura = 5

# Inicializa o estado do relé como desligado (0)
estado_rele = 0

# Loop principal
while True:
    try:
        # Lê os valores de temperatura e umidade do sensor DHT11
        temperatura, umidade = ler_sensor_dht(dht_pin)
        print("Temperatura = {}°C, Umidade = {}%".format(temperatura, umidade))
        
        # Controla o relé com base nos valores lidos do sensor e atualiza o estado do relé
        if temperatura > 31 or umidade > 70:
            print("Rele ligado")
            estado_rele = controlar_rele(relay_pin, 1)
        else:
            print("Rele desligado")
            estado_rele = controlar_rele(relay_pin, 0)
        
        # Envia os dados para o ThingSpeak
        enviar_para_thingspeak(thingspeak_api_key, temperatura, umidade, estado_rele)
        
        # Aguarda pelo intervalo de leitura antes de continuar
        time.sleep(intervalo_leitura)
        
    except Exception as e:
        print("Erro:", e)
        print("Aguardando 5 segundos antes de tentar novamente.")
        time.sleep(5)


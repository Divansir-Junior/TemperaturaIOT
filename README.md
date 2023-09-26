Este projeto consiste na implementação de um sistema de monitoramento ambiental utilizando um microcontrolador ESP8266, um sensor de temperatura e umidade DHT11 e um relé para controle de dispositivos externos.

Funcionalidades
Conexão à rede Wi-Fi
Leitura de dados do sensor DHT11
Controle de um dispositivo através do relé
Envio de dados para o ThingSpeak
Como Utilizar : 
Configuração da Rede Wi-Fi:
Substitua NOMEDOWIFI pelo nome da sua rede Wi-Fi.
Substitua SENHADOWIFI pela senha da sua rede Wi-Fi.

ssid = "NOMEDOWIFI"  # SSID da rede Wi-Fi
password = "SENHADOWIFI"   # Senha da rede Wi-Fi
Configuração dos Pinos:
Defina os pinos onde o sensor DHT11 e o relé estão conectados.
python
Copy code
dht_pin = 4    # Pino onde o sensor DHT11 está conectado
relay_pin = 2  # Pino onde o relé está conectado
Chave da API ThingSpeak:
Substitua "APIKEY" pela sua chave de API do ThingSpeak.
python
Copy code
thingspeak_api_key = "APIKEY"
Intervalo de Leitura:
Defina o intervalo de leitura e envio de dados para o ThingSpeak em segundos.
python
Copy code
intervalo_leitura = 5
Execução:
Carregue o código no microcontrolador ESP8266.

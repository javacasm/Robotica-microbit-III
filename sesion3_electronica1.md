# Sesión 3 - microbit + electrónica

## Maqueen a fondo

[Documentación dfrobot](https://wiki.dfrobot.com/micro_Maqueen_for_micro_bit_SKU_ROB0148-EN)


![pinout](./images/maqueenv2_pinout.png)

![](./images/descripcionMaqueen.jpeg)

1. Sensor de línea: 2 sensores digitales blanco y negro (Niveles alto y bajo)
2. Buzzer: Tonos y música para tu proyecto
3. Infrarrojo: Receptor infrarrojo para controlar tu Maqueen (Decodificador NEC)
4. LEDs indicadores frontales: 2  LEDs color rojo difuso
5. LEDs RGB multicolor de ambiente: 4 LEDs capaces de hacer hasta 16 millones de colores
6. Sensor de distancia ultrasónico: 1SR04, SR04P (5V)
7. Conector para comunicación I2C: sólo funciona con 3.3V
8. Puertos para servomotor: 2 líneas
9. Conector para pines digitales multipropósito
10. Conector para micro:bit


## Pinout

v2

![Pinout v2](./images/edge-connector-2.svg)

v1

![Pinout](./images/edge_connector.svg)

[Detalles](https://tech.microbit.org/hardware/edgeconnector/)

Es openSource [Esquema electrónico](https://tech.microbit.org/hardware/schematic/)

## Componentes y conexiones maqueen


## Extensor

Tipos y variedades:

* Para cables con pinzas/cocodrilos

![](./images/KS0434-000-650x350)

Existen kits con todo tipo de componentes, como [los de MonkMakes](https://monkmakes.com/products.html)

![](./images/fan_project_web.jpeg)

para cables

![](./images/sensorbit-extensor-io-para-microbit.jpeg)

para protoboard

![](./images/placa-extension-tipo-t-protoboard-gpio-para-microbit-con-salida-de-5v-y-33-v.webp)

con motores


[Extensor Keyestudio KS0360 Sensor shield v2](https://wiki.keyestudio.com/Ks0360_Keyestudio_Sensor_Shield_V2_for_BBC_micro:bit)

![](./images/KS0360_400px.jpeg)

[Más detalle](./images/KS0360_1500px.jpeg)



### Alimentación

USB o power

## LCD

Añadimos la extensión 

Primero hay que inicializar la p

![](./images/programa_temp_luz_lcd.png)


### Extensión makerkit

Crear caracter de usuario

![](./images/programa_makerkit_crear_caracter.png)

Mostramos los datos y los carateres de usuario

![](./images/programa_makerkit_mostrarDatos.png)

Otra de las ventajas de esta librería es que nos facilita el cálculo de la posición y la confección de las pantallas

![](./images/programa_makerbit_seleccion_posicion.png)

[Proyecto](https://github.com/javacasm/Robotica-microbit-III/tree/main)
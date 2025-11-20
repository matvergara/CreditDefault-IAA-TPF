# 💳 De la deuda al dato: *Machine Learning* para predecir defaults 

Modelado predictivo a partir de datos crediticios de Taiwán (año 2005) bajo el marco del **Trabajo Práctico Final** para la materia *Introducción al Aprendizaje Automático* (LCD-UNSAM)

---

## 📚 Contexto

En el año 2005, Taiwán sufrió una crisis en su sistema bancario originada por el impago de las tarjetas de crédito por parte de los clientes de los bancos. Las causas estructurales pueden encontrarse en la falta de responsabilidad por parte de las entidades bancarias al evaluar a sus potenciales clientes y en las dificultades de estos últimos para afrontar los gastos por la coyuntura del país en ese momento. 

A pesar de esas condiciones iniciales, **¿los bancos se podrían haber anticipado a la situación e identificado a potenciales deudores con anterioridad?**

## 🎯 Definición del Problema

El impago de tarjetas de crédito genera múltiples problemáticas a las entidades bancarias entre las que se encuentran: pérdidas por créditos incobrables, costos de recuperación (gestión de cobranza, procesos judiciales, etc.), impacto en el flujo de caja que afecta directamente la capacidad de otorgar nuevos créditos, un deterioro en la reputación del banco sobre la calidad de su gestión, entre otros.

Por todas estas razones, resulta clave para estas entidades anticiparse a la situación e identificar con tiempo y efectividad al segmento de clientes con mayores probabilidades de entrar en mora. Teniendo esta información se pueden dirigir los esfuerzos especificamente a ese grupo, tomando medidas preventivas en etapas tempranas de la deuda e incluso mejorar los criterios de decisión previos para el otorgamiento de nuevo crédito.

## 💡 Solución Propuesta

En este proyecto trabjamos con la familia de modelos de árboles de decisión para identificar a potenciales deudores utilizando datos demográficos y de comportamiento financiero para el aprendizaje de los modelos. 

Dado que el costo de no identificar a clientes deudores es mucho más elevado al costo de catalogar como deudor a un cliente que al final paga su deuda (en este último caso la pérdida económica solo implicaría la primera etapa de la gestión de cobranza), buscaremos optimizar el modelo para que **maximice el** ***recall*** que es justamente la métrica que nos indica la capacidad de identificar a deudores reales sobre todo el total de deudores. 

## 📊 Resultados principales

Utilizando técnicas de optimización de hiperparámetros como GridSearchCV nos acercamos a un modelo que identifica con a 77 de cada 100 deudores. La cantidad de meses de deuda acumulados junto al limite de crédito son claves a la hora de hacer esta predicción

## 📁 Estructura del proyecto
```
CreditDefault-LCD-TPF/
├── data/                       # Sets de datos crudos y procesados
│   ├── raw/
│   └── processed/
├── src/                       # Código fuente para cada etapa del desarrollo
│   ├── data/                  # Carga de datos y preprocesamiento
│   └── models/                # Desarrollo de modelo
├── requirements.txt           # Lista de librerías necesarias 
└── README.md  
```

## 📩 Datos Utilizados

El dataset obtenido desde [UCI Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients), fue recolectado por los autores (Yeh y Lien, 2009) con el objetivo de evaluar la precisión predictiva de la probabilidad de default a través de distintos metodos de minería de datos. 

Este conjunto de datos contiene observaciones de pago de clientes de un banco taiwanés en el año 2005, incluyendo variables demográficas (genero, estado civil, edad, nivel educativo), variables categoricas que describen el estado de pago de un mes dado para el periodo Abril-Septiembre y variables numéricas que describen tanto la factura a pagar en cada uno de esos meses como el pago efectivo realizado por la persona en dicho mes. También se incluye la linea de crédito de la persona y un estado binario para el mes de octubre que indica si la persona pago su resumen en ese mes. En este proyecto trabajamos con los datos de septiembre para predecir el default en octubre.

## 🛠️ Tecnologías utilizadas
- **Python 3.14** - Lenguaje de desarrollo
- **Jupyter Notebooks** - Entorno interactivo para análisis y documentación
- **scikit-learn** - Implementación de modelos y pipelines de ML
- **seaborn & matplotlib** - Visualización de datos y resultados
- **numpy & pandas** - Manipulación y análisis de datos

## 📈 Metodología
1. **

2. Obtuvimos los datos desde ***UCI ML Repository***, tradujimos variables al español y realizamos la limpieza de registros inconsistentes con el problema de negocio, como clientes con transiciones de deuda incoherentes. También reagrupamos datos mal catalogados en la fuente original.

3. **Feature Engineering


## 🧠 Conclusiones y Aprendizajes


## 🧑‍💻 Autores | Contacto
Estamos abiertos a recibir ideas, sugerencias o comentarios! Podes contactarnos por LinkedIn o Gmail.
- **Bruno Inguanzo** · [LinkedIn](https://www.linkedin.com/in/bruno-inguanzo-974021212/) · [brunoinguanzo14@gmail.com](mailto:brunoinguanzo14@gmail.com)
- **Javier Valdez** · [LinkedIn](https://www.linkedin.com/in/javiervaldez2/) · [javiervaldez145@gmail.com](mailto:javiervaldez145@gmail.com) 
- **Matías Vergara** · [LinkedIn](https://www.linkedin.com/in/matiasvergaravicencio/) · [ma.vergaravicencio@gmail.com](mailto:ma.vergaravicencio@gmail.com)
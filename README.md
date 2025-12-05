# 📌 **Encargo 3 – Pruebas de Carga y Rendimiento con Locust**

**Asignatura:** *Calidad de Software – DUOC UC*

---

## 📖 **Descripción General**

Este repositorio contiene el desarrollo completo del **Encargo 3**, enfocado en la ejecución de **pruebas de carga, estrés y medición de tiempos de respuesta** utilizando **Locust**, junto a un **informe final** con análisis y recomendaciones.

La entrega incluye:

* ✔ **Tres scripts en Python** con distintos escenarios de prueba.
* ✔ **Un informe final** con resultados, evidencias y conclusiones técnicas.

El objetivo principal es evaluar el rendimiento de un sitio web bajo diferentes escenarios, midiendo:

* ⏱ **Tiempo de respuesta**
* 👥 **Carga realista** (usuarios navegando normalmente)
* 🔥 **Carga extrema** (stress test)

Con ello se busca determinar si el sistema cumple los **requisitos no funcionales** de rendimiento exigidos por la industria.

---

# 📂 **Contenido del Repositorio**

```
📁 Calidad-de-software-prueba-3
│
├── 📁 scripts
│   ├── 📄 script_1_medicion_basica.py
│   ├── 📄 script_2_carga_realista.py
│   └── 📄 script_3_carga_extrema.py
├── 📄 requirements.txt
└── 📄 README.md
```

---

# 🧪 **Descripción de los Scripts**

## 1️⃣ Script de Medición Básica – *script_1_medicion_basica.py*

Este script ejecuta solicitudes simples al sitio para obtener:

* Tiempos de respuesta por URL
* Errores o fallos en el servidor
* Promedios y variaciones básicas

🔍 Permite establecer la **línea base** del rendimiento.

---

## 2️⃣ Script de Carga Realista – *script_2_carga_realista.py*

Simula usuarios reales:

* Flujos de navegación comunes
* Intervalos entre solicitudes
* Carga moderada y controlada

🎯 Evalúa cómo se comporta el sitio en condiciones normales de uso.

---

## 3️⃣ Script de Carga Extrema – *script_3_carga_extrema.py*

Diseñado para pruebas de estrés:

* Alto volumen de usuarios simultáneos
* Requests constantes o agresivos
* Detección de puntos de saturación

🔥 Permite identificar límites operativos y cuellos de botella.

---

# 📝 **Informe Final**

El archivo `informe_encargo_3.pdf` incluye:

* Resultados detallados de cada prueba
* Gráficos y estadísticas generadas por Locust
* Evidencias de ejecución
* Análisis técnico del rendimiento
* Recomendaciones de mejora
* Conclusión sobre el cumplimiento de métricas de la industria

📎 **El informe completo también se encuentra disponible en el siguiente enlace:**
👉 [https://docs.google.com/document/d/1FsDFQ7wFsL5vVGLqeg2ZUUc-e8078_EX/edit](https://docs.google.com/document/d/1FsDFQ7wFsL5vVGLqeg2ZUUc-e8078_EX/edit)

---

# ▶️ **Instalación y Ejecución**

## 📌 Requirements

El archivo `requirements.txt` contiene:

```
locust
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar Locust con los Scripts

Ejecutar cada escenario:

```bash
locust -f script_1_medicion_basica.py --host=https://makasuim.github.io/
```

```bash
locust -f script_2_carga_realista.py --host=https://makasuim.github.io/
```

```bash
locust -f script_3_carga_extrema.py --host=https://makasuim.github.io/
```

Abrir interfaz web de Locust:

```
http://localhost:8089
```

Desde ahí podrás:

* Configurar número de usuarios
* Ajustar el spawn rate
* Visualizar gráficos en tiempo real
* Descargar métricas

---

# 👥 **Integrantes del Grupo**

* **Elías Ortiz**
* **Rodrigo Román**
* **Ignacio Leyton**

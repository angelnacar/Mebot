# 🤖 Mebot — AI Professional Portfolio Agent

Mebot es un agente de inteligencia artificial avanzado diseñado para actuar como la interfaz interactiva del perfil profesional de **Ángel Nácar Jiménez**. No es un simple chatbot de preguntas y respuestas, sino un sistema híbrido de agentes con evaluación de calidad y seguridad en tiempo real.

## 🚀 Arquitectura del Sistema

El proyecto implementa un pipeline de procesamiento sofisticado para garantizar respuestas precisas, profesionales y seguras:

1.  **Filtro de Toxicidad:** Cada mensaje de entrada es evaluado por un modelo especializado para bloquear contenido inapropiado antes de que llegue al agente principal.
2.  **Agente Principal (Híbrido):** Utiliza una arquitectura de fallback entre **Groq (gpt-oss-120b)** y **Ollama (nemotron-3-super)** para asegurar una latencia mínima y alta disponibilidad.
3.  **Tool Loop:** El agente puede ejecutar herramientas internas para registrar leads (emails de contacto) o preguntas no resueltas, enviando notificaciones instantáneas vía **Pushover**.
4.  **Evaluador de Calidad:** Una segunda capa de IA analiza la respuesta generada. Si la calidad es inferior al umbral definido, el sistema dispara un **Rerun** automático para corregir la respuesta.
5.  **Capa de Sanitización:** Un filtro final de post-procesamiento elimina cualquier fuga de datos técnicos, UUIDs o detalles de la infraestructura.

## 🛠️ Stack Tecnológico

- **LLMs:** Groq API, Ollama Cloud.
- **Frameworks:** `openai` SDK, `gradio` (UI), `jinja2` (Templating).
- **Infraestructura:** Docker, Python 3.11+.
- **Monitoreo:** Pushover API para alertas en tiempo real.

## 📦 Instalación y Ejecución

### Requisitos
- Python 3.11+
- Claves de API para Groq y Pushover (configuradas en `.env`)

### Pasos para ejecutar
1. **Clonar el repositorio:**
   ```bash
   git clone <repo-url>
   cd Mebot
   ```

2. **Configurar variables de entorno:**
   Crea un archivo `.env` con las siguientes claves:
   ```env
   GROQ_API_KEY=your_key
   OLLAMA_API_KEY=your_key
   OLLAMA_BASE_URL=https://ollama.com/v1
   PUSHOVER_USER=your_user_key
   PUSHOVER_TOKEN=your_app_token
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lanzar el bot:**
   ```bash
   python chat_optimized_Hybrid.py
   ```

## 🛡️ Seguridad y Privacidad
El sistema incluye protecciones contra *Prompt Injection* y fugas de información, asegurando que la identidad profesional de Ángel se mantenga intacta y que los detalles técnicos del sistema permanezcan confidenciales.

---
*Desarrollado por Ángel Nácar Jiménez — AI Systems Engineer*

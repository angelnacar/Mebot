# =============================================================================
# ui.py — Interfaz Gradio para CV Interactivo Ángel Nácar (Versión Avatar)
# =============================================================================

import gradio as gr
import os

# ── Configuración de Preguntas y Rutas ──────────────────────────────────────────

# SUGGESTED_QUESTIONS = [
#     "¿Cuál es tu experiencia con sistemas críticos?",
#     "¿Qué stack tecnológico dominas actualmente?",
#     "¿Cómo gestionas un equipo ágil como Scrum Master?",
#     "Cuéntame sobre tus proyectos de IA y automatización.",
#     "¿Qué certificaciones tienes en Cloud e IA?",
# ]

# Definimos la ruta del avatar (usando ruta absoluta para asegurar la carga en Gradio)
AVATAR_PATH = os.path.abspath(os.path.join("assets", "avatar.jpg"))
# Generic user avatar URL (Mystery Person de Gravatar)
AVATAR_USER = "https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y"

# Tu avatar local para el Bot
AVATAR_BOT = os.path.join("assets", "avatar.jpg")

# ── CSS Maestro (Responsivo, Estilo Matrix + Avatar) ───────────────────────

CUSTOM_CSS = """
/* Variables de Estilo */
:root {
    --matrix-green:     #00ff41;
    --matrix-green-dim: #00c832;
    --matrix-dark:      #0d0d0d;
    --matrix-panel:     #111411;
    --matrix-border:    #1a2e1a;
    --text-primary:     #e8f5e9;
    --text-secondary:   #4caf50;
    --accent-glow:      0 0 15px rgba(0,255,65,0.2);
    --avatar-size:      120px; /* Tamaño del avatar en desktop */
}

/* ── Tablas Responsivas (Fix para Móvil) ────────────────────────── */
#chatbot-container .prose table {
    display: block !important;
    width: 100% !important;
    overflow-x: auto !important; /* Habilita scroll horizontal */
    border-collapse: collapse !important;
    margin: 15px 0 !important;
    scrollbar-width: thin;
    scrollbar-color: var(--matrix-green) transparent;
}

/* Evitar que las columnas se estrujen */
#chatbot-container table th, 
#chatbot-container table td {
    min-width: 140px !important; /* Ancho mínimo para que el texto respire */
    padding: 10px !important;
    word-break: normal !important; /* Evita que rompa palabras letra por letra */
    white-space: normal !important; /* Permite saltos de línea naturales */
    border: 1px solid var(--matrix-border) !important;
    vertical-align: top !important;
    font-size: 0.85rem !important;
}

/* Estilo para los encabezados de tabla */
#chatbot-container table th {
    background: rgba(0, 255, 65, 0.1) !important;
    color: var(--matrix-green) !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Personalizar el scrollbar de la tabla para que sea estilo Matrix */
#chatbot-container .prose table::-webkit-scrollbar {
    height: 4px;
}
#chatbot-container .prose table::-webkit-scrollbar-thumb {
    background: var(--matrix-green-dim);
    border-radius: 10px;
}

/* Contenedor Principal: Full Width Responsivo */
.gradio-container {
    background: var(--matrix-dark) !important;
    max-width: 1400px !important; 
    width: 95% !important;
    margin: 0 auto !important;
    padding: 10px 0 !important;
    font-family: 'JetBrains Mono', monospace !important;
}

/* Eliminar espacios en blanco superiores de Gradio */
.contain { padding: 0 !important; }
.gap { gap: 15px !important; }

/* Header Estilo Matrix */
#cv-header {
    width: 100% !important;
    text-align: center;
    padding: 40px 20px;
    border: 1px solid var(--matrix-border);
    border-radius: 12px;
    background: var(--matrix-panel);
    box-shadow: var(--accent-glow);
    margin-bottom: 5px;
    box-sizing: border-box;
}

/* Estilos para el Avatar Imagen */
#header-avatar {
    width: var(--avatar-size);
    height: var(--avatar-size);
    border-radius: 50%; /* Lo hace redondo */
    object-fit: cover; /* Asegura que la imagen no se deforme */
    border: 3px solid var(--matrix-green); /* Borde verde */
    box-shadow: 0 0 25px rgba(0,255,65,0.5); /* Resplandor del avatar */
    margin-bottom: 20px;
}

#header-name {
    font-size: clamp(1.8rem, 5vw, 2.8rem);
    font-weight: 800;
    color: var(--matrix-green);
    letter-spacing: 4px;
    text-shadow: 0 0 20px rgba(0,255,65,0.4);
    margin: 0;
}

#header-title {
    font-size: clamp(0.9rem, 2.5vw, 1.2rem);
    color: var(--text-secondary);
    margin-top: 10px;
    margin-bottom: 20px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* Skill Badges */
.badge-container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
}
.skill-badge {
    font-size: 0.75rem;
    padding: 4px 12px;
    border: 1px solid var(--matrix-green-dim);
    border-radius: 20px;
    color: var(--matrix-green);
    background: rgba(0,255,65,0.05);
}

/* Chatbot: Ajustes burbujas */
#chatbot-container {
    background: var(--matrix-panel) !important;
    border: 1px solid var(--matrix-border) !important;
    border-radius: 12px !important;
}
#chatbot-container .message {
    font-size: 0.95rem !important;
}

/* Sugerencias: Scroll horizontal tipo Chips */
#suggestions-row {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    gap: 10px !important;
    padding: 5px 0 !important;
    scrollbar-width: none;
}
#suggestions-row::-webkit-scrollbar { display: none; }

.suggestion-btn {
    flex: 0 0 auto !important;
    background: #1a1a1a !important;
    border: 1px solid var(--matrix-border) !important;
    color: var(--text-secondary) !important;
    border-radius: 20px !important;
    padding: 5px 15px !important;
    transition: all 0.3s ease !important;
}
.suggestion-btn:hover {
    border-color: var(--matrix-green) !important;
    color: var(--matrix-green) !important;
    box-shadow: var(--accent-glow);
}

/* Área de Input */
#input-area {
    background: var(--matrix-panel);
    padding: 20px;
    border: 1px solid var(--matrix-border);
    border-radius: 12px;
}
#msg-input textarea {
    background: #000 !important;
    border: 1px solid var(--matrix-border) !important;
    color: var(--text-primary) !important;
    font-size: 1rem !important;
}

/* Botones Acción: Sin superposición */
#send-btn {
    background: var(--matrix-green) !important;
    color: black !important;
    font-weight: bold !important;
    border-radius: 8px !important;
}
#clear-btn {
    background: transparent !important;
    color: #ff5555 !important;
    border: 1px solid #442222 !important;
    border-radius: 8px !important;
}

/* Móvil: Ajustes finales */
@media (max-width: 600px) {
    :root { --avatar-size: 90px; } /* Avatar más pequeño en móvil */
    .gradio-container { width: 98% !important; }
    #cv-header { padding: 25px 10px; }
}
"""

# ── HTML de Componentes (Ahora con la imagen) ───────────────────────────

# Usamos file/ prefixed path para Gradio local.
HEADER_HTML = f"""
<div id="cv-header">
  <h1 id="header-name">ÁNGEL NÁCAR</h1>
  <p id="header-title">Senior Software Developer • Scrum Master • AI Engineer</p>
  <div class="badge-container">
    <span class="skill-badge">Java</span>
    <span class="skill-badge">Python</span>
    <span class="skill-badge">AWS</span>
    <span class="skill-badge">Oracle PL/SQL</span>
    <span class="skill-badge">LLM Agents</span>
    <span class="skill-badge">Madrid</span>
  </div>
</div>
"""

FOOTER_HTML = """
<div style="text-align: center; color: #333; font-size: 0.7rem; margin-top: 15px; font-family: sans-serif;">
  [ SYS ] CV INTERACTIVO v2.3 • GROQ + OLLAMA HYBRID PIPELINE
</div>
"""

# ── Construcción de la UI ──────────────────────────────────────────────────

def build_ui(chat_fn):
    with gr.Blocks(
        css=CUSTOM_CSS,
        title="Ángel Nácar — CV Interactivo",
        theme=gr.themes.Base()
    ) as app:

        # 1. Encabezado (con Avatar)
        gr.HTML(HEADER_HTML)

        # 2. Chatbot
        chatbot = gr.Chatbot(
            value=[{"role": "assistant", "content": "¡Hola! Soy Mebot, un proyecto agéntico de Ángel Nácar. ¿Qué te gustaría saber sobre él?"}],
            elem_id="chatbot-container",
            height=450,
            show_label=False,
            # avatar_images=(
            #      None,                         # usuario — sin avatar
            #     #  None,                         # bot — sin avatar (usamos ::before CSS)
            #     # Para habilitar tu foto real descomenta:
            #      "assets/avatar.jpg",
            # ),
            avatar_images=(AVATAR_USER, AVATAR_BOT), # Orden: (Usuario, Bot)
           # type="messages",
        )

        # # 3. Sugerencias
        # with gr.Row(elem_id="suggestions-row"):
        #     for q in SUGGESTED_QUESTIONS:
        #         btn = gr.Button(q, elem_classes=["suggestion-btn"], size="sm")
        #         # Lógica para autocompletar el textbox
        #         btn.click(fn=lambda x=q: x, outputs=[gr.State(q)]).then(
        #             fn=None, js=f"(q) => {{ document.querySelector('#msg-input textarea').value = '{q}'; }}"
        #         )

        # 4. Área de Entrada
        with gr.Column(elem_id="input-area"):
            msg = gr.Textbox(
                placeholder="Escribe tu pregunta aquí (ej. ¿Cuál es su experiencia en Java?)...",
                show_label=False,
                lines=1,
                elem_id="msg-input",
                max_lines=3,
                autofocus=True
            )
            with gr.Row():
                # clear_btn = gr.Button("↺ LIMPIAR", elem_id="clear-btn", scale=1)
                send_btn = gr.Button("ENVIAR", elem_id="send-btn", scale=4)

        gr.HTML(FOOTER_HTML)

        # ── Lógica de Interacción ──

        # def respond(message, history):
        #     if not message or message.strip() == "":
        #         return "", history
            
        #     # Obtener respuesta del agente
        #     reply = chat_fn(message, history)
            
        #     # Actualizar historial
        #     history.append({"role": "user", "content": message})
        #     history.append({"role": "assistant", "content": reply})
        #     return "", history

        def user_message(message, history):
            # Agrega el mensaje del usuario a la historia inmediatamente
            # y devuelve un string vacío para limpiar el input
            return "", history + [{"role": "user", "content": message}]

        def bot_message(history, chat_fn):
            # Toma el último mensaje del usuario (ya presente en history)
            user_query = history[-1]["content"]
            
            # Llama a tu función de IA
            bot_response = chat_fn(user_query, history[:-1])
            
            # Agrega la respuesta del bot a la historia
            history.append({"role": "assistant", "content": bot_response})
            return history

        # Eventos de envío
        # --- Lógica de Interacción Fluida ---
        
        # 1. Definimos qué pasa cuando el usuario envía
        submit_event = msg.submit(
            fn=user_message, 
            inputs=[msg, chatbot], 
            outputs=[msg, chatbot], 
            queue=False # Importante para que sea instantáneo
        ).then(
            fn=lambda h: bot_message(h, chat_fn),
            inputs=[chatbot],
            outputs=[chatbot]
        )

        # 2. Lo mismo para el botón de enviar
        send_btn.click(
            fn=user_message, 
            inputs=[msg, chatbot], 
            outputs=[msg, chatbot], 
            queue=False
        ).then(
            fn=lambda h: bot_message(h, chat_fn),
            inputs=[chatbot],
            outputs=[chatbot]
        )
        # msg.submit(respond, [msg, chatbot], [msg, chatbot])
        # send_btn.click(respond, [msg, chatbot], [msg, chatbot])

        # Evento de limpieza
        # clear_btn.click(
        #     lambda: (None, [{"role": "assistant", "content": "Conversación reiniciada. ¿En qué más puedo ayudarte?"}]),
        #     outputs=[msg, chatbot]
        # )

    return app

# Testing Standalone
if __name__ == "__main__":
    def mock_chat(msg, hist): return f"Has preguntado: **{msg}**. Esta es una respuesta de prueba simulando al agente."
    
    # # IMPORTANTE: AVISAR A GRADIO QUE PERMITA EL ACCESO A LA CARPETA 'assets'
    # build_ui(mock_chat).launch(allowed_paths=[os.path.dirname(AVATAR_PATH)])
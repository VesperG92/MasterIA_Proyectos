ESTIMATION_EXAMPLES = [
    {
        "meeting_summary": """
        El cliente necesita una plataforma web para gestionar el inventario
        de tres almacenes. Actualmente utiliza hojas Excel y quiere
        centralizar productos, controlar el stock, registrar movimientos
        y consultar alertas de existencias mínimas.
        Habrá aproximadamente 15 usuarios con distintos permisos.
        Se requiere exportación a Excel, pero no integraciones con ERP.
        """,
        "estimation": """
        ## Estimación: Plataforma de Gestión de Inventario

        ### Desglose de tareas:
        1. Análisis funcional y requisitos: 20 horas
        2. Diseño UI/UX: 40 horas
        3. Backend API y modelo de datos: 60 horas
        4. Gestión de productos y movimientos: 55 horas
        5. Autenticación y roles: 25 horas
        6. Dashboard y alertas de stock: 35 horas
        7. Exportación Excel: 15 horas
        8. Testing y QA: 35 horas
        9. Despliegue y documentación: 20 horas

        **Total estimado: 305 horas**
        **Equipo recomendado: 2 desarrolladores full-stack + 1 diseñador UX (part-time)**
        **Duración estimada: 6-8 semanas**

        ### Supuestos:
        - Aplicación web responsive.
        - Sin integración con sistemas externos.
        - Infraestructura cloud estándar.
        - No incluye migración masiva de datos históricos.
        """
    },
    {
        "meeting_summary": """
        Una empresa de servicios quiere desarrollar un CRM a medida
        para 30 empleados comerciales. Necesita registrar clientes,
        contactos, oportunidades, actividades y estados de negociación.
        Solicita un pipeline comercial visual, informes básicos y
        notificaciones por correo electrónico.
        No necesita integraciones con Salesforce ni HubSpot.
        """,
        "estimation": """
        ## Estimación: CRM Comercial Personalizado

        ### Desglose de tareas:
        1. Análisis de procesos comerciales: 35 horas
        2. Diseño UI/UX: 55 horas
        3. Arquitectura y base de datos: 35 horas
        4. Gestión de clientes y contactos: 65 horas
        5. Gestión de oportunidades y pipeline: 85 horas
        6. Gestión de actividades y tareas: 45 horas
        7. Autenticación y permisos: 30 horas
        8. Informes y dashboard comercial: 55 horas
        9. Notificaciones por email: 25 horas
        10. Testing y QA: 60 horas
        11. Despliegue y formación: 30 horas

        **Total estimado: 520 horas**
        **Equipo recomendado: 2 desarrolladores full-stack + 1 diseñador UX + 1 QA (part-time)**
        **Duración estimada: 9-12 semanas**

        ### Supuestos:
        - CRM web responsive.
        - Hasta 30 usuarios internos.
        - Sin integraciones con CRM externos.
        - Informes estándar, sin analítica predictiva.
        """
    },
    {
        "meeting_summary": """
        Una startup quiere lanzar una aplicación móvil para reservar
        clases deportivas. Los usuarios podrán registrarse, consultar
        centros, reservar sesiones y pagar online.
        Los administradores gestionarán horarios, aforos y reservas.
        La aplicación debe funcionar en iOS y Android.
        Se utilizará Stripe como pasarela de pago.
        """,
        "estimation": """
        ## Estimación: App Móvil de Reservas Deportivas

        ### Desglose de tareas:
        1. Análisis funcional: 35 horas
        2. Diseño UX/UI móvil: 90 horas
        3. Arquitectura backend: 50 horas
        4. Registro y autenticación: 45 horas
        5. Catálogo de centros y actividades: 65 horas
        6. Motor de reservas y disponibilidad: 110 horas
        7. Integración Stripe: 55 horas
        8. Notificaciones push: 40 horas
        9. Panel de administración: 90 horas
        10. Testing iOS y Android: 90 horas
        11. Publicación en stores: 35 horas
        12. Documentación: 25 horas

        **Total estimado: 730 horas**
        **Equipo recomendado: 2 desarrolladores mobile/full-stack + 1 diseñador UX + 1 QA**
        **Duración estimada: 12-16 semanas**

        ### Supuestos:
        - Desarrollo multiplataforma con Flutter o React Native.
        - Una única pasarela de pago.
        - Sin integración con software externo de gimnasios.
        - No incluye mantenimiento posterior.
        """
    },
    {
        "meeting_summary": """
        Una empresa recibe unas 500 facturas mensuales en PDF y quiere
        automatizar su procesamiento. El sistema debe extraer proveedor,
        fecha, importe, impuestos y número de factura mediante OCR.
        Los datos se validarán y exportarán a Excel.
        Las facturas con errores se revisarán manualmente.
        No se requiere integración directa con SAP.
        """,
        "estimation": """
        ## Estimación: Automatización de Facturas con OCR

        ### Desglose de tareas:
        1. Análisis de documentos y requisitos: 30 horas
        2. Diseño del flujo de procesamiento: 30 horas
        3. Integración con servicio OCR: 65 horas
        4. Extracción y normalización de campos: 75 horas
        5. Validaciones de negocio: 50 horas
        6. Interfaz de revisión manual: 65 horas
        7. Exportación Excel: 20 horas
        8. Gestión de errores y logs: 35 horas
        9. Testing con documentos reales: 65 horas
        10. Despliegue y documentación: 35 horas

        **Total estimado: 470 horas**
        **Equipo recomendado: 1 desarrollador backend + 1 especialista IA/OCR + 1 QA (part-time)**
        **Duración estimada: 8-11 semanas**

        ### Supuestos:
        - Uso de servicios OCR existentes.
        - Facturas en español y formatos PDF habituales.
        - Sin entrenamiento de un modelo OCR desde cero.
        - No incluye licencias ni costes por documento.
        """
    },
    {
        "meeting_summary": """
        Una empresa quiere implementar un chatbot interno basado en IA
        generativa para consultar documentación corporativa.
        El asistente responderá preguntas utilizando unos 2.000
        documentos PDF y Word.
        Debe citar las fuentes y permitir actualizar la documentación.
        El acceso estará restringido a empleados autenticados.
        Se utilizará un modelo LLM mediante API y una arquitectura RAG.
        """,
        "estimation": """
        ## Estimación: Asistente Corporativo con IA y RAG

        ### Desglose de tareas:
        1. Análisis de casos de uso: 40 horas
        2. Diseño de arquitectura RAG: 55 horas
        3. Ingesta y procesamiento documental: 90 horas
        4. Chunking, embeddings y base vectorial: 75 horas
        5. Integración con API LLM: 55 horas
        6. Recuperación y ranking de documentos: 75 horas
        7. Desarrollo de interfaz conversacional: 75 horas
        8. Autenticación y control de acceso: 50 horas
        9. Evaluación de respuestas y alucinaciones: 95 horas
        10. Observabilidad y logs: 40 horas
        11. Testing funcional y seguridad: 70 horas
        12. Despliegue y documentación: 50 horas

        **Total estimado: 770 horas**
        **Equipo recomendado: 1 ingeniero IA + 1 desarrollador backend + 1 desarrollador frontend + 1 QA (part-time)**
        **Duración estimada: 12-16 semanas**

        ### Supuestos:
        - Uso de un LLM comercial mediante API.
        - Documentación digital con texto extraíble.
        - Sin fine-tuning del modelo.
        - Control de acceso a documentos por permisos.
        - No incluye consumo de tokens ni infraestructura cloud.
        """
    },
    {
        "meeting_summary": """
        Una empresa necesita conectar su tienda Shopify con su ERP.
        Actualmente los pedidos se introducen manualmente.
        Quiere sincronizar productos, precios, stock, clientes
        y pedidos de forma bidireccional.
        El ERP dispone de una API REST documentada.
        La sincronización debe ejecutarse automáticamente y registrar
        errores para facilitar su seguimiento.
        """,
        "estimation": """
        ## Estimación: Integración Shopify - ERP

        ### Desglose de tareas:
        1. Análisis de APIs y procesos: 40 horas
        2. Diseño de arquitectura de integración: 35 horas
        3. Autenticación y conexión con APIs: 40 horas
        4. Sincronización de productos: 55 horas
        5. Sincronización de precios y stock: 55 horas
        6. Sincronización de clientes: 40 horas
        7. Sincronización de pedidos: 70 horas
        8. Gestión de errores y reintentos: 45 horas
        9. Logs y monitorización: 35 horas
        10. Testing de integración: 65 horas
        11. Despliegue y documentación: 35 horas

        **Total estimado: 515 horas**
        **Equipo recomendado: 2 desarrolladores backend/integraciones + 1 QA (part-time)**
        **Duración estimada: 9-12 semanas**

        ### Supuestos:
        - APIs REST disponibles y documentadas.
        - Acceso a entornos de pruebas.
        - Sin modificaciones internas del ERP.
        - Volumen moderado de transacciones.
        """
    },
    {
        "meeting_summary": """
        La dirección financiera necesita un dashboard de Power BI
        para analizar ventas, costes y rentabilidad.
        Los datos proceden de cinco archivos Excel y una base SQL.
        Se requieren actualizaciones diarias, filtros por región
        y producto, y aproximadamente 20 indicadores financieros.
        Habrá 25 usuarios de negocio.
        """,
        "estimation": """
        ## Estimación: Dashboard Financiero con Power BI

        ### Desglose de tareas:
        1. Análisis de KPIs y requisitos: 35 horas
        2. Auditoría de fuentes de datos: 30 horas
        3. Conexión y extracción de datos: 45 horas
        4. Limpieza y transformación Power Query: 65 horas
        5. Modelo de datos: 55 horas
        6. Desarrollo de medidas DAX: 70 horas
        7. Diseño de dashboards: 75 horas
        8. Configuración de actualización diaria: 25 horas
        9. Validación de métricas: 50 horas
        10. Publicación y permisos: 25 horas
        11. Formación y documentación: 25 horas

        **Total estimado: 500 horas**
        **Equipo recomendado: 1 ingeniero de datos + 1 especialista Power BI + 1 analista funcional (part-time)**
        **Duración estimada: 8-11 semanas**

        ### Supuestos:
        - Datos accesibles y con calidad razonable.
        - No incluye construcción de un data warehouse.
        - No incluye licencias Power BI.
        - Actualización batch diaria, no tiempo real.
        """
    },
    {
        "meeting_summary": """
        Una pyme quiere crear una tienda online para vender unos
        300 productos físicos. Necesita catálogo, buscador, carrito,
        checkout, pagos con tarjeta, gestión de pedidos y un panel
        administrativo. Se utilizará WooCommerce.
        La empresa aportará fotografías y descripciones.
        Se requiere una configuración SEO básica.
        """,
        "estimation": """
        ## Estimación: Ecommerce con WooCommerce

        ### Desglose de tareas:
        1. Análisis y definición de requisitos: 20 horas
        2. Diseño visual y adaptación de plantilla: 45 horas
        3. Configuración WooCommerce: 35 horas
        4. Catálogo y categorías: 35 horas
        5. Configuración de pagos: 25 horas
        6. Envíos e impuestos: 30 horas
        7. Gestión de pedidos: 25 horas
        8. Importación de productos: 30 horas
        9. SEO técnico básico: 20 horas
        10. Testing funcional: 35 horas
        11. Despliegue y formación: 25 horas

        **Total estimado: 325 horas**
        **Equipo recomendado: 1 desarrollador WordPress/WooCommerce + 1 diseñador UX (part-time)**
        **Duración estimada: 6-9 semanas**

        ### Supuestos:
        - Uso de plantilla comercial.
        - Sin desarrollo de plugins complejos.
        - Productos y contenidos proporcionados por el cliente.
        - Sin integración con ERP.
        - No incluye licencias, hosting ni comisiones de pago.
        """
    },
    {
        "meeting_summary": """
        Una empresa dispone de una aplicación interna desarrollada
        en Java 8 con una base de datos PostgreSQL.
        Quiere actualizarla a Java 21 y modernizar el frontend.
        La aplicación tiene aproximadamente 25 pantallas,
        40 endpoints y 15 procesos batch.
        Es necesario mantener toda la funcionalidad actual
        y minimizar el impacto sobre los usuarios.
        """,
        "estimation": """
        ## Estimación: Modernización de Aplicación Legacy

        ### Desglose de tareas:
        1. Auditoría técnica del sistema: 80 horas
        2. Análisis de dependencias y riesgos: 55 horas
        3. Diseño de arquitectura objetivo: 65 horas
        4. Actualización de Java y frameworks: 140 horas
        5. Migración de 25 pantallas frontend: 240 horas
        6. Adaptación de 40 endpoints: 130 horas
        7. Adaptación de procesos batch: 100 horas
        8. Pruebas de regresión: 170 horas
        9. Optimización y seguridad: 80 horas
        10. Preparación de despliegue: 65 horas
        11. Documentación y transferencia: 55 horas

        **Total estimado: 1180 horas**
        **Equipo recomendado: 2 desarrolladores Java senior + 1 desarrollador frontend + 1 QA**
        **Duración estimada: 16-22 semanas**

        ### Supuestos:
        - Sin cambios funcionales significativos.
        - Base de datos PostgreSQL conservada.
        - Código fuente disponible y mantenible.
        - Migración progresiva con pruebas de regresión.
        - No incluye reingeniería completa del sistema.
        """
    },
    {
        "meeting_summary": """
        El departamento de recursos humanos quiere automatizar
        el proceso de incorporación de empleados.
        Actualmente utiliza correos y hojas de cálculo.
        El sistema debe generar tareas para IT y RRHH,
        enviar notificaciones, recoger documentación
        y mostrar el estado de cada incorporación.
        La empresa utiliza Microsoft 365 y Power Automate.
        Se esperan unas 20 incorporaciones mensuales.
        """,
        "estimation": """
        ## Estimación: Automatización de Onboarding con Power Platform

        ### Desglose de tareas:
        1. Análisis del proceso actual: 30 horas
        2. Diseño del flujo automatizado: 35 horas
        3. Configuración de SharePoint Lists: 30 horas
        4. Desarrollo de flujos Power Automate: 75 horas
        5. Formularios Power Apps: 65 horas
        6. Notificaciones y recordatorios: 30 horas
        7. Gestión de documentos: 40 horas
        8. Dashboard de seguimiento: 40 horas
        9. Pruebas funcionales: 45 horas
        10. Formación y documentación: 30 horas

        **Total estimado: 420 horas**
        **Equipo recomendado: 1 especialista Power Platform + 1 analista funcional + 1 QA (part-time)**
        **Duración estimada: 7-10 semanas**

        ### Supuestos:
        - Microsoft 365 ya disponible.
        - Uso de conectores estándar.
        - Sin integración compleja con sistemas de nóminas.
        - No incluye licencias adicionales.
        """
    },
    {
        "meeting_summary": """
        Una entidad financiera quiere desarrollar una API para
        consultar movimientos y saldos de cuentas desde aplicaciones
        internas. Se integrará con un sistema bancario existente.
        La solución debe incluir OAuth 2.0, auditoría de accesos,
        trazabilidad, limitación de peticiones y cifrado.
        Se estima un volumen de 100.000 peticiones diarias.
        No se permitirán operaciones monetarias.
        """,
        "estimation": """
        ## Estimación: API Bancaria de Consulta de Cuentas

        ### Desglose de tareas:
        1. Análisis funcional y regulatorio: 70 horas
        2. Diseño de arquitectura y seguridad: 90 horas
        3. Contratos OpenAPI y modelo de datos: 50 horas
        4. Integración con sistema bancario: 130 horas
        5. Endpoints de cuentas y saldos: 65 horas
        6. Endpoints de movimientos: 75 horas
        7. OAuth 2.0 y autorización: 85 horas
        8. Auditoría y trazabilidad: 65 horas
        9. Rate limiting y resiliencia: 55 horas
        10. Pruebas de seguridad: 90 horas
        11. Pruebas de rendimiento: 75 horas
        12. Testing de integración y regresión: 100 horas
        13. Despliegue, observabilidad y documentación: 70 horas

        **Total estimado: 1020 horas**
        **Equipo recomendado: 2 desarrolladores backend senior + 1 arquitecto de seguridad (part-time) + 1 QA**
        **Duración estimada: 15-20 semanas**

        ### Supuestos:
        - APIs del core bancario disponibles.
        - Sin operaciones de pago ni transferencia.
        - Infraestructura y herramientas corporativas existentes.
        - No incluye procesos de certificación regulatoria externos.
        - Requisitos de seguridad sujetos a validación corporativa.
        """
    },
    {
        "meeting_summary": """
        Una empresa quiere crear un sistema de predicción de demanda
        para optimizar sus compras.
        Dispone de tres años de ventas históricas de 500 productos.
        Necesita generar previsiones semanales y mostrar resultados
        en un dashboard.
        Se utilizarán modelos de machine learning existentes.
        El sistema deberá reentrenarse mensualmente.
        """,
        "estimation": """
        ## Estimación: Sistema de Predicción de Demanda con ML

        ### Desglose de tareas:
        1. Análisis del caso de uso: 40 horas
        2. Auditoría de calidad de datos: 65 horas
        3. Ingesta y limpieza de datos: 95 horas
        4. Análisis exploratorio: 65 horas
        5. Ingeniería de variables: 85 horas
        6. Entrenamiento de modelos baseline: 75 horas
        7. Optimización y comparación de modelos: 105 horas
        8. Evaluación de precisión: 75 horas
        9. Pipeline de inferencia: 70 horas
        10. Automatización de reentrenamiento: 75 horas
        11. Dashboard de previsiones: 80 horas
        12. Testing y monitorización: 80 horas
        13. Despliegue y documentación: 65 horas

        **Total estimado: 975 horas**
        **Equipo recomendado: 1 data scientist + 1 data engineer + 1 desarrollador backend/BI + 1 QA (part-time)**
        **Duración estimada: 14-20 semanas**

        ### Supuestos:
        - Datos históricos accesibles y suficientemente completos.
        - Modelos clásicos de forecasting y machine learning.
        - Sin desarrollo de modelos fundacionales.
        - No se garantiza una precisión concreta sin análisis previo.
        - No incluye infraestructura ni mantenimiento posterior.
        """
    }
]
# JSON.PE - Consulta DNI y RUC

## Descripción

Este módulo integra Odoo con la API de **json.pe** para consultar información de DNI y RUC peruanos directamente desde el formulario de contactos (Partners). Permite autocompletar automáticamente los datos del contacto con la información obtenida de la API.

### Características principales:
- Consulta de DNI (Documento Nacional de Identidad) desde el formulario de Partner
- Consulta de RUC (Registro Único de Contribuyente) desde el formulario de Partner
- Autocompletado automático de campos: nombre, dirección, ciudad, código postal, etc.
- Validación de formatos (DNI: 8 dígitos, RUC: 11 dígitos)
- Manejo de errores y mensajes informativos

---

## Configuración del API Token

Antes de usar el módulo, es necesario configurar tu API Token de json.pe:

1. Ve a **Configuración** (Settings) → **Configuración General** (General Settings)
2. Busca la sección **JSON.PE - Consulta DNI y RUC**
3. En el campo **API Token**, ingresa tu token de autenticación
4. Haz clic en **Guardar** (Save)

> **Nota:** Si no tienes un API Token, puedes obtenerlo en [https://json.pe](https://json.pe)

---

## Uso de los Botones DNI/RUC

### Consultar DNI

1. Abre o crea un contacto (Partner) en Odoo
2. Ingresa el **DNI** (8 dígitos) en el campo correspondiente
3. Haz clic en el botón **"Consultar DNI"** ubicado en el encabezado del formulario
4. El sistema consultará la API y autocompletará automáticamente:
   - Nombre completo
   - Dirección (si está disponible)

### Consultar RUC

1. Abre o crea un contacto (Partner) en Odoo
2. Ingresa el **RUC** (11 dígitos) en el campo correspondiente
3. Haz clic en el botón **"Consultar RUC"** ubicado en el encabezado del formulario
4. El sistema consultará la API y autocompletará automáticamente:
   - Nombre o Razón Social
   - Número de identificación fiscal (VAT)
   - Dirección completa
   - Ciudad/Distrito
   - Código postal (Ubigeo)

> **Importante:** Los botones solo aparecerán si has ingresado un DNI o RUC válido en el formulario.

---

## Enlaces

- **API JSON.PE:** [https://json.pe](https://json.pe)
- **Documentación:** [https://json.pe/docs](https://json.pe/docs)

---

## Requisitos

- Odoo 17.0
- Módulo `contacts` instalado
- Biblioteca Python `requests`
- Conexión a internet
- API Token válido de json.pe

---

## Soporte

Para más información sobre la API de json.pe, visita [https://json.pe](https://json.pe)

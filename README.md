# 🌐 My_Web

Un proyecto web desarrollado con **Django**, que incluye un blog, una sección de herramientas y empresas colaboradoras, y un sistema de contacto seguro que evita spam con ayuda de **Cloudflare Turnstile**.

---

## 🧰 Requisitos iniciales

Si acabas de clonar o descargar el proyecto, sigue estos pasos para configurarlo correctamente:

### 1️⃣ Crear entorno virtual (recomendado)
```bash
python -m venv .env
```
#### Activar entorno virtual
En Windows:
```bash
.env\Scripts\activate
```
En Linux / macOS:
```bash
source .env/bin/activate
```
### 2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```
### 3️⃣ Configuración de entorno
El archivo de configuración se encuentra en:
```bash
my_web/core/settings/env.py
```
Este archivo contiene claves sensibles (como contraseñas, claves de API, correos, etc.).

⚠️ Importante: No utilices las mismas claves que vienen de ejemplo en el repositorio.
Cámbialas antes de subir a producción.

En este archivo también podrás configurar:

📧 El correo de la página y el correo de notificaciones.

🔑 Las claves Turnstile (de Cloudflare) que se usan para evitar spam y verificar que los usuarios no son bots.

### 4️⃣ Migraciones de base de datos
Ejecuta las siguientes órdenes para crear y aplicar las migraciones:

```bash
my_web\manage.py makemigrations blog my_web_app
my_web\manage.py migrate
```
### 5️⃣ Crear usuario administrador
```bash
my_web\manage.py createsuperuser
```
🚀 Modos de ejecución:

🧪 Modo desarrollo
(Asegúrate de tener Docker Desktop ejecutándose.)
```bash]
docker-compose up
```
🏗️ Modo producción
```bash
docker-compose -f docker-compose-production.yml up
```

📰 Características principales
✅ Blog dinámico:
Crea y edita publicaciones fácilmente con django-ckeditor para mayor personalización.

✅ Página de contacto segura:
Incluye verificación Turnstile (Cloudflare) y envío de correos desde un mail propio hacia el correo configurado.

✅ Secciones informativas:
Muestra herramientas utilizadas y empresas con las que se ha trabajado.

🧩 Tecnologías utilizadas
🐍 Python 3

🌱 Django

🐋 Docker / Docker Compose

📝 django-ckeditor

☁️ Cloudflare Turnstile

💌 SMTP / Email backend

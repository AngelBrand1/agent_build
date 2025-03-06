# Proyecto Agent Build

Este proyecto es una implementación de sistemas multiagentes inteligentes utilizando Python. A continuación, se detallan los pasos para configurar y ejecutar el proyecto.

## Requisitos

- Python 3.8 o superior
- pip

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/AngelBrand1/agent_build.git
    cd agent_build
    ```

2. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En Windows:
        ```bash
        venv\Scripts\activate
        ```
    - En macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

5. Crea el archivo `.env` basado en `.env.example`:
    ```bash
    cp .env.example .env
    ```

## Ejecución

Para ejecutar el proyecto, asegúrate de que el entorno virtual esté activado y luego ejecuta el siguiente comando:
```bash
python main.py
```

## Resultados

Los resultados se encuentran en la carpeta `runs`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio importante.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

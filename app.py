import io, sys, os, sqlite3, importlib, pkgutil, textwrap
import streamlit as st
from contextlib import redirect_stdout

st.set_page_config(page_title="Demo: Pruebas Unitarias e Integración en Python", layout="wide")
st.title("🧪 Demo Didáctica: Pruebas Unitarias e Integración en Python")
st.caption("Hecha con Streamlit · incluye ejemplos ejecutables con unittest + SQLite")

st.sidebar.header("Navegación")
choice = st.sidebar.radio(
    "Secciones",
    [
        "Introducción",
        "Código de ejemplo (src)",
        "Pruebas unitarias",
        "Pruebas de integración",
        "Laboratorio guiado",
        "Créditos"
    ],
    index=0
)

project_root = os.path.dirname(__file__)
src_dir = os.path.join(project_root, "src")
tests_dir = os.path.join(project_root, "tests")

def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

if choice == "Introducción":
    st.subheader("¿Qué veremos?")
    st.markdown(
        """
        **Objetivo:** Comprender la diferencia entre **pruebas unitarias** (probar funciones/clases aisladas)
        y **pruebas de integración** (probar componentes trabajando juntos).

        **Stack usado:**
        - Python `unittest` (estándar)
        - SQLite en memoria (sin dependencias externas)
        - Streamlit para interfaz didáctica

        **Estructura del proyecto:**
        ```
        streamlit_testing_demo/
        ├─ app.py
        ├─ src/
        │  ├─ calculator.py
        │  ├─ repository.py
        │  └─ service.py
        └─ tests/
           ├─ test_unit_calculator.py
           └─ test_integration_vehicle.py
        ```
        """
    )
    st.info("Usa el menú lateral para explorar el código y ejecutar las pruebas.")

elif choice == "Código de ejemplo (src)":
    st.subheader("Módulos de ejemplo")
    file = st.selectbox("Selecciona un archivo", ["calculator.py", "repository.py", "service.py"])
    path = os.path.join(src_dir, file)
    st.code(read_file(path), language="python")

elif choice == "Pruebas unitarias":
    st.subheader("Ejecutar pruebas **unitarias**")
    st.write("Archivo: `tests/test_unit_calculator.py`")
    st.code(read_file(os.path.join(tests_dir, "test_unit_calculator.py")), language="python")

    if st.button("▶️ Ejecutar pruebas unitarias"):
        # Ejecutamos unittest programáticamente y capturamos la salida
        import unittest
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName("tests.test_unit_calculator")
        stream = io.StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2)
        result = runner.run(suite)
        st.text(stream.getvalue())
        st.success(f"OK: {result.wasSuccessful()} — Tests: {result.testsRun} · Fallos: {len(result.failures)} · Errores: {len(result.errors)}")

elif choice == "Pruebas de integración":
    st.subheader("Ejecutar pruebas de **integración**")
    st.write("Archivo: `tests/test_integration_vehicle.py` (usa SQLite en memoria + capas repo/servicio)")
    st.code(read_file(os.path.join(tests_dir, "test_integration_vehicle.py")), language="python")

    if st.button("▶️ Ejecutar pruebas de integración"):
        import unittest
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName("tests.test_integration_vehicle")
        stream = io.StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2)
        result = runner.run(suite)
        st.text(stream.getvalue())
        st.success(f"OK: {result.wasSuccessful()} — Tests: {result.testsRun} · Fallos: {len(result.failures)} · Errores: {len(result.errors)}")

elif choice == "Laboratorio guiado":
    st.subheader("Laboratorio: agrega un caso de prueba")
    st.markdown(
        """
        1. **Abre** `src/calculator.py` y agrega una función `power(a, b)`.
        2. **Crea** un test en `tests/test_unit_calculator.py` que verifique varios casos de `power`.
        3. **Vuelve** y ejecuta las pruebas unitarias desde aquí.

        *Tip:* Puedes editar los archivos en tu IDE y recargar la app.
        """
    )
    with st.expander("Sugerencia de implementación de `power`"):
        st.code(
            """
            # src/calculator.py
            def power(a: float, b: int) -> float:
                return a ** b
            """, language="python"
        )
    with st.expander("Sugerencia de test para `power`"):
        st.code(
            """
            # tests/test_unit_calculator.py
            def test_power(self):
                from src.calculator import power
                self.assertEqual(power(2, 3), 8)
                self.assertEqual(power(5, 0), 1)
                self.assertEqual(power(9, 0.5), 3)  # raíz cuadrada
            """, language="python"
        )

else:
    st.subheader("Créditos")
    st.markdown("Hecho con ❤️ para demostrar buenas prácticas de testing en Python + Streamlit.")
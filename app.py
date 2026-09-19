# PROYECTO 1 - PYTHON FOR ANALYTICS
# PETMARKET ANALYTICS

import streamlit as st
import pandas as pd
import numpy as np

from libreria_funciones_proyecto1 import calcular_margen_neto
from libreria_clases_proyecto1 import InventarioProducto

st.set_page_config(
    page_title="PetMarket Analytics",
    page_icon="🐾",
    layout="wide"
)

# MENÚ LATERAL

st.sidebar.title("🐾 PetMarket Analytics")

opcion = st.sidebar.selectbox(
    "Seleccione una sección:",
    [
        "Home",
        "Ejercicio 1",
        "Ejercicio 2",
        "Ejercicio 3",
        "Ejercicio 4"
    ]
)

# HOME

if opcion == "Home":

    st.title("🐾 PetMarket Analytics")

    st.subheader("Sistema de Gestión y Análisis para Tienda de Mascotas")

    # Logo del proyecto
    try:
        st.image(
            "logo_petmarket.png",
            width=350
        )
    except:
        st.info("Agregar el archivo logo_petmarket.png en la carpeta del proyecto.")

    st.markdown("---")

    st.subheader("Información del estudiante")

    st.write("**Nombre:** ANDREA ALIAGA GARMA")
    st.write("**Curso:** Python for Analytics")
    st.write("**Módulo:** Módulo 1 - Python Fundamentals")
    st.write("**Año:** 2026")

    st.markdown("---")

    st.subheader("Descripción del proyecto")

    st.markdown("""
    **PetMarket Analytics** es una aplicación desarrollada para simular
    algunos procesos de gestión de una empresa dedicada a la venta de
    productos para mascotas.

    La aplicación permite realizar las siguientes actividades:

    - Registrar ingresos y gastos de la empresa.
    - Registrar ventas de productos.
    - Analizar el margen neto del negocio.
    - Gestionar el inventario de productos.

    """)

    st.subheader("Tecnologías utilizadas")

    st.write("🐍 Python")
    st.write("📊 Streamlit")
    st.write("🐼 Pandas")
    st.write("🔢 NumPy")
    st.write("📦 Programación Orientada a Objetos")

# EJERCICIO 1
# FLUJO DE CAJA CON LISTAS

elif opcion == "Ejercicio 1":

    st.title("💰 Ejercicio 1 - Flujo de Caja")

    st.markdown("""
    En este ejercicio se registran los **ingresos y gastos de PetMarket**.

    Cada movimiento se almacena en una lista y posteriormente se calcula
    el total de ingresos, total de gastos y saldo final del negocio.
    """)

    # Creamos la lista la primera vez que se ejecuta la aplicación
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    st.subheader("Registrar movimiento")

    concepto = st.text_input(
        "Concepto",
        placeholder="Ejemplo: Venta de alimento para gatos"
    )

    tipo_movimiento = st.selectbox(
        "Tipo de movimiento",
        ["Ingreso", "Gasto"]
    )

    valor = st.number_input(
        "Valor (S/)",
        min_value=0.0,
        step=10.0
    )

    if st.button("Agregar movimiento"):

        if concepto == "":
            st.error("Debe ingresar un concepto.")

        elif valor <= 0:
            st.error("El valor debe ser mayor que cero.")

        else:

            movimiento = {
                "Concepto": concepto,
                "Tipo": tipo_movimiento,
                "Valor": valor
            }

            st.session_state.movimientos.append(movimiento)

            st.success("Movimiento agregado correctamente.")

    # --------------------------------------------------------
    # MOSTRAR MOVIMIENTOS
    # --------------------------------------------------------

    if len(st.session_state.movimientos) > 0:

        st.subheader("Movimientos registrados")

        df_movimientos = pd.DataFrame(
            st.session_state.movimientos
        )

        st.dataframe(
            df_movimientos,
            use_container_width=True
        )

        # ----------------------------------------------------
        # CALCULAR INGRESOS
        # ----------------------------------------------------

        total_ingresos = 0

        for movimiento in st.session_state.movimientos:

            if movimiento["Tipo"] == "Ingreso":
                total_ingresos = total_ingresos + movimiento["Valor"]

        # ----------------------------------------------------
        # CALCULAR GASTOS
        # ----------------------------------------------------

        total_gastos = 0

        for movimiento in st.session_state.movimientos:

            if movimiento["Tipo"] == "Gasto":
                total_gastos = total_gastos + movimiento["Valor"]

        # Saldo final
        saldo_final = total_ingresos - total_gastos

        st.subheader("Resumen del flujo de caja")

        columna1, columna2, columna3 = st.columns(3)

        with columna1:
            st.metric(
                "Total ingresos",
                f"S/ {total_ingresos:,.2f}"
            )

        with columna2:
            st.metric(
                "Total gastos",
                f"S/ {total_gastos:,.2f}"
            )

        with columna3:
            st.metric(
                "Saldo final",
                f"S/ {saldo_final:,.2f}"
            )

        # ----------------------------------------------------
        # EVALUACIÓN DEL FLUJO
        # ----------------------------------------------------

        if saldo_final > 0:

            st.success(
                "El flujo de caja se encuentra A FAVOR."
            )

        elif saldo_final < 0:

            st.error(
                "El flujo de caja se encuentra EN CONTRA."
            )

        else:

            st.info(
                "El flujo de caja se encuentra EQUILIBRADO."
            )

    else:

        st.info(
            "Todavía no existen movimientos registrados."
        )


# ============================================================
# EJERCICIO 2
# REGISTRO CON NUMPY, ARRAYS Y DATAFRAME
# ============================================================

elif opcion == "Ejercicio 2":

    st.title("🛒 Ejercicio 2 - Registro de Ventas")

    st.markdown("""
    Este ejercicio permite registrar las **ventas de productos de PetMarket**.

    Los datos ingresados son almacenados utilizando arrays de **NumPy**
    y posteriormente son convertidos en un **DataFrame de Pandas** para
    visualizar los registros.
    """)

    # Lista donde se almacenarán los arrays
    if "ventas" not in st.session_state:
        st.session_state.ventas = []

    st.subheader("Registrar nueva venta")

    producto = st.text_input(
        "Nombre del producto",
        placeholder="Ejemplo: Alimento para gato 3 kg"
    )

    categoria = st.selectbox(
        "Categoría",
        [
            "Alimentos",
            "Higiene",
            "Accesorios",
            "Juguetes",
            "Salud y bienestar",
            "Otros"
        ]
    )

    precio = st.number_input(
        "Precio unitario (S/)",
        min_value=0.0,
        step=1.0
    )

    cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        step=1
    )

    if st.button("Agregar venta"):

        if producto == "":

            st.error(
                "Debe ingresar el nombre del producto."
            )

        elif precio <= 0:

            st.error(
                "El precio debe ser mayor que cero."
            )

        else:

            # Calculamos el total de la venta
            total = precio * cantidad

            # Creamos un array NumPy
            nueva_venta = np.array(
                [
                    producto,
                    categoria,
                    precio,
                    cantidad,
                    total
                ],
                dtype=object
            )

            # Agregamos el array a la lista
            st.session_state.ventas.append(
                nueva_venta
            )

            st.success(
                "Venta registrada correctamente."
            )

    # --------------------------------------------------------
    # MOSTRAR REGISTROS
    # --------------------------------------------------------

    if len(st.session_state.ventas) > 0:

        st.subheader("Ventas registradas")

        # Convertimos la lista en un array NumPy
        array_ventas = np.array(
            st.session_state.ventas,
            dtype=object
        )

        # Convertimos el array en DataFrame
        df_ventas = pd.DataFrame(
            array_ventas,
            columns=[
                "Producto",
                "Categoría",
                "Precio Unitario",
                "Cantidad",
                "Total"
            ]
        )

        st.dataframe(
            df_ventas,
            use_container_width=True
        )

    else:

        st.info(
            "Todavía no existen ventas registradas."
        )


# ============================================================
# EJERCICIO 3
# FUNCIÓN DESDE LIBRERÍA EXTERNA
# ============================================================

elif opcion == "Ejercicio 3":

    st.title("📈 Ejercicio 3 - Análisis de Margen Neto")

    st.markdown("""
    Este ejercicio utiliza una **función proveniente de una librería
    externa** para analizar la rentabilidad de PetMarket.

    A partir de los ingresos, costos, gastos operativos e impuestos,
    se calcula la utilidad bruta, utilidad neta y margen neto.
    """)

    # --------------------------------------------------------
    # SELECTOR DE FUNCIÓN
    # --------------------------------------------------------

    funcion_seleccionada = st.selectbox(
        "Seleccione la función",
        ["Calcular Margen Neto"]
    )

    # Histórico
    if "historico_margen" not in st.session_state:
        st.session_state.historico_margen = []

    st.subheader("Ingrese los datos financieros")

    ingresos = st.number_input(
        "Ingresos por ventas (S/)",
        min_value=0.0,
        step=100.0
    )

    costos = st.number_input(
        "Costo de los productos vendidos (S/)",
        min_value=0.0,
        step=100.0
    )

    gastos_operativos = st.number_input(
        "Gastos operativos (S/)",
        min_value=0.0,
        step=100.0
    )

    impuestos = st.number_input(
        "Impuestos (S/)",
        min_value=0.0,
        step=100.0
    )

    if st.button("Calcular margen neto"):

        try:

            # Ejecutamos la función de la librería externa
            resultado = calcular_margen_neto(
                ingresos,
                costos,
                gastos_operativos,
                impuestos
            )

            st.success(
                "Cálculo realizado correctamente."
            )

            st.subheader("Resultado")

            columna1, columna2, columna3 = st.columns(3)

            with columna1:

                st.metric(
                    "Utilidad bruta",
                    f"S/ {resultado['utilidad_bruta']:,.2f}"
                )

            with columna2:

                st.metric(
                    "Utilidad neta",
                    f"S/ {resultado['utilidad_neta']:,.2f}"
                )

            with columna3:

                st.metric(
                    "Margen neto",
                    f"{resultado['margen_neto_pct']:.2f}%"
                )

            # Guardamos el resultado en el histórico
            registro = {
                "Ingresos": ingresos,
                "Costos": costos,
                "Gastos Operativos": gastos_operativos,
                "Impuestos": impuestos,
                "Utilidad Bruta": resultado["utilidad_bruta"],
                "Utilidad Neta": resultado["utilidad_neta"],
                "Margen Neto (%)": resultado["margen_neto_pct"]
            }

            st.session_state.historico_margen.append(
                registro
            )

        except ValueError as error:

            st.error(
                f"Error: {error}"
            )

    # --------------------------------------------------------
    # HISTÓRICO
    # --------------------------------------------------------

    if len(st.session_state.historico_margen) > 0:

        st.subheader("Histórico de resultados")

        df_historico = pd.DataFrame(
            st.session_state.historico_margen
        )

        st.dataframe(
            df_historico,
            use_container_width=True
        )

    else:

        st.info(
            "Todavía no existen cálculos registrados."
        )


# ============================================================
# EJERCICIO 4
# CLASE EXTERNA + CRUD
# ============================================================

elif opcion == "Ejercicio 4":

    st.title("📦 Ejercicio 4 - Gestión de Inventario")

    st.markdown("""
    Este ejercicio utiliza la clase **InventarioProducto** proveniente
    de una librería externa.

    La aplicación permite gestionar el inventario de PetMarket mediante
    las operaciones básicas **CRUD**:

    - **Crear:** registrar un nuevo producto.
    - **Leer:** visualizar los productos.
    - **Actualizar:** modificar un producto existente.
    - **Eliminar:** retirar un producto del inventario.
    """)

    # Lista de productos
    if "inventario" not in st.session_state:
        st.session_state.inventario = []

    # Creamos las pestañas
    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(
        [
            "Crear",
            "Leer",
            "Actualizar",
            "Eliminar"
        ]
    )

    # ========================================================
    # CREATE - CREAR
    # ========================================================

    with tab_crear:

        st.subheader("Registrar nuevo producto")

        nombre = st.text_input(
            "Nombre del producto",
            key="crear_nombre",
            placeholder="Ejemplo: Arena sanitaria"
        )

        costo_unitario = st.number_input(
            "Costo unitario (S/)",
            min_value=0.0,
            step=1.0,
            key="crear_costo"
        )

        precio_unitario = st.number_input(
            "Precio de venta (S/)",
            min_value=0.0,
            step=1.0,
            key="crear_precio"
        )

        stock_actual = st.number_input(
            "Stock actual",
            min_value=0,
            step=1,
            key="crear_stock"
        )

        stock_minimo = st.number_input(
            "Stock mínimo",
            min_value=0,
            step=1,
            key="crear_stock_minimo"
        )

        if st.button(
            "Crear producto",
            key="boton_crear"
        ):

            if nombre == "":

                st.error(
                    "Debe ingresar el nombre del producto."
                )

            else:

                try:

                    # Creamos un objeto de la clase InventarioProducto
                    nuevo_producto = InventarioProducto(
                        nombre,
                        costo_unitario,
                        precio_unitario,
                        stock_actual,
                        stock_minimo
                    )

                    # Guardamos el objeto en nuestra lista
                    st.session_state.inventario.append(
                        nuevo_producto
                    )

                    st.success(
                        "Producto creado correctamente."
                    )

                except ValueError as error:

                    st.error(
                        f"Error: {error}"
                    )

    # ========================================================
    # READ - LEER
    # ========================================================

    with tab_leer:

        st.subheader("Inventario de productos")

        if len(st.session_state.inventario) > 0:

            lista_productos = []

            # Recorremos los objetos guardados
            for producto_inventario in st.session_state.inventario:

                # Utilizamos el método resumen de la clase
                datos_producto = producto_inventario.resumen()

                lista_productos.append(
                    datos_producto
                )

            df_inventario = pd.DataFrame(
                lista_productos
            )

            # Cambiamos los nombres para que sean
            # más fáciles de entender en la interfaz
            df_inventario = df_inventario.rename(
                columns={
                    "producto": "Producto",
                    "stock_actual": "Stock Actual",
                    "valor_inventario": "Valor Inventario",
                    "margen_unitario": "Margen Unitario",
                    "margen_pct": "Margen (%)",
                    "necesita_reposicion": "Necesita Reposición"
                }
            )

            st.dataframe(
                df_inventario,
                use_container_width=True
            )

        else:

            st.info(
                "Todavía no existen productos registrados."
            )

    # ========================================================
    # UPDATE - ACTUALIZAR
    # ========================================================

    with tab_actualizar:

        st.subheader("Actualizar producto")

        if len(st.session_state.inventario) > 0:

            # Obtenemos los nombres de los productos
            nombres_productos = []

            for producto_inventario in st.session_state.inventario:

                nombres_productos.append(
                    producto_inventario.nombre
                )

            producto_seleccionado = st.selectbox(
                "Seleccione un producto",
                nombres_productos,
                key="producto_actualizar"
            )

            # Buscamos la posición del producto
            indice = nombres_productos.index(
                producto_seleccionado
            )

            producto_original = (
                st.session_state.inventario[indice]
            )

            st.write(
                "Ingrese los nuevos valores:"
            )

            nuevo_costo = st.number_input(
                "Nuevo costo unitario (S/)",
                min_value=0.0,
                value=float(
                    producto_original.costo_unitario
                ),
                key="actualizar_costo"
            )

            nuevo_precio = st.number_input(
                "Nuevo precio de venta (S/)",
                min_value=0.0,
                value=float(
                    producto_original.precio_unitario
                ),
                key="actualizar_precio"
            )

            nuevo_stock = st.number_input(
                "Nuevo stock actual",
                min_value=0,
                value=int(
                    producto_original.stock_actual
                ),
                key="actualizar_stock"
            )

            nuevo_stock_minimo = st.number_input(
                "Nuevo stock mínimo",
                min_value=0,
                value=int(
                    producto_original.stock_minimo
                ),
                key="actualizar_stock_minimo"
            )

            if st.button(
                "Actualizar producto",
                key="boton_actualizar"
            ):

                try:

                    producto_actualizado = InventarioProducto(
                        producto_original.nombre,
                        nuevo_costo,
                        nuevo_precio,
                        nuevo_stock,
                        nuevo_stock_minimo
                    )

                    # Reemplazamos el producto anterior
                    st.session_state.inventario[indice] = (
                        producto_actualizado
                    )

                    st.success(
                        "Producto actualizado correctamente."
                    )

                except ValueError as error:

                    st.error(
                        f"Error: {error}"
                    )

        else:

            st.info(
                "Primero debe registrar un producto."
            )

    # ========================================================
    # DELETE - ELIMINAR
    # ========================================================

    with tab_eliminar:

        st.subheader("Eliminar producto")

        if len(st.session_state.inventario) > 0:

            nombres_eliminar = []

            for producto_inventario in st.session_state.inventario:

                nombres_eliminar.append(
                    producto_inventario.nombre
                )

            producto_eliminar = st.selectbox(
                "Seleccione el producto que desea eliminar",
                nombres_eliminar,
                key="producto_eliminar"
            )

            st.warning(
                "Esta acción eliminará el producto del inventario."
            )

            if st.button(
                "Eliminar producto",
                key="boton_eliminar"
            ):

                indice_eliminar = nombres_eliminar.index(
                    producto_eliminar
                )

                st.session_state.inventario.pop(
                    indice_eliminar
                )

                st.success(
                    "Producto eliminado correctamente."
                )

                st.rerun()

        else:

            st.info(
                "No existen productos para eliminar."
            )

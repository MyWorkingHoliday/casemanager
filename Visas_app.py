import streamlit as st

# Datos de la Skilled Occupation List (SOL)
skilled_occupation_list = {
    "111111": {
        "nombre": "Gerente de Administración",
        "visas": ["189", "190", "491"],
        "edad_maxima": 45,
        "experiencia_minima": 2
    },
    # ... (agrega más ocupaciones aquí)
}

# Diccionario de visas
visas_australianas = {
    "189": "Visa Independiente de Trabajo Calificado (Subclass 189)",
    "190": "Visa Nominada de Trabajo Calificado (Subclass 190)",
    "491": "Visa de Trabajo Calificado Regional (Subclass 491)",
    "482": "Visa de Patrocinio Temporal (Subclass 482)"
}

def recomendar_visa(edad, profesion, experiencia):
    recomendaciones = []
    for codigo, detalles in skilled_occupation_list.items():
        if profesion.lower() in detalles["nombre"].lower():
            if edad <= detalles["edad_maxima"] and experiencia >= detalles["experiencia_minima"]:
                for visa in detalles["visas"]:
                    recomendaciones.append({
                        "visa": visas_australianas[visa],
                        "ocupacion": detalles["nombre"],
                        "codigo_anzsco": codigo
                    })
    return recomendaciones if recomendaciones else "No se encontraron visas adecuadas."

def main():
    st.title("🗺️ Recomendador de Visas Australianas")
    edad = st.number_input("Edad", min_value=18, max_value=100, value=30)
    profesion = st.text_input("Profesión (ej: Gerente de Administración)", "")
    experiencia = st.number_input("Años de experiencia laboral", min_value=0, value=3)
    
    if st.button("🔍 Buscar recomendaciones"):
        resultado = recomendar_visa(edad, profesion.strip(), experiencia)
        if isinstance(resultado, list):
            st.success("🎉 ¡Estas son tus opciones:")
            for rec in resultado:
                st.markdown(f"""
                **Ocupación:** {rec['ocupacion']}  
                **Código ANZSCO:** `{rec['codigo_anzsco']}`  
                **Visa:** {rec['visa']}
                """)
        else:
            st.error("⚠️ " + resultado)

if __name__ == "__main__":
    main()

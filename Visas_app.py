import streamlit as st

# Datos de la Skilled Occupation List (SOL)
skilled_occupation_list = {
    "411511": {"nombre": "Aboriginal and Torres Strait Islander Health Worker", "visas": ["494", "187"], "edad_maxima": 45, "experiencia_minima": 2},
    "141999": {"nombre": "Accommodation and Hospitality Managers nec", "visas": ["190", "407", "489", "482", "187", "494", "491", "186"], "edad_maxima": 45, "experiencia_minima": 3},
    "221111": {"nombre": "Accountant (General)", "visas": ["186", "189", "190", "407", "485", "489", "482", "187", "494", "491"], "edad_maxima": 45, "experiencia_minima": 2},
    "211111": {"nombre": "Actor", "visas": ["494", "187"], "edad_maxima": 40, "experiencia_minima": 2},
    "224111": {"nombre": "Actuary", "visas": ["186", "189", "190", "407", "485", "489", "482", "187", "494", "491"], "edad_maxima": 45, "experiencia_minima": 4},
    "233911": {"nombre": "Aeronautical Engineer", "visas": ["186", "189", "190", "407", "485", "489", "482", "187", "494", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "231111": {"nombre": "Aeroplane Pilot", "visas": ["407", "489", "482", "187", "494", "491", "186"], "edad_maxima": 50, "experiencia_minima": 5},
    "234111": {"nombre": "Agricultural Consultant", "visas": ["186", "189", "190", "407", "485", "489", "482", "187", "494", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "233912": {"nombre": "Agricultural Engineer", "visas": ["186", "189", "190", "407", "485", "489", "482", "187", "494", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "234112": {"nombre": "Agricultural Scientist", "visas": ["186", "189", "190", "407", "485", "489", "482", "187", "494", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "312111": {"nombre": "Architectural Draftsperson", "visas": ["190", "491", "494"], "edad_maxima": 45, "experiencia_minima": 2},
    "232111": {"nombre": "Architect", "visas": ["186", "189", "190", "407", "485", "489", "482", "187", "494", "491"], "edad_maxima": 45, "experiencia_minima": 3}
}

# Diccionario de visas
visas_australianas = {
    "186": "Employer Nomination Scheme (ENS) visa (Subclass 186)",
    "187": "Regional Sponsored Migration Scheme (RSMS) visa (Subclass 187)",
    "189": "Skilled Independent visa (Subclass 189)",
    "190": "Skilled Nominated visa (Subclass 190)",
    "407": "Training visa (Subclass 407)",
    "482": "Skills in Demand visa (Subclass 482)",
    "485": "Temporary Graduate visa (Subclass 485)",
    "489": "Skilled Regional (Provisional) visa (Subclass 489)",
    "491": "Skilled Work Regional (Provisional) visa (Subclass 491)",
    "494": "Skilled Employer Sponsored Regional (Provisional) visa (Subclass 494)"
}

def recomendar_visa(edad, profesion, experiencia):
    recomendaciones = []
    for codigo, detalles in skilled_occupation_list.items():
        if profesion.lower() in detalles["nombre"].lower():
            if edad <= detalles["edad_maxima"] and experiencia >= detalles["experiencia_minima"]:
                for visa in detalles["visas"]:
                    recomendaciones.append({
                        "visa": visas_australianas.get(visa, "Visa no encontrada"),
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
        if isinstance(resultado, list) and resultado:
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

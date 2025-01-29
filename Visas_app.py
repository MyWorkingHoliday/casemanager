import streamlit as st

# Datos corregidos con nombres en inglés
skilled_occupation_list = {
    "221111": {
        "nombre": "Accountant (General)",
        "visas": ["186", "189", "190", "491"],
        "edad_maxima": 45,
        "experiencia_minima": 3
    },
    "233512": {
        "nombre": "Mechanical Engineer",
        "visas": ["186", "190", "491", "494"],
        "edad_maxima": 45,
        "experiencia_minima": 5
    },
    "261312": {
        "nombre": "Developer Programmer",
        "visas": ["186", "189", "190", "482"],
        "edad_maxima": 45,
        "experiencia_minima": 3
    },
    "272311": {
        "nombre": "Clinical Psychologist",
        "visas": ["186", "189", "190"],
        "edad_maxima": 45,
        "experiencia_minima": 5
    },
    "351311": {
        "nombre": "Chef",
        "visas": ["190", "482", "494"],
        "edad_maxima": 45,
        "experiencia_minima": 3
    }
}

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
    "494": "Skilled Employer Sponsored Regional (Provisional) visa (Subclass 494)"}
}

def recomendar_visa(edad, codigo_anzsco, experiencia):
    if codigo_anzsco not in skilled_occupation_list:
        return "Código ANZSCO no válido"
    
    ocupacion = skilled_occupation_list[codigo_anzsco]
    recomendaciones = []
    
    if edad > ocupacion["edad_maxima"]:
        return f"Edad excede el máximo de {ocupacion['edad_maxima']} años"
    
    if experiencia < ocupacion["experiencia_minima"]:
        return f"Experiencia insuficiente (mínimo {ocupacion['experiencia_minima']} años)"
    
    for visa in ocupacion["visas"]:
        recomendaciones.append({
            "visa": visas_australianas[visa],
            "detalles": "Requisitos adicionales: Examen de inglés y evaluación de habilidades"
        })
    
    return recomendaciones

def main():
    st.title("🧭 Asesor de Visas Australiano")
    
    with st.expander("ℹ️ Instrucciones"):
        st.write("1. Ingrese su código ANZSCO de 6 dígitos")
        st.write("2. Verifique los requisitos específicos para su ocupación")
        st.write("3. Consulte la lista oficial de códigos ANZSCO para referencia")
    
    edad = st.number_input("Edad", min_value=18, max_value=70, value=30)
    codigo_anzsco = st.text_input("Código ANZSCO (ej: 221111)", max_chars=6)
    experiencia = st.number_input("Años de experiencia relevante", min_value=0, value=3)
    
    if st.button("🔍 Verificar elegibilidad"):
        if len(codigo_anzsco) != 6 or not codigo_anzsco.isdigit():
            st.error("❌ Código ANZSCO inválido: debe ser un número de 6 dígitos")
            return
            
        resultado = recomendar_visa(edad, codigo_anzsco, experiencia)
        
        if isinstance(resultado, list):
            nombre_ocupacion = skilled_occupation_list[codigo_anzsco]["nombre"]
            st.success(f"🎉 Oportunidades para: {nombre_ocupacion}")
            for opcion in resultado:
                st.markdown(f"""
                **Tipo de Visa:** {opcion['visa']}  
                **Requisitos:** {opcion['detalles']}
                """)
        else:
            st.error(f"⚠️ {resultado}")

if __name__ == "__main__":
    main()

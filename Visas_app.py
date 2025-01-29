import streamlit as st

# Base de datos de ocupaciones calificadas (SOL)
skilled_occupations = {
    "221111": {
        "name": "Accountant (General)",
        "visas": ["189", "190", "491", "485"],
        "max_age": 45,
        "min_experience": 3
    },
    "233512": {
        "name": "Mechanical Engineer",
        "visas": ["189", "190", "491", "482"],
        "max_age": 45,
        "min_experience": 5
    },
    "261312": {
        "name": "Developer Programmer",
        "visas": ["189", "190", "491", "482"],
        "max_age": 45,
        "min_experience": 3
    },
    "351311": {
        "name": "Chef",
        "visas": ["190", "491", "482"],
        "max_age": 45,
        "min_experience": 2
    },
    "253111": {
        "name": "General Practitioner",
        "visas": ["189", "190", "491"],
        "max_age": 50,
        "min_experience": 5
    }
}

visa_descriptions = {
    "189": "Skilled Independent Visa (Permanent)",
    "190": "Skilled Nominated Visa (Permanent)",
    "491": "Skilled Work Regional Visa (Provisional)",
    "482": "Temporary Skill Shortage Visa",
    "485": "Temporary Graduate Visa"
}

def find_matching_occupations(user_input):
    occupation_names = [occ["name"] for occ in skilled_occupations.values()]
    matches = process.extract(user_input, occupation_names, limit=5)
    return [match[0] for match in matches if match[1] > 60]

def get_occupation_details(occupation_name):
    for code, details in skilled_occupations.items():
        if details["name"].lower() == occupation_name.lower():
            return {"code": code, **details}
    return None

def check_eligibility(age, experience, occupation_details):
    eligibility = {
        "visas": [],
        "requirements": []
    }
    
    if age > occupation_details["max_age"]:
        eligibility["requirements"].append(f"❌ Age exceeds maximum limit ({occupation_details['max_age']} years)")
    else:
        eligibility["requirements"].append(f"✅ Age requirement met ({age}/{occupation_details['max_age']} years)")
    
    if experience < occupation_details["min_experience"]:
        eligibility["requirements"].append(f"❌ Insufficient experience ({experience}/{occupation_details['min_experience']} years)")
    else:
        eligibility["requirements"].append(f"✅ Experience requirement met ({experience}/{occupation_details['min_experience']} years)")
    
    if age <= occupation_details["max_age"] and experience >= occupation_details["min_experience"]:
        eligibility["visas"] = [visa_descriptions[visa] for visa in occupation_details["visas"]]
    
    return eligibility

def main():
    st.title("Visa Eligibility")
    
    with st.expander("ℹ️ Cómo usar"):
        st.write("""
        1. Ingresa tu profesión en inglés (ej: "accountant" o "engineer")
        2. Selecciona tu ocupación exacta del menú desplegable
        3. Ingresa tu edad y años de experiencia
        4. Revisa las opciones de visa disponibles
        """)
    
    # Paso 1: Búsqueda de profesión
    profession_query = st.text_input("🔍 Ingresa tu profesión:", placeholder="Ej: Software Developer")
    
    if profession_query:
        matches = find_matching_occupations(profession_query)
        if matches:
            selected_occupation = st.selectbox("Selecciona tu ocupación:", matches)
        else:
            st.error("No se encontraron coincidencias. Intenta con otras palabras clave.")
            return
    else:
        return
    
    # Paso 2: Entrada de datos personales
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Edad", min_value=18, max_value=70, value=30)
    with col2:
        experience = st.number_input("Años de experiencia relevante", min_value=0, max_value=50, value=3)
    
    # Paso 3: Verificación de elegibilidad
    if st.button("Verificar elegibilidad"):
        occupation_details = get_occupation_details(selected_occupation)
        
        if not occupation_details:
            st.error("Ocupación no encontrada en la lista")
            return
        
        eligibility = check_eligibility(age, experience, occupation_details)
        
        st.subheader(f"Resultados para: {occupation_details['name']}")
        st.caption(f"Código ANZSCO: {occupation_details['code']}")
        
        # Mostrar requisitos
        st.markdown("### Requisitos clave:")
        for req in eligibility["requirements"]:
            st.markdown(req)
        
        # Mostrar visas disponibles
        st.markdown("### 🎉 Visas disponibles:")
        if eligibility["visas"]:
            for visa in eligibility["visas"]:
                st.success(f"#### {visa}")
                st.caption(f"Requisitos adicionales: Examen de inglés y evaluación de habilidades")
        else:
            st.error("No calificas para ninguna visa con los criterios actuales")

if __name__ == "__main__":
    main()

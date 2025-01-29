import streamlit as st
from fuzzywuzzy import process

# Datos de ocupaciones en inglés
skilled_occupation_list = {
    "221111": {"nombre": "Accountant (General)", "visas": ["186", "189", "190"], "edad_maxima": 45, "experiencia_minima": 3},
    "233512": {"nombre": "Mechanical Engineer", "visas": ["186", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "261312": {"nombre": "Developer Programmer", "visas": ["186", "482"], "edad_maxima": 45, "experiencia_minima": 3},
    "351311": {"nombre": "Chef", "visas": ["190", "482"], "edad_maxima": 45, "experiencia_minima": 2},
    "253111": {"nombre": "General Practitioner", "visas": ["186", "189"], "edad_maxima": 50, "experiencia_minima": 5}
}

visas_australianas = {
    "186": "Employer Nomination Scheme (Subclass 186)",
    "189": "Skilled Independent Visa (Subclass 189)",
    "190": "Skilled Nominated Visa (Subclass 190)",
    "482": "Temporary Skill Shortage Visa (Subclass 482)",
    "491": "Skilled Work Regional Visa (Subclass 491)"
}

def buscar_profesion(query, limit=5):
    nombres = [ocupacion["nombre"] for ocupacion in skilled_occupation_list.values()]
    matches = process.extract(query, nombres, limit=limit)
    return [match for match in matches if match[1] > 65]  # Filtra coincidencias pobres

def obtener_detalles_por_nombre(nombre):
    for codigo, detalles in skilled_occupation_list.items():
        if detalles["nombre"].lower() == nombre.lower():
            return {"codigo": codigo, **detalles}
    return None

def recomendar_visa(edad, detalles_ocupacion, experiencia):
    if edad > detalles_ocupacion["edad_maxima"]:
        return f"❌ Age exceeds maximum limit of {detalles_ocupacion['edad_maxima']} years"
    
    if experiencia < detalles_ocupacion["experiencia_minima"]:
        return f"❌ Insufficient experience (minimum {detalles_ocupacion['experiencia_minima']} years required)"
    
    recomendaciones = []
    for visa in detalles_ocupacion["visas"]:
        recomendaciones.append({
            "visa": visas_australianas[visa],
            "requirements": [
                "English proficiency exam (IELTS 6.0+)",
                "Skills assessment",
                "Health insurance"
            ]
        })
    
    return recomendaciones

def main():
    st.title("🇦🇺 Australian Visa Matcher")
    
    with st.expander("ℹ️ How to use"):
        st.write("1. Type your profession (e.g. 'accountant' or 'engineer')")
        st.write("2. Select your exact occupation from the dropdown")
        st.write("3. View visa options and requirements")
    
    # Paso 1: Búsqueda de profesión
    col1, col2 = st.columns([3, 1])
    with col1:
        query = st.text_input("Search your profession:", placeholder="e.g. Software Developer")
    with col2:
        st.write("<div style='height: 28px'></div>", unsafe_allow_html=True)
        search_btn = st.button("🔍 Search")
    
    # Manejar búsqueda
    if search_btn and query:
        matches = buscar_profesion(query)
        if matches:
            st.session_state["matches"] = [m[0] for m in matches]
        else:
            st.error("No matching professions found. Try different keywords.")
    
    # Mostrar resultados de búsqueda
    if "matches" in st.session_state:
        selected_ocup = st.selectbox("Select your exact occupation:", st.session_state["matches"])
        
        # Paso 2: Input de detalles
        with st.form("visa_form"):
            edad = st.slider("Age", 18, 55, 30)
            experiencia = st.slider("Years of relevant experience", 0, 20, 3)
            submit = st.form_submit_button("Check Visa Options")
            
            if submit and selected_ocup:
                detalles = obtener_detalles_por_nombre(selected_ocup)
                if detalles:
                    resultado = recomendar_visa(edad, detalles, experiencia)
                    
                    if isinstance(resultado, list):
                        st.success(f"## Visa Options for {detalles['nombre']}")
                        for visa in resultado:
                            with st.expander(f"**{visa['visa']}**", expanded=True):
                                st.markdown("**Main Requirements:**")
                                for req in visa["requirements"]:
                                    st.markdown(f"- {req}")
                                st.markdown(f"**ANZSCO Code:** `{detalles['codigo']}`")
                    else:
                        st.error(resultado)
                else:
                    st.error("Occupation details not found")

if __name__ == "__main__":
    main()

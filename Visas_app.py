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
    "232111": {"nombre": "Architect", "visas": ["186", "189", "190", "407", "485", "489", "482", "187", "494", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "252711": {"nombre": "Audiologist", "visas": ["186", "189", "190", "407", "489", "187", "494", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "351311": {"nombre": "Chef", "visas": ["190", "491", "494", "482", "407"], "edad_maxima": 45, "experiencia_minima": 2},
    "233512": {"nombre": "Mechanical Engineer", "visas": ["186", "189", "190", "407", "485", "489", "482", "187", "494", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "253111": {"nombre": "General Practitioner", "visas": ["186", "189", "190", "407", "489", "482", "187", "494", "491"], "edad_maxima": 50, "experiencia_minima": 5},
    "233213": {"nombre": "Quantity Surveyor", "visas": ["186", "189", "190", "489", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "272311": {"nombre": "Clinical Psychologist", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "261312": {"nombre": "Developer Programmer", "visas": ["186", "189", "190", "491", "482"], "edad_maxima": 45, "experiencia_minima": 3},
    "133111": {"nombre": "Construction Project Manager", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "134211": {"nombre": "Medical Administrator", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "272499": {"nombre": "Social Worker", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "241111": {"nombre": "Early Childhood (Pre-primary School) Teacher", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "252411": {"nombre": "Occupational Therapist", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "252511": {"nombre": "Physiotherapist", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "252611": {"nombre": "Podiatrist", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "253912": {"nombre": "Emergency Medicine Specialist", "visas": ["186", "189", "190", "491"], "edad_maxima": 50, "experiencia_minima": 5},
    "253317": {"nombre": "Intensive Care Specialist", "visas": ["186", "189", "190", "491"], "edad_maxima": 50, "experiencia_minima": 5},
    "272511": {"nombre": "Clinical Psychologist", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "134299": {"nombre": "Health and Welfare Services Manager nec", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "251512": {"nombre": "Industrial Pharmacist", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "251311": {"nombre": "Environmental Health Officer", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "234311": {"nombre": "Conservator", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "272399": {"nombre": "Psychologist nec", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "252312": {"nombre": "Dentist", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "254425": {"nombre": "Registered Nurse (Paediatrics)", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "133512": {"nombre": "Production Manager (Manufacturing)", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "241311": {"nombre": "Middle School Teacher", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "232212": {"nombre": "Surveyor", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "139914": {"nombre": "Quality Assurance Manager", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "135199": {"nombre": "ICT Managers nec", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "253111": {"nombre": "General Practitioner", "visas": ["186", "189", "190", "407", "489", "482", "187", "494", "491"], "edad_maxima": 50, "experiencia_minima": 5},
    "233213": {"nombre": "Quantity Surveyor", "visas": ["186", "189", "190", "489", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "272311": {"nombre": "Clinical Psychologist", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "261312": {"nombre": "Developer Programmer", "visas": ["186", "189", "190", "491", "482"], "edad_maxima": 45, "experiencia_minima": 3},
    "133111": {"nombre": "Construction Project Manager", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "134211": {"nombre": "Medical Administrator", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "312911": {"nombre": "Maintenance Planner", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "149913": {"nombre": "Facilities Manager", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "263111": {"nombre": "Computer Network and Systems Engineer", "visas": ["186", "189", "190", "491", "482"], "edad_maxima": 45, "experiencia_minima": 3},
    "232411": {"nombre": "Graphic Designer", "visas": ["190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "342414": {"nombre": "Telecommunications Technician", "visas": ["190", "491", "482"], "edad_maxima": 45, "experiencia_minima": 3},
    "251211": {"nombre": "Medical Diagnostic Radiographer", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "251214": {"nombre": "Sonographer", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "253315": {"nombre": "Endocrinologist", "visas": ["186", "189", "190", "491"], "edad_maxima": 50, "experiencia_minima": 5},
    "254415": {"nombre": "Registered Nurse (Critical Care and Emergency)", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "312512": {"nombre": "Mechanical Engineering Technician", "visas": ["190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "313214": {"nombre": "Telecommunications Technical Officer or Technologist", "visas": ["190", "491", "482"], "edad_maxima": 45, "experiencia_minima": 3},
    "234213": {"nombre": "Wine Maker", "visas": ["190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "233214": {"nombre": "Structural Engineer", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "134311": {"nombre": "School Principal", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
    "241411": {"nombre": "Secondary School Teacher", "visas": ["186", "189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 3},
        "111211": {"nombre": "Corporate General Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "121111": {"nombre": "Aquaculture Farmer", "visas": ["491"], "edad_maxima": 45, "experiencia_minima": 3},
    "121311": {"nombre": "Apiarist", "visas": ["491"], "edad_maxima": 45, "experiencia_minima": 3},
    "121313": {"nombre": "Dairy Cattle Farmer", "visas": ["491"], "edad_maxima": 45, "experiencia_minima": 3},
    "121315": {"nombre": "Goat Farmer", "visas": ["491"], "edad_maxima": 45, "experiencia_minima": 3},
    "121318": {"nombre": "Pig Farmer", "visas": ["491"], "edad_maxima": 45, "experiencia_minima": 3},
    "121321": {"nombre": "Poultry Farmer", "visas": ["491"], "edad_maxima": 45, "experiencia_minima": 3},
    "121611": {"nombre": "Flower Grower", "visas": ["491"], "edad_maxima": 45, "experiencia_minima": 3},
    "131112": {"nombre": "Sales and Marketing Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 4},
    "131113": {"nombre": "Advertising Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 4},
    "132111": {"nombre": "Corporate Services Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 4},
    "132211": {"nombre": "Finance Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 4},
    "132311": {"nombre": "Human Resource Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 4},
    "132411": {"nombre": "Policy and Planning Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 4},
    "132511": {"nombre": "Research and Development Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 4},
    "133112": {"nombre": "Project Builder", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "133211": {"nombre": "Engineering Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "133511": {"nombre": "Production Manager (Forestry)", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "133612": {"nombre": "Procurement Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 4},
    "134212": {"nombre": "Nursing Clinical Director", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "134213": {"nombre": "Primary Health Organisation Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "134411": {"nombre": "Faculty Head", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "134499": {"nombre": "Education Managers nec", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "135111": {"nombre": "Chief Information Officer", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "135112": {"nombre": "ICT Project Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "135199": {"nombre": "ICT Managers nec", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 5},
    "139911": {"nombre": "Arts Administrator or Manager", "visas": ["189", "190", "491"], "edad_maxima": 45, "experiencia_minima": 4},
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
    st.title("🗺️ Visa Profile - StudyFirst")
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

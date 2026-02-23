import streamlit as st
import random

st.set_page_config(page_title="Rêve de Dragon - Module de Prédiction")

st.title("🐉 Module de Prédiction - Rêve de Dragon")

# ==============================
# DONNÉES
# ==============================

cartes = {
    "Le Luth": {"type":"Bénéfique","effet_principal":"Une mélodie onirique soigne les blessures.",
                "effet_comp":"+2 Musique","effet_attr":"+2 OUIE"},
    "Les Marais": {"type":"Maléfique","effet_principal":"Les pas s’enlisent.",
                   "effet_comp":"-1 Survie (Marais)","effet_attr":"-1 AGILITÉ"},
}

liste_cartes = list(cartes.keys())

# ==============================
# INITIALISATION SESSION
# ==============================

if "carte_resultat" not in st.session_state:
    st.session_state.carte_resultat = None

if "effet_type" not in st.session_state:
    st.session_state.effet_type = None

# ==============================
# SÉLECTION
# ==============================

c1 = st.selectbox("Première carte", liste_cartes)
c2 = st.selectbox("Seconde carte", liste_cartes, index=1)

if st.button("Tirer les cartes"):

    type1 = cartes[c1]["type"]
    type2 = cartes[c2]["type"]

    if type1 == type2:
        carte = random.choice([c1, c2])
    else:
        st.warning("Tirage mixte : faites un jet de Chance.")
        jet = st.selectbox("Jet de Chance", ["Réussi", "Raté"])

        if jet == "Réussi":
            carte = c1 if cartes[c1]["type"] == "Bénéfique" else c2
        else:
            carte = c1 if cartes[c1]["type"] == "Maléfique" else c2

    # On stocke le résultat
    st.session_state.carte_resultat = carte
    st.session_state.effet_type = cartes[carte]["type"]

# ==============================
# AFFICHAGE PERSISTANT
# ==============================

if st.session_state.carte_resultat:

    carte = st.session_state.carte_resultat
    effet = cartes[carte]

    st.markdown(f"### Effet {effet['type']}")
    st.write(effet["effet_principal"])
    st.write("Compétences :", effet["effet_comp"])
    st.write("Attributs :", effet["effet_attr"])

    st.subheader("🔮 Jet RÊVE / Astrologie à -Dr7")

    jet_duree = st.selectbox(
        "Résultat du jet",
        ["Échec", "Normal", "Significative", "Particulière", "Double Particulière", "01"]
    )

    table_duree = {
        "Échec": "Pas de prédiction ce jour.",
        "Normal": "1 jour",
        "Significative": "4 jours",
        "Particulière": "10 jours",
        "Double Particulière": "1 mois",
        "01": "Permanent"
    }

    st.success(f"Durée : {table_duree[jet_duree]}")

import streamlit as st
import random

st.set_page_config(page_title="Rêve de Dragon - Module de Prédiction")
st.title("🐉 Module de Prédiction - Rêve de Dragon")

# ==============================
# DONNÉES CARTES
# ==============================
cartes = {

    # BÉNÉFIQUES
    "Le Luth": {"type":"Bénéfique","effet_principal":"Une mélodie onirique soigne les blessures et apaise les esprits.",
                "effet_comp":"+2 Musique ou +1 Chant","effet_attr":"+2 OUIE, +1 RÊVE"},

    "Le Coffre": {"type":"Bénéfique","effet_principal":"Un trésor ou un objet utile se révèle.",
                  "effet_comp":"+1 Commerce ou +1 Orfèvrerie","effet_attr":"+1 INTELLECT, +1 CHANCE"},

    "La Licorne": {"type":"Bénéfique","effet_principal":"Une aura de pureté protège le personnage.",
                   "effet_comp":"+1 Vigilance","effet_attr":"+1 CONSTITUTION, +1 EMPATHIE"},

    "Le Haut Rêvant": {"type":"Bénéfique","effet_principal":"Une vision prophétique éclaire l’esprit.",
                       "effet_comp":"+1 Oniros","effet_attr":"+1 RÊVE, +1 VOLONTÉ"},

    "Le Grimoire": {"type":"Bénéfique","effet_principal":"Un savoir oublié devient accessible.",
                    "effet_comp":"+1 Narcos ou +1 Thanatos","effet_attr":"+1 INTELLECT, +1 VOLONTÉ"},

    "La Vierge": {"type":"Bénéfique","effet_principal":"Une bénédiction de pureté et de chance.",
                  "effet_comp":"+1 Séduction","effet_attr":"+1 EMPATHIE, +1 CHANCE"},

    "La Couronne": {"type":"Bénéfique","effet_principal":"Autorité et charisme se renforcent.",
                    "effet_comp":"+1 Commerce","effet_attr":"+1 APPARENCE, +1 INTELLECT"},

    "Le Soleil": {"type":"Bénéfique","effet_principal":"La lumière dissipe ombres et malédictions.",
                  "effet_comp":"+1 Survie (Forêts)","effet_attr":"+1 VUE, +1 RÊVE"},

    "Le Vaisseau": {"type":"Bénéfique","effet_principal":"Le voyage devient sûr et favorable.",
                    "effet_comp":"+1 Navigation","effet_attr":"+1 AGILITÉ, +1 INTELLECT"},

    "Le Voyageur": {"type":"Bénéfique","effet_principal":"Un allié providentiel apparaît.",
                    "effet_comp":"+1 Survie (Extérieur)","effet_attr":"+1 VOLONTÉ, +1 EMPATHIE"},

    "L’Auberge": {"type":"Bénéfique","effet_principal":"Repos réparateur et chaleur humaine.",
                  "effet_comp":"+1 Médecine ou +1 Cuisine","effet_attr":"+1 CONSTITUTION, +1 ODORAT-GOÛT"},

    # MALÉFIQUES
    "Les Marais": {"type":"Maléfique","effet_principal":"Les pas s’enlisent dans la brume stagnante.",
                   "effet_comp":"-1 Survie (Marais)","effet_attr":"-1 AGILITÉ, -1 VUE"},

    "Le Rabot": {"type":"Maléfique","effet_principal":"Les outils et armes se fragilisent.",
                 "effet_comp":"-1 Métallurgie","effet_attr":"-1 FORCE, -1 DEXTÉRITÉ"},

    "L’Esprit Thanataire": {"type":"Maléfique","effet_principal":"Des visions de mort troublent l’âme.",
                            "effet_comp":"-1 Oniros","effet_attr":"-1 VOLONTÉ, -1 RÊVE"},

    "La Sébile": {"type":"Maléfique","effet_principal":"La chance se détourne.",
                  "effet_comp":"-1 Commerce","effet_attr":"-1 CHANCE, -1 EMPATHIE"},

    "Le Groin": {"type":"Maléfique","effet_principal":"Une créature brutale attaque.",
                 "effet_comp":"-1 Corps à corps","effet_attr":"-1 FORCE, -1 AGILITÉ"},

    "L’Épée": {"type":"Maléfique","effet_principal":"Un conflit éclate soudainement.",
               "effet_comp":"-1 Epées à 1 main","effet_attr":"-1 FORCE, -1 VOLONTÉ"},

    "Le Gibet": {"type":"Maléfique","effet_principal":"Une aura de peur s’installe.",
                 "effet_comp":"-1 Séduction","effet_attr":"-1 VOLONTÉ, -1 EMPATHIE"},

    "La Lune": {"type":"Maléfique","effet_principal":"La folie nocturne trouble les esprits.",
                "effet_comp":"-1 Hypnos","effet_attr":"-1 RÊVE, -1 VOLONTÉ"},

    "Le Château": {"type":"Maléfique","effet_principal":"Un lieu hostile piège les héros.",
                   "effet_comp":"-1 Navigation","effet_attr":"-1 INTELLECT, -1 AGILITÉ"},

    "La Déchirure": {"type":"Maléfique","effet_principal":"Une faille onirique s’ouvre.",
                     "effet_comp":"-1 Survie (Extérieur)","effet_attr":"-1 VOLONTÉ, -1 INTELLECT"},
}

liste_cartes = list(cartes.keys())

# ==============================
# SESSION STATE
# ==============================
if "tirage_fait" not in st.session_state:
    st.session_state.tirage_fait = False
if "carte_resultat" not in st.session_state:
    st.session_state.carte_resultat = None
if "mixte" not in st.session_state:
    st.session_state.mixte = False
if "jet_chance" not in st.session_state:
    st.session_state.jet_chance = None

# ==============================
# SÉLECTION CARTES
# ==============================
c1 = st.selectbox("Première carte", liste_cartes)
c2 = st.selectbox("Seconde carte", liste_cartes, index=1)

if st.button("Tirer les cartes"):
    type1 = cartes[c1]["type"]
    type2 = cartes[c2]["type"]

    if type1 == type2:
        # Tirage homogène → effet directement
        carte = random.choice([c1, c2])
        st.session_state.carte_resultat = carte
        st.session_state.mixte = False
        st.session_state.tirage_fait = True
    else:
        # Tirage mixte → demander jet de chance
        st.session_state.mixte = True
        st.session_state.tirage_fait = True

# ==============================
# JET DE CHANCE (si mixte)
# ==============================
if st.session_state.tirage_fait and st.session_state.mixte:
    st.warning("Tirage mixte : faites un jet de CHANCE à 0.")

    jet_chance = st.selectbox("Résultat du jet de Chance", ["Réussi", "Raté"], key="jet_chance")
    st.session_state.jet_chance = jet_chance

    if st.session_state.jet_chance:
        # Déterminer quelle carte s'applique
        carte = c1 if (cartes[c1]["type"] == "Bénéfique" and st.session_state.jet_chance == "Réussi") \
                    or (cartes[c1]["type"] == "Maléfique" and st.session_state.jet_chance == "Raté") else c2
        st.session_state.carte_resultat = carte

# ==============================
# AFFICHAGE DE L'EFFET
# ==============================
if st.session_state.carte_resultat:
    carte = st.session_state.carte_resultat
    effet = cartes[carte]

    st.markdown(f"### Effet {effet['type']}")
    st.write(effet["effet_principal"])
    st.write("Compétences :", effet["effet_comp"])
    st.write("Attributs :", effet["effet_attr"])

    # ==============================
    # JET RÊVE / ASTROLOGIE
    # ==============================
    st.subheader("🔮 Jet Pts de RÊVE / Astrologie à -Dr7")
    jet_duree = st.selectbox(
        "Résultat du jet",
        ["Échec", "Normal", "Significative", "Particulière", "Double Particulière", "01"],
        key="jet_duree"
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

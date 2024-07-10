import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'user',
   'password': 'userMDP',
   'email': 'ericrascle42@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'ericrascle42@gmail.com ',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)
authenticator.login()

if st.session_state["authentication_status"]:
      
    with st.sidebar:
        selection = option_menu(
                menu_title="Menu",
                options = ["Accueil", "Photos"],
                
            )
    
        # Le bouton de déconnexion
        st.write(f"Bienvenu(e) {lesDonneesDesComptes['usernames']['root']['name']}")
        authenticator.logout("Déconnexion")

    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil !")
        st.image('https://media.gettyimages.com/id/1138843777/fr/vectoriel/grand-groupe-de-personnes-c%C3%A9l%C3%A9brant.jpg?s=612x612&w=gi&k=20&c=VmpwgVZEKQvq061f54PVnW-24zv2l2hsylNK2DtnhLE=')
    elif selection == "Photos":
        st.title("Bienvenu(e) sur mon album photo:cat::dog::owl:")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        with col3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg")

elif st.session_state["authentication_status"] is False:
    st.error("Le username ou le password est/sont incorrect(s)")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être rempli')
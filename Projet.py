import streamlit as st
import numpy as np
import matplotlib.pyplot as plt 

# Configuration de la page
st.set_page_config(
    page_title="Résolution de l'équation de Boltzmann",
    page_icon="📘",
    layout="wide"
)

# Titre principal (Page de garde)
st.title("Résolution de l'équation de Boltzmann avec la méthode de Monte Carlo")
st.markdown("---")

# Menu de navigation
menu = ["Accueil", "Contexte de l'équation", "Méthode Monte Carlo", "Études de cas", "Conclusion"]
choix = st.sidebar.radio("Navigation", menu)

# Affichage des pages selon le choix
if choix == "Accueil":
    st.header("Bienvenue")
    st.write(
        "Bienvenue sur notre site dédié à la résolution de l'équation de Boltzmann linéaire avec la méthode de Monte Carlo."
    )
    st.write("Ce projet a été réalisé par :")
    st.write("- **Ikram EL OUARDY**")
    st.write("- **Salma JEMLI**")
    st.write("- **Nawfal MAGHRAOUI**")
    st.write("- **Yassine AYOUN**")
    st.write("Encadré par : **Gael Poette**")
    
    # Centrage de l'image avec des colonnes
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("./CEA1.png", caption="Exemple d'application de la méthode Monte Carlo")

elif choix == "Contexte de l'équation":
    st.header("Contexte de l'équation")
    st.subheader("L'équation de Boltzmann linéaire")
    st.latex(r"""
    \partial_t u(x, t, v) + v \cdot \nabla u(x, t, v) = -\sigma_t(x, v) u(x, t, v) + \int \sigma_s(x, v, v') u(x, t, v') dv'
    """)
    st.write(
        "Cette équation décrit l'évolution de la densité de particules $u(x, t, v)$ sous l'influence de différents phénomènes tels que la collision et le transport."
    )

elif choix == "Méthode Monte Carlo":
    st.header("Méthode Monte Carlo")
    st.subheader("Introduction")
    st.write(
        "La méthode Monte Carlo est une approche stochastique permettant de résoudre des problèmes complexes, notamment les équations intégrales, en simulant des processus aléatoires."
    )
    
    # Centrer l'image avec des colonnes
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://via.placeholder.com/800x400", caption="Illustration de la méthode Monte Carlo pour estimer π", use_container_width=True)
    
    # Exemple interactif pour estimer π
    st.subheader("Estimation de π")
    points = st.slider("Nombre de points à générer", min_value=100, max_value=10000, step=1000, value=1000)
    
    x = np.random.rand(points)
    y = np.random.rand(points)
    inside = x**2 + y**2 <= 1
    
    fig, ax = plt.subplots(figsize=(5, 5))  # Taille réduite de la figure
    ax.scatter(x[inside], y[inside], color="blue", label="Inside")
    ax.scatter(x[~inside], y[~inside], color="red", label="Outside")
    ax.set_aspect('equal')
    ax.legend()
    
    # Centrer le graphique avec des colonnes
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.pyplot(fig, use_container_width=True)
    
    pi_estimation = 4 * np.sum(inside) / points
    st.write(f"Valeur estimée de π : {pi_estimation:.4f}")

elif choix == "Études de cas":
    st.header("Études de cas")
    st.subheader("Advection")
    st.write("Description de l'advection avec résultats numériques.")
    st.subheader("Absorption et transport")
    st.write("Description de l'absorption et du transport avec visualisations.")
    st.subheader("Limite de diffusion")
    st.write("Présentation des résultats obtenus en utilisant la méthode Monte Carlo pour la diffusion.")

elif choix == "Conclusion":
    st.header("Conclusion")
    st.write(
        "La méthode Monte Carlo a prouvé son efficacité dans la résolution de l'équation de Boltzmann linéaire. Elle permet de traiter des problèmes à haute dimension avec flexibilité."
    )
    st.write(
        "**Perspectives** : Étendre cette méthode à des simulations 3D et explorer des scénarios plus complexes."
    )

# Footer
st.markdown("---")
st.write("Projet académique - Janvier 2025")

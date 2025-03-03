## 🦠 SIR Model: Understanding Epidemic Spread  
The **Susceptible-Infected-Recovered (SIR) model** is a fundamental epidemiological model used to describe the spread of infectious diseases. It divides a population into three compartments:  

- **S (Susceptible)**: Individuals who can be infected.  
- **I (Infected)**: Individuals currently infected and capable of spreading the disease.  
- **R (Recovered)**: Individuals who have recovered and gained immunity.  

# 👋 Hi, I’m Gaurav Lute  

🔬 **M.Tech in Modeling and Simulation** | 🎓 **Savitribai Phule Pune University**  
📊 **Passionate about Data Science, Machine Learning, and Optimization**  

## 🚀 About Me  
- 👀 I’m interested in **mathematical modeling, AI/ML, and simulation-based problem solving**  
- 🌱 I’m currently learning **CNNs and deep learning techniques**  
- 💡 I enjoy working on **real-world applications of AI and data-driven decision-making**  
- 💞️ I’m looking to collaborate on **data science projects, research work, and innovative simulations**  
- 📫 How to reach me: **[Your Email / LinkedIn / GitHub Profile Link]**  
- 😄 Pronouns: **He/Him**  
- ⚡ Fun fact: **I love exploring optimization algorithms and their practical applications!**  

---

## 🦠 SIR Model: Understanding Epidemic Spread  
The **Susceptible-Infected-Recovered (SIR) model** is a fundamental epidemiological model used to describe the spread of infectious diseases. It divides a population into three compartments:  

- **S (Susceptible)**: Individuals who can be infected.  
- **I (Infected)**: Individuals currently infected and capable of spreading the disease.  
- **R (Recovered)**: Individuals who have recovered and gained immunity.  

### 📈 Mathematical Representation  
The model is governed by the following differential equations:  

\[
\frac{dS}{dt} = - \beta S I
\]  
\[
\frac{dI}{dt} = \beta S I - \gamma I
\]  
\[
\frac{dR}{dt} = \gamma I
\]  

where:  
- \( \beta \) is the transmission rate (probability of infection per contact).  
- \( \gamma \) is the recovery rate (rate at which infected individuals recover).  
- The basic reproduction number, \( R_0 \), is given by \( R_0 = \frac{\beta}{\gamma} \), determining whether an outbreak will spread.  

### 🔍 Key Insights  
- If \( R_0 > 1 \), the disease spreads; if \( R_0 < 1 \), the outbreak dies out.  
- Peak infection occurs when \( S \) reaches a critical threshold.  
- Vaccination and quarantine strategies aim to reduce \( R_0 \) and control outbreaks.  

### 🛠 Applications  
- **COVID-19 modeling** and forecasting.  
- **Policy-making** for epidemic control.  
- **Public health interventions** like social distancing and vaccination.  

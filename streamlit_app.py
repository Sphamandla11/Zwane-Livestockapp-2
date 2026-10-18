import streamlit as st
import pandas as pd

st.set_page_config(page_title="Family Livestock Management App", page_icon="🐄", layout="wide")

st.title("🐄 Family Livestock Register & Health App")
st.write("Manage your **15 Cattle** and **11 Goats**, track vaccination dates, and lookup illness codes directly on your phone.")

# Navigation Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔍 Health Code Lookup", 
    "🐄 Cattle Register (15)", 
    "🐐 Goat Register (11)", 
    "💉 Vaccine & Health Log", 
    "📘 Seasonal Guide"
])

# ----------------------------------------------------
# TAB 1: HEALTH CODE LOOKUP SYSTEM
# ----------------------------------------------------
with tab1:
    st.header("🔍 Quick Health Code Lookup")
    st.write("Enter a code from a sick animal's ear tag to immediately view symptoms, primary treatments, and alternative farm medicines.")

    HEALTH_CODES = {
        "H-0": {
            "name": "Healthy / Normal",
            "symptoms": "Bright eyes, eating well, clear nostrils, active.",
            "primary": "None required (Maintain routine tick dipping & seasonal deworming).",
            "alternatives": "Multimin boost or Kyrovite if preparing for winter.",
            "urgency": "Normal"
        },
        "S-1": {
            "name": "Sponsiekte (Blackquarter)",
            "symptoms": "Lame leg, swollen thigh/shoulder, crackling gas sound under skin, high fever.",
            "primary": "Mexitet-LA or Tremycin / Penicillin injection (Inject immediately!).",
            "alternatives": "Maxitet-LA + Covexin 10 vaccine for remaining healthy herd.",
            "urgency": "CRITICAL / URGENT"
        },
        "L-2": {
            "name": "Lumpy Skin Disease",
            "symptoms": "Hard lumps/nodules on skin, discharge from eyes/nose, fever, refusal to eat.",
            "primary": "Mexitet-LA or Tremycin (To prevent secondary skin bacterial infections).",
            "alternatives": "Spray with Triatix dip / fly repellent + apply wound spray on burst lumps.",
            "urgency": "HIGH"
        },
        "W-3": {
            "name": "Heavy Worms / Anemia",
            "symptoms": "Pale white inner eyes, bottle jaw (swollen under chin), weakness, diarrhea.",
            "primary": "Endo+lint (Oral drench).",
            "alternatives": "Valbazen, ProDrench, or Ivormax injection + Multimin boost.",
            "urgency": "MEDIUM"
        },
        "P-4": {
            "name": "Pulpy Kidney (Bloednier)",
            "symptoms": "Sudden illness/death in goats, nervous twitching, head pulled back.",
            "primary": "Multivax P vaccine (Preventative).",
            "alternatives": "Emergency broad-spectrum antibiotic (Tremycin) if caught very early.",
            "urgency": "CRITICAL / URGENT"
        },
        "F-5": {
            "name": "Foot Rot / Lame",
            "symptoms": "Swollen hoof, bad smell between claws, limping, grazing on knees.",
            "primary": "Clean hoof + Purple Wound Spray + Mexitet-LA injection.",
            "alternatives": "Tremycin injection + 10% Zinc Sulphate footbath.",
            "urgency": "MEDIUM"
        },
        "E-6": {
            "name": "Eye Infection (Pink Eye)",
            "symptoms": "Watery eye, cloudy white spot on cornea, keeping eye closed.",
            "primary": "Oxytetracycline eye powder or ointment.",
            "alternatives": "Mexitet-LA injection if severe + keep animal in shade.",
            "urgency": "LOW / MEDIUM"
        },
        "R-7": {
            "name": "Redwater / Heartwater",
            "symptoms": "Dark red urine, nervous high-stepping walk, high fever, heavy tick infestation.",
            "primary": "Berenil / Imizol (Redwater) or Terramycin (Heartwater).",
            "alternatives": "Mexitet-LA + immediate tick dip with Triatix.",
            "urgency": "CRITICAL / URGENT"
        },
        "T-8": {
            "name": "Tick Heavy Attack",
            "symptoms": "Clusters of ticks under tail, around ears, udder, or scrotum.",
            "primary": "Triatix spray dip or Drastic Deadline pour-on.",
            "alternatives": "Tick Grease smeared on affected areas + Ivormax injection.",
            "urgency": "MEDIUM"
        },
        "V-9": {
            "name": "Vitamin / Condition Weakness",
            "symptoms": "Thin ribs visible, dull coat, struggling in dry winter.",
            "primary": "Multimin trace mineral injection.",
            "alternatives": "Kyrovite B-Co injection + winter lick supplement.",
            "urgency": "LOW"
        }
    }

    selected_code = st.selectbox("Select Health Code or Type Below:", list(HEALTH_CODES.keys()))
    code_info = HEALTH_CODES[selected_code]
    
    st.subheader(f"Code {selected_code}: {code_info['name']}")
    if "CRITICAL" in code_info['urgency']:
        st.error(f"Urgency: {code_info['urgency']}")
    elif code_info['urgency'] in ["HIGH", "MEDIUM"]:
        st.warning(f"Urgency: {code_info['urgency']}")
    else:
        st.success(f"Urgency: {code_info['urgency']}")

    st.markdown(f"**Symptoms:** {code_info['symptoms']}")
    st.markdown(f"**Primary Treatment:** {code_info['primary']}")
    st.markdown(f"**Alternative Medications:** {code_info['alternatives']}")


# ----------------------------------------------------
# TAB 2: CATTLE REGISTER
# ----------------------------------------------------
with tab2:
    st.header("🐄 Cattle Register")
    st.write("Track birth dates, ages, purpose, and target sale dates. Add new cattle using the '+' button.")

    cattle_data = [
        {"Tag ID": "C-01", "Sex": "Female", "Birth Year/Date": "2021", "Est. Age": "5 Yrs", "Breed": "Bonsmara Cross", "Purpose": "Breeding Cow", "Target Sale": "Keep", "Health Notes": "Healthy - Calved twice"},
        {"Tag ID": "C-02", "Sex": "Male", "Birth Year/Date": "2025-11", "Est. Age": "9 Mos", "Breed": "Nguni Cross", "Purpose": "Bull Calf", "Target Sale": "Nov 2027 (Age 2)", "Health Notes": "Good growth"},
    ]
    for i in range(3, 21):
        cattle_data.append({"Tag ID": f"C-{i:02d}", "Sex": "", "Birth Year/Date": "", "Est. Age": "", "Breed": "", "Purpose": "", "Target Sale": "", "Health Notes": ""})

    df_cattle = pd.DataFrame(cattle_data)
    edited_cattle = st.data_editor(df_cattle, num_rows="dynamic", use_container_width=True, key="cattle_editor")

    # Download Button for Cattle Backup
    csv_cattle = edited_cattle.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Cattle Register Backup (CSV)",
        data=csv_cattle,
        file_name="cattle_register_backup.csv",
        mime="text/csv",
    )

# ----------------------------------------------------
# TAB 3: GOAT REGISTER
# ----------------------------------------------------
with tab3:
    st.header("🐐 Goat Register")
    st.write("Track birth dates, wethers for market sale, and stud bucks. Add new goats using the '+' button.")

    goat_data = [
        {"Tag ID": "G-01", "Sex": "Male (Stud)", "Birth Year/Date": "2023-05", "Est. Age": "3 Yrs", "Breed": "Boerbok", "Purpose": "Breeding Buck", "Target Sale": "Keep", "Health Notes": "Main stud buck"},
        {"Tag ID": "G-02", "Sex": "Male (Castrated)", "Birth Year/Date": "2025-09", "Est. Age": "11 Mos", "Breed": "Boerbok Cross", "Purpose": "Wether", "Target Sale": "Dec 2026 (Festive)", "Health Notes": "Fattening for market"},
    ]
    for i in range(3, 16):
        goat_data.append({"Tag ID": f"G-{i:02d}", "Sex": "", "Birth Year/Date": "", "Est. Age": "", "Breed": "", "Purpose": "", "Target Sale": "", "Health Notes": ""})

    df_goats = pd.DataFrame(goat_data)
    edited_goats = st.data_editor(df_goats, num_rows="dynamic", use_container_width=True, key="goat_editor")

    # Download Button for Goat Backup
    csv_goats = edited_goats.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Goat Register Backup (CSV)",
        data=csv_goats,
        file_name="goat_register_backup.csv",
        mime="text/csv",
    )

# ----------------------------------------------------
# TAB 4: VACCINE & HEALTH LOG
# ----------------------------------------------------
with tab4:
    st.header("💉 Vaccine & Health Treatment Log")
    st.write("Record treatments given to animals (e.g., Endo+lint, Mexitet, Ivormax, Multimin). Add new treatments using the '+' button.")

    health_log = [
        {"Date": "2026-03-15", "Animal / Group": "All Goats (G-01 to G-11)", "Treatment": "Deworming", "Product Used": "Endo+lint / Valbazen", "Dose": "5 ml Oral", "Next Due Date": "2026-06-15"},
        {"Date": "2026-04-05", "Animal / Group": "Young Calves", "Treatment": "Vaccination", "Product Used": "Covexin 10 (Sponsiekte)", "Dose": "2 ml Subcut", "Next Due Date": "2027-04-05"},
        {"Date": "2026-08-01", "Animal / Group": "All Cattle (C-01 to C-15)", "Treatment": "Tick Dip", "Product Used": "Triatix Spray", "Dose": "Spray Dip", "Next Due Date": "2026-08-15"}
    ]
    df_health = pd.DataFrame(health_log)
    edited_health = st.data_editor(df_health, num_rows="dynamic", use_container_width=True, key="health_editor")

    # Download Button for Vaccine Log Backup
    csv_health = edited_health.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Vaccine Log Backup (CSV)",
        data=csv_health,
        file_name="vaccine_health_log_backup.csv",
        mime="text/csv",
    )

# ----------------------------------------------------
# TAB 5: SEASONAL HEALTH GUIDE
# ----------------------------------------------------
with tab5:
    st.header("📘 Seasonal Health Guide")
    st.markdown('''
    * **Spring (Sept – Nov):** **Vaccine Season!** Give Cattle annual Sponsiekte (Covexin/Supavax) & Lumpy Skin vaccines. Give Goats their Pulpy Kidney booster (Multivax P).
    * **Summer (Dec – Feb):** **Deworming & Tick Season!** Rains bring wireworm & ticks. Dip/spray with Triatix. Drench with Endo+lint or Valbazen.
    * **Autumn (March – May):** **Pre-Winter Prep!** Inject Multimin / Kyrovite vitamins as grass turns brown. Give goats 2nd Pulpy Kidney dose.
    * **Winter (June – Aug):** **Condition Maintenance!** Give Ivormax injection for winter external mites/lice. Keep winter licks out.
    ''')
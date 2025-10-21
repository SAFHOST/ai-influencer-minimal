import streamlit as st
import json
import time
import random
from datetime import datetime, timedelta
import os

st.set_page_config(
    page_title="AI Influencer Empire",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF4B4B;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

class InfluencerManager:
    def _init_(self):
        self.influencers = self.load_data()
    
    def load_data(self):
        try:
            if os.path.exists('data.json'):
                with open('data.json', 'r') as f:
                    return json.load(f)
        except:
            return []
    
    def save_data(self):
        with open('data.json', 'w') as f:
            json.dump(self.influencers, f, indent=2)
    
    def create_influencer(self, name, niche, personality):
        influencer = {
            "id": len(self.influencers) + 1,
            "name": name,
            "niche": niche,
            "personality": personality,
            "created_date": datetime.now().isoformat(),
            "followers": random.randint(10000, 50000),
            "engagement": round(random.uniform(3.5, 8.2), 1),
            "monthly_earnings": random.randint(2000, 8000)
        }
        
        self.influencers.append(influencer)
        self.save_data()
        return influencer

def main():
    st.markdown('<div class="main-header">AI INFLUENCER EMPIRE</div>', unsafe_allow_html=True)
    
    manager = InfluencerManager()
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Create Influencer", "Revenue"])
    
    if page == "Dashboard":
        show_dashboard(manager)
    elif page == "Create Influencer":
        create_influencer(manager)
    elif page == "Revenue":
        show_revenue(manager)

def show_dashboard(manager):
    st.header("Dashboard")
    
    if not manager.influencers:
        st.info("Create your first AI influencer to get started!")
        return
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Influencers", len(manager.influencers))
    with col2:
        total_followers = sum(inf["followers"] for inf in manager.influencers)
        st.metric("Total Followers", f"{total_followers:,}")
    with col3:
        total_revenue = sum(inf["monthly_earnings"] for inf in manager.influencers)
        st.metric("Monthly Revenue", f"${total_revenue:,}")
    
    for inf in manager.influencers:
        with st.container():
            st.markdown(f"""
            <div class="card">
                <h3>{inf['name']}</h3>
                <p>Niche: {inf['niche'].title()} | Followers: {inf['followers']:,}</p>
                <p>Engagement: {inf['engagement']}% | Monthly: ${inf['monthly_earnings']:,}</p>
            </div>
            """, unsafe_allow_html=True)

def create_influencer(manager):
    st.header("Create AI Influencer")
    
    with st.form("influencer_form"):
        name = st.text_input("Influencer Name", "Digital Creator")
        niche = st.selectbox("Niche", ["fashion", "tech", "fitness", "lifestyle", "business"])
        personality = st.selectbox("Personality", ["sophisticated", "energetic", "authentic", "luxury"])
        
        if st.form_submit_button("Create Influencer"):
            with st.spinner("Creating influencer..."):
                time.sleep(1)
                influencer = manager.create_influencer(name, niche, personality)
                st.success(f"{name} created successfully!")
                st.balloons()

def show_revenue(manager):
    st.header("Revenue Projections")
    
    if manager.influencers:
        total_revenue = sum(inf["monthly_earnings"] for inf in manager.influencers)
        st.metric("Total Monthly Revenue", f"${total_revenue:,}")
        st.metric("Projected Yearly", f"${total_revenue * 12:,}")
        
        st.write("### Revenue Breakdown")
        for inf in manager.influencers:
            st.write(f"{inf['name']}: ${inf['monthly_earnings']:,}/month")
    else:
        st.info("Create influencers to see revenue projections!")

if _name_ == "_main_":
    main()

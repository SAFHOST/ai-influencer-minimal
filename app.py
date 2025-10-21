import streamlit as st
import json
import time
import random
from datetime import datetime, timedelta
import os

# Page configuration
st.set_page_config(
    page_title="AI Influencer Empire",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS
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
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

class InfluencerManager:
    def __init__(self):
        self.influencers = self.load_data()

    def load_data(self):
        try:
            if os.path.exists('data.json'):
                with open('data.json', 'r') as f:
                    return json.load(f)
        except:
            return []

    def save_data(self):
        try:
            with open('data.json', 'w') as f:
                json.dump(self.influencers, f, indent=2)
            return True
        except Exception as e:
            st.error(f"Save error: {e}")
            return False

    def create_influencer(self, name, niche, personality, target_audience):
        try:
            # Ensure target_audience is a list
            if target_audience is None:
                target_audience = ["Millennials"]
            elif isinstance(target_audience, str):
                target_audience = [target_audience]

            influencer = {
                "id": len(self.influencers) + 1,
                "name": name,
                "niche": niche,
                "personality": personality,
                "target_audience": target_audience,
                "created_date": datetime.now().isoformat(),
                "followers": random.randint(10000, 50000),
                "engagement": round(random.uniform(3.5, 8.2), 1),
                "monthly_earnings": random.randint(2000, 8000),
                "content_types": self.get_content_types(niche),
                "target_brands": self.get_target_brands(niche)
            }

            self.influencers.append(influencer)
            if self.save_data():
                return influencer
            else:
                return None
        except Exception as e:
            st.error(f"Creation error: {e}")
            return None

    def get_content_types(self, niche):
        content_map = {
            "fashion": ["OOTD", "Style Guides", "Brand Reviews", "Trend Reports"],
            "tech": ["Product Reviews", "Tutorials", "Tech News", "Unboxing"],
            "fitness": ["Workouts", "Nutrition Tips", "Progress Updates", "Motivation"],
            "lifestyle": ["Daily Routines", "Product Reviews", "Travel", "Home Decor"],
            "business": ["Entrepreneurship Tips", "Case Studies", "Tool Reviews", "Strategies"]
        }
        return content_map.get(niche, content_map["lifestyle"])

    def get_target_brands(self, niche):
        brand_map = {
            "fashion": ["Nike", "Zara", "H&M", "Fashion Nova"],
            "tech": ["Apple", "Samsung", "Google", "Microsoft"],
            "fitness": ["Nike", "Gymshark", "MyProtein", "Peloton"],
            "lifestyle": ["Amazon", "Target", "IKEA", "Airbnb"],
            "business": ["Shopify", "HubSpot", "Salesforce", "Zoom"]
        }
        return brand_map.get(niche, brand_map["lifestyle"])

def main():
    st.markdown('<div class="main-header">🚀 AI INFLUENCER EMPIRE</div>', unsafe_allow_html=True)

    manager = InfluencerManager()

    # Sidebar navigation
    st.sidebar.title("🎯 Navigation")
    page = st.sidebar.radio("Go to", [
        "🏠 Dashboard",
        "👑 Create Influencer",
        "💰 Revenue",
        "🚀 Quick Start"
    ])

    if page == "🏠 Dashboard":
        show_dashboard(manager)
    elif page == "👑 Create Influencer":
        create_influencer_page(manager)
    elif page == "💰 Revenue":
        show_revenue_page(manager)
    elif page == "🚀 Quick Start":
        show_quick_start()

def show_dashboard(manager):
    st.header("📊 Dashboard Overview")

    if not manager.influencers:
        st.info("🎯 Create your first AI influencer to start your empire!")
        return

    # Metrics
    col1, col2, col3, col4 = st.columns(4)

    total_followers = sum(inf["followers"] for inf in manager.influencers)
    total_engagement = sum(inf["engagement"] for inf in manager.influencers) / len(manager.influencers)
    total_revenue = sum(inf["monthly_earnings"] for inf in manager.influencers)

    with col1:
        st.metric("Total Influencers", len(manager.influencers))
    with col2:
        st.metric("Total Followers", f"{total_followers:,}")
    with col3:
        st.metric("Avg Engagement", f"{total_engagement:.1f}%")
    with col4:
        st.metric("Monthly Revenue", f"${total_revenue:,}")

    # Influencer cards
    st.subheader("👑 Your AI Influencers")
    for influencer in manager.influencers:
        with st.container():
            st.markdown(f"""
            <div class="card">
                <h3>👑 {influencer['name']}</h3>
                <p><strong>Niche:</strong> {influencer['niche'].title()} |
                <strong>Personality:</strong> {influencer['personality'].title()}</p>
                <p><strong>Followers:</strong> {influencer['followers']:,} |
                <strong>Engagement:</strong> {influencer['engagement']}%</p>
                <p><strong>Monthly Earnings:</strong> ${influencer['monthly_earnings']:,}</p>
            </div>
            """, unsafe_allow_html=True)

def create_influencer_page(manager):
    st.header("👑 Create AI Influencer")

    with st.form("influencer_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Influencer Name", "Digital Creator Pro")
            niche = st.selectbox("Niche", ["fashion", "tech", "fitness", "lifestyle", "business"])

        with col2:
            personality = st.selectbox("Personality", ["sophisticated", "energetic", "authentic", "luxury", "relatable"])
            target_audience = st.multiselect("Target Audience", ["Gen Z", "Millennials", "Professionals", "Students"], default=["Millennials"])

        submitted = st.form_submit_button("🚀 Create AI Influencer", type="primary")

        if submitted:
            if not name:
                st.error("❌ Please enter an influencer name!")
            elif not target_audience:
                st.error("❌ Please select at least one target audience!")
            else:
                with st.spinner("Creating your AI influencer..."):
                    time.sleep(2)
                    # FIXED: Pass all required parameters including target_audience
                    influencer = manager.create_influencer(
                        name=name,
                        niche=niche,
                        personality=personality,
                        target_audience=target_audience
                    )

                    if influencer:
                        st.success(f"✅ {name} created successfully!")

                        st.markdown(f"""
                        <div class="success-box">
                            <h3>🎉 Ready to Monetize!</h3>
                            <p><strong>{name}</strong> is now active in the {niche} niche with {influencer['followers']:,} followers.</p>
                            <p><strong>Content Types:</strong> {', '.join(influencer['content_types'])}</p>
                            <p><strong>Target Brands:</strong> {', '.join(influencer['target_brands'])}</p>
                            <p><strong>Monthly Revenue Potential:</strong> ${influencer['monthly_earnings']:,}</p>
                        </div>
                        """, unsafe_allow_html=True)

                        st.balloons()
                    else:
                        st.error("❌ Failed to create influencer. Please try again.")

def show_revenue_page(manager):
    st.header("💰 Revenue Projections")

    if not manager.influencers:
        st.info("Create influencers to see revenue projections!")
        return

    total_monthly = 0
    total_yearly = 0

    for influencer in manager.influencers:
        st.subheader(f"💎 {influencer['name']}")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Monthly Revenue", f"${influencer['monthly_earnings']:,}")
        with col2:
            st.metric("Quarterly", f"${influencer['monthly_earnings'] * 3:,}")
        with col3:
            st.metric("Yearly", f"${influencer['monthly_earnings'] * 12:,}")

        total_monthly += influencer['monthly_earnings']
        total_yearly += influencer['monthly_earnings'] * 12

    # Total projections
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📊 Total Monthly", f"${total_monthly:,}")
    with col2:
        st.metric("🎯 Total Yearly", f"${total_yearly:,}")

def show_quick_start():
    st.header("🚀 Quick Start Guide")

    st.markdown("""
    ## Your First 7 Days to Revenue

    ### Day 1: Foundation
    1. **Create 3 AI Influencers** in different niches
    2. **Note their target brands** for outreach
    3. **Set up social media profiles**

    ### Day 2-3: Brand Outreach 
    1. **Contact 5-10 brands** from your target lists
    2. **Use personalized pitches**
    3. **Aim for $1,000-5,000 per deal**

    ### Day 4-7: Execution
    1. **Post daily content** consistently
    2. **Engage with your audience**
    3. **Follow up with brands**
    4. **Scale to more influencers**

    ## 💰 Expected Revenue
    - **Week 1:** $3,000-8,000
    - **Month 1:** $15,000-35,000
    - **Month 3:** $50,000-100,000

    ## 🎯 Pro Tips
    - Focus on 2-3 niches you understand
    - Quality content beats quantity
    - Build authentic engagement
    - Track everything in your dashboard
    """)

if __name__ == "__main__":
    main()

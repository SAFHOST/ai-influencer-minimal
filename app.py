import streamlit as st
import pandas as pd
import json
import time
import random
from datetime import datetime, timedelta
import os

# Page configuration
st.set_page_config(
    page_title="AI Influencer Empire",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
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
    .influencer-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        border-left: 5px solid #FF4B4B;
    }
    .revenue-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem;
    }
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        border-left: 5px solid #28a745;
    }
    .platform-tag {
        background: #FF4B4B;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        margin: 0.2rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

class AIInfluencerManager:
    def _init_(self):
        self.influencers = []
        self.load_data()
    
    def load_data(self):
        try:
            if os.path.exists('influencers.json'):
                with open('influencers.json', 'r') as f:
                    self.influencers = json.load(f)
        except:
            self.influencers = []
    
    def save_data(self):
        with open('influencers.json', 'w') as f:
            json.dump(self.influencers, f, indent=2)
    
    def create_influencer(self, name, niche, personality, target_audience, style):
        influencer = {
            "id": f"inf_{int(datetime.now().timestamp())}",
            "name": name,
            "niche": niche,
            "personality": personality,
            "target_audience": target_audience,
            "style": style,
            "created_date": datetime.now().isoformat(),
            "stats": {
                "followers": random.randint(15000, 75000),
                "engagement_rate": round(random.uniform(4.5, 9.2), 1),
                "monthly_earnings": 0,
                "total_earnings": 0
            },
            "content_strategy": self.generate_content_strategy(niche),
            "brand_deals": self.generate_brand_deals(niche),
            "social_platforms": ["Instagram", "TikTok", "YouTube", "Twitter"]
        }
        
        self.influencers.append(influencer)
        self.save_data()
        return influencer
    
    def generate_content_strategy(self, niche):
        strategies = {
            "fashion": ["OOTD Posts", "Style Guides", "Brand Hauls", "Trend Reports", "Fashion Tips"],
            "tech": ["Product Reviews", "Tech Tutorials", "Gadget Unboxing", "Industry News", "App Recommendations"],
            "fitness": ["Workout Routines", "Nutrition Tips", "Progress Updates", "Motivational Content", "Q&A Sessions"],
            "business": ["Entrepreneurship Tips", "Case Studies", "Tool Reviews", "Industry Insights", "Success Stories"],
            "lifestyle": ["Daily Routines", "Product Reviews", "Travel Content", "Home Decor", "Personal Stories"]
        }
        return strategies.get(niche, strategies["lifestyle"])
    
    def generate_brand_deals(self, niche):
        brand_templates = {
            "fashion": [
                {"brand": "Nike", "potential": 5000, "status": "Available"},
                {"brand": "Zara", "potential": 3000, "status": "Available"},
                {"brand": "Fashion Nova", "potential": 4000, "status": "Available"}
            ],
            "tech": [
                {"brand": "Apple", "potential": 8000, "status": "Available"},
                {"brand": "Samsung", "potential": 6000, "status": "Available"},
                {"brand": "Google", "potential": 7000, "status": "Available"}
            ],
            "fitness": [
                {"brand": "Gymshark", "potential": 4500, "status": "Available"},
                {"brand": "MyProtein", "potential": 3500, "status": "Available"},
                {"brand": "Peloton", "potential": 6000, "status": "Available"}
            ],
            "business": [
                {"brand": "Shopify", "potential": 5500, "status": "Available"},
                {"brand": "HubSpot", "potential": 5000, "status": "Available"},
                {"brand": "Salesforce", "potential": 7000, "status": "Available"}
            ]
        }
        return brand_templates.get(niche, brand_templates["lifestyle"])

class ContentEngine:
    def generate_content_calendar(self, influencer, days=7):
        calendar = []
        
        for day in range(days):
            date = datetime.now() + timedelta(days=day)
            daily_posts = []
            
            for post_num in range(random.randint(2, 3)):
                post = {
                    "date": date.strftime("%Y-%m-%d"),
                    "time": self.get_post_time(post_num),
                    "platform": random.choice(influencer["social_platforms"]),
                    "content_type": random.choice(influencer["content_strategy"]),
                    "caption": self.generate_caption(influencer),
                    "hashtags": self.generate_hashtags(influencer),
                    "estimated_engagement": f"{random.randint(85, 98)}%"
                }
                daily_posts.append(post)
            
            calendar.append({
                "date": date.strftime("%Y-%m-%d"),
                "posts": daily_posts
            })
        
        return calendar
    
    def get_post_time(self, post_num):
        times = ["09:00 AM", "12:00 PM", "03:00 PM", "06:00 PM", "08:00 PM"]
        return times[post_num] if post_num < len(times) else "06:00 PM"
    
    def generate_caption(self, influencer):
        templates = [
            f"Leveling up in the {influencer['niche']} space! Who's with me?",
            f"Game-changing {influencer['niche']} insight coming through!",
            f"Living the {influencer['niche']} dream one post at a time!",
            f"This {influencer['niche']} strategy changed everything for me!",
            f"Hot take in the {influencer['niche']} world - what do you think?"
        ]
        return random.choice(templates)
    
    def generate_hashtags(self, influencer):
        base_hashtags = {
            "fashion": ["fashion", "style", "ootd", "fashionista", "trending"],
            "tech": ["tech", "innovation", "gadgets", "technology", "future"],
            "fitness": ["fitness", "workout", "health", "motivation", "gym"],
            "business": ["business", "entrepreneur", "success", "marketing", "leadership"],
            "lifestyle": ["lifestyle", "life", "inspiration", "daily", "vibes"]
        }
        
        niche_tags = base_hashtags.get(influencer["niche"], base_hashtags["lifestyle"])
        viral_tags = ["viral", "trending", "fyp", "explorepage", "instagram"]
        
        all_tags = niche_tags + viral_tags
        random.shuffle(all_tags)
        
        return " ".join([f"#{tag}" for tag in all_tags[:12]])

class RevenueCalculator:
    def calculate_earnings(self, influencer):
        base_earning = random.randint(2500, 10000)
        niche_multiplier = {
            "fashion": 1.2,
            "tech": 1.5,
            "fitness": 1.1,
            "business": 1.4,
            "lifestyle": 1.0
        }
        
        multiplier = niche_multiplier.get(influencer["niche"], 1.0)
        monthly = int(base_earning * multiplier)
        
        return {
            "brand_deals": monthly,
            "affiliate_marketing": int(monthly * 0.3),
            "sponsored_content": int(monthly * 0.4),
            "digital_products": int(monthly * 0.2),
            "total_monthly": monthly + int(monthly * 0.9),
            "total_quarterly": (monthly + int(monthly * 0.9)) * 3,
            "total_yearly": (monthly + int(monthly * 0.9)) * 12
        }

def main():
    st.markdown('<div class="main-header">AI INFLUENCER EMPIRE</div>', unsafe_allow_html=True)
    
    manager = AIInfluencerManager()
    content_engine = ContentEngine()
    revenue_calc = RevenueCalculator()
    
    st.sidebar.title("NAVIGATION")
    page = st.sidebar.radio("Go to", [
        "Dashboard", 
        "Create Influencer", 
        "Content Calendar", 
        "Brand Deals",
        "Revenue Projections",
        "Quick Start"
    ])
    
    if page == "Dashboard":
        show_dashboard(manager, revenue_calc)
    elif page == "Create Influencer":
        create_influencer_page(manager)
    elif page == "Content Calendar":
        content_calendar_page(manager, content_engine)
    elif page == "Brand Deals":
        brand_deals_page(manager)
    elif page == "Revenue Projections":
        revenue_page(manager, revenue_calc)
    elif page == "Quick Start":
        quick_start_guide()

def show_dashboard(manager, revenue_calc):
    st.header("DASHBOARD OVERVIEW")
    
    if not manager.influencers:
        st.info("Create your first AI influencer to start your empire!")
        return
    
    col1, col2, col3, col4 = st.columns(4)
    
    total_followers = sum(inf["stats"]["followers"] for inf in manager.influencers)
    total_engagement = sum(inf["stats"]["engagement_rate"] for inf in manager.influencers) / len(manager.influencers)
    total_monthly_revenue = sum(revenue_calc.calculate_earnings(inf)["total_monthly"] for inf in manager.influencers)
    
    with col1:
        st.metric("Total Influencers", len(manager.influencers))
    with col2:
        st.metric("Total Followers", f"{total_followers:,}")
    with col3:
        st.metric("Avg Engagement", f"{total_engagement:.1f}%")
    with col4:
        st.metric("Monthly Revenue", f"${total_monthly_revenue:,}")
    
    st.subheader("YOUR AI INFLUENCERS")
    for influencer in manager.influencers:
        with st.container():
            st.markdown(f"""
            <div class="influencer-card">
                <h2>{influencer['name']}</h2>
                <p><strong>Niche:</strong> {influencer['niche'].title()} 
                <strong>Personality:</strong> {influencer['personality'].title()} 
                <strong>Style:</strong> {influencer['style'].title()}</p>
                <p><strong>Followers:</strong> {influencer['stats']['followers']:,} 
                <strong>Engagement:</strong> {influencer['stats']['engagement_rate']}%</p>
            </div>
            """, unsafe_allow_html=True)
            
            earnings = revenue_calc.calculate_earnings(influencer)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Monthly Revenue", f"${earnings['total_monthly']:,}")
            with col2:
                st.metric("Brand Deals", f"${earnings['brand_deals']:,}")
            with col3:
                st.metric("Yearly Potential", f"${earnings['total_yearly']:,}")

def create_influencer_page(manager):
    st.header("CREATE AI INFLUENCER")
    
    with st.form("influencer_creation_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Influencer Name", "Digital Visionary")
            niche = st.selectbox("Primary Niche", 
                ["fashion", "tech", "fitness", "business", "lifestyle"])
            personality = st.selectbox("Personality Type", 
                ["sophisticated", "energetic", "authentic", "luxury", "relatable"])
        
        with col2:
            target_audience = st.multiselect("Target Audience",
                ["Gen Z (18-24)", "Millennials (25-40)", "Professionals", "Students", "Entrepreneurs"])
            content_style = st.selectbox("Content Style",
                ["minimal", "bold", "vibrant", "elegant", "urban"])
        
        submitted = st.form_submit_button("CREATE AI INFLUENCER")
        
        if submitted:
            if not name or not target_audience:
                st.error("Please fill in all required fields!")
            else:
                with st.spinner("Creating your AI influencer..."):
                    time.sleep(2)
                    influencer = manager.create_influencer(
                        name=name,
                        niche=niche,
                        personality=personality,
                        target_audience=target_audience,
                        style=content_style
                    )
                    
                    st.success(f"{name} successfully created!")
                    
                    st.markdown(f"""
                    <div class="success-box">
                        <h3>Ready to Monetize!</h3>
                        <p><strong>{name}</strong> is now active in the {niche} niche with {influencer['stats']['followers']:,} followers.</p>
                    </div>
                    """, unsafe_allow_html=True)

def content_calendar_page(manager, content_engine):
    st.header("CONTENT CALENDAR")
    
    if not manager.influencers:
        st.info("Create an influencer first to generate content!")
        return
    
    selected_influencer = st.selectbox("Select Influencer", 
        [f"{inf['name']} ({inf['niche']})" for inf in manager.influencers])
    
    influencer_name = selected_influencer.split(" (")[0]
    influencer = next(inf for inf in manager.influencers if inf["name"] == influencer_name)
    
    if st.button("GENERATE 7-DAY CONTENT CALENDAR"):
        with st.spinner("Creating optimized content calendar..."):
            time.sleep(1)
            calendar = content_engine.generate_content_calendar(influencer, days=7)
            
            for day in calendar:
                with st.expander(f"{day['date']} - {len(day['posts'])} Posts"):
                    for i, post in enumerate(day["posts"], 1):
                        st.write(f"Post {i} - {post['time']}")
                        st.write(f"Platform: {post['platform']}")
                        st.write(f"Content Type: {post['content_type']}")
                        st.write(f"Caption: {post['caption']}")
                        st.write(f"Hashtags: {post['hashtags']}")
                        st.write(f"Estimated Engagement: {post['estimated_engagement']}")
                        st.divider()

def brand_deals_page(manager):
    st.header("BRAND DEAL OPPORTUNITIES")
    
    if not manager.influencers:
        st.info("Create influencers to see brand deal opportunities!")
        return
    
    for influencer in manager.influencers:
        st.subheader(f"Opportunities for {influencer['name']}")
        
        for deal in influencer["brand_deals"]:
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            
            with col1:
                st.write(f"{deal['brand']}")
                st.write(f"Perfect fit for {influencer['niche']} niche")
            
            with col2:
                st.metric("Potential Value", f"${deal['potential']:,}")
            
            with col3:
                st.write(f"Status: *{deal['status']}*")
            
            with col4:
                if st.button("Contact", key=f"contact_{deal['brand']}_{influencer['id']}"):
                    st.success(f"Outreach initiated with {deal['brand']}!")

def revenue_page(manager, revenue_calc):
    st.header("REVENUE PROJECTIONS")
    
    if not manager.influencers:
        st.info("Create influencers to see revenue projections!")
        return
    
    total_monthly = 0
    total_yearly = 0
    
    for influencer in manager.influencers:
        st.subheader(f"{influencer['name']} - {influencer['niche'].title()} Niche")
        
        earnings = revenue_calc.calculate_earnings(influencer)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Brand Deals", f"${earnings['brand_deals']:,}")
        with col2:
            st.metric("Affiliate Marketing", f"${earnings['affiliate_marketing']:,}")
        with col3:
            st.metric("Sponsored Content", f"${earnings['sponsored_content']:,}")
        with col4:
            st.metric("Monthly Total", f"${earnings['total_monthly']:,}")
        
        st.markdown(f"""
        <div class="revenue-card">
            <h3>Projected Yearly Income: ${earnings['total_yearly']:,}</h3>
            <p>Based on current engagement and market rates</p>
        </div>
        """, unsafe_allow_html=True)
        
        total_monthly += earnings['total_monthly']
        total_yearly += earnings['total_yearly']
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Monthly Revenue", f"${total_monthly:,}")
    with col2:
        st.metric("Total Yearly Revenue", f"${total_yearly:,}")

def quick_start_guide():
    st.header("QUICK START GUIDE")
    
    st.markdown("""
    ## Your First 7 Days to Revenue
    
    ### Day 1: Foundation
    1. *Create 3 AI Influencers* in different niches
    2. *Generate content calendars* for each
    3. *Set up social media profiles*
    
    ### Day 2-3: Brand Outreach
    1. *Contact 10 brands* from your deal opportunities
    2. *Follow up* with personalized pitches
    3. *Negotiate your first deals* ($1,000-5,000 each)
    
    ### Day 4-7: Execution & Scaling
    1. *Post daily content* as per calendar
    2. *Engage with your audience*
    3. *Secure 2-3 more brand deals*
    4. *Scale to 5+ influencers*
    
    ## Expected Week 1 Revenue: $3,000-8,000
    ## Expected Month 1 Revenue: $15,000-35,000
    """)

if _name_ == "_main_":
    main()

"""
Revenue Sharing AI Chatbot Platform
A demonstration platform showcasing AI-powered conversations with transparent revenue sharing
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json
import time

# Page configuration
st.set_page_config(
    page_title="AI Revenue Share Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(120deg, #2563eb, #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .user-message {
        background-color: #2563eb;
        color: white;
        margin-left: 20%;
    }
    .assistant-message {
        background-color: #f3f4f6;
        color: #1f2937;
        margin-right: 20%;
    }
    .stButton>button {
        width: 100%;
        border-radius: 0.5rem;
        height: 3rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'total_revenue' not in st.session_state:
    st.session_state.total_revenue = 15420.50
if 'total_interactions' not in st.session_state:
    st.session_state.total_interactions = 102815
if 'active_users' not in st.session_state:
    st.session_state.active_users = 12847

# Revenue sharing configuration
REVENUE_PER_INTERACTION = 0.15
PLATFORM_SHARE = 0.30
CONTRIBUTOR_SHARE = 0.70

# Sidebar navigation
with st.sidebar:
    st.image("https://api.dicebear.com/7.x/bottts/svg?seed=AI", width=100)
    st.markdown("### 🤖 AI Revenue Platform")
    
    page = st.radio(
        "Navigation",
        ["💬 Chat Interface", "📊 Revenue Dashboard", "👥 Contributors", "📈 Analytics", "ℹ️ About"],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Quick stats in sidebar
    st.metric("Total Revenue", f"${st.session_state.total_revenue:,.2f}", "+23.5%")
    st.metric("Active Users", f"{st.session_state.active_users:,}", "+18.2%")
    st.metric("Interactions", f"{st.session_state.total_interactions:,}", "+31.8%")

# Main content area
if page == "💬 Chat Interface":
    st.markdown('<p class="main-header">AI Chat Interface</p>', unsafe_allow_html=True)
    st.markdown("**Experience AI-powered conversations with transparent revenue sharing**")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Chat container
        chat_container = st.container(height=500)
        
        with chat_container:
            if not st.session_state.messages:
                st.info("👋 Welcome! Start a conversation to see how revenue sharing works in real-time.")
            
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    st.markdown(f'<div class="chat-message user-message">👤 You: {msg["content"]}</div>', 
                              unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="chat-message assistant-message">🤖 AI: {msg["content"]}</div>', 
                              unsafe_allow_html=True)
        
        # Input area
        with st.container():
            col_input, col_button = st.columns([5, 1])
            with col_input:
                user_input = st.text_input(
                    "Message",
                    placeholder="Type your message here...",
                    label_visibility="collapsed",
                    key="user_input"
                )
            with col_button:
                send_button = st.button("Send", type="primary", use_container_width=True)
        
        if send_button and user_input:
            # Add user message
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Simulate AI response (replace with real API call)
            with st.spinner("🤖 AI is thinking..."):
                time.sleep(1)
                
                # Sample responses
                responses = [
                    "That's a great question! Let me help you with that.",
                    "I understand your concern. Here's what I can tell you...",
                    "Excellent point! Let's explore this together.",
                    "I'm here to assist you. Based on what you've shared...",
                    "Thank you for asking! Here's my perspective..."
                ]
                
                import random
                ai_response = random.choice(responses) + f" (Demo response to: '{user_input}')"
                
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                
                # Update revenue
                st.session_state.total_revenue += REVENUE_PER_INTERACTION
                st.session_state.total_interactions += 1
            
            st.rerun()
    
    with col2:
        st.markdown("### 💰 Revenue Tracker")
        
        # Revenue per interaction
        st.info(f"""
        **Per Interaction:**
        - Revenue: ${REVENUE_PER_INTERACTION}
        - Platform: ${REVENUE_PER_INTERACTION * PLATFORM_SHARE:.3f}
        - Contributors: ${REVENUE_PER_INTERACTION * CONTRIBUTOR_SHARE:.3f}
        """)
        
        # Session stats
        st.success(f"""
        **This Session:**
        - Messages: {len(st.session_state.messages)}
        - Revenue Generated: ${len(st.session_state.messages) * REVENUE_PER_INTERACTION / 2:.2f}
        """)
        
        # How it works
        with st.expander("ℹ️ How Revenue Sharing Works"):
            st.markdown("""
            **Platform Model:**
            1. Users interact with AI chatbot
            2. Each interaction generates $0.15
            3. Revenue split:
               - 30% → Platform (operations)
               - 70% → Contributors (creators)
            
            **Contributors include:**
            - AI model trainers
            - Knowledge base providers
            - Domain experts
            - Data contributors
            """)

elif page == "📊 Revenue Dashboard":
    st.markdown('<p class="main-header">Revenue Dashboard</p>', unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Revenue",
            f"${st.session_state.total_revenue:,.2f}",
            "+23.5%",
            help="Total revenue generated from all interactions"
        )
    
    with col2:
        platform_revenue = st.session_state.total_revenue * PLATFORM_SHARE
        st.metric(
            "Platform Share (30%)",
            f"${platform_revenue:,.2f}",
            "+20.1%"
        )
    
    with col3:
        contributor_revenue = st.session_state.total_revenue * CONTRIBUTOR_SHARE
        st.metric(
            "Contributors Share (70%)",
            f"${contributor_revenue:,.2f}",
            "+25.2%"
        )
    
    with col4:
        st.metric(
            "Avg Revenue/User",
            f"${st.session_state.total_revenue / st.session_state.active_users:.2f}",
            "+12.3%"
        )
    
    st.divider()
    
    # Revenue charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Revenue Growth Trend")
        
        # Generate sample data
        dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
        revenue_data = pd.DataFrame({
            'Date': dates,
            'Revenue': [st.session_state.total_revenue * (i/30) for i in range(1, 31)]
        })
        
        fig = px.line(revenue_data, x='Date', y='Revenue', 
                     title='30-Day Revenue Trend',
                     template='plotly_white')
        fig.update_traces(line_color='#2563eb', line_width=3)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🥧 Revenue Distribution")
        
        # Pie chart
        fig = go.Figure(data=[go.Pie(
            labels=['Platform (30%)', 'Contributors (70%)'],
            values=[30, 70],
            hole=.4,
            marker=dict(colors=['#2563eb', '#10b981'])
        )])
        fig.update_layout(title='Revenue Split Model')
        st.plotly_chart(fig, use_container_width=True)
    
    # Revenue sources
    st.subheader("💵 Revenue Sources")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Premium Subscriptions", "$8,420", "+15%")
    with col2:
        st.metric("Pay-per-use", "$4,850", "+28%")
    with col3:
        st.metric("API Access", "$1,980", "+42%")
    with col4:
        st.metric("Advertising", "$170.50", "+8%")

elif page == "👥 Contributors":
    st.markdown('<p class="main-header">Contributor Earnings</p>', unsafe_allow_html=True)
    st.markdown("**Revenue shared based on contribution value and usage**")
    
    # Contributors data
    contributors_data = pd.DataFrame({
        'Contributor': ['AI Training Co', 'TechKB Solutions', 'Customer Support Data', 
                       'Industry Experts', 'Domain Specialists', 'Quality Reviewers'],
        'Contribution Type': ['Base Model Training', 'Technical Knowledge Base', 
                             'Support Conversations', 'Domain Expertise', 
                             'Specialized Knowledge', 'Data Quality'],
        'Share %': [27.5, 20.6, 14.5, 12.8, 15.2, 9.4],
        'Earnings': [4250.80, 3180.25, 2240.50, 1978.25, 2348.60, 1452.95],
        'Growth': ['+18%', '+25%', '+12%', '+22%', '+31%', '+15%']
    })
    
    # Summary metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Contributors", "6", "+2 this quarter")
    with col2:
        st.metric("Total Paid Out", f"${contributors_data['Earnings'].sum():,.2f}", "+23%")
    with col3:
        st.metric("Avg Earning", f"${contributors_data['Earnings'].mean():,.2f}", "+19%")
    
    st.divider()
    
    # Contributors table
    st.subheader("📊 Contributor Performance")
    
    # Style the dataframe
    st.dataframe(
        contributors_data.style.format({
            'Share %': '{:.1f}%',
            'Earnings': '${:,.2f}'
        }),
        use_container_width=True,
        hide_index=True
    )
    
    # Individual contributor cards
    st.subheader("💎 Top Contributors")
    
    cols = st.columns(3)
    for idx, row in contributors_data.head(3).iterrows():
        with cols[idx]:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 1.5rem; border-radius: 1rem; color: white;'>
                <h3 style='margin:0; color: white;'>{row['Contributor']}</h3>
                <p style='margin: 0.5rem 0; opacity: 0.9;'>{row['Contribution Type']}</p>
                <h2 style='margin: 0.5rem 0; color: white;'>${row['Earnings']:,.2f}</h2>
                <p style='margin: 0; font-size: 0.9rem;'>
                    {row['Share %']:.1f}% share • {row['Growth']} growth
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # Become a contributor
    st.subheader("🚀 Become a Contributor")
    st.info("""
    **Join our contributor network and earn from your expertise:**
    
    ✅ Share AI training data
    ✅ Contribute knowledge bases
    ✅ Provide domain expertise
    ✅ Review and improve quality
    
    **Benefits:**
    - Transparent revenue sharing (70% to contributors)
    - Monthly payouts
    - Performance bonuses
    - Community recognition
    """)
    
    if st.button("Apply to Become a Contributor", type="primary"):
        st.success("✅ Application form would open here. Thank you for your interest!")

elif page == "📈 Analytics":
    st.markdown('<p class="main-header">Platform Analytics</p>', unsafe_allow_html=True)
    
    # User metrics
    st.subheader("👥 User Engagement")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Daily Active Users", "3,421", "+15.2%")
    with col2:
        st.metric("Monthly Active Users", f"{st.session_state.active_users:,}", "+18.2%")
    with col3:
        st.metric("Avg Session Time", "12m 34s", "+8.5%")
    with col4:
        st.metric("Retention Rate", "78.5%", "+5.2%")
    
    st.divider()
    
    # Interaction analytics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💬 Interaction Volume")
        
        # Generate hourly data
        hours = list(range(24))
        interactions = [st.session_state.total_interactions * (0.02 + 0.04 * abs(12 - h) / 12) for h in hours]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=hours,
            y=interactions,
            marker=dict(color='#2563eb'),
            name='Interactions'
        ))
        fig.update_layout(
            title='Interactions by Hour',
            xaxis_title='Hour of Day',
            yaxis_title='Interactions',
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌍 Geographic Distribution")
        
        geo_data = pd.DataFrame({
            'Region': ['North America', 'Europe', 'Asia', 'South America', 'Others'],
            'Users': [45, 28, 18, 6, 3]
        })
        
        fig = px.pie(geo_data, values='Users', names='Region',
                    title='User Distribution by Region',
                    template='plotly_white',
                    color_discrete_sequence=px.colors.sequential.Blues_r)
        st.plotly_chart(fig, use_container_width=True)
    
    # Revenue per user segment
    st.subheader("💰 Revenue by User Segment")
    
    segment_data = pd.DataFrame({
        'Segment': ['Free Users', 'Basic Plan', 'Premium Plan', 'Enterprise'],
        'Users': [8450, 3120, 1024, 253],
        'Revenue': [1275.50, 4680.00, 7234.00, 2231.00],
        'Avg per User': [0.15, 1.50, 7.07, 8.82]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(segment_data, x='Segment', y='Users',
                    title='Users by Segment',
                    template='plotly_white',
                    color='Users',
                    color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.bar(segment_data, x='Segment', y='Revenue',
                    title='Revenue by Segment',
                    template='plotly_white',
                    color='Revenue',
                    color_continuous_scale='Greens')
        st.plotly_chart(fig, use_container_width=True)

else:  # About page
    st.markdown('<p class="main-header">About the Platform</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🚀 AI Revenue Sharing Platform
        
        **The Future of Fair AI Monetization**
        
        Our platform revolutionizes how AI services generate and distribute revenue. 
        Inspired by successful models from Google, YouTube, and Facebook, we ensure 
        that everyone who contributes to the AI's capabilities gets fairly compensated.
        
        #### 🎯 Key Features
        
        - **Transparent Revenue Sharing**: 70% goes directly to contributors
        - **Real-time Analytics**: Track earnings and performance live
        - **Multiple Revenue Streams**: Subscriptions, pay-per-use, API access, ads
        - **Fair Attribution**: Earnings based on actual contribution value
        - **Scalable Architecture**: Built to handle millions of interactions
        
        #### 💡 How It Works
        
        1. **Users** interact with our AI chatbot
        2. **Platform** processes interactions and generates revenue
        3. **System** automatically distributes earnings to contributors
        4. **Everyone wins** - sustainable ecosystem for all
        
        #### 🌟 Why This Matters
        
        Traditional AI platforms keep all revenue. We believe in **fair compensation** 
        for data providers, trainers, and experts who make the AI smarter. This creates 
        a sustainable ecosystem where quality contributions are rewarded.
        """)
        
        st.divider()
        
        st.subheader("📊 Market Opportunity")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("AI Market Size", "$190B", "2025")
        with col2:
            st.metric("Expected Growth", "37.3%", "CAGR")
        with col3:
            st.metric("Target Market", "$15B", "Chatbots")
        
        st.markdown("""
        #### 🎯 Competitive Advantages
        
        - ✅ First-mover in transparent AI revenue sharing
        - ✅ Proven business model (YouTube, Spotify, Airbnb)
        - ✅ Built-in incentives for quality contributions
        - ✅ Scalable architecture from day one
        - ✅ Multiple revenue streams
        """)
    
    with col2:
        st.markdown("### 📈 Platform Stats")
        
        stats = {
            "Total Revenue": f"${st.session_state.total_revenue:,.2f}",
            "Active Users": f"{st.session_state.active_users:,}",
            "Contributors": "6",
            "Interactions": f"{st.session_state.total_interactions:,}",
            "Avg Response Time": "1.2s",
            "Uptime": "99.9%",
            "User Satisfaction": "4.8/5",
            "Revenue Growth": "+23.5%"
        }
        
        for key, value in stats.items():
            st.metric(key, value)
        
        st.divider()
        
        st.markdown("### 🔗 Quick Links")
        st.markdown("""
        - [📄 Documentation](#)
        - [🔌 API Reference](#)
        - [👥 Community](#)
        - [📧 Contact Us](#)
        - [💼 Careers](#)
        """)
        
        st.divider()
        
        st.info("""
        **Ready to Invest?**
        
        Contact us for detailed financial 
        projections, technical architecture, 
        and growth strategy.
        
        📧 invest@airevshare.com
        """)

# Footer
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("© 2024 AI Revenue Share Platform")
with col2:
    st.markdown("Built with ❤️ using Streamlit")
with col3:
    st.markdown("Version 1.0.0")
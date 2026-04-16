import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

# --- 1. 頁面配置 ---
st.set_page_config(page_title="健功醫療器材", page_icon="🏥", layout="wide")

# --- 2. CSS 注入：調整適當行距與精緻間隙 ---
st.markdown("""
    <style>
    /* 全域字體設定：18px 微軟正黑體，搭配 1.6 舒適行高 */
    html, body, [class*="css"], .stMarkdown, p, li, span, div {
        font-family: "Microsoft JhengHei", "微軟正黑體", sans-serif !important;
        font-size: 18px !important;
        line-height: 1.6 !important; 
        color: #333333;
    }

    /* 調整 Streamlit 頂部預設空白：適度留白 */
    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 1rem !important;
    }

    /* 標題區塊：適度間距 */
    h1 { 
        font-size: 2.6rem !important; 
        font-weight: 800 !important; 
        color: #0D47A1; 
        text-align: center; 
        margin-bottom: 10px !important; 
    }
    
    /* 主要容器：優化內距 (Padding) */
    .comfort-container {
        background-color: #FFFFFF;
        padding: 25px 45px !important; 
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        max-width: 1150px;
        margin: auto;
    }

    /* 針對紅圈處的優化：適度的組件間距 */
    .stVerticalBlock {
        gap: 1.2rem !important; /* 從擠壓狀態恢復到適中距離 */
    }

    /* 地圖區標題與內容的精緻間距 */
    .map-title {
        margin-top: 15px !important;
        margin-bottom: 10px !important;
        font-weight: 600;
        color: #0D47A1;
    }

    hr {
        margin: 25px 0 !important;
        border: 0;
        border-top: 1px solid #EEE;
    }

    /* 按鈕樣式 */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #0D47A1 !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 18px !important;
        padding: 10px !important;
        border: none !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1976D2 !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 網頁頂部標題 ---
st.markdown("<h1>健功醫療器材</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #546E7A; margin-bottom: 20px;'>專業醫材供應 · 守護您的健康</p>", unsafe_allow_html=True)

# --- 4. 主要內容容器 ---
with st.container():
    st.markdown('<div class="comfort-container">', unsafe_allow_html=True)
    
    # 上方資訊區
    col_intro, col_contact = st.columns([1.5, 1], gap="large")
    
    with col_intro:
        st.markdown("### 💡 個人簡介")
        st.write("深耕於醫療器材產業，代表**健功醫療器材**提供專業且具溫度的服務。優質的醫療設備是健康生活的基石，我們致力於連接最先進的技術與使用者的需求。")
        st.write("**核心專長：**")
        st.write("• 行動輔具諮詢 (輪椅、助行器)  \n• 復健器材規劃 / 客戶售後關懷")

    with col_contact:
        st.markdown("### 📬 聯絡細節")
        st.write(f"👤 **負責窗口：** Li Chieh Lin")
        st.write(f"📧 **郵件：** [6b4xz009@stust.edu.tw](mailto:6b4xz009@stust.edu.tw)")
        st.write(f"📞 **電話：** [06-2375525](tel:062375525)")
        st.link_button("👉 Facebook 官方專頁", "https://www.facebook.com/healthsuccess89/?locale=zh_TW")

    st.markdown("<hr>", unsafe_allow_html=True)

    # 下方地圖區
    st.markdown("<h3 class='map-title'>📍 服務據點導航</h3>", unsafe_allow_html=True)
    map_col1, map_col2 = st.columns(2, gap="large")

    stores = [
        {"name": "奇美店", "addr": "台南市永康區中華路990號"},
        {"name": "成大店", "addr": "台南市北區勝利路180號"}
    ]

    for i, m_col in enumerate([map_col1, map_col2]):
        with m_col:
            data = stores[i]
            st.markdown(f"**{data['name']}** | {data['addr']}")
            
            encoded_addr = urllib.parse.quote(data['addr'])
            preview_url = f"https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q={encoded_addr}" 
            # 沿用穩定免 Key 預覽格式
            preview_url = f"https://maps.google.com/maps?q={encoded_addr}&hl=zh-TW&z=16&output=embed"
            
            components.iframe(preview_url, height=350)
            st.link_button(f"🚗 開啟 Google 地圖導航", f"https://www.google.com/maps/dir/?api=1&destination={encoded_addr}")

    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. 頁尾 ---
st.markdown("<p style='text-align: center; color: #999; font-size: 15px !important; margin-top: 25px;'>© 2026 健功醫療器材 | 專業呈現</p>", unsafe_allow_html=True)
import pandas as pd
import plotly.express as px
import streamlit as st

# 페이지 설정 (와이드 레이아웃)
st.set_page_config(
    page_title="EcoPulse: 지구 생명 & 환경 위기 아카이브",
    page_icon="🌿",
    layout="wide",
)

# 🌿 자연환경 테마를 위한 커스텀 CSS 적용
st.markdown(
    """
    <style>
    .main {
        background-color: #f4f9f4;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #e2ede2;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
        color: #2c5e3b;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2c5e3b !important;
        color: white !important;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 5px solid #2c5e3b;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 타이틀 영역
st.title("🌿 EcoPulse: 지구 생명과 환경 위기 탐색기")
st.markdown(
    "지구촌 곳곳의 생물다양성 위기, **아마존의 눈물**, 그리고 환경 악화의 근본적인 원인을"
    " 데이터로 추적합니다."
)

# 4개의 탭으로 세부화
tab1, tab2, tab3, tab4 = st.tabs([
    "🌐 세계 환경 및 멸종 위기 맵",
    "🌳 아마존 & 열대우림 딥다이브",
    "⚠️ 환경 악화의 세부 원인 분석",
    "🇰🇷 대한민국 생태계 현황",
])

# ==========================================
# 탭 1: 세계 환경 및 멸종 위기 맵
# ==========================================
with tab1:
  st.subheader("전 세계 국가별 생물다양성 위험도 지도")
  st.markdown(
      "위험도가 높을수록 **빨간색(위험)**, 안전할수록 **초록색(안전)**으로"
      " 표시됩니다."
  )

  world_data = {
      "Country": [
          "South Korea",
          "Madagascar",
          "Brazil",
          "Indonesia",
          "United States",
          "Canada",
          "Australia",
          "Germany",
          "Japan",
          "India",
          "China",
          "Russia",
          "Kenya",
          "Norway",
          "Finland",
      ],
      "ISO_A3": [
          "KOR",
          "MDG",
          "BRA",
          "IDN",
          "USA",
          "CAN",
          "AUS",
          "DEU",
          "JPN",
          "IND",
          "CHN",
          "RUS",
          "KEN",
          "NOR",
          "FIN",
      ],
      "Extinction_Risk_Score": [
          65,
          92,
          88,
          85,
          45,
          30,
          78,
          40,
          55,
          72,
          70,
          35,
          60,
          20,
          25,
      ],
      "Main_Threat": [
          "서식지 분절화, 난개발",
          "삼림 벌채, 화전 농업",
          "아마존 개발, 불법 벌목",
          "팜유 플랜테이션, 삼림 파괴",
          "기후 변화, 도시화",
          "기후 변화(고위도 온난화)",
          "대규모 산불, 가뭄",
          "환경 오염, 서식지 축소",
          "도시화, 생태계 교란종",
          "서식지 파괴, 과도한 밀렵",
          "환경 오염, 급격한 산업화",
          "기후 변화, 자원 채굴",
          "가뭄, 사막화, 밀렵",
          "기후 변화",
          "기후 변화",
      ],
  }
  df_world = pd.DataFrame(world_data)

  fig_world = px.choropleth(
      df_world,
      locations="ISO_A3",
      color="Extinction_Risk_Score",
      hover_name="Country",
      hover_data=["Main_Threat"],
      color_continuous_scale=[
          (0.0, "#2ecc71"),
          (0.4, "#f1c40f"),
          (0.7, "#e67e22"),
          (1.0, "#c0392b"),
      ],
      labels={"Extinction_Risk_Score": "위험 지수 (100점 만점)"},
      title="세계 국가별 환경 위기 지수 맵",
  )
  fig_world.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0}, height=500)
  st.plotly_chart(fig_world, use_container_width=True)

  with st.expander("🌍 국가별 상세 데이터 원본 보기"):
    st.dataframe(df_world, use_container_width=True)

# ==========================================
# 탭 2: 아마존 & 열대우림 딥다이브
# ==========================================
with tab2:
  st.subheader("🌳 아마존 유역 파괴 및 산림 손실 시뮬레이션")
  st.markdown(
      "세계의 허파라 불리는 **아마존**은 지구 산소의 상당 부분을 공급하지만,"
      " 최근 인간의 활동으로 파괴가 극심합니다."
  )

  col1, col2 = st.columns(2)
  with col1:
    st.markdown(
        """
        <div class="metric-card">
        <h4>🔥 아마존 환경 파괴의 주된 원인</h4>
        <ul>
            <li><b>불법 벌목 및 목재 채취:</b> 고급 가구 및 건축 자재용 나무 무단 벌목</li>
            <li><b>축산업을 위한 방목지 개간:</b> 소고기 생산을 위한 대규모 초지 조성</li>
            <li><b>플랜테이션 및 화전 농업:</b> 콩(대두) 단일 경작지 확대</li>
            <li><b>광산 개발(금광 등):</b> 수은 등 유독 물질로 인한 하천 오염</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

  with col2:
    # 연도별 아마존 삼림 손실 추이 가상 데이터
    amazon_loss_data = {
        "Year": [2020, 2021, 2022, 2023, 2024, 2025],
        "Deforestation_Area_Thousand_ha": [
            11088,
            13038,
            11594,
            9001,
            8500,
            8200,
        ],
    }
    df_amazon = pd.DataFrame(amazon_loss_data)

    fig_amazon = px.line(
        df_amazon,
        x="Year",
        y="Deforestation_Area_Thousand_ha",
        markers=True,
        title="아마존 연도별 삼림 손실 면적 (단위: 천 헥타르)",
        labels={"Deforestation_Area_Thousand_ha": "손실 면적 (천 ha)"},
    )
    fig_amazon.update_traces(line_color="#c0392b", line_width=3)
    st.plotly_chart(fig_amazon, use_container_width=True)

# ==========================================
# 탭 3: 환경 악화의 세부 원인 분석
# ==========================================
with tab3:
  st.subheader("⚠️ 왜 환경은 악화되고 생물은 사라지는가? (4대 주원인)")
  st.markdown(
      "생태계 파괴는 단일 요인이 아닌 **복합적인 인류 활동**에서 비롯됩니다."
  )

  # 원인별 비중 데이터
  causes_data = {
      "Cause": [
          "서식지 파괴 및 전환 (농경지/도시)",
          "기후 변화 및 지구 온난화",
          "자연 자원 과다 채취 (밀렵/남획)",
          "외래종 유입 및 환경 오염",
      ],
      "Impact_Percentage": [45, 25, 20, 10],
  }
  df_causes = pd.DataFrame(causes_data)

  col_c1, col_c2 = st.columns([1, 1])

  with col_c1:
    fig_pie = px.pie(
        df_causes,
        names="Cause",
        values="Impact_Percentage",
        title="생물다양성 위협 요인별 영향 비중",
        color_discrete_sequence=px.colors.sequential.Greens_r,
    )
    st.plotly_chart(fig_pie, use_container_width=True)

  with col_c2:
    st.markdown(
        """
        ### 📌 세부 원인 해설
        1. **서식지 파괴 (45%):** 도시화, 도로 건설, 농지 개간 등으로 인해 동물의 집이 산조각(서식지 분절화)나며 이동과 번식이 차단됩니다.
        2. **기후 변화 (25%):** 극심한 가뭄, 산불, 해수면 상승으로 생물들이 적응할 겨를도 없이 생태계가 무너집니다.
        3. **과도한 남획 및 밀렵 (20%):** 상업적 목적이나 전통 약재 명목으로 특정 동식물을 무분별하게 포획하여 멸종에 이르게 합니다.
        4. **환경 오염 및 외래종 (10%):** 미세플라스틱, 화학 물질, 그리고 토착 생태계를 파괴하는 외래 생물의 유입이 원인입니다.
        """
    )

# ==========================================
# 탭 4: 대한민국 생태계 현황
# ==========================================
with tab4:
  st.subheader("🇰🇷 대한민국 권역별 멸종위기 야생생물 현황")
  st.markdown("국내 시·도별 멸종위기 야생생물(I급, II급) 서식 현황입니다.")

  korea_data = {
      "Region": [
          "강원도",
          "제주특별자치도",
          "경상북도",
          "전라남도",
          "경기도",
          "충청북도",
          "경상남도",
          "전라북도",
          "서울특별시",
      ],
      "Endangered_Species_Count": [128, 95, 110, 102, 65, 58, 82, 70, 25],
      "Primary_Vulnerable_Taxa": [
          "산양, 설악우슬초",
          "남방큰돌고래, 붉은어깨거북",
          "산양, 수달",
          "수달, 매",
          "수원청개구리",
          "하늘다람쥐",
          "남생이, 수달",
          "붉은박쥐",
          "맹꽁이(도심 습지)",
      ],
  }
  df_korea = pd.DataFrame(korea_data)

  fig_korea = px.bar(
      df_korea,
      x="Region",
      y="Endangered_Species_Count",
      color="Endangered_Species_Count",
      color_continuous_scale=[(0.0, "#27ae60"), (1.0, "#c0392b")],
      labels={"Endangered_Species_Count": "멸종위기종 수 (종)"},
      title="국내 지역별 멸종위기종 분포",
  )
  st.plotly_chart(fig_korea, use_container_width=True)
  st.dataframe(df_korea, use_container_width=True)

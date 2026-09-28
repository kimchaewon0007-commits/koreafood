import pandas as pd
import plotly.express as px
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="지구 생명 멸종 위기 & 환경 통계 대시보드",
    page_icon="🌍",
    layout="wide",
)

st.title("🌍 지구 생명 및 멸종 위기 환경 대시보드")
st.markdown(
    "전 세계 국가별 환경 위험도(멸종 위기종 비율)와 국내(한국) 지역별 멸종위기 야생생물 현황을 시각화합니다."
)

# 탭 메뉴 구성 (세계 지도 vs 국내 통계)
tab1, tab2 = st.tabs(["🌐 세계 멸종 위기 & 환경 지도", "🇰🇷 대한민국 지역별 멸종위기종 현황"])

with tab1:
  st.subheader("전 세계 국가별 생물다양성 및 멸종 위기 지수")
  st.markdown(
    "위험도가 높을수록 **빨간색**, 안전할수록 **초록색**으로 표시됩니다."
    " (수치가 높을수록 멸종 위기종 비율 및 환경 악화도가 높음을 의미합니다)"
  )

  # 가상의 전 세계 국가별 데이터 (실제 서비스에서는 IUCN Red List나 세계은행 데이터 API와 연동 가능)
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
      ],  # 100에 가까울수록 위험
      "Main_Threat": [
          "서식지 분절화, 개발",
          "삼림 벌채, 서식지 파괴",
          "아마존 개발, 불법 벌목",
          "팜유 플랜테이션, 벌목",
          "기후 변화, 도시화",
          "기후 변화(고위도 온난화)",
          "산불, 기후 변화",
          "환경 오염, 서식지 감소",
          "개발, 생태계 교란종",
          "서식지 파괴, 밀렵",
          "환경 오염, 난개발",
          "기후 변화, 자원 개발",
          "가뭄, 밀렵",
          "기후 변화",
          "기후 변화",
      ],
  }

  df_world = pd.DataFrame(world_data)

  # Plotly Choropleth 세계 지도 생성
  # 색상 범위: 초록색(안전) -> 노란색 -> 빨간색(위험)
  fig_world = px.choropleth(
      df_world,
      locations="ISO_A3",
      color="Extinction_Risk_Score",
      hover_name="Country",
      hover_data=["Main_Threat"],
      color_continuous_scale=[
          (0.0, "green"),
          (0.3, "lightgreen"),
          (0.6, "yellow"),
          (0.8, "orange"),
          (1.0, "red"),
      ],
      labels={"Extinction_Risk_Score": "위험 지수 (높을수록 위험)"},
      title="세계 국가별 환경 및 멸종 위기 위험도 맵",
  )

  fig_world.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0}, height=500)
  st.plotly_chart(fig_world, use_container_width=True)

  # 데이터 테이블 보기 옵션
  with st.expander("데이터 원본 표로 보기"):
    st.dataframe(df_world)

with tab2:
  st.subheader("🇰🇷 대한민국 권역별 멸종위기 야생생물 현황")
  st.markdown(
      "국내 시·도별 멸종위기 야생생물(I급, II급) 서식 현황 및 주요 위협 요인을"
      " 확인합니다."
  )

  # 국내 지역별 가상 통계 데이터 (환경부 통계 기반 응용)
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
      "Risk_Level": [
          "매우 높음",
          "매우 높음",
          "높음",
          "높음",
          "보통",
          "보통",
          "높음",
          "보통",
          "낮음",
      ],
  }

  df_korea = pd.DataFrame(korea_data)

  # 시각화: 막대 그래프
  fig_korea = px.bar(
      df_korea,
      x="Region",
      y="Endangered_Species_Count",
      color="Endangered_Species_Count",
      color_continuous_scale=[
          (0.0, "green"),
          (0.4, "yellow"),
          (0.7, "orange"),
          (1.0, "red"),
      ],
      labels={"Endangered_Species_Count": "멸종위기종 서식/출현 수 (종)"},
      title="국내 지역별 멸종위기 야생생물 분포 수",
  )

  st.plotly_chart(fig_korea, use_container_width=True)

  # 상세 테이블
  st.markdown("### 📋 지역별 상세 정보 및 주요 보호종")
  st.dataframe(df_korea, use_container_width=True)

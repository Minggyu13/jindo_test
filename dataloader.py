import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# 데이터 불러오기
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# 텍스트 요소 생성. 사용자에게 데이터가 로드 되고 있음을 알린다.
data_load_state = st.text('Loading data...')

# 10000개의 행의 데이터를 로드한다.
data = load_data(10000)

# 데이터가 성공적으로 로드 되었음을 알린다.
data_load_state.text('Loading data...done!')

# 부제목 만들기
st.subheader('Raw data')
st.write(data)

# 히스토그램 추가 (시간대별 Uber 픽업 빈도)
st.subheader('Number of pickups by hour')

# 시간대 컬럼 추가
data['hour'] = data[DATE_COLUMN].dt.hour

# 히스토그램 생성
hist_values = np.histogram(data['hour'], bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# 지도 시각화 추가
st.subheader('Map of all pickups')

# Pydeck을 이용한 지도 시각화
st.map(data)

# 더 복잡한 지도 시각화
st.subheader('Enhanced map with Pydeck')

# Pydeck 시각화를 위한 Layer 생성
layer = pdk.Layer(
    'HexagonLayer',
    data=data,
    get_position=['lon', 'lat'],
    radius=100,
    elevation_scale=4,
    elevation_range=[0, 1000],
    pickable=True,
    extruded=True,
)

# Pydeck 시각화를 위한 View 설정
view_state = pdk.ViewState(
    latitude=data['lat'].mean(),
    longitude=data['lon'].mean(),
    zoom=10,
    pitch=50,
)

# Pydeck Deck 생성
r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
)

# Pydeck 지도 표시
st.pydeck_chart(r)

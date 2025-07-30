import streamlit as st

# 페이지 설정
st.set_page_config(page_title="약 추천 AI", page_icon="💊")

st.title("💊 증상 기반 약 추천 AI")

# 상태 저장 (입력 전/후 화면 전환)
if "단계" not in st.session_state:
    st.session_state["단계"] = "입력화면"

# 약 데이터
증상_데이터 = {
    "두통": {
        "키워드": ["머리", "두통"],
        "약": "이부프로펜, 타이레놀",
        "이미지": "https://www.tylenol.co.kr/products/tylenol-500mg"
    },
    "기침": {
        "키워드": ["기침", "기침이", "기침나요"],
        "약": "벤토린, 코푸시럽",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Ibuprofen_200mg_tablets.jpg/800px-Ibuprofen_200mg_tablets.jpg"
    },
    "콧물": {
        "키워드": ["콧물", "코가", "코막힘"],
        "약": "클라리틴, 알러지약",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Loratadine_10mg_tablets.jpg/800px-Loratadine_10mg_tablets.jpg"
    },
    "열": {
        "키워드": ["열", "열나요", "열이"],
        "약": "타이레놀, 해열제",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Tylenol2006.jpg/640px-Tylenol2006.jpg"
    },
    "복통": {
        "키워드": ["배", "복통", "속이"],
        "약": "베아제, 훼스탈",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Festal_tablets.jpg/800px-Festal_tablets.jpg"
    }
}

# 단계별 화면 처리
if st.session_state["단계"] == "입력화면":
    입력 = st.text_input("어디가 아프세요? (예: 머리가 아파요)")

    if 입력:
        추천_약 = None
        추천_이미지 = None

        for 증상 in 증상_데이터:
            키워드들 = 증상_데이터[증상]["키워드"]
            for 키워드 in 키워드들:
                if 키워드 in 입력:
                    추천_약 = 증상_데이터[증상]["약"]
                    추천_이미지 = 증상_데이터[증상]["이미지"]
                    break
            if 추천_약:
                break

        if 추천_약:
            st.session_state["추천_약"] = 추천_약
            st.session_state["추천_이미지"] = 추천_이미지
            st.session_state["단계"] = "결과화면"
            st.rerun()
        else:
            st.error("😢 죄송해요, 그 증상에 대한 정보가 아직 없어요.")

elif st.session_state["단계"] == "결과화면":
    st.success(f"💊 추천 약: {st.session_state['추천_약']}")
    st.image(st.session_state["추천_이미지"], use_container_width=True)

    # 왼쪽 아래에 "이전" 버튼
    with st.sidebar:
        if st.button("⬅ 이전으로 돌아가기"):
            st.session_state["단계"] = "입력화면"
            st.rerun()


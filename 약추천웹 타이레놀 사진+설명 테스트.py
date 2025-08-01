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
        "약": "타이레놀",
        "이미지": "https://sdmntpreastus.oaiusercontent.com/files/00000000-fb8c-61f9-84bd-6febd5f08841/raw?se=2025-07-31T13%3A11%3A46Z&sp=r&sv=2024-08-04&sr=b&scid=a0a35075-7f24-5138-bed0-85d541973d4e&skoid=5c72dd08-68ae-4091-b4e1-40ccec0693ae&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-07-30T22%3A14%3A57Z&ske=2025-07-31T22%3A14%3A57Z&sks=b&skv=2024-08-04&sig=KEtXLBDVWtaxmE9My2ceQAdhp9JyJoJ/qgE3xfVjQrI%3D"
    },
    "기침": {
        "키워드": ["기침", "기침이", "기침나요"],
        "약": "코푸스탑",
        "이미지": "https://sdmntprwestus3.oaiusercontent.com/files/00000000-e874-61fd-951a-ec9275ce9ed6/raw?se=2025-07-31T14%3A10%3A18Z&sp=r&sv=2024-08-04&sr=b&scid=b7a308b5-39c5-5de0-9529-7597e9e1232c&skoid=c953efd6-2ae8-41b4-a6d6-34b1475ac07c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-07-30T22%3A38%3A30Z&ske=2025-07-31T22%3A38%3A30Z&sks=b&skv=2024-08-04&sig=xPpMPYqfOQZHoDVZ0HXh3/xg9QKTytvzYNLii728oy0%3D"
    },
    "콧물": {
        "키워드": ["콧물", "코", "코가", "코막힘"],
        "약": "알러샷",
        "이미지": "https://github.com/Chohw10/medicine-ai/blob/main/%EC%95%8C%EB%9F%AC%EC%83%B7.png?raw=true"
    },
    "열": {
        "키워드": ["열", "열나요", "열이"],
        "약": "타세놀",
        "이미지": "https://sdmntpritalynorth.oaiusercontent.com/files/00000000-2484-6246-b6cc-179b6d224b84/raw?se=2025-07-31T13%3A43%3A15Z&sp=r&sv=2024-08-04&sr=b&scid=860ccaf0-8088-5fe4-9f3e-d8e4e95379b9&skoid=5c72dd08-68ae-4091-b4e1-40ccec0693ae&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-07-30T22%3A16%3A34Z&ske=2025-07-31T22%3A16%3A34Z&sks=b&skv=2024-08-04&sig=IVrWDShdk8TXdARzMyEEti24AkPsQ44vT1nhzKepZJE%3D"
    },
    "복통": {
        "키워드": ["배", "복통", "속이"],
        "약": "부스코판",
        "이미지": "https://sdmntprwestus3.oaiusercontent.com/files/00000000-b6f4-61fd-8694-e4fc16e1aecd/raw?se=2025-07-31T13%3A59%3A41Z&sp=r&sv=2024-08-04&sr=b&scid=945606ef-257f-5a29-8824-a0d42d03266b&skoid=c953efd6-2ae8-41b4-a6d6-34b1475ac07c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-07-30T22%3A38%3A30Z&ske=2025-07-31T22%3A38%3A30Z&sks=b&skv=2024-08-04&sig=GzirWX2B3obQk6fsJhbNvxK5ssO5KpCFimgGzMBlyH0%3D"
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
    st.image(st.session_state["추천_이미지"], width=300)

     # 약 설명 자동 출력
    약설명 = ""
    if "타이레놀" in st.session_state["추천_약"]:
        약설명 = "💡 타이레놀은 두통, 치통, 근육통, 감기 증상 등의 완화에 사용되는 해열진통제입니다. 만 12세 이상 소아 및 성인 기준 최대 1회에 2정씩 1일 4회(4-6시간마다) 복용할 수 있습니다."
    if "코푸스탑" in st.session_state["추천_약"]:
        약설명 = "💡 코푸스탑은 기침·가래에 사용되는 복합 진해·거담제입니다. 성인 기준  1회 1캡슐씩 1일 3회 식후에 복용해야 합니다."
    if "알러샷" in st.session_state["추천_약"]:
        약설명 = "💡 알러샷은 코막힘, 콧물, 재채기 같은 알레르기 비염 증상을 완화해주는 약입니다. 성인 및 12세 이상 소아 기준 1일 1회, 1정 복용합니다."
    if "타세놀" in st.session_state["추천_약"]:
        약설명 = "💡 타세놀은 열을 내리고 통증을 완화하는 해열진통제입니다. 성인 (만 12세 이상) 기준 1회 1~2정씩 1일 3-4회 (4-6시간 마다) 필요시 복용할 수 있습니다."
    if "부스코판" in st.session_state["추천_약"]:
        약설명 = "💡 부스코판은 장이나 위의 경련을 완화해 복통을 줄여주는 약입니다. 성인 및 12세 이상 소아 기준 1회 1-2정씩 1일 3회, 최대 6정 복용할 수 있습니다."

    if 약설명:
        st.info(약설명)
        
    # 왼쪽 아래에 "이전" 버튼
    with st.sidebar:
        if st.button("⬅ 이전으로 돌아가기"):
            st.session_state["단계"] = "입력화면"
            st.rerun()


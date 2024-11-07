import streamlit as st
import torch
from PIL import Image
import os
import torch.nn as nn
from efficientnet_pytorch import EfficientNet
from torchvision import models, transforms
import pandas as pd
from openai import OpenAI
from matplotlib import pyplot as plt
import shutil
import json
from datetime import date

st.set_page_config(
    # layout="wide",
    page_title="두피케어 제품 추천 서비스",
    page_icon=".data/images/monsterball.png"
)

st.markdown(
    """
    <style>    
    .main > div {
        max-width: 80%; /* 기본값은 80%입니다. 필요한 만큼 넓힐 수 있습니다 */
        padding-left: 5%;
        padding-right: 5%;
    }   

    </style>
    """, unsafe_allow_html=True)
# /*
#     img {
#         max-height: 500px;
#     }
#     .streamlit-expanderContent div {
#         display: flex;
#         justify-content: center;
#         font-size: 20px;
#     }
#     [data-testid="stExpanderToggleIcon"] {
#         visibility: hidden;
#     }
#     .streamlit-expanderHeader {
#         pointer-events: none;
#     }
#     [data-testid="StyledFullScreenButton"] {
#         visibility: hidden;
#     }
#     */

# 오늘의 날짜 가져오기
today = date.today()

# 화면에 오늘 날짜 표시
st.image("./data/banner_1.jpg", use_column_width=True)
st.markdown(f"{today.strftime('%Y.%m.%d')}, made by DeepRoot(김성환, 김준호, 이혜진, 전민정)")


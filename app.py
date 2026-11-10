import streamlit as st
import google.generativeai as genai

# 1. API KALITINGIZNI SHU YERGA QO'YING
API_KEY = "AQ.Ab8RN6IzaWPsyr_53agbgj4G8evB5PuvDGBT1VjWaRslQkqurQ" # 
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="LogiAI Demo", layout="wide")
st.title("🚀 LogiAI: AI Boshqaruv Agenti")
st.markdown("Tizim kalit so'zlar emas, balki **transferable skills** (o'tkaziladigan ko'nikmalar) asosida ishlaydi.")

st.subheader("1. Vakansiya talabini kiriting")
job_desc = st.text_area("Masalan: Aeroport logistika bo'limi menejeri. Talab: stressga chidamlilik, ma'lumotlar bilan ishlash, smenali grafik, ingliz tili.", height=100)

st.subheader("2. Nomzodlar CV ma'lumotlarini kiriting")
cvs = st.text_area("1-nomzod: 3 yil temir yo'l dispetcheri, smenali ish tajribasi bor...\n2-nomzod: 1 yil ofis menejeri, ingliz tili B1...", height=150)

if st.button("AI orqali tahlil qilish"):
    if not job_desc or not cvs:
        st.error("Iltimos, barcha maydonlarni to'ldiring!")
    else:
        with st.spinner("Semantik tahlil amalga oshirilmoqda..."):
            prompt = f"""
            Vakansiya: {job_desc}
            Nomzodlar: {cvs}
            
            Sen tajribali HR AI agentsan. 
            1. Har bir nomzodga 0-100% moslik balli ber.
            2. Transferable skills asosida nega mos kelishini yoki kelmasligini izohla.
            3. Eng yaxshi 2 nomzodni tanla va ularga 3 tadan intervyu savoli tuz.
            """
            try:
                # Gemini modelini chaqirish (bepul versiya uchun)
                model = genai.GenerativeModel('gemini-1.5-flash') 
                response = model.generate_content(prompt)
                st.success("Tahlil yakunlandi!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Xatolik yuz berdi: {e}")
                st.info("API kalitingiz to'g'riligini yoki internet aloqasini tekshiring.")

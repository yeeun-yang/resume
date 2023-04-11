import streamlit as st
from PIL import Image
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# theme
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

col1, col2 = st.columns([3,7])

with col1:
    
    # profile image frame
    eun = Image.open('eun.png')
    st.image(eun, width=100)
    
    # education frame
    st.subheader('Education')
    st.markdown('Kyunghee University')
    st.markdown('B.A in Global Communication (GPA: 3.8/4.5)')
    st.markdown('Scholarship received <br>in 2016, 2017 and 2018', unsafe_allow_html=True)
    
    # company frame
    st.subheader('Companies')
    c_1 = st.empty()
    c_2 = st.empty()
    c_3 = st.empty()
    c_1.markdown('<p style="color: black;">LG Electronics<br>(2020.12~2023.02)</p>', unsafe_allow_html=True)
    c_2.markdown('<p style="color: black;">Korea Agro-Fisheries and Food Trade Corporation<br>(2019.06~2019.11)</p>', unsafe_allow_html=True)
    c_3.markdown("<p style='color: black;'>STAR's TECH<br>(2018.09~2019.02)</p>", unsafe_allow_html=True)
    
    # skill frame
    st.subheader('Skills')
    s1 = st.empty()
    s2 = st.empty()
    s3 = st.empty()
    s1.progress(90, text='Data Aanalysis')
    s2.progress(80, text='Overseas Sales')
    s3.progress(75, text='SCM Management')
    
    # language frame
    st.subheader('Language')    
    st.markdown(
        """
        <style>
            .stProgress > div > div > div > div {
                background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
            }
        </style>""",
        unsafe_allow_html=True,
    )

    st.progress(100, 'Korean')
    st.progress(80, 'English')
    st.progress(50, 'Japanese')
    
    # computer skill frame
    st.subheader('Computer skill')
    st.progress(100, 'Excel')
    st.progress(70, 'Python')
    st.progress(80, 'Tableau')
    
    # Achievement frame
    st.subheader('Achievement')
    st.progress(100, 'Best employee of the month by LG')
    st.progress(100, 'Best practice of GTM project by LG')
    
with col2:
    
    # profile overview
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        st.header('Yeeun Yang')
        
    with subcol2:
        st.markdown('<h6>koreanresearch2018@gmail.com</h6>', unsafe_allow_html=True)
        st.markdown('<h6>www.linkedin.com/in/yeeunyang1996</h6>', unsafe_allow_html=True)
        st.markdown('<h6>Budapest,&nbsp;Hungary</h6>', unsafe_allow_html=True)
        st.markdown('', unsafe_allow_html=True)
    
    o = st.empty()
    o.markdown("""<p style="font-size:13px; ">I've worked in USA, Mongolia and Hungary, building global careers related to overseas sales and market research.
               You can select below list box, reading my major skills, company and specific period for each country. Please select it!</p>""", unsafe_allow_html=True)

    # map display
    st.subheader('International career path')

    # locaton info
    # 미국 중심위치 기반 위도 경도 설정
    us_lat = 39.8283
    us_lon = -98.5795
    # 몽골 중심위치 기반 위도 경도 설정
    mn_lat = 46.8625
    mn_lon = 103.8467
    # 헝가리 중심위치 기반 위도 경도 설정
    hu_lat = 47.1625
    hu_lon = 19.5033
    
        
    # country list
    country = st.selectbox('Please choose a country', ('', 'USA', 'Mongolia', 'Hungary'), label_visibility='visible')

    # country function
    def us():
        # map
        m = folium.Map(location=[us_lat, us_lon], zoom_start=3, width=485, height=300, zoom_control=False)
        folium.Marker([us_lat, us_lon], popup='USA', icon=folium.Icon(color='red')).add_to(m)
        folium_static(m, width=485, height=300)
        # company
        c_3.markdown("<p style='color: red;'>STAR's TECH<br>(2018.09~2019.02)</p>", unsafe_allow_html=True)
        # overview
        o.markdown('''<p style="font-size:13px; ">As a US export market research project leader for eco-friendly deicer, 
                   I planned business interviews with major competitors in USA and performed market research with KOTRA mentoring, 
                   drawing export strategy for US market. </p>
                    ''', unsafe_allow_html=True)     
        # skill
        s1.progress(90, text='Overseas Market Research')
        s2.progress(80, text='Business Interview')
        s3.progress(75, text='Analysis and Strategy')
        # experience
        st.subheader('Experience')
        e1 = st.empty()
        e2 = st.empty()
        e3 = st.empty()
        e1.markdown('''<p style="font-size:18px; "><b>Planned US Market Research Project</b></p>
                    <p style="font-size:13px; "><b>&#10003; Business interview and Market Research</b>
                    <br>- Researched major competitors in USA, inviting them for business interview
                    <br>- Conducted business interviews with 3 companies having different channel portfolio - B2C, B2B and B2G - in New York, Philadelphia and Utah
                    <br>- Performed market research in major big distributions for normal consumers, analyzing consumers' preference and competitors' product strength. </p>
                    ''', unsafe_allow_html=True)
        e2.markdown('''<p style="font-size:18px; "><b>Analyzed gathered market information</b></p>
                    <p style="font-size:13px; "><b>&#10003; Market Information Analysis for Export Strategy</b>
                    <br>- Figured out the process adn needed qualifications for exporting korean eco-friendly deicer to USA
                    <br>- Got the market insight and marketing strategies depending on channel portfolio ; B2C, B2B and B2G </p>
                    ''', unsafe_allow_html=True)

        # # project
        # st.subheader('Project')
        # e1 = st.empty()
        # e2 = st.empty()
        # e3 = st.empty()
        # e1.markdown('usa project')
        # e2.markdown('usa project')
        # e3.markdown('usa project') 
        
    def mn():
        # map
        m = folium.Map(location=[mn_lat, mn_lon], zoom_start=3, width=485, height=300, zoom_control=False)
        folium.Marker([mn_lat, mn_lon], popup='Mongolia', icon=folium.Icon(color='purple')).add_to(m)
        folium_static(m, width=485, height=300)
        # company
        c_2.markdown('<p style="color: red;">Korea Agro-Fisheries and Food Trade Corporation<br>(2019.06~2019.11)</p>', unsafe_allow_html=True)
        # overview
        o.markdown('''<p style="font-size:13px; ">As a overseas sales intern, I performed market research and did 4P & SWOT analysis, 
                   drawing sales and marketing strategy for Mongolia market with Mongolian buyers at a Korean food trade company's request. Addtionally, I 
                   managed several international exhibitions also trade show with Korean companies and Mongolia buyers as a team leader, 
                   suceeding in making MOU agreement between them.</p>
                    ''', unsafe_allow_html=True)        
        # skill
        s1.progress(90, text='Market Research')
        s2.progress(80, text='Overseas Sales Strategy')
        s3.progress(70, text='Project Management')
        # experience
        st.subheader('Experience')
        e1 = st.empty()
        e2 = st.empty()
        e3 = st.empty()
        e1.markdown('''<p style="font-size:18px; "><b>Market Research</b></p>
                    <p style="font-size:13px; "><b>&#10003; Competitor and Consumer Research for snack product</b>
                    <br>- Researched major competitors' popular snacks, analyzing each brand's price range and marketing strategy. 
                    <br>- Prepared for snack tasting event and survey questions to gather Mongolian consumers' opinion on our snack product.
                    <br>- Performed business interview with a food distributor about supply chain and distribution system in Mongolia. </p>
                    ''', unsafe_allow_html=True)
        e2.markdown('''<p style="font-size:18px; "><b>Overseas Sales & Marketing Strategy</b></p>
                    <p style="font-size:13px; "><b>&#10003; SWOT & 4P Analysis and Marketing Strategy</b>
                    <br>- Analyzed market information collected by previous market research, making SWOT & 4P analysis for market insight. 
                    <br>- Drawed marketing strategy targeted for Mongolian women consumer at 30's, using ATL marketing such as SNS and building sign board.
                    <br>- Increased sales volumes by 120%, broadening partner's portfolio.</p>
                    ''', unsafe_allow_html=True)
        e3.markdown('''<p style="font-size:18px; "><b>Project Management</b></p>
                    <p style="font-size:13px; "><b>&#10003; Trade Fair Project leading and management</b>
                    <br>- Planned and led trade fair project for Korean food/trade companies and Mongolian buyers, helping Korean companies to appeal their products and make trade contract.
                    <br>- Made several trade deals worth of $1.32 million, making MOU contract</p>
                    ''', unsafe_allow_html=True)
        # # project
        # st.subheader('Project')
        # e1 = st.empty()
        # e2 = st.empty()
        # e3 = st.empty()
        # e1.markdown('mn project')
        # e2.markdown('mn project')
        # e3.markdown('mn project') 
                
    def hu():
        # map
        m = folium.Map(location=[hu_lat, hu_lon], zoom_start=4, width=485, height=300, zoom_control=False)
        folium.Marker([hu_lat, hu_lon], popup='Hungary', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=[46.0569, 14.5058], tooltip="Slovenia").add_to(m)
        folium.Marker(location=[45.1, 15.2], tooltip="Croatia").add_to(m)
        folium.Marker(location=[44.7872, 20.4573], tooltip="Serbia").add_to(m)
        folium.Marker(location=[41.6086, 21.7453], tooltip="Macedonia").add_to(m)
        folium.Marker(location=[44.0165, 21.0059], tooltip="Serbia").add_to(m)
        folium.Marker(location=[42.7339, 25.4858], tooltip="Bulgaria").add_to(m)
        folium.Marker(location=[42.7167, 19.2664], tooltip="Montenegro").add_to(m)
        folium.Marker(location=[41.3275, 19.8187], tooltip="Albania").add_to(m)
        folium_static(m, width=485, height=300)
        # company
        c_1.markdown('<p style="color: red;">LG Electronics<br>(2020.12~2023.02)</p>', unsafe_allow_html=True)
        # overview
        o.markdown('''<p style="font-size:13px; ">As a HA(Home Appliance) Assistant Product Manager, I have managed
                    overall business operation and performed 
                    business analysis especially focusing on product management and SCM operation for 10 Balkan countries.
                    In addtion, I performed Product Manager role for small appliance(microwave oven & dishwaher).
                    Importantly, I introduced new system called GSMS to enforce GTM(Go-To Market) function along with LGCNS.</p>
                    ''', unsafe_allow_html=True)
        # skill
        s1.progress(80, text='Product Management')
        s2.progress(90, text='SCM Management')
        s3.progress(100, text='Data Analysis')
        # experience
        st.subheader('Professional Experience')
        e1 = st.empty()
        e2 = st.empty()
        e3 = st.empty()
        e1.markdown('''<p style="font-size:18px; "><b>Product Management</b></p>
                    <p style="font-size:13px; "><b>&#10003; NPI(New Product Introduction) preparation for small appliance</b>
                    <br>- Communicated with HQ PIC about NPI line-up and development/production schedule, analyzing estimated profitability considering material cost and committed container shipment cost
                    <br>- Analyzed major competitors' product line up, price range and USP(Unique Selling Point), setting targeted RRP based on each countries' VAT and each partners' front/back margin
                    <br>- Negotiated with KAMs about new line-up and targeted RRP, scheduled for estimated shipment date to partners</p>
                    ''', unsafe_allow_html=True)
        e2.markdown('''<p style="font-size:18px; "><b>SCM Management</b></p>
                    <p style="font-size:13px; "><b>&#10003; SCM Management with various stakeholders (factories, HQ sales & SCM and 3PL)</b>
                    <br>- Managed all SCM operation by communicating 
                    <br>1) with factories about productionschedule, 
                    <br>2) with HQ sales team about PLC management, mainly about releasing EOL products, 
                    <br>3) with HQ SCM team about weekly sales allocation and production issues and 
                    <br>4)with Pantos (LG 3PL) to manage shipment delay & issues as well as trucking schedule.
                    <br><b>&#10003; Inventory KPI target set up and LTI (Long Term Inventory) & WOS management</b>
                    <br>- Set LG inventory KPI target based on M+3 order situation and sales allocation status and
                    managed LTI by communicating with KAMs to clear them, especially malignity ones but
                    also made major channels’ inventory KPI target considering sell-in and sell-out forecast.</p>'''
                    , unsafe_allow_html=True)
        e3.markdown('''<p style="font-size:18px; "><b>Data Analysis</b></p>
                    <p style="font-size:13px; "><b>&#10003; Analysis on profitability structure and PRM(Product Road Map) Management</b>
                    <br>- Analyzed +300 models’ profitability, specially focused on material cost, different
                    transportation fee depending on its origin production site, marginal profit and operating
                    income for HA products, supporting PM to decide PLC also make PRM strategy.
                    <br><b>&#10003; SOM(Sell Out Management) Analysis</b>
                    <br>- Provided major channels’ weekly sell-out and market share analysis report including sell-out trend, growth rate, weekly hit models and high inventory ones.
                    <br>- Made sell-out forecast and target based on promotion plan, market trend and each major channels’ product portfolio and sales strategy by communicating with KAMs, product specialist, marketing team and PM during SOM meeting.</p>
                    ''', unsafe_allow_html=True)     
        
        # project
        st.subheader('Project & Education')
        e1 = st.empty()
        e2 = st.empty()
        e3 = st.empty()
        e1.markdown('''<p style="font-size:18px; "><b>GTM Enforce Project</b>
                    <p style="font-size:13px; ">- Introduced new GTM system for shop promoters to report major channels’ market information on real time basis through mobile application which is linked to LG internal system by collaborating with LGCNS
                    <br>- Made new system to automatically track RRP information on online website using python programming
                    <br>- Rewarded best practice prize of GTM Enforce Task among 15 EU subsidiaries</p>
                    ''', unsafe_allow_html=True)
        e2.markdown('''<p style="font-size:18px; "><b>Education about factory work flow in Poland</b>
                    <p style="font-size:13px; ">- Got training on production process from manufacturing to packaging, improving understanding of factor’s work flow
                    <br>- Participated in SCM process improvement TASK with EU subsidiaries’ top management, translating meeting for foreign subsidiaries’ leaders.</p>
                    ''', unsafe_allow_html=True)
        
    def world():
        m = folium.Map(width=485, height=300)
        folium.Marker([us_lat, us_lon], popup='USA', icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([mn_lat, mn_lon], popup='Mongolia', icon=folium.Icon(color='purple')).add_to(m)
        folium.Marker([hu_lat, hu_lon], popup='Hungary', icon=folium.Icon(color='green')).add_to(m)
        folium_static(m, width=485, height=300)
        # # experience
        # st.subheader('Experience')
        # e1 = st.empty()
        # e2 = st.empty()
        # e3 = st.empty()
        # e1.markdown('experience')
        # e2.markdown('experience')
        # e3.markdown('experience')  
        # # project
        # st.subheader('Project')
        # e1 = st.empty()
        # e2 = st.empty()
        # e3 = st.empty()
        # e1.markdown('project')
        # e2.markdown('project')
        # e3.markdown('project') 
        
    if country == 'USA':
        us()
    elif country == 'Mongolia':
        mn()
    elif country == 'Hungary':
        hu()
    else:
        world()  
                
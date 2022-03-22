import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Lilian Martin, Data analyst
#### Resume 
''')

image = Image.open('dp.png')
st.image(image, width = 250)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Junior Data analyst 
- Data training Manager at Matrice
- Worked at Secours Catholique on the statistical report "Etat de la pauvreté en France"
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/lilianmartin4/" target="_blank">Lilian Martin</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Work Experience
''')

txt('**Data training Manager**, Matrice, Paris',
'2021-today')
st.markdown('''
- Training people to Data Analysis.

''')

txt('**Data analyst**, Rise Up, Paris',
'2019-21')
txt('**Statistical analyst**, Secours Catholique Caritas France, Paris',
'2009-12')
txt('**Census officer**, INSEE/Mairie du 13e, Paris',
'2018')
txt('**Investigator**, ORIVE, Paris',
'2017-18')
txt('**Activity leader**,Enfants du métro, Paris',
'2015-18')
txt('**Odd jobs**, Adecco, Paris',
'2012-15')

st.markdown('''
- Provided mentorship and supervision to junior faculty, researchers, Ph.D./M.Sc./B.Sc. students. Mentored `3` Post-doctoral fellows, supervised `13` Ph.D. students, supervised `8` M.Sc. students, supervised `13` B.Sc. students and hosted `6` visiting students from U.S., Sweden and India.
- Wrote and applied for research grants. Served as Principal Investigator for research grants that have been awarded `12.5 million THB` and `1.117 million SEK` in research funding from Thai and Swedish grant agencies.
- Conducted research by applying machine learning to computational drug discovery and ensuring that research output exceeds `20+` articles per year.
- Taught `10+` undergraduate/graduate classes on Bioinformatics, Data Mining, Scientific Research and Presentation, Research Methodology, Graduate Seminar, Programming for Health Data Science, etc.
- Peer reviewed `100+` research articles for leading scientific journals.
''')

#####################
st.markdown('''
## Education
''')

txt('#### **Data Analyst** OpenClassrooms X ENSAE-ENSAI', '2019-21'
)
st.markdown('''
- GPA: `3.89`
- Research thesis entitled `Computer-aided molecular design for biological and chemical applications : Quantum chemical and machine learning approach`.
- Received Royal Golden Jubilee Ph.D. Scholarship of `2.152 million THB` covering tuition and stipend.
- Thesis awarded `1st` Prize by the National Research Council of Thailand.
''')

txt("**Paris 1 Panthéon-Sorbonne –Professional Master's degree–Expert Demographer**, Faculty of Medical Technology, Mahidol University, Thailand",
'2014-2019')

txt('**Bachelors of Science** (Biological Science), *Mahidol University International College*, Thailand',
'1998-2002')
st.markdown('''
- GPA: `3.65`
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `VBA`, `SAS`, `Stata`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Business Intelligence', '`AWS Quicksight`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Model deployment', '`streamlit`')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/lilianmartin4/')

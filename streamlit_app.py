import streamlit as st
from PIL import Image

#st.set_page_config(layout="wide", page_title="Interactive table app")
# 📰 
st.set_page_config(page_icon="🈺", page_title = "Lilian Martin CV")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Custom function for printing text
def head(a, b):
  col1, col2 = st.columns([3,1])
  with col1:
    st.markdown(a)
  with col2:
    st.image(b, width = 200)

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


#####################
# Header 
image = Image.open('dp.png')

head('''
# Lilian Martin, Data analyst
#### Resume 
''', image)

#st.markdown('[this is a text link](upload:image)')

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
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #;">
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
st.markdown('''
# Work Experience
''')

txt('#### **Data training Manager**, Matrice, Paris',
'2021-today')
st.markdown('''
- Training people to Data Analysis
- Creation of training content
- Professional integration coaching
- Reference : s.olivera.silvera@gmail.com
''')

txt('##### **Data analyst**, Rise Up, Paris',
'2019-21')
st.markdown('''
- Creation of a datalab for our customers
- Business Intelligence: dashboards realization (`AWS Quicksight` & `MySQL`)
- Communication with customers
- Reference : guillaume@riseup.ai

''')
txt('##### **Statistical analyst**, Secours Catholique Caritas France, Paris',
'2018-19')
txt('##### **Census officer**, INSEE/Mairie du 13e, Paris',
'2018')
txt('##### **Investigator**, ORIVE, Paris',
'2017-18')
txt('##### **Activity leader**,Enfants du métro, Paris',
'2015-18')
st.markdown('''
- Caring for children in summer camp
''')
txt('**Odd jobs**, Adecco, Paris',
'2012-15')


#####################
st.markdown('''
### Voluntary work
''')

txt('#### **Bar referent**, La base, Paris',
'2019-today')

st.markdown('''
- Bar tending
- Events management, communication
- Marauding
- Mentoring
''')

txt('**Volunteer**, Secours Catholique Caritas France, Paris',
'2018-19')

st.markdown('''
- Take care of the children of the people welcomed during the events organized (Christmas, football tournament at claire-fontaine...)
''')

#####################
st.markdown('''
# Education
''')

txt('#### **Data Analyst** OpenClassrooms X ENSAE-ENSAI', '2019-21'
)
st.markdown('''
- Data analysis, machine learning
- Learned `Python3` & `MySQL`
- Data scrapping
- 10 professional projects. 
- A final statiscal report on `UFC`
- Reference: romainwarlop@gmail.com
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

st.markdown("[LinkedIn](https://www.linkedin.com/in/lilianmartin4/)")

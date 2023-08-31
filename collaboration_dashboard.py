import streamlit as st

# FMR logo on top - will adjust the align later
st.image('https://www.fidelity.com/bin-public/060_www_fidelity_com/images/Fidelity-footer-logo.png')
# Titles and headers
st.title("Fidelity AMT Learning Days")
st.divider()
st.header('Learning Objectives Submission Form')
st.caption('This tool will assist in finding associates with similar learning interests, enabling collaboration and the set up of study groups')
st.divider()
st.subheader('Please enter your details:')

#init session state
if "ideasList" not in st.session_state:
    st.session_state.ideasList = []

if 'userId' not in st.session_state:
    st.session_state.userId = ''

if 'validateUderID' not in st.session_state:
    st.session_state.validateUderID = ''

# Test data (to be removed once we connect to Snowflake)
learningList = ['PL/SQL', 'Snowflake', 'AWS', 'Oracle','PowerBI', 'Tableau']
certificationList = ['AWS Certified Architect Associate', 'Snowflake SnowPro Core', 'AWS Certified Cloud Practitioner', 'Oracle PL/SQL Developer Certified Associate']
projectList = ['AngularJS web application', 'Android mobile app']

#lists
objectiveList = []
finalListObjs = []

def validateUserID():
  # This will check in Snowflake if the user already exists (with a select count to check if exists)
  # Will return True or False based on st.session_state.userId
  if 1 == 1:
      st.session_state.validateUderID =':heavy_check_mark: Username ' + st.session_state.userId + ' is available'
  else:
      st.session_state.validateUderID =':x: Username ' + st.session_state.userId + ' is not available. Please enter a new one.'
  return True 

# Allow the end user to insert a new objective
#def insert_row_snowflake(new_fruit):
  #with  my_cnx.cursor() as my_cur:
   # my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
   # return "Thanks for adding " + new_fruit   

# Adding container to group Input elements
with st.container():
    # Input fields
    st.text_input(label="Your preferred User ID", value="",on_change=validateUserID, key='userId')
    st.caption(st.session_state.validateUderID)
    # st.session_state.userId is what needs to be validated
    userName = st.text_input("Your Full Name", "")
    userEmail = st.text_input("Your E-mail","")
    
    objective = st.radio(
    "What are you interested in achieving during Learning Days?",
    ["Learning :open_book:", "Certification :medal:", "Building a project :desktop_computer:"])

    if objective == 'Learning:open_book:':
        objectiveList = learningList
        objectiveList.append('Submit New Objective')
        #st.write('You selected Learning.')
    else:
        if objective == 'Certification:medal:':
            objectiveList = certificationList
            objectiveList.append('Submit New Objective')
            #st.write('You selected Certification.')
        else:
            if objective == 'Building a project:desktop_computer:':
                objectiveList = projectList
                objectiveList.append('Submit New Objective')
                #st.write('You selected Build a project.')

    extraLearningObjectives = st.text_area("Please provide additional input on your Learning Day objectives", "")

    selectedObjectives = st.multiselect(
        label='Select any specific item you are interested in as per your learning interests (you can select multiple items): ',
        default=objectiveList)

    if "Submit New Objective" in selectedObjectives:
        # Allow users to enter a new learning objective that is not present in the list
        st.caption('You wanted to enter a new learning objective. Please use the textbox below for this:')
        newObjective = st.text_input("Your new learning objective")
        # call to snowflake insert routine capturing both objective and newObjective
        # TBD
        # Also add to the list of selected stuff
        objectiveList.append(newObjective)
        

# Submit button
if st.button("Submit"):
    if st.session_state.userId and userName and objective and selectedObjectives:
        
        for obj in selectedObjectives:
            if obj != 'Submit New Objective':
                finalListObjs.append(tech)
                #st.session_state.ideasList.append(f"{userName} : Study ideas: {quickList}    My Objectives: {objectives}") 

    else:
        st.warning("Please fill in both your details and learning objectives.")
 #display ideas back to the user

st.divider()

with st.expander("People with similar learning objectives"):

    st.subheader('People with Similar Interests:')

    with st.spinner('Performing associate matching...'):
        time.sleep(10)
    st.success('Sorry, no associates have been matched to your learning objectives')

# Adding new container for debug (to be removed)
with st.container():    

    st.write('You selected:', technology)
    
    if st.session_state.ideasList:
        st.title("Ideas")
        for idea in st.session_state.ideasList:
            st.write(idea)

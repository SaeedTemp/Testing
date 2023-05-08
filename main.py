import streamlit as st
import pymongo
import pdfplumber


st.title("Job seeker Portal!!")
st.subheader(':blue[Apply Now!]')



def dataConnectivity():
    conn_str = "mongodb://project3343:rsproject@ac-gjl3aea-shard-00-00.sop0wqm.mongodb.net:27017,ac-gjl3aea-shard-00-01.sop0wqm.mongodb.net:27017,ac-gjl3aea-shard-00-02.sop0wqm.mongodb.net:27017/?ssl=true&replicaSet=atlas-xr3bsz-shard-0&authSource=admin&retryWrites=true&w=majority"
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    print("Whole stuff running Again!")
    try:
        print(client.server_info())
    except Exception:
        print("Unable to connect to the server.")
    db = client.resumeDB
    jd = db.jd
    print(db.list_collection_names())
    return jd



# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb://project3343:rsproject@ac-gjl3aea-shard-00-00.sop0wqm.mongodb.net:27017,ac-gjl3aea-shard-00-01.sop0wqm.mongodb.net:27017,ac-gjl3aea-shard-00-02.sop0wqm.mongodb.net:27017/?ssl=true&replicaSet=atlas-xr3bsz-shard-0&authSource=admin&retryWrites=true&w=majority"

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server port.")

db = client.resumeDB
users = db.users
jd = dataConnectivity()
jdList = jd.find({})
#adding JD names to list
dropDisplay = []
for jds in jdList:
    dropDisplay.append(jds["name"])

#dropdownlist for selecting job description 
option = st.selectbox("Select Job Description",(dropDisplay))
st.write(option)
selectedJD = jd.find_one({"name":option})
st.write(selectedJD["desc"])
job_description = selectedJD["desc"]


with st.form("form1",clear_on_submit=True):
    Name = st.text_input('Name')
    Email = st.text_input('Email')
    resume = st.file_uploader('Upload your Resume')
    

    submit = st.form_submit_button("Submit")
    if submit:
        resumeText = ""
        def extract_text_from_pdf(file):
            with pdfplumber.open(file) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
                # Remove unwanted characters and extra white spaces
                text = " ".join(text.split())
            return text
        if resume is not None:
        # Convert PDF to clean text
            resumeText = extract_text_from_pdf(resume)

            

    #inserting

        def newdataFun():
            newData={
                "name":Name,
                "emailId":Email,
                "description":resumeText,
                "job_description":job_description
            }
            return newData 
        users.insert_one(newdataFun())
       

        st.subheader(':blue[Submitted Sucessfully]')
        

for user in users.find():
    print(user)


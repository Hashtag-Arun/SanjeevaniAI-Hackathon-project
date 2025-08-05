\# **SanjeevaniAI – Hackathon Project**



A Smart AI-Powered Platform for Thalassemia Warriors to connect with trusted blood donors, predict availability, track rare blood types, and ensure safe donations.



---



**## *Project Features***



\- Donor availability prediction using AI logic

\- Health eligibility check (hemoglobin, fever, surgery)

\- Blood group analytics and rare blood alerts

\- Donor trust and safety scoring

\- Rule-based chatbot for guidance

\- React Web dashboard for Blood Warriors team



---



**##  Backend (FastAPI)**



Path: `backend/fastapi/main.py`



**### How to Run**

```bash

cd backend/fastapi

uvicorn main:app --reload

 

**APIs**

**Endpoint**	             **Description**

POST /predict	             Predict donor's next eligibility

POST /check-eligibility	     AI health check

POST /chat	             Chatbot

GET /blood-stats	     Blood group stats

GET /donor-trust/{name}	     Donor trust score



&nbsp;

**Frontend (React Web Admin)**



Path: frontend/react-web-admin/App.js



**How to Run**



cd frontend/react-web-admin

npm install

npm start



**Example Donors**



Arun (A+)



Varun (B+)



Liya (O-)



Ramiya (AB+)



Soniya (A-)



Praddep (B-)



Duptha (O+)



**AI Logic**



**Trust Score (simplified)**

trust = (donations \* 20) - (last\_donation // 10)



**Eligibility Check**

eligible = hemoglobin >= 12.5 and not has\_fever and not recent\_surgery



**Full Setup Summary**



**# Start backend**



cd backend/fastapi

uvicorn main:app --reload



**# Start frontend**



cd frontend/react-web-admin

npm install

npm start



**Built By**

Arun a.k.a. Hashtag-Arun

🔗 https://github.com/Hashtag-Arun/SanjeevaniAI-Hackathon-project



**###  Final Tips:**

\- Save this file as `README.md` in the \*\*root folder\*\* of your project

\- Then commit it to GitHub:

```bash

git add README.md

git commit -m "Add full project README"

git push


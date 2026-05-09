# JSW Motors — Competency TNA Portal

A Django MVP for collecting and analysing Training Needs Assessment (TNA) data across all 9 JSW Motors functions.

## Features
- **Welcome Page** — Employee name, code, role & function selection
- **Functional Head Questionnaire (FHQ)** — Rate competency importance + desired proficiency for GET & MT
- **GET Self-Assessment** — Current proficiency self-rating
- **MT Self-Assessment** — Current proficiency self-rating
- **Admin Dashboard** — Response counts by function
- **Gap Analysis** — Desired vs current levels per competency
- **Excel Export** — FHQ, Self-Assessment, and Gap Analysis exports

## Functions Covered
Sales & Marketing | Engineering | New Product Development | Finance | HR | Procurement & Localisation | SCM & Logistics | IT & Digital | Manufacturing

---

## Local Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # edit as needed
python manage.py migrate
python manage.py runserver
```

Visit `http://localhost:8000`  
Admin: `http://localhost:8000/admin-login/`  
Default credentials: `admin` / `JSW@TNA2025`

---

## Deploy on Railway

1. Push to GitHub
2. Create new Railway project → **Deploy from GitHub repo**
3. Add **PostgreSQL** plugin — Railway auto-sets `DATABASE_URL`
4. Set environment variables in Railway dashboard:
   ```
   SECRET_KEY=<generate a secure random string>
   DEBUG=False
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=<your secure password>
   BASE_URL=https://<your-app>.up.railway.app
   ```
5. Railway auto-runs `build.sh` (migrate + collectstatic) on every deploy
6. App goes live — share the Railway URL with respondents

---

## Admin Login
`/admin-login/`

## Key URL Routes
| Route | Description |
|-------|-------------|
| `/` | Welcome / survey entry |
| `/survey/fhq/` | Functional Head Questionnaire |
| `/survey/get/self-assessment/` | GET Self-Assessment |
| `/survey/mt/self-assessment/` | MT Self-Assessment |
| `/admin-dashboard/` | Admin overview |
| `/admin-gap-analysis/` | Gap analysis by function |
| `/admin-responses/fhq/` | View FHQ responses |
| `/admin-responses/self-assessment/` | View self-assessment responses |
| `/admin-export/fhq/` | Download FHQ Excel |
| `/admin-export/self-assessment/` | Download SA Excel |
| `/admin-export/gap-analysis/` | Download Gap Analysis Excel |

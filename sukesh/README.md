# 🚀 DevProfile Optimizer

> An AI-powered dashboard that builds, tracks, and optimizes your developer profile — from GitHub activity to job-ready resumes.

---

## 📌 Overview

**DevProfile Optimizer** helps developers, students, and job-seekers craft tailored resumes, improve their GitHub profiles, and track their credibility for dream tech roles.

With AI integration, daily progress insights, and real-time GitHub analysis, it’s your personal career assistant — powered by code and intelligence.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔐 **GitHub Login** | OAuth-based sign-in and profile sync |
| 🧠 **AI Resume Generator** | Creates tailored, role-specific resumes from GitHub data |
| 📊 **GitHub Analyzer** | Displays top languages, repositories, and activity trends |
| 📄 **PDF Export** | Download resumes in clean, ATS-friendly templates |
| 🎯 **Credibility Score** | Score based on coding streaks, repo quality, commit history |
| 💡 **Daily Tips** | AI-suggested profile improvements upon login |
| 🗂️ **Role Selector** | Lets users target job roles like "MERN SDE", "Data Engineer", etc. |

---

## 🧠 How It Works

1. **Login with GitHub**
2. **Choose a target role**
3. **System fetches GitHub data** (repos, commits, languages)
4. **AI generates your resume** based on skills + job requirements
5. **Get a credibility score** + improvement tips daily

---

## 🧰 Tech Stack

### Frontend
- [Next.js](https://nextjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Recharts](https://recharts.org/)
- [Lucide Icons](https://lucide.dev/)
- [React Hook Form](https://react-hook-form.com/)

### Backend
- [Node.js](https://nodejs.org/)
- [Express.js](https://expressjs.com/)
- [GitHub REST API](https://docs.github.com/en/rest)
- [OpenAI API (GPT-4o)](https://platform.openai.com/)
- [LangChain](https://www.langchain.com/) (optional)

### Database & Auth
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [Mongoose](https://mongoosejs.com/)
- [Clerk](https://clerk.dev/) / [Firebase Auth](https://firebase.google.com/docs/auth)

---

## 🖼️ Screenshots

> Add screenshots to show off:
- Dashboard
- Resume PDF
- GitHub stats viewer
- Daily tip UI

---

## How to Run Locally (MVP)

```bash
# Clone the repo
git clone https://github.com/your-username/devprofile-optimizer.git
cd devprofile-optimizer

# Install dependencies
npm install

# Add environment variables for GitHub OAuth & OpenAI
cp .env.example .env

# Run frontend and backend
npm run dev
```

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/devprofile-optimizer.git
cd devprofile-optimizer
```

### 2. Install dependencies
```bash
npm install
```

### 3. Add environment variables
Create a .env file in the root with:
```env
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
OPENAI_API_KEY=your_openai_key
MONGODB_URI=your_mongodb_connection_string
NEXT_PUBLIC_BASE_URL=http://localhost:3000
```

### 4. Run the project
```bash
npm run dev
```
Frontend should be up at `http://localhost:3000`.

## 📁 Folder Structure
```java
devprofile-optimizer/
│
├── frontend/
│   ├── pages/
│   ├── components/
│   └── styles/
│
├── backend/
│   ├── routes/
│   ├── controllers/
│   ├── services/
│   └── models/
│
├── public/
├── .env
├── README.md
└── package.json
```

📈 Roadmap
[] GitHub OAuth login
 
[] GitHub repo + commit analysis

[] Resume PDF generator (AI-based)

[] Daily improvement tips

[] Portfolio auto-builder (v2)

[] Resume versioning and tracking

[] LinkedIn/Glassdoor job parsing

👨‍💻 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

```bash
git checkout -b feature/your-feature-name
git commit -m "Add your feature"
git push origin feature/your-feature-name
```

📄 License
MIT License © 2025 [sukeshofficial]

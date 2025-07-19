# VoiceAssist
Build ai voice assistant 

## <small> this will also help learn git for real world applications </small>

# Goal
- Train voice recognition ml model
- Build data scraping program to help it gather info from web
- "thats all for now"

# Setup 
- Fork & Clone repo
```bash
$ git checkout pre_main 

NB: Create new branch for new features
```
- Do whatever you want

## Project Structure
```
voiceassist/
│
├── data/                  # Training data, datasets, and scraped info
│   └── raw/               # Raw audio/text data
│   └── processed/         # Cleaned and processed data
|
├── demos/                  # Training data, datasets, and scraped info
│   └── Voice_turtle/      # Voice Controlled cursor game with turtle
|       └── raw/               # Raw audio/text data
│       └── processed/         # Cleaned and processed data
│
├── models/                # ML models and training scripts
│   └── voice_recognition/ # Voice recognition model code
│
├── scraping/              # Web scraping scripts
│
├── assistant/             # Core assistant logic and main app
│
├── tests/                 # Unit and integration tests
│
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```
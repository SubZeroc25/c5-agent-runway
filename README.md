# C5 Agent Runway

This project is ready to deploy as a custom model on RunwayML.

## Files to include in your GitHub repo for RunwayML
- `runway_model.py`  
- `runway_model.yaml`  
- `requirements.txt`
- `README.md` (this file, optional but recommended)

**Do NOT upload your `.env` file to GitHub!** Instead, copy the values from `.env` and add them as environment variables in the RunwayML dashboard.

## How to deploy on RunwayML
1. Push these files to a new GitHub repository.
2. In RunwayML, choose "Import from GitHub" and select your repo.
3. Set the entrypoint to `python runway_model.py`.
4. Set Python version to 3.10 if possible.
5. Add your API keys as environment variables in the RunwayML dashboard:
   - `OPENAI_API_KEY`
   - `GATE_API_KEY`
   - `GATE_API_SECRET`
6. Deploy and test your model.

---

**If you need to update your API keys, edit your `.env` file locally, but never upload it to GitHub.**

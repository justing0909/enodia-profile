# Professional Profile Page

A Streamlit-based professional profile page with interactive elements and email capture functionality.

## Features
- Professional profile display with logo and headshot
- Interactive buttons for LinkedIn, company website, and Calendly
- Email capture form for product summary
- Admin view for managing email subscriptions

## Local Development
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deployment
This app is configured for deployment on Streamlit Community Cloud. The `emails` directory is kept local and not deployed to maintain privacy of subscriber data.

## File Structure
- `app.py`: Main application file
- `requirements.txt`: Python dependencies
- `emails/`: Local directory for storing subscriber data (not tracked in git)
- Images:
  - `Enodia_PNG_02_Transparent_BG.png`: Company logo
  - `linkedin_headshot-2.jpeg`: Profile picture 
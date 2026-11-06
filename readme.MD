# Diwali Wishes 🪔

A friendly, cinematic Diwali greeting built with Streamlit (single file: `app.py`).

## Run
```
pip install -r requirements.txt
streamlit run app.py
```

## Notes
- Navigation uses `st.session_state`; animations run in `st.components.v1.html` iframes.
- Music is synthesised in the browser (WebAudio), so there are no audio files to go missing.
  It only starts when you tap "Play music" and must be toggled on each page, since each page is its own iframe.
- Tap anywhere on a page to launch a rocket; there is also a Sweet Catch mini-game.
- Fully responsive; respects reduced-motion settings.
- Personalise by adding `?name=Anu` to the app URL; without it the greeting is generic ("Hey there!").
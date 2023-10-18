import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source);


try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))

finally:

    GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "polarform",
  "private_key_id": "4a2adb0b245a39ca1290a7b3409b0b0ffba028ae",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCb0MOm5eAaNqav\nZVGfgNPXhGNIzCqfyfGogijTC9l/M8MeeDJ6ty1H2E+zBi18FVcKZKyb7Wran5Cm\n+YIjs7SO/GTEtAjIDjDQlMuFuOQGIHpNw9Sdv90PU02fC9920rOZfGPhidzeGNyM\n3CrpN1m1FqXmVuKQa/IsrLFte05scsyVYNYexsOzDlftJGyS6aWHG+II7bVpcRqe\n/gpY9l07x7GnhEE8aSQPm4LNMP1O8193T/uXko9lcTwBKjaEuSJt2D0yj1jSVMzM\noQlaLaWA1klJ8LO9zAEojIr3ZD4ulSemdo1y7OPei1R3wfXwDca2OGtadg2Pa2R+\nkTL5N5vrAgMBAAECggEAPA/ko1ygHqqrZRfytz/TKRPsq56b3Z1cDF8j+npqXAip\ncYDWwIwEpdmhmzpJ5TdapnR5Pt/tXRm+CkdKnZWDh8yN0W8upWMm+PgqXcEQELaL\nPpe6yRYw0dwEI0dR2/1LYuJapBFe9LPzrE6gMeb2qwHwcFJUomQh5YuqFzA9Yjrh\n61Jy6hCLWCrQhzdBjjpjA/ZPSSceCDr+QZQOvks7aqvblVJlOAF7uE0F0q1YZ6BS\nvMsr+wQR4G1P5ttJvIqS0ACCXJic48CX1xtnMT/wVcHYZPb4o4ob9ltZJiCR5BiW\nAMM8U5lxVB572FJyVKgCTNlPSWgsqNmuNgEJpGBnLQKBgQDXem5ZNsR56HX4wq/o\nu8QFLvMtpySLXW0Jx2X5TV3Lc/pM7PobAdWf2GNjhn0on+mJ25VTWxsI0OuJpSVj\nEuUMs9mZqZzo7PnP01vi10qPLmck+5Ea9tsKIBchH+dqGRYww2KguhJKAptQyzdL\n68nZl6PeJ2ffi5Cs+NPGeCPixQKBgQC5HgtbwlfAOHjhLflDKv99vA7KXgB7T07K\ng6d8laQig7ojFiMvvsmIBJrBm/wwXNj6Ba/bZ2W6JR8oFbXEi3+wTb1Azqvm/1ko\nevPOFX5ZJq42OB3IeIUZDpOBTmxlijmfz4CbS5SiYswgZ5rbJ0dOZfsBhAc+HK2g\nd3RAspGu7wKBgA9rkY4M306iFh8xP4l2NnbwfzKbLYBTtUPn4yJOKRIwQI9UvilE\nnlcME0DCFR7dIsdc0XjfojWlTdXR3bUTWxTnogDfJH1+x/nZdE/tfEZ22abJ4f59\n//rfhQg30kXDedUPhnVeG4T0Xs0PXeuu+gj6Ux3I0CQtRrM6M12Wp2rJAoGAakJv\nvK0y17jS0lckdMTSwWbYipso5Z9hl+e4lVAEVneMuiUz720xm60g9C/ItC4nsmTf\nTC7u+sniN402uGpm0lndX70CeedrU0w4dLxruVr1t1PA7NkZdYejbh8JI8QTTcO7\ni+j3mbrid1thTZkfWkY5reYOjj3CAJFxHs4hx+sCgYAXvO3Oz8/ORYiY53vq0K2s\nuiLmRxkXwjKuOi0zJzrp/szUmhBbj7zkCumhDpLQvQ+OHhcaChkrrcFkpBuWCdnl\nUJReJs2mLvruQulBWybxb0RUumGRlcq+VM+4KqSMws3PSbUF64TC3nNCoJIgSfM1\nnDejRU0GrvQKW6TAtnhRWQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "stt-728@polarform.iam.gserviceaccount.com",
  "client_id": "114719619285075413196",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/stt-728%40polarform.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
"""
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

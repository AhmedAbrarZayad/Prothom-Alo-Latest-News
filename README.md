# Prothom-Alo-Latest-News

- So this is a little project of mine I did on python. It's job is to automate the process of sending the latest news of the Bangladeshi news portal 'Prothom Alo'. It shows the top 10 news of 'Prothom Alo' for that moment. You can save the emails of people you want to send it to and then just run it. It will send the news to those emails automatically.
# Requirements:
  - You need to have python installed.
  - then you need to have beautifulsoup and requests module installed. use the following commands <b>pip install requests</b> and <b>pip install beautifulsoup4</b>. If you dont have pip        installed then follow this [installation_guide](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)
# Instructions:
  - ## Setup
    - ### Setup sender data
      - First, run the sender.py. Input the email of the sender in the <b>"Sender's email"</b> field.
      - Secondly, go to your google account. Then go to Security. Then search for <b>"App Passwords"</b>. There, create an app by giving an           <b>"App Name"</b>. You will then get an <b>"App Password"</b>. Copy it, and input it in the <b>"Sender's Google App Password"</b>              field.
    - ### Setup receiver data
      - Run receivers.py. Input the number of receivers you will add in the <b>"Number_of_receivers"</b> field.
      - Then input the receivers' email in the <b>"Receiver's email"</b> field.
  - ## Sending Emails
      - Now all you have to do is just run prothom_alo.py. If you want to <b>add new receivers</b>, then run <b>receivers.py</b> and do              the process mentioned in the <b>Setup receiver data</b> section of <b>Setup</b>. If you want to change the <b>sender</b>, then run           <b>sender.py</b> and do the process mentioned in the <b>Setup sender data</b> section of <b>Setup</b>.

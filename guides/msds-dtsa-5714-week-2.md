# Setting up a Web Application

To get started on the development of your project, we will set up a simple website with a public facing website. We will use Flask as the web framework, GitHub to host the code repository, and Heroku to provide us with a public facing URL for the website.

## Getting Started with Flask

To get started on development we shall create a virtual environment using Python and then upload the contents of the repository to GitHub.

To create a Python virtual environment in Linux, use the following commands:

1. Install Python's venv module:  sudo apt install python3-venv
2. Create a new directory for the application, and then make that directory your current working directory: mkdir my_flask_app && cd my_flask_app
3. Create the virtual environment and source the activation script:  python3 -m venv venv && source venv/bin/activate
4. Install Flask: pip install Flask

Once the virtual environment has been created, we can go ahead and create a simple website. To get started on the Flask application, follow the ensuing steps:

1. Create a source folder: mkdir src
This is where majority of the source code for the project will reside.
2. Create the application file: touch src/app.py
3. Tell the system which file is the application file: export FLASK_APP=src/app.py
4. The next step is to add code to app.py. Insert the following code to the file:

## Sample Data for Testing

- [Apple AAPL Q3 2021 Earnings Call Transcript | Rev](https://www.rev.com/blog/transcripts/apple-aapl-q3-2021-earnings-call-transcript)

## Additional Resource

- [Python Flask — Ep.1 เรียนรู้ Flask Framework และเริ่มต้นสร้างโปรเจคท์ | by stackpython | Medium](https://stackpython.medium.com/flask-101-%E0%B8%9E%E0%B8%B1%E0%B8%92%E0%B8%99%E0%B8%B2%E0%B9%80%E0%B8%A7%E0%B9%87%E0%B8%9A%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%9E%E0%B8%98%E0%B8%AD%E0%B8%99-flask-framework-3cae1c0b45d9)
- [ทำ API ด้วยไพธอนง่ายนิดเดียว โดยใช้ Flask (ที่เหลือยากหมด) Ep.1 | by stackpython | Medium](https://stackpython.medium.com/%E0%B8%97%E0%B8%B3-api-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B9%84%E0%B8%9E%E0%B8%98%E0%B8%AD%E0%B8%99%E0%B8%87%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%99%E0%B8%B4%E0%B8%94%E0%B9%80%E0%B8%94%E0%B8%B5%E0%B8%A2%E0%B8%A7-%E0%B9%82%E0%B8%94%E0%B8%A2%E0%B9%83%E0%B8%8A%E0%B9%89-flask-%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%AB%E0%B8%A5%E0%B8%B7%E0%B8%AD%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%AB%E0%B8%A1%E0%B8%94-84ed925b3293)
- [How to install Python packages with pip and requirements.txt | note.nkmk.me](https://note.nkmk.me/en/python-pip-install-requirements/)
- [gs146/NLP-deployment-heroku-Text-summarizer-: Summarize any text from an article, journal, story and more by simply copying and pasting that text.](https://github.com/gs146/NLP-deployment-heroku-Text-summarizer-)
- [DheerajKumar97/Text-Summarizer-Flask-Deployment: This project is based on a Basic Text summarizer implemented with the concept of Cosine Similarity. Every basic preprocessing and Feature Engineering steps in Natural Language Processing is implemented and deployed as web API using Flask Deployment](https://github.com/DheerajKumar97/Text-Summarizer-Flask-Deployment)
- [Create a Text Summarization API With Flask, Sumy, and Trafilatura | by Paymon | DataDrivenInvestor](https://medium.datadriveninvestor.com/create-a-text-summarization-api-with-flask-sumy-and-trafilatura-385212b759d8)
- [A Flask Web App for Automatic Text Summarization Using SBERT](https://www.analyticsvidhya.com/blog/2022/02/a-flask-web-app-for-automatic-text-summarization-using-sbert/)
- [พัฒนาโปรแกรมใน Container กัน | Vscode Python Flask | Medium](https://piravit-chenpittaya.medium.com/%E0%B8%A1%E0%B8%B2-developing-inside-a-container-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-remote-containers-%E0%B8%81%E0%B8%B1%E0%B8%99-python-flask-573ae3ca4bbf)
- [Build and Deploy Flask REST API on Docker - DEV Community](https://dev.to/codemaker2015/build-and-deploy-flask-rest-api-on-docker-25mf)
- [How To Dockerize Your Flask API. Exploring how to dockerize a Flask… | by Nacho Vargas | Better Programming](https://betterprogramming.pub/how-to-dockerize-your-flask-api-cc95843ab625)

## Know Issues & Debug

- [Git Large File Storage | Git Large File Storage (LFS) replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.](https://git-lfs.com/)
- [ใช้ Git LFS จัดการกับไฟล์ขนาดใหญ่ | KT](https://karn18.github.io/dev/2020/10/26/git-lfs.html)
- [installation - How can I get `pip install`'s download progress? - Stack Overflow](https://stackoverflow.com/questions/20771148/how-can-i-get-pip-installs-download-progress)
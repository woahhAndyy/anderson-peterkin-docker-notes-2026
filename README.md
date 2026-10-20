# Notes for Anderson Peterkin — Docker assignment

This is a self-contained replacement Flask Notes app if the instructor's starter files were not supplied. If your instructor provided an app, use that app and adapt its Dockerfile instead.

## Local test
```bash
python -m pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000, then stop with Ctrl+C.

## Part 1 — Build image
```bash
docker build -t note_app .
docker images
```
Take a screenshot of `docker images` showing `note_app`.

## Part 2 — Run two containers simultaneously
Open **two separate terminals**:
```bash
docker run --name notes_one -p 5000:5000 note_app
```
```bash
docker run --name notes_two -p 5001:5000 note_app
```
Open http://localhost:5000 and http://localhost:5001, then capture both browser windows and `docker ps` from a third terminal. Each container uses its own temporary SQLite database; notes are not shared and are lost when containers are removed.

## Part 3 — Docker Hub
Replace YOUR_DOCKERHUB_USERNAME with your actual Docker Hub username:
```bash
docker tag note_app YOUR_DOCKERHUB_USERNAME/note_app:v1
docker login -u YOUR_DOCKERHUB_USERNAME
docker push YOUR_DOCKERHUB_USERNAME/note_app:v1
```
Set the repository's visibility to public if needed. Capture the Docker Hub repository page showing the v1 tag.

## Part 4 — Render
In Render, create a Web Service, choose **Existing Image**, and enter:
```
docker.io/YOUR_DOCKERHUB_USERNAME/note_app:v1
```
If Render asks for a port, set `5000` (or `PORT=5000`). After deployment succeeds, open the generated `https://...onrender.com` URL and test adding and deleting a note. Capture the service dashboard and paste the actual URL into the PDF report. Free services may sleep when idle. Notes are stored in temporary container storage and may disappear on restart/redeploy.

## Cleanup
```bash
docker stop notes_one notes_two
docker rm notes_one notes_two
```

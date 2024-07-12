# Repro for issue 7435

## Versions

platform: macOS Sonoma 14.5<br>
firebase-tools: v13.13.2<br>
gcloud: v476.0.0<br>
Google Cloud SDK 483.0.0<br>
beta 2024.06.28<br>
bq 2.1.6<br>
cloud-datastore-emulator 2.3.1<br>
cloud-firestore-emulator 1.19.7<br>
core 2024.06.28<br>
gcloud-crc32c 1.0.0<br>
gsutil 5.30

## Steps to reproduce

1. Run `python3.11 -m venv venv`
   - Note: You might have a different version of python installed, try replacing `python3.11` with `python3.12`, or `python<VERSION>`
1. Run `. ./venv/bin/activate`
1. Run `pip install -r requirements.txt `
   - Installs the `requests` library
1. Open a separate terminal and run `gcloud emulators firestore start --host-port=127.0.0.1:54510 --database-mode=datastore-mode`
1. Run `python3 main.py`
   - Prints

```json
{ "mutationResults": [{}] }
```

## Notes

1. When using `gcloud --project=testbed-test beta emulators datastore start --use-firestore-in-datastore-mode --host-port=127.0.0.1:54510`
1. Run `. ./venv/bin/activate`
   - You don't have to do this if you're already ran `. ./venv/bin/activate`
1. Running `python3 main.py`
   - Prints

```json
{ "mutationResults": [{ "version": "2" }] }
```

1. pip install dvc  
2. dvc remote add -d storage gdrive://"your id"
3. git commit .dvc/config -m "Configure remote storage"   
4. dvc add data/mushrooms.csv 
5. dvc push

6. dvc repro
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

project_name="mlops_project_setup"
list_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py'
]

for file_paths in list_files:
    file_paths = Path(file_paths)
    file_dirs,file_names = os.path.split(file_paths)

    if file_dirs !="":
        os.makedirs(file_dirs,exist_ok=True)
        logging.info("Creating {file_dirs} for the files: {file_names}")

    if (not os.path.exists(file_paths)) or (os.path.getsize(file_paths) == 0):
        with open(file_paths,'w') as file:
            pass
        logging.info(f"Created empty files: {file_paths}")
    else:
        logging.info(f"{file_names} already exists")


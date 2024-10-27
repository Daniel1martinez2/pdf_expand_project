# Activate the Conda environment using the correct path
source <path/to/conda> conda-env-name

# Run the Python script on each selected PDF file
for f in "$@"
do
    /path/to/conda/env "/path/to/your/script.py" "$f"
done

# Deactivate the Conda environment
conda deactivate

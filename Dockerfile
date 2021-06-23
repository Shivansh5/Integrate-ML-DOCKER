FROM ml:v5

COPY SalaryData.csv .

COPY ml.py .


CMD ["python3","ml.py"]